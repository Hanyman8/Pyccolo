# aiohttpdemo_polls/views.py
import os
import aiohttp_jinja2
from aiohttp import web


@aiohttp_jinja2.template('index.html')
async def index(request):
    pass


@aiohttp_jinja2.template('mp3.html')
async def store_mp3_handler(request):
    reader = await request.multipart()

    # /!\ Don't forget to validate your inputs /!\

    # reader.next() will `yield` the fields of your form

    field = await reader.next()

    print('1111111111111111111111')
    print(field.filename)
    print('2222222222222222222222')

    # assert field.name == 'name'
    # name = await field.read(decode=True)
    #
    # field = await reader.next()
    # assert field.name == 'mp3'
    filename = field.filename
    # print(f'    {os.path.join("./uploads/mp3/", filename)}')

    # You cannot rely on Content-Length if transfer is chunked.
    size = 0
    with open(os.path.join('./uploads/mp3/', filename), 'wb') as f:
        print('333333333333333')
        while True:
            chunk = await field.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            size += len(chunk)
            f.write(chunk)

    return web.Response(text='{} sized of {} successfully stored'
                             ''.format(filename, size))
