from flask import Flask, render_template, request, Markup
import data

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    u_Name = request.form.get('Full_Name')
    u_Email = str(request.form.get('Email')).lower()
    u_Password = request.form.get('Password')
    err = data.insertData(u_Name, u_Email, u_Password)
    err = Markup(err)
    print(u_Name, u_Email, u_Password)
    return render_template("index.html", err=err)


@app.route('/welcome/', methods=['GET', 'POST'])
def welcome():
    return render_template("welcome.html")


if __name__ == "__main__":
    app.run(debug=True)
