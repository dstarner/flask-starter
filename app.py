from flask import Flask, render_template, request
from models.user import Base
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Tell Flask where the Database will be 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'

# Import the classes we want as models here, the must inherit from models.Base
from models.user import User

# Create the actual database object
db = SQLAlchemy(app)

# Create the database tables on startup
Base.metadata.create_all(bind=db.engine)

# How you set up a basic route...
# @app.route("/myurl", methods=["GET"])
# def handle_myurl():
#     print("I got a request!")

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # Get all of the users' rows from the database
    past_users = db.session.query(User).all()
    myname = None  # Set my name to None to start

    if request.method == "POST":  # This will be true if they submit the form
         myname = request.form.get('username', None)  # Set the myname variable
                                                      # to the value from the input
         
         old_user = db.session.query(User).filter_by(name=myname).first()
         if old_user:                                # If that name already existed.
             old_user.frequency += 1                 # increment the frequency
             db.session.add(old_user)                # Save and commit to DB
             db.session.commit()

         elif myname is not None:                       # If their name isn't in the DB
            user = User(name=myname)                  # Then create a user object and
            db.session.add(user)                      # Add it to the database and
            db.session.commit()                       # commit that database change

    # Return a rendered webage. 'index.html' in templates
    return render_template('index.html', name=myname, users=past_users)

# Used to run the app
if __name__ == '__main__':
    app.run(debug=True)
