import os, subprocess
from django.core.management.base import BaseCommand

# Tip from:
# https://github.com/dpgaspar/Flask-AppBuilder/issues/733#issuecomment-379009480
PORT = int(os.environ.get("PORT", 3000))

class Command(BaseCommand):
    help = 'runs server with gunicorn in a production setting'

    def add_arguments(self, parser):
        parser.add_argument('addrport', nargs='?', default='0.0.0.0:' + str(PORT), help='Optional ipaddr:port')

    def handle(self, *args, **options):
        cmd = ['gunicorn', '-b', options['addrport'], 'pythondjangoapp.wsgi']
        subprocess.call(cmd)
