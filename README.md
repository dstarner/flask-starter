# Flask Starter Pack

Basics needed for flask. Includes a basic User class, Sqlite database, and an example route.

### To Install

1. (Optional) Install a virtual environment. Using the command `virtualenv -p python3 venv`. This will create a Python 3 virtual environment called venv, so you can keep track of your dependencies.
  * To run Python scripts in this virtual environment, run `source venv/bin/activate` in the directory where `venv` is located.
2. Install the dependencies with pip. `pip install -r requirements.txt` will do the trick.
3. Run the actual Flask server. Do this with `python app.py`. Your database will be created automatically.
  * If you want to change any of the database models, delete `development.db` and restart `app.py`
4. Visit your browser at `localhost:5000` or `127.0.0.1:5000` to see your website.

For more info:

  * [Flask Login][1]: Allows you to login/logout users.
  * [Flask SQLAlchemy][2]: Allows you to create database models easily.
  * [Flask Tutorial][3]: Structured a little differently, but really awesome Flask tutorial.


[1]: https://flask-login.readthedocs.io/en/latest/
[2]: http://flask-sqlalchemy.pocoo.org/2.1/
[3]: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
