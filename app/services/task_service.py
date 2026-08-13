from functools import wraps

from app.database import SessionLocal
from app.models import Task


def with_database_session(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        session = SessionLocal()
        try:
            return function(session, *args, **kwargs)
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    return wrapper


@with_database_session
def create_task(session, task):
    new_task = Task(
        title=task.title,
        completed=task.completed,
    )

    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task


@with_database_session
def get_task_by_id(session, task_id: int):
    return session.query(Task).filter(Task.id == task_id).first()


@with_database_session
def get_tasks_by_completed(session, completed: bool | None):
    if completed is None:
        return session.query(Task).all()
    return session.query(Task).filter(Task.completed == completed).all()


@with_database_session
def update_task(session, task_id: int, updated_task):
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None

    task.title = updated_task.title
    task.completed = updated_task.completed
    session.commit()
    session.refresh(task)
    return task


@with_database_session
def delete_task(session, task_id: int):
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        return False

    session.delete(task)
    session.commit()
    return True
