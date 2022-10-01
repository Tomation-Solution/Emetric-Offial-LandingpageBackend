"""
create super_user
"""
from ...models import User

from django.core.management import BaseCommand


class Command(BaseCommand):
    """
        Django command to create super_user
    """


    def handle(self, *args, **options):

        self.stdout.write('Checking if superuser exists')
        email = 'myadmin@gmail.com'
        if User.objects.filter(email=email).exists():
            self.stdout.write(f'Super Admin Already Exists -> {email}')

        else:
            'since the user does not exists we create the user'
            super_user = User.objects.create_superuser(
                email = email,
                password ='backup2020',
                first_name=' ',
                last_name=' ',
            )
            self.stdout.write(f'Super Admin Created Succesful ->email:{email},password:backup2020')

            


    # def  add_arguments(self, parser) -> None:
    #     parser.add_argument('email',type=str,help='enter the admin email')