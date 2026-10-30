from django.core.management.base import BaseCommand
from djangoapp.models import Dealer, Review, CarMake, CarModel
class Command(BaseCommand):
    help = "Load sample dealership data"
    def handle(self, *args, **kwargs):
        dealer, _ = Dealer.objects.get_or_create(full_name="Kansas City Auto Center",
            defaults={"address":"100 Main Street","city":"Kansas City","state":"Kansas","phone":"555-0100"})
        Review.objects.get_or_create(dealer=dealer, review="Fantastic services", defaults={"name":"Demo Customer"})
        for make_name, models in {"Toyota":["Camry","Corolla"],"Honda":["Civic","Accord"],"Ford":["Mustang","F-150"]}.items():
            make, _ = CarMake.objects.get_or_create(name=make_name)
            for model in models: CarModel.objects.get_or_create(make=make, name=model)
        Dealer.objects.get_or_create(full_name="Wichita Motors", defaults={"city":"Wichita","state":"Kansas"})
        self.stdout.write(self.style.SUCCESS("Demo data loaded"))
