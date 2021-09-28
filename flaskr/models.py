from flaskr import db
from datetime import date, datetime

class Category(db.Model):

  __tablename__ = 'categories'

  id = db.Column(db.Integer, primary_key=True)
  category_name = db.Column(db.String(20), index=True, nullable=False, unique=True,)
  create_at = db.Column(db.DateTime, default=datetime.now)
  update_at = db.Column(db.DateTime, default=datetime.now)

  def __init__(self, category_name):
    self.category_name = category_name

  @classmethod
  def select_all_category(cls):
    return cls.query.all()
  
  def create_category(self):
    db.session.add(self)

class Todo(db.Model):

  __tablename__ = 'todos'

  id = db.Column(db.Integer, primary_key=True)
  todo_name = db.Column(db.String(64), index=True, nullable=False)
  create_at = db.Column(db.DateTime, default=datetime.now)
  update_at = db.Column(db.DateTime, default=datetime.now)
  limit_date = db.Column(db.DateTime, nullable=False)
  category_id = db.Column(db.ForeignKey('categories.id'), nullable=False)
  is_done = db.Column(db.Boolean, default=False)

  def __init__(self, todo_name, limit_date, category_id):
    self.todo_name = todo_name
    self.limit_date = limit_date
    self.category_id = category_id

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

