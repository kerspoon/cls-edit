#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import unittest

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

class Window(object):
   def __init__(self, window, tbuffer):
      self.tbuffer = tbuffer
      self.window = window
      self.window.clear()
      self.window.box()
      self.window.refresh()

   def render(self):
      self.window.clear()

      my, mx = self.window.getmaxyx()
      for n,line in enumerate(self.tbuffer):
         if n >= my-2:
            break
         self.window.addstr(n+1, 1, line[:mx-2])

      self.window.box()
      self.window.move(1,1)
      self.window.refresh()

   def clear(self):
      self.window.clear()
      self.window.refresh()

   def addstr(self, text):
      self.window.addstr(text)
      self.window.refresh()

   def move(self, x, y):
      my, mx = self.window.getmaxyx()
      ny = clamp(y, 1, my-2)
      nx = clamp(x, 1, mx-2)
      self.window.move(ny, nx)
      self.window.refresh()

   def rmove(self, rx, ry):
      y, x = self.window.getyx()
      my, mx = self.window.getmaxyx()
      ny = clamp(y+ry, 1, my-2)
      nx = clamp(x+rx, 1, mx-2)
      self.window.move(ny, nx)
      self.window.refresh()

   def caret(self):
      y, x = self.window.getyx()
      my, mx = self.window.getmaxyx()
      ny = clamp(y, 1, my-2)
      nx = clamp(x, 1, mx-2)
      return nx, ny

   def rmovef(self, func):
      ox, oy = self.caret()
      nx, ny = func(self.tbuffer.buf, ox-1, oy-1)
      if nx and ny:
         self.rmove(nx-1, ny-1)

def clamp(value, vmin, vmax):
   if value > vmax:
      return vmax
   if value < vmin:
      return vmin
   return value

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

class TmpWin:
   def clear(*x):
      pass
   def box(*x):
      pass
   def addstr(self, y, x, text):
      print y, x, len(text)
   def refresh(*x):
      pass

def test():
   textstuff = []
   for x in range(100):
      textstuff.append("-"*100)

   win = Window(TmpWin(), (24,80), (0,0), textstuff)
   win.render()

# text()

