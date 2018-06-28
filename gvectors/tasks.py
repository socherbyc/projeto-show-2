import time

from celery import shared_task

from .models import GVector


@shared_task
def process_gvector(gvector_id):
    gvector = GVector.objects.get(id=gvector_id)
    gvector.is_processing = True
    gvector.save()

    total = 100
    for i in range(total):
        time.sleep(0.3)
        GVector.objects.filter(id=gvector_id).update(percentage=(i + 1)/100)

    GVector.objects.filter(id=gvector_id).update(is_in_queue=False)    
    GVector.objects.filter(id=gvector_id).update(is_processing=False)

    return '{} random users created with success!'.format(total)