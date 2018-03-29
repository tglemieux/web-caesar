from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action='/encrypt' method = 'POST'>
            <div>
                <label>Rotate By:
                    <input name="rot" type="text" value=0 />
                </lable>
            </div>
            <textarea name="text" type="text">{0}</textarea>
            <br>
            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    new_string = rotate_string(text, rot)
    return form.format(new_string)

app.run()