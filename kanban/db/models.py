from . import DB


class Kanban(DB.Model):
    id_ = DB.Column(DB.Integer, primary_key=True)
    task = DB.Column(DB.String(100))
    stage = DB.Column(DB.String(20))
