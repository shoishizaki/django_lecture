import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

##FAKE POP SCRIPT
import random
from first_app.models import AccessRecord
from first_app.models import Webpage
from first_app.models import Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.object.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # Create the fake data for entry
        fake_url = fakegen.full_url()
        fake_data = fakegen.data()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.object.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.object.get_or_create(name=webpg,data=fake_data)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete!')