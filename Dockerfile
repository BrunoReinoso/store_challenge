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

RUN apt update -y \
 && apt install -y --no-install-recommends curl vim tree \
 && apt -y autoremove \
 && rm -fr /var/lib/apt/lists/* \
 && rm -fr /var/cache/apt/archives/*

RUN mkdir /tmp/requirements
COPY requirements/* /tmp/requirements/

RUN tree /tmp/requirements \
  && pip install --upgrade pip \
  && pip install -r /tmp/requirements/base.txt \
  && rm -fr /root/.cache

RUN groupadd -r -g "$GID" appuser; useradd -l --create-home -u "$UID" -g "$GID" appuser
WORKDIR /home/appuser
COPY . /home/appuser

RUN /bin/bash -l -c 'chown -R "$UID:$GID" /home/appuser'

USER appuser
RUN echo "User details: $(id)" && ls -la /home/appuser

EXPOSE ${EXPOSE_PORT}

ENTRYPOINT ["/bin/bash", "-c"]

CMD make run-server