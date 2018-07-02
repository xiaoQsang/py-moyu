from flask import Flask, render_template, request
from countdays import count_days_between_two_years
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/countdays', methods=["GET", "POST"])
def countdays():
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        total = count_days_between_two_years(start, end)
        return render_template('countdays.html', countDays= total, hidden="")
    else:
        return render_template('countdays.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)