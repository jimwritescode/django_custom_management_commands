from django.core.management.base import BaseCommand
from customer_manager.models import Customer


class Command(BaseCommand):
    help = 'This command tries to delete the specified customer IDs. Pass IDs in separated by spaces. ' \
           'Ex: "delete_customers_by_id 1 2 3" will delete customers with IDs 1, 2, and 3 (assuming they exist)'

    def add_arguments(self, parser):
        parser.add_argument('customer_id', nargs='+', type=int, help='Customer ID')

    def handle(self, *args, **kwargs):
        customer_ids = kwargs['customer_id']

        for customer_id in customer_ids:
            try:
                Customer.objects.get(pk=customer_id).delete()
                self.stdout.write(self.style.SUCCESS(f'Customer ID {customer_id} deleted successfully!'))
            except Customer.DoesNotExist:
                self.stderr.write(self.style.ERROR(f'Customer ID {customer_id} not found.'))