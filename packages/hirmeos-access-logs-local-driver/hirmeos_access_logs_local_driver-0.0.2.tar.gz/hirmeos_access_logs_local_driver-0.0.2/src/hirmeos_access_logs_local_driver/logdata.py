import datetime
import gzip
import os
import re
import socket
import sys
import time

from typing import Iterator, Tuple
import urllib.error
import urllib.parse


class Request(object):
    """Represent the data in a single line of the Apache log file."""

    def __init__(
            self,
            ip_address: str,
            timestamp: str,
            method: str,
            url: str,
            response_code: int,
            content_length: int,
            referer: str,
            user_agent: str,
    ):
        assert response_code >= 100
        assert response_code < 1000
        assert content_length >= 0

        self.ip_address = ip_address
        self.timestamp = time.strptime(timestamp[:20], "%d/%b/%Y:%H:%M:%S")
        self.method = method
        self.url = self.normalise_url(url)
        self.response_code = response_code
        self.content_length = content_length
        self.referer = referer
        self.user_agent = user_agent

    @staticmethod
    def normalise_url(url: str) -> str:
        """We just avoid the malformed urls from the line_to_request
        'if len(request.split()) >= 3:' but we have to be safe to don't save
        wrong values."""
        try:
            if url[-1] == "/":
                return url[:-1]
            return url
        except IndexError as err:
            raise IndexError(f"Error parsing: {url}, {err}")

    def fmttime(self) -> datetime:
        fmt = "%Y-%m-%d %H:%M:%S"
        return datetime.datetime(*self.timestamp[:6]).strftime(fmt)

    def __str__(self) -> str:
        return f"Request {self.fmttime()}, {self.ip_address}, {self.url}"

    def as_tuple(self) -> tuple[datetime.datetime, int, str]:
        return (self.fmttime(), self.ip_address, self.url, self.user_agent)

    def sanitise_url(self, regexes: str) -> None:
        for regex in regexes:
            matched = re.search(re.compile(regex), self.url)
            if matched is not None:
                self.url = matched.group(0)
                break


