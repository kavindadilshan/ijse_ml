from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = f"{request.args['name']}"
    nic = f"{request.args['nic']}"

    print(f"{name}")
    print(f"{nic}")
    return f'My Name is '


@app.route('/html_read')
def using_html():
    html_file = open('./templates/index.html')
    html_string = html_file.readlines()

    return f"{''.join(html_string)}"


@app.route('/index')
def index():
    return render_template("index.html", age='12')


@app.route('/user', methods=["get", "post"])
def get_data():
    print(request.method)

    name=""

    if request.method == "POST":
        print("inside the post method")
        name=request.form.get("user_name")

    return render_template("insert_data.html",name=name)


if __name__ == '__main__':
    app.run(port=3232)
