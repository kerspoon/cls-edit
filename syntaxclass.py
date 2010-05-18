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

    def find(self, name, text, start_line=0, start_col=0):
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
           return start_line, start_col + match.start()
       else:
           for n,line in enumerate(text[start_line+1]):
               match = re.search(self.syntaxmap[name], line)
               if match:
                   return start_line + n, match.start()

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
        self.assertEqual((0,1), sc.find("character", ["abc"]))
        self.assertEqual((0,1), sc.find("bees", ["abc"]))
        self.assertEqual((0,3), sc.find("word", ["abc def"]))
        self.assertEqual((0,7), sc.find("word", ["abc def ghi"], 0, 3))
        
    def test_002(self):
        """test second line"""
        sc = SyntaxClass("sc")
        sc.add("character", r".")
        sc.add("word", r" ")
        text = """hello line one
goodbye line two
"""
        self.assertEqual((0,1), sc.find("character", text.splitlines()))
        self.assertEqual((1,4), sc.find("character", text.splitlines(), 1, 3))

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()
    curses.wrapper(main)
