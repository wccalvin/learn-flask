import flask

app = flask.Flask(__name__)


def get_latest_packages():
    return [
        {"name": "flask", "version": "1.2.3"},
        {"name": "sqlalchemy", "version": "2.1.0"},
        {"name": "passlib", "version": "0.3.2"},
    ]


@app.route("/")
def index():
    test_packages = get_latest_packages()
    return flask.render_template("index.html", packages=test_packages)


if __name__ == "__main__":
    app.run(debug=True)
