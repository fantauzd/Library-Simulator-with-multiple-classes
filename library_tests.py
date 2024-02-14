# Unit Test file for Library.py

import unittest
from Library import *

b1 = Book("1111", "Phantom Tollbooth", "Juster")
b2 = Book("1114", "Harry Potter", "Rowling")
a1 = Album("1112", "...And His Orchestra", "The Fastbacks")
a2 = Album("1115", "Come Back", "Lil Yachty")
m1 = Movie("1113", "Laputa", "Miyazaki")
m2 = Movie("1116", "Harry Potter", "David Yates")
print(b1.get_author())
print(a1.get_artist())
print(m1.get_director())

p1 = Patron("aaa", "Felicity")
p2 = Patron("aab", "Waldo")
p3 = Patron("aac", "Ivy")

lib = Library()
lib.add_library_item(b1)
lib.add_library_item(b2)
lib.add_library_item(a1)
lib.add_library_item(a2)
lib.add_library_item(m1)
lib.add_library_item(m2)
lib.add_patron(p1)
lib.add_patron(p2)
lib.add_patron(p3)

# Made following tests:
# 1. test fines for accuracy when multiple patrons are overdue
# 2. test result when patron requests item that is checked out
# 3. test result when patron requests item that is checked out and on hold
# 4. test result when patron tries to check out item that is on hold
# 5. test pay_fine method
# 6. test return library item when not requested and returning item not belonging to library
class library_tests(unittest.TestCase):

    def test_1(self):
        """
        test fines for accuracy when multiple patrons are overdue
        """
        lib.check_out_library_item("aaa", "1111")
        lib.check_out_library_item("aaa", "1112")
        lib.check_out_library_item("aab", "1113")
        for i in range(60):
            lib.increment_current_date() # 60 days pass
        self.assertAlmostEqual(p1.get_fine_amount(), 8.50)
        self.assertAlmostEqual(p2.get_fine_amount(), 5.30)
        lib.return_library_item("1111")
        lib.check_out_library_item("aac", "1116")
        for i in range(20):
            lib.increment_current_date() # 20 days pass
        self.assertAlmostEqual(p1.get_fine_amount(), 10.50)
        self.assertAlmostEqual(p3.get_fine_amount(), 1.30)


    def test_2(self):
        """
        test result when patron requests item that is checked out
        """
        self.assertEqual(lib.check_out_library_item("aac","1112"), "item already checked out")

    def test_3(self):
        """
        test result when patron requests item that is checked out and on hold
        """
        lib.request_library_item("aac", "1112")
        self.assertEqual(lib.request_library_item("aab", "1112"), "item already on hold")

    def test_4(self):
        """
        test result when patron tries to check out item that is on hold
        """
        lib.return_library_item("1112")
        self.assertEqual(lib.check_out_library_item("aab", "1112"), "item on hold by other patron")

    def test_5(self):
        """
        test pay_fine method
        """
        lib.pay_fine("aaa", 10)
        self.assertAlmostEqual(p1.get_fine_amount(), 0.50)
        self.assertAlmostEqual(p3.get_fine_amount(), 1.30)
        self.assertAlmostEqual(p2.get_fine_amount(), 7.30)
        lib.pay_fine("aab", 8)
        self.assertAlmostEqual(p3.get_fine_amount(), 1.30)
        self.assertAlmostEqual(p2.get_fine_amount(), -0.70)


    def test_6(self):
        """
        test return library item when not requested and returning item not belonging to library
        """
        self.assertEqual(lib.return_library_item("116"), "item not found")
        lib.return_library_item("1116")
        self.assertAlmostEqual(p3.get_fine_amount(), 1.30)
        self.assertEqual(m2.get_location(), "ON_SHELF")
