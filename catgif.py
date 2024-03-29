import os
import random
from flask import Flask, render_template

app = Flask(__name__)

images = [
    "https://raw.githubusercontent.com/manifoldailearning/mlops-with-aws-datascientists/main/Section-11-Docker/images/image1.gif",
    "https://raw.githubusercontent.com/manifoldailearning/mlops-with-aws-datascientists/main/Section-11-Docker/images/image2.gif",
    "https://raw.githubusercontent.com/manifoldailearning/mlops-with-aws-datascientists/main/Section-11-Docker/images/image3.gif",
    "https://raw.githubusercontent.com/manifoldailearning/mlops-with-aws-datascientists/main/Section-11-Docker/images/image4.gif",
    "https://raw.githubusercontent.com/manifoldailearning/mlops-with-aws-datascientists/main/Section-11-Docker/images/image5.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))