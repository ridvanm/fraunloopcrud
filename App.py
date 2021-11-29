from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


 
 
 
app = Flask(__name__)
app.secret_key = "Secret Key"

##############Image upload





 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/fraunloopCrud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 

 
#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    gender = db.Column(db.String(100))
    image = db.Column(db.String(255))
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
 
 
    def __init__(self, gender, image, firstname,lastname):
 
        self.gender = gender
        self.image = image
        self.firstname = firstname
        self.lastname = lastname
 
 
 
 
 
#This is the index route where we are going to

@app.route('/')
def Index():
    all_data = Data.query.all()
    #all_data = Data.query.order_by(Data.id).all()
 
    return render_template("index.html", members = all_data)
 
 
 
#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        gender = request.form['gender']
        image = request.form['image']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
 
      
 

 
        my_data = Data(gender, image, firstname,lastname)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Data Inserted Successfully")
 
        return redirect(url_for('Index'))
 
 
#this is our update route where we are going to update 
@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
 
        my_data.gender = request.form['gender']
        my_data.image = request.form['image']
        my_data.firstname = request.form['firstname']
        my_data.lastname = request.form['lastname']
 
        db.session.commit()
        flash("Updated Successfully")
 
        return redirect(url_for('Index'))
 
 
 
 
#This route is for deleting 
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Deleted Successfully")
 
    return redirect(url_for('Index'))
 
 

 
 
 
if __name__ == "__main__":
    app.run(debug=True)