from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Secrert Key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hunter@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('/index.html', title='Home')


@app.route('/about')
def about():
    return render_template('/about.html', title='About')


@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/register')
def register():
    return render_template('/register.html')


if __name__ == '__main__':
    app.run(debug=True)