from . import celery_obj

@celery_obj.task
def echodoc():
    print("fdsfdsfdsfd")
