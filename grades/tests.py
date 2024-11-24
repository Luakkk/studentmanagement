from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from students.models import Student
from courses.models import Course
from .models import Grade

class GradeTests(APITestCase):

    def setUp(self):
        # Create users, students, and courses
        self.teacher = User.objects.create_user(username="teacher1", password="password", role="teacher")
        self.student = Student.objects.create(user=User.objects.create_user(username="student1", password="password", role="student"))
        self.course = Course.objects.create(name="Math 101", instructor=self.teacher)
        self.client.login(username="teacher1", password="password")

    def test_create_grade(self):
        # Test creating a grade for a student
        data = {
            "student": self.student.id,
            "course": self.course.id,
            "grade": "A",
            "teacher": self.teacher.id
        }
        response = self.client.post('/grades/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_grade(self):
        # Test updating an existing grade
        grade = Grade.objects.create(student=self.student, course=self.course, grade="B", teacher=self.teacher)
        data = {"grade": "A+"}
        response = self.client.patch(f'/grades/{grade.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
