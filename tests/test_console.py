#!/usr/bin/python3
"""
    console tester
    unittest module
    return: nothing
"""
import unittest
import subprocess

def get_out(inp):
    comm = 'echo "{}" | ./console.py'.format(inp)
    capture = subprocess.run(comm, shell=True, capture_output=True, text=True)
    return capture.stdout[7:-8]
class TestConsole(unittest.TestCase):
    """ 
        Test class
    """

    def test(self):
        expect = '*** Unknown syntax: jaja'
        self.assertEqual(get_out('jaja'), expect)
