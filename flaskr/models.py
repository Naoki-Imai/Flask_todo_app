from flaskr import db
from datetime import date, datetime

class Todo(db.Model):

  __tablename__ = 'todos'

  id = db.Column(db.Integer, primary_key=True)
  todo_name = db.Column(db.String(64), index=True, nullable=False)
  create_at = db.Column(db.DateTime, default=datetime.now)
  update_at = db.Column(db.DateTime, default=datetime.now)
  limit_date = db.Column(db.DateTime)
  is_done = db.Column(db.Boolean, default=False)

  def __init__(self, todo_name, limit_date):
    self.todo_name = todo_name
    self.limit_date = limit_date

  @classmethod
  def select_all_todo(cls):
    return cls.query.all()
  
  @classmethod
  def select_todo_by_id(cls, id):
    return cls.query.filter_by(id=id).first()

  def create_todo(self):
    db.session.add(self)
  
  def update_todo(self, todo_name, limit_date):
    self.todo_name = todo_name
    self.limit_date = limit_date
    # self.update_at = datetime.now()
  # todoのis_doneをTrue
  def todo_is_done(self):
    self.is_done = True
    # self.update_at = datetime.now
  # 完了Todoをselect
  @classmethod
  def select_done_todo(cls):
    return cls.query.filter(cls.is_done == True).all()

  # 削除
  @classmethod
  def delete_todo(cls, id):
    return cls.query.filter(id=id).delete()

  # is_doneがTrueをselect
  @classmethod
  def select_is_done(cls):
    return cls.query.filter(cls.is_done == True).all()

  # is_doneがFalseをselect
  @classmethod
  def select_is_done_false(cls):
    return cls.query.filter(cls.is_done == False).all()