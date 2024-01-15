#!/usr/bin/python3
"""Module for Square unit tests."""
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    """Tests the Base class."""

    def test_I_area_no_args(self):
        m = Square(7)
        with self.assertRaises(TypeError) as e:
            Square.area()
        n = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), n)
    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([8, 7, 6])
    def test_display_s(self):
        m = Square(1)
        n = io.StringIO()
        with redirect_stdout(n):
            m.display()
        p = "#\n"
        self.assertEqual(n.getvalue(), p)

        m.size = 2
        n = io.StringIO()
        with redirect_stdout(n):
            m.display()
        p = "\
##\n\
##\n\
"
        self.assertEqual(n.getvalue(), p)

        m = Square(5, 5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            m.display()
        p = """\





     #####
     #####
     #####
     #####
     #####
"""
        self.assertEqual(f.getvalue(), p)

        m = Square(8, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            m.display()
        n = """\
        ########
        ########
        ########
        ########
        ########
        ########
        ########
        ########
"""
        self.assertEqual(f.getvalue(), n)

    def test_B_inheritance(self):
        self.assertTrue(issubclass(Square, Base))

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({7, 2, 7}, 9)

    def test_J_display_no_args(self):
        m = Square(3)
        with self.assertRaises(TypeError) as e:
            Square.display()
        p = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), p)

if __name__ == "__main__":
    unittest.main()
			
