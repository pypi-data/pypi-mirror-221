import re

from requests.models import Response


def only_successful(request: Response) -> str:
    return request.response_code in [200, 304]


def no_star(request: Response) -> str:
    return request.url != "*"


def method_ok(request: str) -> str:
    return request.method == "GET" or request.method == "POST"


def no_plus_http(request: str) -> str:
    return "+http" not in request.user_agent


def make_filters(regexes: re, excluded: str, spiders: set()) -> list:
    def not_known_spider(request):
        return request.user_agent not in spiders

    def not_excluded_ip(request):
        return request.ip_address not in excluded

    def filter_url(request):
        for regex in regexes:
            if re.search(re.compile(regex), request.url) is not None:
                return True
        return False

    return [
        filter_url,
        only_successful,
        no_star,
        method_ok,
        no_plus_http,
        not_known_spider,
        not_excluded_ip,
    ]
