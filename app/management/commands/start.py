import subprocess
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'runs server with gunicorn in a production setting'

    def add_arguments(self, parser):
        parser.add_argument('addrport', nargs='?', default='0.0.0.0:3000', help='Optional ipaddr:port')

    def handle(self, *args, **options):
        cmd = ['gunicorn', '-b', options['addrport'], 'pythondjangoapp.wsgi']
        subprocess.call(cmd)
