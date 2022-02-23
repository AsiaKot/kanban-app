from flask import render_template, url_for, redirect, request

from kanban.db import DB
from kanban.db.models import Kanban
from . import SERVER_BLUEPRINT


@SERVER_BLUEPRINT.route("/")
def home_page():
    kanban_tb = Kanban.query.all()
    return render_template("index.html", kanban_tb=kanban_tb)


@SERVER_BLUEPRINT.route("/add", methods=["POST"])
def add_task():
    new_task = Kanban(task=request.form.get("new_task"), stage="ToDo")
    DB.session.add(new_task)
    DB.session.commit()
    return redirect(url_for(".home_page"))


@SERVER_BLUEPRINT.route("/delete/<int:id_>")
def delete_task(id_):
    task2delete = Kanban.query.filter_by(id_=id_).first()
    DB.session.delete(task2delete)
    DB.session.commit()
    return redirect(url_for(".home_page"))


@SERVER_BLUEPRINT.route("/move_to/<stage>/<int:id_>")
def move_to(stage, id_):
    task2move = Kanban.query.filter_by(id_=id_).first()
    task2move.stage = stage
    DB.session.commit()
    return redirect(url_for(".home_page"))
