from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/form-acceptor', methods=["POST"])
def accept():
    name = request.form["userName"]
    surname = request.form["userSurname"]
    pw = request.form["password"]
    if pw == "qwerty":
        return render_template("display.html",
                               name=name,
                               surname=surname)
    else:
        return render_template("denied.html")


if __name__ == '__main__':
    app.run()
