from aiohttp import web


def hello(request):
    return web.Response(text="Hello, world")