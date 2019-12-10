FROM registry.access.redhat.com/ubi8/python-36

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

## NOTE - rhel enforces user container permissions stronger ##
USER root
RUN yum install python3-pip wget

RUN pip install --upgrade pip \
  && pip install --upgrade pipenv\
  && pip install --upgrade -r /tmp/requirements.txt

USER 1001

COPY . /app
CMD ["gunicorn", "-b", "0.0.0.0:3000", "--env", "DJANGO_SETTINGS_MODULE=pythondjangoapp.settings.production", "pythondjangoapp.wsgi", "--timeout 120"]
