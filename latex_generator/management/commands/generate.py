import os

from django.conf import settings
from django.core.management import BaseCommand
from django.template.backends.jinja2 import Template
from django.template.loader import get_template

from data.models import Stay, Tranche


def save_generated(file_name, content):
    os.makedirs(settings.LATEX_GENERATED_DIR, exist_ok=True)
    with open(settings.LATEX_GENERATED_DIR / file_name, 'w', encoding='utf-8') as output:
        output.write(content)


class Command(BaseCommand):
    help = "Genera i documenti LaTeX per l'itinerario"

    def handle(self, *args, **options):
        tranches = Tranche.objects.all().order_by("order")
        template: Template = get_template("tranches.tex")
        rendered = template.render(context={"tranches": tranches})
        save_generated("tranches.tex", rendered)

        for tranche in tranches:
            stays = Stay.objects.filter(tranche=tranche)
            template = get_template("tranche.tex")
            rendered = template.render(context={"tranche": tranche, "stays": stays})
            save_generated(f"{tranche.id}.tex", rendered)
