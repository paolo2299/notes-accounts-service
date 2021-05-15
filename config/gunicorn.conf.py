import os

_env = os.environ['NOTES_ENV']

bind = "0.0.0.0:8080"
workers = 1
threads = 4
loglevel = 'info'
accesslog = '-'
if _env == 'development':
    reload = True