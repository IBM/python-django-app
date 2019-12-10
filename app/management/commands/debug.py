import subprocess
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'starts dev server without reload; use with an IDE\'s remote debugger'

    def add_arguments(self, parser):
        parser.add_argument('addrport', nargs='?', default='0.0.0.0:3000', help='Optional port number, or ipaddr:port')

    def handle(self, *args, **options):
        cmd = 'python manage.py runserver {0} --noreload'.format(options['addrport'])
        subprocess.call(cmd, shell=True)
