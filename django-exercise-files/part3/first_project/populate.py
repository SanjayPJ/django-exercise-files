import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Subscriber
from faker import Faker

fakegen = Faker()

for i in range(20):
    fake_name = fakegen.name()
    fake_email = fakegen.email()
    fake_url = fakegen.url()
    user1 = Subscriber.objects.get_or_create(name = fake_name, email = fake_email, url = fake_url)