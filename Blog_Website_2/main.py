from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    blog_response = requests.get(url="https://api.npoint.io/674f5423f73deab1e9a7")
    blog_data = blog_response.json()
    title_one = blog_data[0]["title"]
    title_two = blog_data[1]["title"]
    title_three = blog_data[2]["title"]
    subtitle_one = blog_data[0]["title"]
    subtitle_two = blog_data[1]["subtitle"]
    subtitle_three = blog_data[2]["subtitle"]

    curr_year = datetime.datetime.now().year
    return render_template('index.html', year=curr_year, title_1=title_one, subtitle_1=subtitle_one, title_2=title_two, subtitle_2=subtitle_two, title_3=title_three, subtitle_3=subtitle_three)

@app.route("/about")
def about():
     return render_template('about.html')

@app.route("/contact")
def contact():
     return render_template('contact.html')

@app.route("/post")
def get_post():
     return render_template('post.html')

if __name__ == "__main__":
    app.run(debug=True)
