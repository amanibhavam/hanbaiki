FROM python:3.10

COPY requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt

COPY --chown=app:app app app

ENTRYPOINT [ "hypercorn" ]

CMD [ "--reload", "--worker-class", "trio", "--bind", "0.0.0.0:8000", "app.main:app"  ]
