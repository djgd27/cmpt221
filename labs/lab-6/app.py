"""app.py: render and route to webpages"""

from flask import request, render_template, redirect, url_for
from sqlalchemy import insert, text, select

from db.server import app
from db.server import db

from db.schema.user import User
from db.models.usermodel import UserModel


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            # Parse form data into UserModel
            user_data = UserModel(
                first_name=request.form.get('first_name'),
                last_name=request.form.get('last_name'),
                email=request.form.get('email'),
                phone_number=request.form.get('phone_number'),
                password=request.form.get('password')
            )

            # Create a new User instance using ORM
            new_user = User(
                FirstName=user_data.first_name,
                LastName=user_data.last_name,
                Email=user_data.email,
                PhoneNumber=user_data.phone_number,
                Password=user_data.password
            )

            # Add the new user to the session
            db.session.add(new_user)

            # Commit the session to save the user to the database
            db.session.commit()

            # Redirect to a login page or another route
            return redirect(url_for('login'))

        except Exception as e:
            db.session.rollback()  # Rollback the transaction on error
            print(f"An error occurred: {e}")
            return render_template('signup.html', error="Failed to create user.")

    return render_template('signup.html')


@app.route('/login')
def login():
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
