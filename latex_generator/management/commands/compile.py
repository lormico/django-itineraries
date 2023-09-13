import subprocess

from django.conf import settings
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        p = subprocess.Popen(["xelatex.exe",
                              "-synctex=1",
                              "-interaction=nonstopmode",
                              "-output-directory=output",
                              "itinerario.tex"],
                             cwd=settings.LATEX_DIR)
        p.wait()
