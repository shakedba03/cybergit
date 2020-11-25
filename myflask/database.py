from model import Base, ToDo
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_task(content, date):
    session = DBSession()
    task_object = ToDo(
    content = content,
    date = date)
    session.add(task_object)
    session.commit()

def return_all_tasks():
    session = DBSession()
    tasks = session.query(ToDo).all()
    return tasks

def return_task(id):
    session = DBSession()
    task = session.query(ToDo).filter_by(id = id).first()
    return task

def edit_task(id, edited_content):
    #session = DBSession()
    task_object = session.query(ToDo).filter_by(id = id).first()
    print(task_object)
    task_object.content = edited_content
    session.commit()
  

def delete_task(task_id):
    session = DBSession()
    session.query(ToDo).filter_by(id=task_id).delete()
    session.commit()


