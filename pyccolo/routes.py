# aiohttpdemo_polls/routes.py
from views import index, store_mp3_handler

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_post('/mp3.html', store_mp3_handler)