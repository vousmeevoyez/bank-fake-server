import pytest
from aiohttp import web
from aiojobs.aiohttp import setup as aiojobs_setup


from app import register_routes


@pytest.fixture
def cli(loop, aiohttp_client):
    app = web.Application()
    register_routes(app)
    aiojobs_setup(app)
    return loop.run_until_complete(aiohttp_client(app))
