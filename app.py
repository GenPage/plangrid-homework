import logging
import json
import os

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/hello')
def hello_world() -> str:
    app.logger.debug(f'{request.date} - {request.url}')
    try:
        if request.headers["Accept"].lower() == "application/json":
            return json.dump(f'{"message": "Hello, World"}')
    except KeyError:
        # The header was not present
        pass
    return f'<p>Hello, World</p>\n'


def debug_mode():
    if os.getenv('LOGLEVEL') == 'DEBUG':
        return True
    return False


if __name__ == '__main__':
    app.run(debug=debug_mode(), use_reloader=False)


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
