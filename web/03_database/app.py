from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///messages.db'


from model import Message

db.create_all()


@app.route('/')
def hello_world():
    messages = list(Message.query.all())
    return render_template("messages.html", msgs=messages)


@app.route('/add_message', methods=["GET", "POST"])
def add_message():
    if request.method == "GET":
        return render_template("add_message.html")
    else:
        msg = Message()
        msg.sender = request.form["username"]
        msg.contents = request.form["contents"]
        db.session.add(msg)
        db.session.commit()
        return redirect("/")

if __name__ == '__main__':
    app.run()
