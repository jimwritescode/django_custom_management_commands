from django.core.management.base import BaseCommand
from customer_manager.models import Customer


class Command(BaseCommand):
    help = 'This command deletes all customer records from the database'

    def handle(self, *args, **options):
        number_of_customers = Customer.objects.count()
        Customer.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'{number_of_customers} customers were deleted!'))