#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from pathlib import Path

from flask import Flask, render_template


app = Flask(__name__, template_folder=str(Path(__file__).parent))


@app.route("/")
def hello_world():
    return render_template("index.html", utc_dt=datetime.utcnow())


if __name__ == "__main__":
    app.run(host="0.0.0.0")
