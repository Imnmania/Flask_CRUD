from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Secrert Key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hunter@localhost/crud'    #dbSysName://user:password@host/dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# This acts as table named 'data' in our database
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

@app.route('/register', methods=['GET','POST'])
def register():
    #return render_template('/register.html')
    return "huuuu"

@app.route('/insert', methods=['GET','POST'])
def insert():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee inserted successfully")

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)