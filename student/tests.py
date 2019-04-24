from django.test import TestCase, Client
from .models import Student


# Create your tests here.
class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='theerick',
            sex=1,
            email='theerick@123.com',
            profession='码农',
            qq=333,
            phone='22222',
            status=1
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='longlong',
            sex=1,
            email='ppppp@123.com',
            profession='it',
            qq='4444',
            phone='33333',
            status=1
        )
        self.assertEqual(student.get_sex_display(),'男','必须一致哈')

    def test_filter(self):
        Student.objects.create(
            name='longfff',
            sex=1,
            email='p555@123.com',
            profession='it5',
            qq='444466666666',
            phone='33333777777',
            status=1
        )
        name = 'longfff'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1,'heihh')

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='p555@123.com',
            profession='it5',
            qq='444466666666',
            phone='33333777777',
            status=1
        )
        response = client.post('/', data)
        print(response.status_code)
        self.assertEqual(response.status_code,302, 'status must be 302')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.content, 'response content must contain test_for_post')
