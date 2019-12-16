import logging
import json

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def main():
    return ''


@app.route('/hello', methods=['GET', 'POST'])
def hello_world() -> str:
    app.logger.debug(f'{request.date} - {request.url}')
    try:
        if request.headers["Accept"].lower() == "application/json":
            return json.dumps('{"message": "Hello, World"}')
    except KeyError:
        # The header was not present
        pass
    return f'<p>Hello, World</p>\n'


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
