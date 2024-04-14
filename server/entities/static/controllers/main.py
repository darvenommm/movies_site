from functools import lru_cache
from http.server import BaseHTTPRequestHandler as HTTPRequest
from os import getcwd

from common.http import http_statuses


class StaticController:
    @classmethod
    def load_styles(cls, request: HTTPRequest) -> None:
        request.send_response(http_statuses.OK)
        request.send_header('Content-Type', 'text/css')
        request.end_headers()

        request.wfile.write(cls.__get_file_text('server/static/styles/styles.css'))

    @classmethod
    def load_movies_js(cls, request: HTTPRequest) -> None:
        request.send_response(http_statuses.OK)
        request.send_header('Content-Type', 'application/javascript')
        request.end_headers()

        request.wfile.write(cls.__get_file_text('server/static/js/movies.js'))

    @staticmethod
    @lru_cache
    def __get_file_text(path: str) -> bytes:
        with open(f'{getcwd()}/{path}') as text_file:
            return text_file.read().encode()
