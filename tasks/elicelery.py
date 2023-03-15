from celery import Celery
def makeCelery(app):
    capp = Celery('tasks')
    capp.config_from_object("config.celery")
    capp.autodiscover_tasks(["tasks"])
    class CeleryContext(capp.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    capp.Task = CeleryContext
    return capp

