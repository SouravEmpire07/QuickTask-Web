from flask import Flask,render_template, request, redirect
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
    type = db.Column(db.String(50), nullable=False, default='General')
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"<Todo {self.sno} --> {self.title}"

@app.route("/" , methods = ['GET','POST'])
def hello_sourav_welcome_to_flask():
    filter_type = request.args.get('filter')
    
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo_type = request.form.get('type', 'General')
        todo = Todo(title=title, desc=desc, type=todo_type)
        db.session.add(todo)
        db.session.commit()

    if filter_type:
        allTodo = Todo.query.filter_by(type=filter_type).all()
    else:
        allTodo = Todo.query.all()
        
    return render_template("index.html", allTodo = allTodo)

@app.route("/show")
def show():
    allTodo = Todo.query.all()
    print(allTodo)
    return "<p>Welcome to Flask get ready!</p>"

@app.route("/update/<int:sno>", methods = ['GET','POST'])
def update(sno):
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo_type = request.form.get('type', 'General')
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        todo.type = todo_type
        db.session.add(todo)
        db.session.commit() 
        return redirect("/")
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html", todo = todo)

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
