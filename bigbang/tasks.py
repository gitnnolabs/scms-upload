import logging

from django.contrib.auth import get_user_model

from bigbang import tasks_scheduler
from bigbang.setup import setup
from config import celery_app

User = get_user_model()


def _get_user(user_id, username):
    if user_id:
        return User.objects.get(pk=user_id)
    if username:
        return User.objects.get(username=username)


@celery_app.task(bind=True)
def task_start(
    self, user_id=None, username=None, file_path=None, enable=False,
    config=None
):
    user = _get_user(user_id, username)

    if file_path or config:
        setup(user, file_path, config)

    tasks_scheduler.schedule_publication_subtasks(username, enabled=enable)
    tasks_scheduler.schedule_migration_subtasks(username, enabled=enable)
    tasks_scheduler.schedule_task_synchronize_to_pid_provider(username, enabled=enable)
