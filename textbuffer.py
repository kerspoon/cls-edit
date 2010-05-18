#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import unittest

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

class Buffer(object):
    """holds text to be drawn to the screen"""
    def __init__(self):
        pass

class LogBuffer(Buffer):
    def __init__(self):
        self.log = []
        self.render = None

    def msg(self, text):
        self.log.insert(0, text)
        if self.render:
            self.render()

    def __iter__(self):
        return iter(self.log)

    def __len__(self):
        return len(self.log)

    def __getitem__(self):
        return self.log

class FileBuffer(Buffer):
    def __init__(self, infile):
        self.buf = []
        self.infile = infile
        self.reload()

    def reload(self):
        for line in self.infile:
            self.buf.append(line[:])

    def __iter__(self):
        return iter(self.buf)

    def __len__(self):
        return len(self.buf)

    def __getitem__(self):
        return self.buf


def num_buffer():
   text_buffer = FileBuffer(None)

   for x in range(15):
       text_buffer.buf.append(str(x*10) + "-"*(x*10-2) + "\n")

   return text_buffer
   
