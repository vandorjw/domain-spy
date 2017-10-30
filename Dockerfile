FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT=True

RUN useradd -c 'django' --home-dir /app -s /bin/bash django
RUN echo 'django:django' | chpasswd

RUN pip install pipenv

COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock
RUN cd /app && pipenv install

COPY ./entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh \
    && chmod a+x /entrypoint.sh \
    && chown django:django /entrypoint.sh

RUN mkdir -p /app/demo
COPY ./demo /app/demo

USER django

WORKDIR /app/demo

EXPOSE 5000
ENTRYPOINT ["/entrypoint.sh"]
