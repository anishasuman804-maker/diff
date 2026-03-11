from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")
    date1 = request.form.get("date1")
    date2 = request.form.get("date2")
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    difference = abs((d2 - d1).days)
    return render_template("index.html", diff=difference)
if __name__ == "__main__":
    app.run(port=5000, debug=True)