from django.core.management.base import BaseCommand
from customer_manager.models import Customer
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'This command adds 10 test customers to the database.' \
           'You can override this number with the --total argument.' \
           'Use the -r or --random flag to randomize the customer names'

    def add_arguments(self, parser):
        # Optional argument
        parser.add_argument('--number_of_customers', type=int, help='Number of customers to create')

        # Flag argument
        parser.add_argument('-r', '--random', action='store_true', help='Randomize the customer namez')

    def handle(self, *args, **kwargs):
        number_of_customers = kwargs['number_of_customers']
        random = kwargs['random']

        if not number_of_customers:
            number_of_customers = 10

        for i in range(number_of_customers):
            if random:
                name = get_random_string()
            else:
                name = 'Customer ' + str(i + 1)

            customer = Customer(name=f'{name}')
            customer.save()
            self.stdout.write(self.style.SUCCESS(f'Customer {name} created with ID {customer.id}'))