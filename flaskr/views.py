import flaskr
from flaskr import forms
from flaskr.models import Todo
from flask import Blueprint, redirect, render_template, flash, request
from flaskr import db
from flask.helpers import url_for
from flaskr.models import Todo
from flaskr.forms import TodoForm



bp = Blueprint('app', __name__, url_prefix='')

############ home ####################
@bp.route('/')
def home():
  return render_template('home.html')

######################################

############ todo ######################
# 一覧表示
@bp.route('/todo')
def show_todo():
  todos = Todo.select_is_done_false()
  done_todo_items = Todo.select_is_done()
  return render_template('show_todo.html', todos=todos, done_todo_items=done_todo_items)

# 作成
@bp.route('/todo/create', methods=['GET', 'POST'])
def create_todo():
  form = TodoForm(request.form)
  if request.method == 'POST' and form.validate():
    todo = Todo(todo_name = form.todo_name.data)
    with db.session.begin(subtransactions=True):
      todo.create_todo()
    db.session.commit()
    flash('Create Todo Success')
    return redirect(url_for('app.show_todo'))
  return render_template('create_todo.html', form=form)

# todo完了
@bp.route('/todo/<int:id>', methods=['GET', 'POST'])
def done_todo(id):
  done_item = Todo.select_todo_by_id(id)
  if request.method == 'POST':
    with db.session.begin(subtransactions=True):
      done_item.todo_is_done()
    db.session.commit()
    flash('タスクを完了しました')
    return redirect(url_for('app.show_todo'))
  return redirect(url_for('app.home'))


########################################