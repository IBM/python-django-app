import subprocess
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'compiles python files in project into .pyc binaries'

    def handle(self, *args, **options):
        cmd = ['python', '-m', 'compileall', '.']
        subprocess.call(cmd)
