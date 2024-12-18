"""app.py: render and route to webpages"""

from flask import request, render_template, redirect, url_for
from sqlalchemy import insert, text, select

from db.server import app
from db.server import db

from db.schema.user import User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:

            new_user = insert(User).values(request.form)

            db.session.add(new_user)
            db.session.commit()

            # Redirect to a login page or another route
            return redirect(url_for('login'))

        except Exception as e:
            db.session.rollback()  # Rollback the transaction on error
            print(f"An error occurred: {e}")
            return render_template('signup.html', error="Failed to create user.")

    return render_template('signup.html')


# +
@app.route('/login', methods=['GET', 'POST'])  # +
def login():
    if request.method == 'POST':

        try:

            username = request.form.get("email")
            password = request.form.get("password")

            db_password = db.session.execute(text("""SELECT "Password" FROM "Users" WHERE "Email" = :username"""), {
                "username": username}).fetchone()

            if db_password is None:
                return render_template('fail.html')

            if db_password[0] == password:
                print("Login Successful")
                return render_template('success.html')

        except Exception as e:
            print(f"An error occurred: {e}")

    return render_template('login.html')


@app.route('/users')
def users():
    with app.app_context():
        # select users where the first name is Calista
        # stmt = select(User).where(User.FirstName == "Calista")

        # select all users
        stmt = select(User)
        all_users = db.session.execute(stmt)

        return render_template('users.html', users=all_users)

    return render_template('users.html')


if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)
