from app import app
from tasks.elicelery import makeCelery
celery_obj = makeCelery(app)
__all__ = ("celery_obj")
