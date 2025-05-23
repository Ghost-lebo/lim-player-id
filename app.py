from flask import Flask, render_template, request

app = Flask(__name__)

PASSWORD = "Zorro123abc#@!"

@app.route('/', methods=['GET'])
def index():
    player_data = {
        "name": "John Doe",
        "dob": "2005-07-15",
        "team": "Green Strikers FC",
        "position": "Midfielder",
        "tournament": "Youth Soccer League"
    }
    return render_template("index.html", **player_data)

@app.route('/view_certificate', methods=['POST'])
def view_certificate():
    password = request.form.get("password")
    player_data = {
        "name": "John Doe",
        "dob": "2005-07-15",
        "team": "Green Strikers FC",
        "position": "Midfielder",
        "tournament": "Youth Soccer League"
    }

    if password == PASSWORD:
        return render_template("index.html", show_certificate=True, **player_data)
    else:
        return render_template("index.html", error="Incorrect password", **player_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

