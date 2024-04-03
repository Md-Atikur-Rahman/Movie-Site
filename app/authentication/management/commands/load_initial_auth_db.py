
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

from core.utils import load_users


USER_ADMIN = 'admin'
PASSWORD = 'pass'


def create_general_users(self, users):
    for user in users:
        full_name = user['name']
        first_name, last_name = full_name.split()
        phone = user['phone']
        email = user['email']
        password = user['password']
        # print(first_name, last_name, phone, email, password)

        if not User.objects.filter(username=email).exists():
            new_user = User.objects.create_user(
                username=email, email=email, password=password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created user: {email} password: {password}'))
        else:
            self.stdout.write(self.style.WARNING(
                f'User {email} already exists. Skipping...'))


def create_super_user(self):
    username = USER_ADMIN
    password = PASSWORD

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, password=password)
        self.stdout.write(self.style.SUCCESS(
            f'Superuser\n\t email:\t\t {username}\n\t password:\t {password}'))
    else:
        self.stdout.write(self.style.WARNING(
            f'User {username} already exists. Skipping...'))


class Command(BaseCommand):
    help = 'Creates a user'

    def handle(self, *args, **kwargs):
        users = load_users()
        create_general_users(self, users)
        create_super_user(self)
