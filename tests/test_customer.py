import pytest
from app import create_app, db
from app.models import Customer
from app.models import Order

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_customer(client):
    response = client.post('/api/customers/', json={"name": "John", "phone": "1234567890"})
    assert response.status_code == 201
    assert response.json['message'] == "Customer created successfully and SMS sent!"
