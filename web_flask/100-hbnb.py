#!/usr/bin/python3
"""Starting a Flask web application.

The application listensss on 0.0.0.0, port 5000.
Routes:
    /hbnb: HBnB home page.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displayss main HBnB filters HTML pagee"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """Removing current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")