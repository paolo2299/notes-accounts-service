FROM python:3.9.0-buster

ENV PIPENV_VENV_IN_PROJECT 1
ENV PORT 8080

WORKDIR /app
RUN pip install pipenv
COPY Pipfile* /app/
RUN pipenv install

ENV PYTHONUNBUFFERED TRUE
ENV FLASK_APP "accounts_service:create_app()"

EXPOSE 8080
COPY . /app/

CMD ["pipenv", "run", "gunicorn", "-c", "config/gunicorn.conf.py", "accounts_service:create_app()"]
