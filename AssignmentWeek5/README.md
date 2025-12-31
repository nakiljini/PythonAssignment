# Doctor Appointment API

A production-ready RESTful API for managing doctor appointments with full authentication and role-based access control (RBAC).

## 🛠 Tech Stack

- **Language**: Python 3.12+
- **Web Framework**: FastAPI
- **Database**: PostgreSQL (with MySQL support)
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Testing**: Pytest
- **Containerization**: Docker & Docker Compose

## 📦 Features

- ✅ User registration and authentication (Doctor/Patient)
- ✅ JWT-based authentication
- ✅ Role-based access control (RBAC)
- ✅ Doctor availability management
- ✅ Appointment booking with double-booking prevention
- ✅ Appointment cancellation
- ✅ Comprehensive test coverage
- ✅ Production-ready code structure (Service/Repository pattern)

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Python 3.12+ (if running locally)

### Setup with Docker (Recommended)

1. **Clone the repository and navigate to the project:**

```bash
cd AssignmentWeek5
```

2. **Create a `.env` file (optional - defaults are provided):**

The application will work with default values, but you can create a `.env` file to customize settings:

```bash
# Create .env file with custom settings
cat > .env << EOF
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/doctor_appointment_db
SECRET_KEY=your-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
EOF
```

**Note**: If you don't create a `.env` file, the application will use default values.

3. **Start the services:**

```bash
docker-compose up -d
```

This will:
- Start PostgreSQL database
- Build and start the FastAPI application
- Create database tables automatically

4. **Access the API:**

- API: http://localhost:8000
- Interactive API Docs: http://localhost:8000/docs
- Alternative API Docs: http://localhost:8000/redoc

### Setup without Docker

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Set up PostgreSQL database:**

Create a database named `doctor_appointment_db` (or update the connection string).

3. **Create `.env` file:**

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/doctor_appointment_db
SECRET_KEY=your-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

4. **Run the application:**

```bash
uvicorn main:app --reload
```

## 📚 API Endpoints

### Authentication

#### `POST /auth/register`
Register a new user (Doctor or Patient)

**Request Body:**
```json
{
  "email": "doctor@example.com",
  "password": "password123",
  "role": "Doctor",
  "name": "Dr. John Smith"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "doctor@example.com",
    "name": "Dr. John Smith",
    "role": "Doctor"
  }
}
```

#### `POST /auth/login`
Login and get JWT token

**Request Body:**
```json
{
  "email": "doctor@example.com",
  "password": "password123"
}
```

#### `POST /auth/forgot-password`
Mock forgot password flow (no email sending)

**Request Body:**
```json
{
  "email": "doctor@example.com"
}
```

### Doctors (Public Endpoints)

#### `GET /doctors`
Get list of all doctors

#### `GET /doctors/{doctor_id}/availability`
Get availability slots for a specific doctor

### Appointments (Protected Endpoints)

#### `POST /appointments`
Book an appointment (Patient only)

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "doctor_id": 1,
  "availability_id": 1,
  "appointment_time": "2024-01-15T10:00:00"
}
```

#### `GET /appointments/my-appointments`
Get current user's appointments (Doctor or Patient)

#### `POST /appointments/cancel/{appointment_id}`
Cancel an appointment (Patient only)

#### `POST /appointments/availability`
Set availability slots (Doctor only)

**Request Body:**
```json
{
  "start_time": "2024-01-15T09:00:00",
  "end_time": "2024-01-15T17:00:00"
}
```

#### `GET /appointments/upcoming`
Get upcoming appointments (Doctor only)

## 🔐 Authentication Flow

### Overview

The API uses JWT (JSON Web Tokens) for authentication. Here's how it works:

1. **Registration/Login**: User provides credentials and receives a JWT token
2. **Token Usage**: Client includes token in `Authorization: Bearer <token>` header
3. **Token Validation**: Server validates token on each protected request
4. **Role Verification**: Server checks user role for role-specific endpoints

### JWT Token Structure

The JWT token contains:
- `sub`: User email
- `role`: User role (Doctor/Patient)
- `exp`: Token expiration time

### Token Expiration

Tokens expire after 30 minutes (configurable via `ACCESS_TOKEN_EXPIRE_MINUTES`).

### Example Flow

```python
# 1. Register
POST /auth/register
{
  "email": "patient@example.com",
  "password": "password123",
  "role": "Patient",
  "name": "John Doe"
}

# Response includes access_token

