
#!/bin/sh

python manage.py migrate
python manage.py createSuperuser
python manage.py create_category