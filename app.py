from flask import Flask, render_template
import futbol_martes

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("promiedos.html",players=futbol_martes.get_results("futbol_martes"))


if __name__ == "__main__":
    app.run(debug=True)
