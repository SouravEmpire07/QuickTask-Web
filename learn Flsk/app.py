from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
    # complition_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"<Todo {self.sno} --> {self.title}"

@app.route("/" , methods = ['GET','POST'])
def hello_sourav_welcome_to_flask():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    # return "<p>Hello, Sourav, Welcome to Flask!</p>"
    # todo = Todo(title="First Todo", desc="Start learning flask and fastAPI")
    # db.session.add(todo)
    # db.session.commit()
    allTodo = Todo.query.all()
    return render_template("index.html", allTodo = allTodo)

@app.route("/show")
def show():
    allTodo = Todo.query.all()
    print(allTodo)
    return "<p>Welcome to Flask get ready!</p>"

if __name__ == "__main__":
    app.run(debug=True)
