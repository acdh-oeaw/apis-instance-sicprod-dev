import json
from pathlib import Path

from django.core.management.base import BaseCommand
from apis_core.apis_relations.models import Property
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = "Import properties from data/properties.json"

    def handle(self, *args, **options):
        base_path = Path(__file__).resolve().parent.parent.parent.parent
        properties_json = base_path / "data/properties.json"
        data = json.loads(properties_json.read_text())

        for p in data:
            prop, created = Property.objects.get_or_create(pk=p["id"])
            prop.name = p["name"]
            prop.name_reverse = p["name_reverse"]
            prop.save()
            prop.obj_class.clear()
            for obj in p["obj"]:
                prop.obj_class.add(ContentType.objects.get(model=obj))
            prop.subj_class.clear()
            for subj in p["subj"]:
                prop.subj_class.add(ContentType.objects.get(model=subj))
            if created:
                print(f"Created {prop}")
            else:
                print(f"Updated {prop}")