class LogStream(object):
    def __init__(self, log_dir: str, filter_groups: list, url_prefix) -> None:
        self.log_dir = log_dir
        self.filter_groups = filter_groups
        self.url_prefix = url_prefix

    request_re = re.compile(r'^(.*[^\\]") ([0-9]+) ([0-9]+) (.*)$')
    r_n_ua_re = re.compile(r'^"(.*)" "(.*)" *$')
    fallback_re = r'^()" ([0-9]+) ([0-9]+) (.*)$'

    @staticmethod
    def parse_url(url: str, url_prefix: str) -> str:
        try:
            if url.startswith("http"):
                return url_prefix + urllib.parse.urlparse(url).path.lower()
            return url_prefix + url.lower()
        except ValueError:
            raise ValueError(f"Error parsing: {url}, {sys.stderr}")

    def line_to_request(self, line: str) -> str:
        """
        Check it's a legit log first. Then use regex or slicing
        to identify each part, we distinguish apache logs from nginx
        when match_refererer_and_ua should be apache acording to
        the actual data. Finally, when we're happy with each
        extracted piece of data call the Request class.
        """
        self.check_right_struct_log(line)
        matches, timestamp, ip_address = self.process_logs(line)
        if matches:
            request = matches.group(1).strip('"')
            response_code = int(matches.group(2))
            content_length = int(matches.group(3))
            referer_and_ua = matches.group(4)
            if match_refererer_and_ua := self.r_n_ua_re.match(referer_and_ua):
                referer = match_refererer_and_ua.group(1)
                user_agent = match_refererer_and_ua.group(2)
            else:
                referer_and_ua = referer_and_ua.split('"', 1)
                referer, user_agent = referer_and_ua
        else:
            raise ValueError("There wasn't any match with the url")

        if len(request.split()) == 3:
            # version is unused, also ignore request if it's missing stuff
            method, url, _ = request.split()
        else:
            return
        parsed_url = self.parse_url(url, self.url_prefix)

        request = Request(
            ip_address,
            timestamp,
            method,
            parsed_url,
            response_code,
            content_length,
            referer,
            user_agent,
        )

        return request

    def check_right_struct_log(self, line: str) -> None:
        """Check for different access logs formats. Types: apache logs,
        nginx logs, will look for a request, a url and a
        user agent."""
        check_any_three = '\\[[^][]*]|"[^"]*"|\\S+'

        try:
            re.compile(check_any_three).match(line)
        except ValueError as err:
            raise ValueError("There is not a match with the regex, ", err)

    def process_logs(self, line: str) -> Tuple:
        """Usually the apache logs' strucure have the ip_adress in
        second position, the nginx will be found in 1st pos. also
        the rest slice would be different. Else, the ip address is not valid."""
        parts = line.split(" ", 4)
        try:
            _, ip_address, _, _, rest = parts
            if self.validate_ip_address(ip_address):
                req_url_and_user_agent = rest[30:]
            else:
                ip_address, _, _, _, rest = parts
                if self.validate_ip_address(ip_address):
                    req_url_and_user_agent = line.split('"')[1:-1]
                    req_url_and_user_agent = '"'.join(req_url_and_user_agent)
                else:
                    raise ValueError(
                        "the line:", line, "does not hold a valid ip addrees"
                    )
        except ValueError as err:
            raise ValueError(err)
        pattern_timestamp = re.compile(r"(?<=\[).*(?=\])")
        if timestamp := re.search(pattern_timestamp, line):
            timestamp = timestamp.group(0)
        else:
            raise ValueError("The line ", line, "does not have a timestamp")
        matches = self.request_re.match(req_url_and_user_agent)
        if not matches:
            matches = re.compile(self.fallback_re).match(req_url_and_user_agent)
        return matches, timestamp, ip_address

    def unzip(self, filename: str) -> gzip:
        file = gzip.open(filename, "r")
        file_content = file.read()
        return file_content

    def validate_ip_address(self, ip_adrress):
        """Validate the ip_address using socket,
        Better approach than REGEX since would validate
        999.999.999.999"""
        try:
            socket.inet_aton(ip_adrress)
            return True
        except:
            return False

    def logfile_names(self) -> Iterator[str]:
        for path in sorted(os.listdir(self.log_dir)):
            """
            Generate a list of matching logfile names in the directory
            Note - can't assume logs start with 'access.log' - e.g. our log
            names have the format <service>_<code>_access.log-<datestamp>.gz
            """
            if "access.log" not in path or not path.endswith(".gz"):
                continue

            """The timestamp in our logs also don't include a '-'
            i.e. they would end like this: access.log-20230602.gz
            """
            match_pattern = re.compile(
                r"(?P<year>\d{4})-?(?P<month>\d{2})-?(?P<day>\d{2})"
            )
            match = match_pattern.search(path)
            if match is None:
                raise AttributeError(
                    "Your file has to have a date at the end of it's name"
                )
            date_dict = match.groupdict()
            timestamp = (
                f"{date_dict['year']}-{date_dict['month']}" f"-{date_dict['day']}"
            )
            try:
                time.strptime(timestamp, "%Y-%m-%d")
            except ValueError:
                continue

            yield os.path.join(self.log_dir, path)

    def lines(self) -> Iterator[str]:
        """Generate a stream of lines from the zipped log files."""
        for logfile in self.logfile_names():
            data = self.unzip(logfile)
            for line in data.splitlines():
                if line:
                    yield line

    def relevant_requests(self) -> Iterator[tuple]:
        """Generate a filtered stream of requests; apply the predicate list
        `self.filters' to these requests; if any predicate fails, ignore
        the request and do not generate it for downstream processing."""
        for line in self.lines():
            if line_request := self.line_to_request(line.decode("utf-8")):
                for filter_group in self.filter_groups:
                    filters, regex = filter_group
                    if not self.filter_in_line_request(filters, line_request):
                        continue
                    line_request.sanitise_url(regex)
                    yield line_request

    def filter_in_line_request(self, filters: list, line_request: str) -> bool:
        """If the filter from make_filters doesn't align with the line_request
        ignore the next iteration in the parent loop."""
        for filter in filters:
            if not filter(line_request):
                return False
        return True

    def __iter__(self):
        for i in self.relevant_requests():
            yield i

    def return_output(self) -> list[str]:
        """Return the results from the filters."""
        return [str(result) for result in self]
