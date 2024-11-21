import os
import sys
import pytest

# Add the path to the app directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")))

from app import app
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# contains table objects
Base = declarative_base()

# import environment variables from .env
load_dotenv()

db_name: str = os.getenv('db_name')
db_owner: str = os.getenv('db_owner')
db_pass: str = os.getenv('db_pass')
db_uri: str = f"postgresql://{db_owner}:{db_pass}@localhost/{db_name}"

# create db connection w/o Flask
# NOTE: creates new session for each test function


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(db_uri)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # create tables
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    yield session
    session.close()
    # drop tables
    Base.metadata.drop_all(bind=engine)

# example fixture - user sign in input
# hint... can you do something similar for login?


@pytest.fixture
def sample_signup_input():
    return {'FirstName': 'Calista',
            'LastName': 'Phippen',
            'Email': 'calista.phippen1@marist.edu',
            'PhoneNumber': '1234567891',
            'Password': 'mypassword2'
            }


@pytest.fixture
def sample_login_input():
    return {
        'Email': 'calista.phippen1@marist.edu',
        'Password': 'mypassword1'  # expected to fail
    }


@pytest.fixture
def sample_users():
    return [
        {"FirstName": "Calista", "LastName": "Phippen"},
        {"FirstName": "John", "LastName": "Doe"},
        {"FirstName": "Jane", "LastName": "Smith"}
    ]


@pytest.fixture
def app_client():
    # Set the app config for testing
    app.config["TESTING"] = True  # Enable testing mode
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Use an in-memory database for testing

    # Use app's test client and yield it
    with app.test_client() as client:
        with app.app_context():
            # Initialize the database or any other setup tasks if necessary
            yield client  # Provide the test client to the test function