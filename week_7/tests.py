from student_file import Student
import unittest

class TestStudent(unittest.TestCase):
    def test_gpa(self):
        st = Student("Aaa", "Bbb", 21, 4, "IT", 3.5)
        gpa = st.get_gpa()
        self.assertEqual(gpa, 3.5)

    def test_convert_gpa(self):
        st = Student("Aaa", "Bbb", 21, 4, "IT", 3.5)
        gpa_2 = st.convert_gpa()
        ans = 4.375
        self.assertEqual(gpa_2, ans)

    def test_str(self):
        st = Student("Aaa", "Bbb", 21, 4, "IT", 3.5)
        str_repr = st.__str__()
        ans = "Bbb 4 IT"
        self.assertEqual(str_repr, ans)


if __name__ == "__main__":
    unittest.main()