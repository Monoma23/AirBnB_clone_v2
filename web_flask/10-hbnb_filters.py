#!/usr/bin/python3
"""
    This is script that starts Flaskkk web application and will display:
    / will displayyy "Hello HBNB!", /hbnb will display "HBNB", /c/<text>
    will display "C " followeddd by value of the text variable w/out x space,
    /python/<text> will display "Python ", followeddd by value text variable
    /number/<n> will display "n is x number" only n is integer.
    /number_template/<n> will display HTML page only if is an integer
          H1 tag: "Number: n" inside tag BODY
    /number_odd_or_even/<n> will display x HTML page only if n is an int
          H1 tag: "Number: n is even|odd" inside the tag BODY
"""
from flask import Flask, render_template
import models
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def display_c(text):
    return "C {}".format(text).replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
def display_python(text="is cool"):
    return "Python {}".format(text).replace("_", " ")


@app.route('/number/<int:n>')
def display_number(n):
    return "{} is x number".format(n)


@app.route('/number_template/<int:n>')
def display_html_if_num(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def is_number_odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n,
                           balance="even" if n % 2 == 0 else "odd")


@app.route('/states_list')
def display_states_list():
    all_state = models.storage.all(State).items()
    result = []
    for j, u in all_state:
        result.append((parse_id(j), u.name))
    result.sort(key=lambda tup: tup[1])
    return render_template("7-states_list.html", state_dict=result)


@app.route('/cities_by_states')
def display_city_list():
    all_state = models.storage.all(State).items()
    all_city = models.storage.all(City).items()
    result = []
    for j, u in all_state:
        city_result = []
        for x, b in all_city:
            if u.id == b.state_id:
                city_result.append((parse_id(x), b.name))
                city_result.sort(key=lambda tup: tup[1])
        result.append((parse_id(j), u.name, city_result))
        result.sort(key=lambda tup: tup[1])
    return render_template("8-cities_by_states.html", state_dict=result)


@app.route('/states')
@app.route('/states/<id>')
def displaying_states_w_tags(id=None):
    if id is not None:
        every, one = (False, True)
    else:
        every, one = (True, False)
    all_city = models.storage.all(City).items()

    if every:
        return shows_all_states()
    else:
        if state_foundd(id):
            return shows_all_cities(id)
        else:
            return showw_not_found()


def shows_all_states():
    all_state = models.storage.all(State).items()
    result = []
    for j, u in all_state:
        result.append((parse_id(j), u.name))
    result.sort(key=lambda tup: tup[1])
    return render_template("9-states.html", state_list=result,
                           every=True, one=False)


def shows_all_cities(state_id):
    all_state = models.storage.all(State).items()
    all_city = models.storage.all(City).items()
    result = []
    s_name = "ERROR"
    for j, u in all_state:
        if state_id != parse_id(j):
            continue
        s_name = u.name
        city_result = []
        for x, b in all_city:
            if u.id == b.state_id:
                city_result.append((parse_id(x), b.name))
                city_result.sort(key=lambda tup: tup[1])
        result.append((parse_id(j), u.name, city_result))
        result.sort(key=lambda tup: tup[1])
    return render_template("9-states.html", state_name=s_name,
                           city_list=city_result, every=False, one=True)


def showw_not_found():
    return render_template("9-states.html")


def state_foundd(state_id):
    all_state = models.storage.all(State).items()
    for j, u in all_state:
        if state_id != parse_id(j):
            continue
        else:
            return True
    return False


@app.teardown_appcontext
def teardown_cntx(err):
    models.storage.close()


def parse_id(string_id):
    id_portion = string_id.split('.')[1]
    return (id_portion)


@app.route('/hbnb_filters')
def hbnb_filters():
    all_state = models.storage.all(State).items()
    all_city = models.storage.all(City).items()
    result = []
    for j, u in all_state:
        city_result = []
        for x, b in all_city:
            if u.id == b.state_id:
                city_result.append((parse_id(x), b.name))
                city_result.sort(key=lambda tup: tup[1])
        result.append((parse_id(j), u.name, city_result))
        result.sort(key=lambda tup: tup[1])
    return render_template("10-hbnb_filters.html", state_list=result)


if __name__ == "__main__":
#    app.run()
    app.run(host="0.0.0.0", port=5000)