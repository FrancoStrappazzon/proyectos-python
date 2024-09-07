#!/usr/bin/env python3

import unittest 
from students import calculate_median_student   #import function from students.py
from author import calculate_median_author   #import function from author.py

class test_calculate_median(unittest.TestCase):
    #auxiliar function
    def run_test(self, actual_output, expected_output, test_case, file):
        try:
            self.assertEqual(actual_output,expected_output)
            print(f"test case {test_case} pass in {file}")
        except AssertionError as e:
            print(f"test case {test_case}: Failed (Expected '{expected_output}', got '{actual_output}') in {file}" )
            raise e

    def test_even_student(self):
        actual_output = calculate_median_student([3, 6, 5, 7, 9, 1])
        self.run_test(actual_output,5.5,'even',"students.py")
        
    def test_even_author(self):
        actual_output = calculate_median_author([3, 6, 5, 7, 9, 1])
        self.run_test(actual_output,5.5,'even',"author.py")

    def test_odd_student(self):
        actual_output = calculate_median_student([3, 6, 5, 7, 9])
        self.run_test(actual_output,6.0,'odd',"students.py")
        
    def test_odd_author(self):
        actual_output = calculate_median_author([3, 6, 5, 7, 9])
        self.run_test(actual_output,6.0,'odd',"author.py")

    def test_single_student(self):
        actual_output = calculate_median_student([1])
        self.run_test(actual_output,1.0,'single',"students.py")
        
    def test_single_author(self):
        actual_output = calculate_median_author([1])
        self.run_test(actual_output,1.0,'single',"author.py")

    def test_empty_student(self):
        actual_output = calculate_median_student([])
        self.run_test(actual_output,None,'empty',"students.py")
        
    def test_empty_author(self):
        actual_output = calculate_median_author([])
        self.run_test(actual_output,None,'empty',"author.py")


if __name__ == '__main__':
    unittest.main()