from flask import Flask, render_template
import MatchProcessor

app = Flask(__name__)
matchProcessor = MatchProcessor.MatchProcessor("data/futbol_martes.csv")


@app.route("/")
def home():
    return render_template("promiedos.jinja2", players=matchProcessor.get_position_table())


if __name__ == "__main__":
    app.run(debug=True)
