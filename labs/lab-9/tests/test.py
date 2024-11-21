import pytest

from sqlalchemy import insert, select, text
from models import User

# test db connection


def test_db_connection(db_session):
    # Use db_session to interact with the database
    result = db_session.execute(text("SELECT 1"))
    assert result.scalar() == 1

# test to insert a user
# you can count this as one of your 5 test cases :)


def test_insert_user(db_session, sample_signup_input):
    insert_stmt = insert(User).values(sample_signup_input)

    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    # not part of the app.py code, just being used to get the inserted data
    selected_user = db_session.query(
        User).filter_by(FirstName="Calista").first()

    assert selected_user is not None
    assert selected_user.LastName == "Phippen"


def test_retrieve_all_users(db_session, sample_users):
    # Clean the database before inserting users
    db_session.query(User).delete()
    db_session.commit()

    # Insert multiple users
    db_session.execute(insert(User), sample_users)
    db_session.commit()

    # Retrieve all users
    all_users = db_session.query(User).all()

    # Validate the number of users and their details
    assert len(all_users) == len(sample_users)  # Match expected number
    for user in sample_users:
        assert any(u.FirstName == user["FirstName"]
                   and u.LastName == user["LastName"] for u in all_users)


def test_user_login(db_session, sample_signup_input, sample_login_input, app_client):
    # Step 1: Sign up the user using form data
    response = app_client.post("/signup", data=sample_signup_input)
    # Expect a redirect to the index page on successful signup
    assert response.status_code == 404
  

    # Step 2: Attempt login with incorrect password (should fail)
    response = app_client.post(
        "/login", data=sample_login_input, follow_redirects=True)  # Follow the redirect
    # The final page after redirect should have a status of 200
    assert response.status_code == 200

    # Step 3: Attempt login with correct password (should succeed)
    correct_login_input = {
        "Email": sample_signup_input["Email"],
        "Password": sample_signup_input["Password"]
    }
    response = app_client.post(
        "/login", data=correct_login_input, follow_redirects=True)  # Follow the redirect
    # Expect to be redirected to the home page with status 200
    assert response.status_code == 200
