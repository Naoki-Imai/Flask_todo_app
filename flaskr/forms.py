from wtforms.form import Form
from wtforms.fields import (
  StringField, FileField, PasswordField, SubmitField, HiddenField, TextAreaField
)
from wtforms.validators import DataRequired

class TodoForm(Form):
  todo_name = StringField('タスク名：', validators=[ DataRequired() ])
  submit = SubmitField('追加')