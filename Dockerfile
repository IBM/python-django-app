FROM registry.access.redhat.com/ubi8/python-39:1

WORKDIR /opt/app-root/src

COPY Pipfile* /opt/app-root/src/

## NOTE - rhel enforces user container permissions stronger ##
USER root
RUN yum -y install wget

RUN pip3 install --upgrade pip==21.0.1 \
  && pip3 install --upgrade pipenv==2020.11.15 \
  && pipenv install --system --deploy

USER 1001

COPY . /opt/app-root/src

ENV PORT 3000

EXPOSE 3000

CMD ["python3", "manage.py", "start"]
