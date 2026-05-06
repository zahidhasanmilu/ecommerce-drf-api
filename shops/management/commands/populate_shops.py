# shop/management/commands/populate_shops.py
from django.core.management.base import BaseCommand
from shops.models import Shop
from accounts.models import User
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = "Populate DB with dummy Shop data."

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of shops to create',
        )

    def handle(self, *args, **options):
        count = options['count']
        
        users = list(User.objects.filter(role='owner')) 
        
        if not users:
            self.stdout.write(
                self.style.WARNING("No users with 'owner' role found. Please create Shop Owners first.")
            )
            return

        self.stdout.write(f"Creating {count} dummy shops for owners...")

        for _ in range(count):
            try:
                owner = random.choice(users)
                shop_name = "BRAND " + fake.company() + str(random.randint(10, 99))
                
                shop = Shop(
                    owner=owner,
                    name=shop_name,
                    description=fake.text(max_nb_chars=300),
                )
                shop.save()
                self.stdout.write(self.style.SUCCESS(f"Shop '{shop_name}' created for owner '{owner.username}'."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error: {e}"))
                continue

        self.stdout.write(
            self.style.SUCCESS(f"--- {count} dummy shops created successfully! ---")
        )