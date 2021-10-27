FROM python:3.10

ENV PYTHONUNBUFFERED 1

ARG UID
ARG GID

RUN echo "Container UID: $UID"
RUN echo "Container GID: $GID"

RUN groupadd -r -g "$GID" appuser; useradd -l --create-home -u "$UID" -g "$GID" appuser

WORKDIR /home/appuser
COPY . /home/appuser

RUN /bin/bash -l -c 'chown -R "$UID:$GID" /home/appuser'

RUN apt update \
  && apt install -y --no-install-recommends  \
  vim curl apt-file

RUN pip install --upgrade pip \
  && pip install -r requirements/base.txt \
  && rm -fr /root/.cache

EXPOSE 8000

ENTRYPOINT make run-server

