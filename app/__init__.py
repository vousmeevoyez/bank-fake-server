"""
    AIOHTTP Entrypoint
    ____________________
"""
from aiohttp import web
from aiohttp_apispec import setup_aiohttp_apispec, validation_middleware
from aiojobs.aiohttp import setup as setup_aiojobs

from app.routes import setup_routes


def register_routes(app):
    setup_routes(app)


# init app
async def init_app(argv=None):
    """ create aiohttp instance """
    app = web.Application()
    # register all known routes here
    register_routes(app)

    setup_aiohttp_apispec(app)
    setup_aiojobs(app)
    app.middlewares.append(validation_middleware)
    return app
