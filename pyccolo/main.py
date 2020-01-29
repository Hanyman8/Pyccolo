# pyccolo/main.py

import logging
from aiohttp import web
import aiohttp_jinja2
import jinja2

from settings import BASE_DIR
from routes import setup_routes

# from db import close_pg, init_pg

app = web.Application()
logging.basicConfig(level=logging.DEBUG)
# app['config'] = config   # todo: will I use DB?
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR / 'pyccolo' / 'templates')))
setup_routes(app)
# app.on_startup.append(init_pg)
# app.on_cleanup.append(close_pg)
web.run_app(app)