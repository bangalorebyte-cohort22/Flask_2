from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __repr__(self):
        return f'<User : {self.name}>'
    
    def __str__(self):
        return f'<User : {self.name}>'

@app.route('/',methods = ['GET','POST'])
def show():
    if request.method == 'POST':        
        name = request.form['name']
        
        
        status = model.alchemy_add_name(User(name=name), db)
        names = model.alchemy_get_names(User)
        return render_template('index.html', text=status , names=names)
    names = model.alchemy_get_names(User)
    return render_template('index.html', text='Stranger' , names=names )

if __name__ == "__main__":
    app.run(debug=True)