# 2. Use token for protected endpoints
GET /appointments/my-appointments
Headers: Authorization: Bearer <access_token>
```

## 🛡️ Role-Based Access Control (RBAC)

### Design Overview

The API implements a two-role system:

1. **Doctor**: Can set availability and view appointments
2. **Patient**: Can view doctors, check availability, and book/cancel appointments

### Role Enforcement

RBAC is enforced at multiple levels:

1. **Dependency Injection**: FastAPI dependencies (`get_current_doctor`, `get_current_patient`)
2. **Service Layer**: Business logic validates roles
3. **Route Level**: Endpoints are protected with role-specific dependencies

### Access Matrix

| Endpoint | Public | Doctor | Patient |
|----------|--------|--------|---------|
| `POST /auth/register` | ✅ | ✅ | ✅ |
| `POST /auth/login` | ✅ | ✅ | ✅ |
| `GET /doctors` | ✅ | ✅ | ✅ |
| `GET /doctors/{id}/availability` | ✅ | ✅ | ✅ |
| `POST /appointments` | ❌ | ❌ | ✅ |
| `GET /appointments/my-appointments` | ❌ | ✅ | ✅ |
| `POST /appointments/cancel/{id}` | ❌ | ❌ | ✅ |
| `POST /appointments/availability` | ❌ | ✅ | ❌ |
| `GET /appointments/upcoming` | ❌ | ✅ | ❌ |

### Implementation Details

**Authentication Dependencies:**
- `get_current_user`: Validates JWT and returns user (any role)
- `get_current_doctor`: Ensures user is a Doctor
- `get_current_patient`: Ensures user is a Patient

**Example:**
```python
@router.post("/appointments/availability")
def set_availability(
    availability_data: AvailabilityCreate,
    current_user: User = Depends(get_current_doctor)  # Doctor only
):
    ...
```

## 🏗️ Architecture

### Code Structure

```
AssignmentWeek5/
├── main.py                 # FastAPI application entry point
├── config.py              # Configuration settings
├── database.py            # Database connection and session
├── models.py              # SQLAlchemy models
├── schemas.py             # Pydantic schemas for validation
├── auth.py                # Authentication utilities
├── repositories/          # Data access layer
│   ├── user_repository.py
│   ├── availability_repository.py
│   └── appointment_repository.py
├── services/              # Business logic layer
│   ├── auth_service.py
│   └── appointment_service.py
├── routes/                # API endpoints
│   ├── auth.py
│   ├── doctors.py
│   └── appointments.py
├── tests/                 # Test suite
│   ├── test_auth.py
│   ├── test_appointments.py
│   └── test_rbac.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

### Design Patterns

1. **Repository Pattern**: Separates data access logic from business logic
2. **Service Pattern**: Encapsulates business rules and validation
3. **Dependency Injection**: FastAPI's dependency system for clean code

### Data Flow

```
Request → Route → Service → Repository → Database
                ↓
            Validation & Business Logic
```

## 🧪 Testing

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_auth.py
```

### Test Coverage

The test suite includes:
- ✅ Authentication tests (registration, login, password hashing)
- ✅ Appointment booking tests (including double-booking prevention)
- ✅ RBAC tests (role-based access control)
- ✅ Availability management tests

## 🔒 Security Features

1. **Password Hashing**: Uses bcrypt for secure password storage
2. **JWT Tokens**: Secure token-based authentication
3. **Input Validation**: Pydantic schemas validate all inputs
4. **SQL Injection Prevention**: SQLAlchemy ORM prevents SQL injection
5. **Role-Based Access**: Endpoints protected by role requirements
6. **Token Expiration**: JWT tokens expire after configured time

## 📝 Database Schema

### Users Table
- `id`: Primary key
- `email`: Unique email address
- `password_hash`: Hashed password
- `role`: Enum (Doctor/Patient)
- `name`: User's full name
- `created_at`, `updated_at`: Timestamps

### Availabilities Table
- `id`: Primary key
- `doctor_id`: Foreign key to users
- `start_time`: Availability start
- `end_time`: Availability end
- `created_at`, `updated_at`: Timestamps

### Appointments Table
- `id`: Primary key
- `doctor_id`: Foreign key to users
- `patient_id`: Foreign key to users
- `availability_id`: Foreign key to availabilities
- `appointment_time`: Scheduled time
- `status`: Appointment status (scheduled/cancelled)
- `created_at`, `updated_at`: Timestamps

## 🐛 Troubleshooting

### Database Connection Issues

If you encounter database connection errors:

1. Ensure PostgreSQL is running
2. Check `DATABASE_URL` in `.env` file
3. Verify database credentials

### Port Already in Use

If port 8000 is already in use:

```bash
# Change port in docker-compose.yml or
uvicorn main:app --port 8001
```

## 📄 License

This project is created for educational purposes.

## 👤 Author

Created as part of Python Assignment Week 5

---

**Note**: This is a production-ready API implementation following best practices for security, testing, and code organization.

