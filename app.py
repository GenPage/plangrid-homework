import logging

from datetime import datetime
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


def format_time():
    dt = datetime.now()
    return dt.strftime("%m/%d/%Y, %H:%M:%S")


@app.route('/hello', methods=['GET', 'POST'])
def hello_world() -> str:
    app.logger.debug(f'{format_time} - {request.url}')
    try:
        if request.headers["Accept"].lower() == "application/json":
            return jsonify({"message": "Hello, World!"})
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
