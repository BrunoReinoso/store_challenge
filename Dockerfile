FROM python:3.8

# The enviroment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

ARG UID
ARG GID
ARG APP_PORT
ENV EXPOSE_PORT=${APP_PORT}

RUN echo "Container UID: $UID"
RUN echo "Container GID: $GID"
RUN echo "EXPOSE: $EXPOSE_PORT"

RUN mkdir -p /api/

WORKDIR /api
COPY . /api

RUN apt update -y

RUN pip install --upgrade pip \
  && pip install -r requirements/base.txt \
  && rm -fr /root/.cache

ENTRYPOINT ["/bin/bash", "-c"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000/tcp

HEALTHCHECK --interval=6s --timeout=3s CMD wget --quiet --tries=1 --spider http://localhost:8000/ || exit 1
