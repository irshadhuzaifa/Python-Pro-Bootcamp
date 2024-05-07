from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response_data = response.json()
    all_posts = response_data
    return render_template("index.html", blogs=all_posts)

@app.route('/blog')
def get_blog():
    post_url= "https://api.npoint.io/c790b4d5cab58020d391"
    post_response = requests.get(post_url)
    post_data = post_response.json()
    blog_posts = post_data
    return render_template("post.html", posts=blog_posts)

if __name__ == "__main__":
    app.run(debug=True)

