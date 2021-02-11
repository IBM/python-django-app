FROM registry.access.redhat.com/ubi8:8.3

WORKDIR /app

COPY Pipfile* /app/

## NOTE - rhel enforces user container permissions stronger ##
USER root
RUN yum -y install python3
RUN yum -y install python3-pip wget

RUN pip3 install --upgrade pip==21.0.1 \
  && pip3 install --upgrade pipenv==2020.11.15 \
  && pipenv install --system --deploy

USER 1001

COPY . /app

ENV PORT 3000

EXPOSE 3000

CMD ["python3", "manage.py", "start"]
