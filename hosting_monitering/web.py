from flask import Flask, render_template
import os
app = Flask(__name__)

# app.config['IMG_FOLDER'] = os.path.join('static', '')

# 일반적인 라우트 방식입니다.
@app.route('/moniter_ring')
def board():
    full_filepath = 'static/images/moniter.png'
    return render_template(
        "moniter.html",
        pics = full_filepath,
    )

app.run(host="localhost",port=5001)

