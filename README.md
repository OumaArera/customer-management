# Customer Management Project

Customer Management is a Flask-based web application designed to manage customers and orders. The platform includes features such as customer creation, order management, SMS notifications, and an authentication system. The project demonstrates the use of REST APIs, unit testing, CI/CD pipelines, and integration with third-party services like Codecov and Heroku.

---

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Setup and Installation](#setup-and-installation)
4. [Environment Variables](#environment-variables)
5. [Testing](#testing)
6. [Continuous Integration/Continuous Deployment (CI/CD)](#continuous-integrationcontinuous-deployment-cicd)
7. [API Endpoints](#api-endpoints)
8. [Deployment](#deployment)
9. [Contributing](#contributing)
10. [License](#license)

---

## Features

- **Customer Management**: Add, retrieve, and manage customer records.
- **Order Management**: Create and manage orders linked to customers.
- **SMS Notifications**: Notify customers via SMS upon order or account creation using Africa's Talking API.
- **Authentication**: Secure access using token-based authentication.
- **Unit Testing**: Comprehensive testing with code coverage reports.
- **CI/CD**: Automated testing and deployment to Heroku.
- **Integration with Codecov**: Generate and upload coverage reports to Codecov for insights.

---

## Tech Stack

- **Backend Framework**: Flask
- **Database**: SQLAlchemy (SQLite/PostgreSQL)
- **Third-party Services**:
  - Africa's Talking API for SMS notifications
  - Codecov for test coverage reporting
  - Heroku for hosting
- **Version Control**: Git/GitHub
- **CI/CD**: GitHub Actions
- **Testing**: Pytest and pytest-cov

---

## Setup and Installation

### Prerequisites

Ensure you have the following installed:
- Python (>= 3.9)
- Git
- Heroku CLI (for deployment)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com:OumaArera/customer-management.git
   cd customer-management
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. **Run the Application**:
   ```bash
   flask run
   ```
   The app will be accessible at `http://127.0.0.1:5000`.

---

## Environment Variables

Configure the following environment variables in a `.env` file or your deployment platform:

```bash
FLASK_APP=app
FLASK_ENV=development
DATABASE_URL=sqlite:///db.sqlite3  # For local testing; use PostgreSQL in production
AFRICASTALKING_USERNAME=your_africastalking_username
AFRICASTALKING_API_KEY=your_africastalking_api_key
SECRET_KEY=your_secret_key
HEROKU_API_KEY=your_heroku_api_key
HEROKU_APP_NAME=your_heroku_app_name
CODECOV_TOKEN=your_codecov_token
```

---

## Testing

### Run Unit Tests with Coverage
Execute the following command to run tests and generate coverage reports:

```bash
pytest --cov=app tests/
```

Coverage reports are generated in `coverage.xml` for integration with Codecov.

---

## Continuous Integration/Continuous Deployment (CI/CD)

### GitHub Actions Workflow

The repository includes a GitHub Actions workflow (`.github/workflows/ci.yml`) for CI/CD:
1. **Run Unit Tests**: Executes tests with coverage reporting.
2. **Upload Coverage**: Sends coverage reports to Codecov.
3. **Deploy to Heroku**: Automatically deploys the app to Heroku upon a successful test run.

Ensure the following secrets are configured in your GitHub repository under **Settings > Secrets and Variables**:
- `HEROKU_API_KEY`
- `HEROKU_APP_NAME`
- `CODECOV_TOKEN`

---

## API Endpoints

### Customers

| Method | Endpoint            | Description                  |
|--------|---------------------|------------------------------|
| POST   | `/api/customers/`   | Create a new customer        |
| GET    | `/api/customers/`   | Retrieve all customers       |

### Orders

| Method | Endpoint            | Description                  |
|--------|---------------------|------------------------------|
| POST   | `/api/orders/`      | Create a new order           |
| GET    | `/api/orders/`      | Retrieve all orders          |

### Authentication

| Method | Endpoint            | Description                  |
|--------|---------------------|------------------------------|
| POST   | `/api/auth/login/`  | User login and token retrieval |

---

## Deployment

### Deploying to Heroku

1. **Install Heroku CLI**:
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Log in to Heroku**:
   ```bash
   heroku login
   ```

3. **Set Heroku Remote**:
   ```bash
   heroku git:remote -a your-app-name
   ```

4. **Deploy**:
   ```bash
   git push heroku main
   ```

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Add feature description"`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---

## Developer

This project has been developed by John Ouma alias Ouma Arera.

---

## License

This project is licensed under the [MIT License](LICENSE).