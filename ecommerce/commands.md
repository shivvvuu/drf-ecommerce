secrate key generater:
1. in python django shell(python manage.py shell)
2. from django.core.management.utils import get_random_secret_key
3. print(get_random_secret_key)

pip freeze > requirements.txt

poetry add python python-dotenv 