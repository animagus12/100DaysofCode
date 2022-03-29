import requests
import smtplib
from flask import Flask, render_template, request

app = Flask(__name__)

BLOG_URL = 'https://api.npoint.io/c790b4d5cab58020d391'
responses = requests.get(BLOG_URL).json()

my_email = "neongen18@gmail.com"
password = "Sbp@2001"

@app.route('/')
def home():
    return render_template('index.html', all_posts=responses)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password= password)
            connection.sendmail(
                from_addr= email, 
                to_addrs= "subhrajit_panda@yahoo.com", 
                msg= f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}")


        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)


@app.route('/post/<int:index>')
def post(index):
    response = None
    for response in responses:
        if response["id"] == index:
            requested_post = response
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
