# Student Management System

Welcome to the **Student Management System**, a robust and comprehensive API designed to efficiently manage students, courses, attendance, grades, and user roles. This system leverages Django and Django Rest Framework (DRF) to provide a scalable and extendable platform for educational institutions.

---

## Features

- **User Management**:
  - Register, authenticate, and manage users with roles like Student, Teacher, and Admin.
  - Role-based permissions for secure API access.
- **Student Records**:
  - Create, view, and update student profiles.
- **Course Management**:
  - Manage courses and enroll students.
  - Assign courses to teachers.
- **Grading System**:
  - Add, update, and retrieve grades for students.
- **Attendance Tracking**:
  - Record and manage attendance for students in courses.
- **Notification System**:
  - Automated email notifications for key actions such as grade updates.
- **Caching**:
  - Redis-based caching for optimized performance on frequently accessed data.
- **Asynchronous Tasks**:
  - Powered by Celery for background task processing.
- **API Documentation**:
  - Explore the API with auto-generated Swagger documentation.
- **Logging**:
  - Comprehensive logging for user actions, errors, and key activities.

---

## Getting Started

### Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd StudentManagementSystem
   ```

2. **Create a Virtual Environment and Activate It**:
   ```bash
   python3 -m venv env
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python3 manage.py migrate
   ```

5. **Create a Superuser**:
   ```bash
   python3 manage.py createsuperuser
   ```

---

### Running the Services

1. **Start the Redis Server**:
   ```bash
   redis-server
   ```

2. **Run the Celery Worker**:
   ```bash
   celery -A StudentManagementSystem worker --loglevel=info
   ```

3. **Run the Development Server**:
   ```bash
   python3 manage.py runserver
   ```

---

### Usage

1. **Access the API**:
   - Base URL: [http://127.0.0.1:8000](http://127.0.0.1:8000)

2. **Admin Panel**:
   - URL: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
   - Login using your superuser credentials.

3. **API Documentation**:
   - Swagger Documentation: [http://127.0.0.1:8000/swagger](http://127.0.0.1:8000/swagger)

---

## Key Components

### 1. User Management
- **Features**:
  - Registration, login, and logout.
  - Role-based permissions (Student, Teacher, Admin).
  - Secure token-based authentication.

### 2. Students
- **Features**:
  - Manage student profiles (view, update, delete).
  - Assign courses to students.

### 3. Courses
- **Features**:
  - Create, view, and update courses.
  - Assign instructors and enroll students.

### 4. Grades
- **Features**:
  - Add, view, and update student grades.
  - Track performance for each course.

### 5. Attendance
- **Features**:
  - Mark attendance for students.
  - Generate attendance reports.

### 6. Notifications
- **Features**:
  - Email notifications for actions like grade updates.
  - Celery tasks for background processing.

---

### Advanced Features

#### 1. Caching
- **Technology**: Redis
- Cached frequently accessed data like course lists and student profiles.
- Automatic cache invalidation on data updates.

#### 2. Logging
- Tracks user activities such as logins, updates, and errors.
- Logs are helpful for debugging and analytics.

#### 3. Asynchronous Tasks
- **Technology**: Celery with Redis
- Tasks:
  - Daily attendance reminders.
  - Grade update notifications.
  - Weekly performance summaries.

#### 4. Analytics (Optional)
- Tracks API usage, most active users, and popular courses.
- Can be extended for advanced reporting.

---

### Testing

1. **Run Unit Tests**:
   ```bash
   python3 manage.py test
   ```

2. **Tests Include**:
   - User registration and authentication.
   - Role-based permissions.
   - CRUD operations for Students, Courses, Grades, and Attendance.
   - Celery task execution.

---

## Bonus Tasks

1. **API Documentation**:
   - Integrated Swagger documentation for all endpoints.
   - Detailed request and response examples.

2. **Analytics**:
   - Added an analytics app for tracking key metrics like API requests, active users, and course popularity.

3. **Extendability**:
   - The modular design allows easy integration of new features or apps.

---

## Project Highlights

This project provides a practical implementation of:
- **Django Rest Framework (DRF)** for building RESTful APIs.
- **Celery** for asynchronous task management.
- **Redis** for caching and message brokering.
- **Role-Based Access Control** for secure operations.
- **Swagger** for API documentation.
