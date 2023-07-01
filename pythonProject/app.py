from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from array import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


with app.app_context():
    db.create_all()

class Test():
    id = 1
    name = "test"

    def __repr__(self):
        return self.id


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    # date = db.Column(db.DateTime)

    def __repr__(self):
        return self.title


@app.route('/')
def index():
    arr = [Test(), Test(), Test()]
    return render_template('index.html', data=arr)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']

        item = Item(title=title, price=price)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')

        except:
            return "ОШИБКА"
    else:
        return render_template('create.html')


@app.route('/dz')
def dz():
    return render_template('dz.html')


if __name__ == '__main__':
    app.run(debug=False)
