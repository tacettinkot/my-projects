from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return  "<h1> Hello World! Everything starts with first step </h1>"

@app.route("/second")
def second():
    return  "<h1> This is second page  </h1>"

@app.route("/third/tunc")
def third():
    return  "This is the subpath of third path"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'

# Default port is 5000 but if we define it could be different number
if __name__ == "__main__":
    app.run(debug=True, port=2000)

