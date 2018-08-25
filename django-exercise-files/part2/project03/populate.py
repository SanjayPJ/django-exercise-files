import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project03.settings')

import django
django.setup()

import random
from users.models import User
from faker import Faker

fakegen = Faker()

for i in range(20):
    fake_first_name = fakegen.first_name()
    fake_last_name = fakegen.last_name()
    fake_email = fakegen.email()
    user1 = User.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email = fake_email)