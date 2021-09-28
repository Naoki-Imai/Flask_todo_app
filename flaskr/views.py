from flaskr.models import Todo
from flask import Blueprint, redirect, render_template, flash, request
from flaskr import db
from flask.helpers import url_for
from flaskr.models import Todo
from flaskr.forms import TodoForm
from datetime import date, datetime


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
  for todo in todos:
    todo.limit_date = todo.limit_date .strftime('%Y-%m-%d')
  #   print(f'after:{type(todo.limit_date)}')
  done_todo_items = Todo.select_is_done()
  for done_todo in done_todo_items:
    done_todo = done_todo.limit_date.strftime('%Y-%m-%d')
  # today = date.today()
  return render_template('show_todo.html', todos=todos, done_todo_items=done_todo_items)

# 作成
@bp.route('/todo/create', methods=['GET', 'POST'])
def create_todo():
  form = TodoForm(request.form)
  limit_date = date.today()
  if request.method == 'POST' and form.validate():
    todo = Todo(
      todo_name = form.todo_name.data,
      limit_date = form.limit_date.data)
    with db.session.begin(subtransactions=True):
      todo.create_todo()
    db.session.commit()
    flash('Create Todo Success')
    return redirect(url_for('app.show_todo'))
  return render_template('create_todo.html', form=form, limit_date=limit_date)

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

@bp.route('/todo/<int:id>/update', methods=['GET', 'POST'])
def update_todo(id):
  todo = Todo.select_todo_by_id(id)
  form = TodoForm(request.form)
  if request.method == 'POST' and form.validate():
    with db.session.begin(subtransactions=True):
      todo.update_todo(form.todo_name.data)
    db.session.commit()
    flash('タスクを更新しました')
    return redirect(url_for('app.show_todo'))
  return render_template('update_todo.html', form=form, todo=todo)


########################################