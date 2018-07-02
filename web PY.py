from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/about Me', methods=["GET", "POST"])
def about_Me():
    return "My name is Wolfgang.Ji"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)