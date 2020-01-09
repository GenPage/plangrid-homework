import logging

from datetime import datetime
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


def format_time():
    dt = datetime.now()
    return dt.strftime("%m/%d/%Y, %H:%M:%S")


def localized(lang: str) -> str:
    if lang == 'es':
        return 'Hola'
    else:
        return 'Hello'


@app.route('/<name>', methods=['GET'])
def hello(name: str) -> str:
    app.logger.debug(f'{format_time} - {request.url}')
    local = localized(request.args.get('lang'))
    format_time()
    try:
        if request.headers["Accept"].lower() == "application/json":
            return jsonify({"message": f"{local}, {name}!"})
    except KeyError:
        # The header was not present
        pass
    return f"<p>{local}, {name}</p>\n"


if __name__ == '__main__':
    app.run(debug=True)


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
