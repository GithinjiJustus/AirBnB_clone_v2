#!/usr/bin/python3

"""Routes:
    /hbnb: HBnB home page.
"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session.
    """
    storage.close()

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays the main HBnB filters HTML page.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
