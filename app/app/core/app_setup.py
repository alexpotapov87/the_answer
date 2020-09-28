from ..api import api  # noqa
from ..main import app
from flask import Flask, render_template, request, redirect


@app.route("/")
def root_dir():
    return render_template('base.html')
