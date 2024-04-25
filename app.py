from flask import Flask, render_template, jsonify
import MatchProcessor

app = Flask(__name__)
matchProcessor = MatchProcessor.MatchProcessor("data/futbol_martes.csv")


@app.route("/")
def home():
    ##return render_template("promiedos.jinja2", players=matchProcessor.get_position_table())
    return render_template("v2/table.jinja2", players=matchProcessor.get_position_table())


@app.route("/api/matches/<int:match_id>")
def match(match_id):
    if match_id > len(matchProcessor.matches):
        return "Not Valid Match id", 400
    return jsonify(matchProcessor.matches[match_id].to_dict())


@app.route("/matches/<int:match_day>")
def matches(match_day):
    match_id = match_day - 1
    return render_template("canchita.jinja2",
                           match=matchProcessor.matches[match_id],
                           match_id = match_id,
                           total_matches=list(range(0, len(matchProcessor.matches))))


@app.route("/match")
def matches2():
    return render_template("canchita.html")


if __name__ == "__main__":
    app.run(debug=True)
