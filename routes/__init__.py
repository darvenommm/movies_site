from http.server import BaseHTTPRequestHandler as HTTPRequest
from typing import Callable, TypeAlias

from . import paths

from controllers.movies import MoviesController
from controllers.movies_api import MoviesApiController
from controllers.assets import AssetsController


RoutesType: TypeAlias = dict[str, dict[str, Callable[[HTTPRequest], None]]]


routes_config: RoutesType  = {
    'HEAD': {},
    'GET': {
        paths.home: MoviesApiController.get_all,
        paths.movies_api: MoviesApiController.get_all,
        paths.movies_api_one: MoviesApiController.get_one,

        paths.movies: MoviesController.get_all,

        paths.styles: AssetsController.get_styles,
    },
    'POST': {
        paths.movies: MoviesController.create,
    },
    'PUT': {
        paths.movies_one: MoviesController.change,
    },
    'DELETE': {
        paths.movies_one: MoviesController.delete,
    },
}


# for creating path like '^{}$' for regex
cached_routes: RoutesType = {}
for method, routes_ in routes_config.items():
    cached_routes[method] = {}

    for path, handler in routes_.items():
        cached_routes[method][rf'^{path}$'] = handler


routes: RoutesType = cached_routes


__all__ = ('routes',)
