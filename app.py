from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    email = "ghuang26@nmhschool.org"
    phone = "857-500-3746"
    is_student = True
    return render_template("contact.html", email=email, is_student=is_student, phone=phone)
    

@app.route("/about")
def about():
    author = "Grace Huang"
    interests = ["Web development", "Coding", "Web browsing"]
    return render_template("about.html", author=author, interests=interests)

app.run(debug=True)