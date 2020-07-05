
from app import app, render_template

@app.route("/")
def f_index():
    page_title = "Services"
    return render_template("index.html", title=page_title)
