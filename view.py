from app import *
from forms import *

#-- Home and about
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

#-- Updates
@app.route("/updates")
def updates():
    return render_template("updates.html")

#-- Contact me
@app.route("/contact_me", methods=["POST","GET"])
def contact_me():
    form = MessageForm()
    if form.validate_on_submit():
        message = form.message.data
        name = form.name.data
        email = form.email.data
        send_mail("khashayarpycodes@gmail.com",name +", "+email+", "+message)
        return render_template("email_sent.html")
    return render_template("contact_me.html", form=form)

#-- Flask
@app.route("/projects/flask_page")
def flask_page():
    return render_template("flask_page.html")
#-- Tkinter
@app.route("/projects/tkinter")
def tkinter():
    return render_template("tkinter.html")

@app.route("/projects/tkinter_2")
def tkinter_2():
    return render_template("tkinter_2.html")

@app.route("/projects/tkinter_3")
def tkinter_3():
    return render_template("tkinter_3.html")


@app.route("/projects/tkinter_4")
def tkinter_4():
    return render_template("tkinter_4.html")

@app.route("/projects/tkinter_5")
def tkinter_5():
    return render_template("tkinter_5.html")



#-- Socket
@app.route("/projects/socket")
def socket():
    return render_template("socket.html")

@app.route("/projects/socket_2")
def socket_2():
    return render_template("socket_2.html")

@app.route("/projects/socket_3")
def socket_3():
    return render_template("socket_3.html")

@app.route("/projects/socket_4")
def socket_4():
    return render_template("socket_4.html")
#-- Turtle
@app.route("/projects/pygame_turtle")
def pygame_turtle():
    return render_template("pygame_turtle.html")

#-- OS
@app.route("/projects/os")
def os():
    return render_template("os.html")

#-- SQLite
@app.route("/projects/sqlite")
def sqlite():
    return render_template("sqlite.html")

@app.route("/projects/sqlite_2")
def sqlite_2():
    return render_template("sqlite_2.html")

@app.route("/projects/sqlite_3")
def sqlite_3():
    return render_template("sqlite_3.html")


if __name__ == '__main__':
    app.run(debug=True)
