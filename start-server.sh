MAKE_ENV=local


export APP_ENV=${MAKE_ENV}
gunicorn --bind 127.0.0.1:5000 runner:app