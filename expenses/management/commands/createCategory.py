from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from expenses.repositories.categoryRepository import CategoryRepository
from expenses.models import Category

class Command(BaseCommand):
    help = 'Creates a category for either expense or income via command console'
    repo = CategoryRepository()

    def add_arguments(self, parser):
        # Positional arguments (required)
        parser.add_argument('name', type=str, help='The name of the new category')
        
        # Optional flag to trigger superuser creation
        parser.add_argument(
            'categoryType',
            type=str,
            choices=['expense', 'income'],
            help='Set the type of category; for expense or income',
        )

    def handle(self, *args, **options):
        name = options['name']
        categoryType = options['categoryType']

        # Prevent duplicate users
        if Category.objects.filter(Q(name=name) & Q(categoryType=categoryType)).exists():
            raise CommandError(f'Category {name} for {categoryType} already exists.')

        try:
            self.repo.create(name=name, categoryType=categoryType)
            self.stdout.write(self.style.SUCCESS(f'Succesfully created {name} category'))
                
        except Exception as e:
            raise CommandError(f'Error creating category: {e}')
