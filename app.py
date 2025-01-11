from flask import Flask, render_template 
from models import init_db,db #imports models folder from FLASK1

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/FitCheck'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app) #initializes database

@app.route("/") #helps in routing
def test():
    return render_template("index.html")
    
if __name__ == "__main__":
    
    with app.app_context(): #checks if u have the table,if not there makes the tables
        db.create_all()
        
    app.run(debug=True)
    