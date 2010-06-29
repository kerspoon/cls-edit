#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import re 
import unittest

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

class SyntaxClass(object):
    """
    Defines some classes of things for simple parsing of a file.
    For instance you might have a function point-to-next-sentance
    which works regardless of which mode you are in as long as the 
    concept of sentance exists here. Best is probably that they are 
    a list of regexps. Not all need to be defined by all modes, they 
    can overlap. 
    """
    def __init__(self, syntaxname):
       self.syntaxname = syntaxname
       self.syntaxmap = {}

    def add(self, name, regexp):
       """
       Add a new class of syntax to this group. 
       """
       self.syntaxmap[name] = regexp

    def find(self, name, text, start_col=0, start_line=0):
       """
       Find the next occurance of the given syntax chunk
       called 'name' in the [Str] 'text'. With optional
       starting point
       """

       start_col = start_col + 1
       # print "test", text[start_line][start_col:]
       match = re.search(self.syntaxmap[name], text[start_line][start_col:])
       if match:
           # print start_line, start_col + match.start()
           return start_col + match.start(), start_line
       elif len(text) > start_line+1:
           self.find(name, text, 0, start_line+1)
           
           #for n,line in enumerate(text[start_line+1]):
           #    match = re.search(self.syntaxmap[name], line)
           #    if match:
           #        return match.start(), start_line + n

       # Nothing Found
       return None, None

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

class Test_SyntaxClass(unittest.TestCase):

    def test_001(self):
        """test first line"""
        sc = SyntaxClass("sc")
        sc.add("character", r".")
        sc.add("bees", r"b")
        sc.add("word", r" ")
        self.assertEqual((1,0), sc.find("character", ["abc"]))
        self.assertEqual((1,0), sc.find("bees", ["abc"]))
        self.assertEqual((3,0), sc.find("word", ["abc def"]))
        self.assertEqual((7,0), sc.find("word", ["abc def ghi"], 3, 0))
        
    def test_002(self):
        """test second line"""
        sc = SyntaxClass("sc")
        sc.add("character", r".")
        sc.add("word", r" ")
        text = """hello line one
goodbye line two
"""
        self.assertEqual((1,0), sc.find("character", text.splitlines()))
        self.assertEqual((4,1), sc.find("character", text.splitlines(), 3, 1))

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

class Test_SyntaxClass_Again(unittest.TestCase):

    def setUp(self):
        self.text = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod 
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse 
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""".splitlines()
        
        self.sc = SyntaxClass("sc")
        self.sc.add("character", r".")
        self.sc.add("bees", r"b")
        self.sc.add("mmms", r"m")
        self.sc.add("word", r" ")
        self.sc.add("nostrud", r"nostrud")

    def test_001(self):
        """test first line"""

        def util_find(item, x, y):
            return self.sc.find(item, self.text, x, y)

        self.assertEqual((1,0), util_find("character", 0, 0))
        self.assertEqual((4,0), util_find("mmms", 0, 0))
        self.assertEqual((5,2), util_find("nostrud", 0, 0))
        self.assertEqual((5,2), util_find("nostrud", 1, 0))
        self.assertEqual((5,2), util_find("nostrud", 0, 1))
        self.assertEqual((5,2), util_find("nostrud", 1, 1))


#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
    curses.wrapper(main)
