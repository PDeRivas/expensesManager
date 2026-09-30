from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.db.models import Q

# Fetch the active User model (works with default or custom user models)
User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a regular user or a superuser via the console'

    def add_arguments(self, parser):
        # Positional arguments (required)
        parser.add_argument('username', type=str, help='The username for the new account')
        parser.add_argument('password', type=str, help='The password for the new account')
        parser.add_argument('email', type=str, help='The email for the new account')
        
        # Optional flag to trigger superuser creation
        parser.add_argument(
            '--superuser',
            action='store_true',
            help='Create the user as a superuser with admin privileges',
        )

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        email = options['email']
        is_superuser = options['superuser']

        # Prevent duplicate users
        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            raise CommandError(f'Username or email already in use.')

        try:
            if is_superuser:
                # Creates a superuser (is_staff=True, is_superuser=True)
                User.objects.create_superuser(username=username, password=password, email=email)
                self.stdout.write(self.style.SUCCESS(f'Successfully created superuser "{username}"'))
            else:
                # Creates a normal user
                User.objects.create_user(username=username, password=password, email=email)
                self.stdout.write(self.style.SUCCESS(f'Successfully created regular user "{username}"'))
                
        except Exception as e:
            raise CommandError(f'Error creating user: {e}')
