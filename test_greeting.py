#!/usr/bin/env python3
"""
Unit tests for the greeting module.
"""

import unittest
from greeting import greet


class TestGreeting(unittest.TestCase):
    """Test cases for the greet function."""
    
    def test_hi_greeting(self):
        """Test response to 'HI' greeting."""
        result = greet("HI")
        self.assertEqual(result, "Hello! Welcome to the DT Fellowship Assignment repository!")
    
    def test_hello_greeting(self):
        """Test response to 'HELLO' greeting."""
        result = greet("HELLO")
        self.assertEqual(result, "Hi there! How can I help you today?")
    
    def test_hey_greeting(self):
        """Test response to 'HEY' greeting."""
        result = greet("HEY")
        self.assertEqual(result, "Hey! Good to see you here!")
    
    def test_unknown_greeting(self):
        """Test response to unknown greeting."""
        result = greet("Good morning")
        self.assertEqual(result, "Hello! Nice to meet you!")
    
    def test_case_insensitive(self):
        """Test that greetings are case-insensitive."""
        self.assertEqual(greet("hi"), greet("HI"))
        self.assertEqual(greet("Hi"), greet("HI"))
        self.assertEqual(greet("hI"), greet("HI"))
    
    def test_whitespace_handling(self):
        """Test that leading/trailing whitespace is handled."""
        self.assertEqual(greet("  HI  "), greet("HI"))
        self.assertEqual(greet("\tHELLO\n"), greet("HELLO"))


if __name__ == "__main__":
    unittest.main()
