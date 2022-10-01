"""
create super_user
"""
from ... import models 
from django.core.management import BaseCommand


class Command(BaseCommand):
    """
        Django command to create super_user
    """


    def handle(self, *args, **options):

        self.stdout.write('Checking if superuser exists')
        email = 'myadmin@gmail.com'
        if models.Categories.objects.count() != 0:
            self.stdout.write(f'Categories Created')


        else:
            'we createe each categoryu'
            cats = [
                'Email Marketing','Instagram Markerting','Sales prospect', 'Cusomer retain','Sales Process',
                
                ]
            for cat in cats:
                models.Categories.objects.create(
                    names= cat,
                    slug=cat
                )
            self.stdout.write(f'Created Categories Successfull')

            


    # def  add_arguments(self, parser) -> None:
    #     parser.add_argument('email',type=str,help='enter the admin email')