import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project02.settings')

import django
django.setup()

import random
from first_app.models import User
from faker import Faker

fakegen = Faker()

for i in range(20):
    fake_name = fakegen.name()
    fake_date = fakegen.date()
    user1 = User.objects.get_or_create(name = fake_name, date = fake_date)