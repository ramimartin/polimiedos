from flask import Flask, render_template, jsonify
import MatchProcessor

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent
import threading
import time

PATH = "data/futbol_martes_2.csv"


class FixtureChangeHandler(FileSystemEventHandler):

    def __init__(self, match_processor):
        self.match_processor = match_processor

    def on_modified(self, event: FileSystemEvent):
        if not event.is_directory:
            self.match_processor = MatchProcessor.MatchProcessor(PATH)


app = Flask(__name__)
handler = FixtureChangeHandler(MatchProcessor.MatchProcessor(PATH))


def run_watcher(path):
    observer = Observer()
    observer.schedule(handler, path)
    observer.start()


@app.route("/")
def home():
    return render_template("v2/table.jinja2", players=handler.match_processor.get_position_table())


@app.route("/matches/<int:match_day>")
def matches(match_day):
    match_id = match_day - 1
    return render_template("v2/fixture.jinja2",
                           match=handler.match_processor.matches[match_id],
                           match_id=match_id,
                           total_matches=list(range(0, len(handler.match_processor.matches))))


if __name__ == "__main__":
    run_watcher(PATH)
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    app.run(debug=True)
