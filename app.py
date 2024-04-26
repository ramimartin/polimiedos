from flask import Flask, render_template, jsonify
import MatchProcessor

app = Flask(__name__)
matchProcessor = MatchProcessor.MatchProcessor("data/futbol_martes.csv")


@app.route("/")
def home():
    return render_template("v2/table.jinja2", players=matchProcessor.get_position_table())


@app.route("/matches/<int:match_day>")
def matches(match_day):
    match_id = match_day - 1
    return render_template("v2/fixture.jinja2",
                           match=matchProcessor.matches[match_id],
                           match_id=match_id,
                           total_matches=list(range(0, len(matchProcessor.matches))))


if __name__ == "__main__":
    app.run(debug=True)
