from flask import Flask, render_template, request
from disease import fetch_medlineplus_data

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        disease = request.form['disease']

        info = fetch_medlineplus_data(disease)

        return render_template(
            'result.html',
            disease=disease,
            info=info
        )

    return "Please search using the form."


if __name__ == '__main__':
    app.run(debug=True)