from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')



def index():
    print(request)
    return render_template('index.html')


@app.route('/about/')
def about():
    return '<h3>About</h3>'


if __name__ == '__main__':
    app.run(debug=True)
