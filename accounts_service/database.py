import os

from flask_sqlalchemy import SQLAlchemy

_connector = 'mysql+mysqlconnector'
_env = os.environ['NOTES_ENV']
_host = ''
_user = os.environ['MYSQL_USER']
_password = os.environ['MYSQL_PASSWORD']
_database = os.environ['MYSQL_DATABASE']
_query = ''

if _env == 'development':
    _host = os.environ['MYSQL_HOST']
else:
    _instance_name = os.environ['INSTANCE_CONNECTION_NAME']
    _query = f"unix_socket=/cloudsql/{_instance_name}"

connection_uri = f"{_connector}://{_user}:{_password}@{_host}/{_database}?{_query}"

db = SQLAlchemy()
