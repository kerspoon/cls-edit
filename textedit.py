#!/usr/bin/env python 
# simple text editor
# -*- coding: utf-8 -*- 

import curses
import re 
import unittest

from syntaxclass import SyntaxClass
from window import Window
from textbuffer import LogBuffer, FileBuffer

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

def screen_caret(screen, x, y):
   screen.move(y, x)

def get_point(window=None):
   if window:
      return window.caret
   else:
      return curses.getsyx()[::-1]

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

def main(screen):

   basic_syntax = SyntaxClass("basic")
   basic_syntax.add("character", r".")
   basic_syntax.add("word", r" ")
   basic_syntax.add("sentance", r"\.")


   maxrow, maxcol = screen.getmaxyx() # 24 * 80 
   log_window_rows = 5
   divider_row = maxrow - log_window_rows 

   logger = LogBuffer()
   tmp_subwin = screen.subwin(log_window_rows, 
                              maxcol, divider_row, 0)
   logwin = Window(tmp_subwin, 
                   (log_window_rows, maxcol), 
                   (divider_row, 0),
                   logger)

   # make logger know how to render itself
   # needed to render for each new log message
   logger.render = logwin.render
   logger.msg("== Program Start ==")

   main_buffer = FileBuffer(open("README.markdown"))
   mainwin = Window(screen.subwin(divider_row, maxcol, 0, 0), 
                    (divider_row, maxcol), 
                    (0, 0),
                    main_buffer)
   mainwin.render()

   while True: 
      event = screen.getch() 
      logger.msg("key: '%c'" % chr(event))
      if event == ord("q"): break 
      
      if event == ord("w"):
         logger.msg("clear")
         mainwin.clear()

      if event == ord("e"):
         mainwin.render()

      if event == ord("r"):
         mainwin.addstr("R")

      if event == ord("j"): mainwin.rmove(0, +1)
      if event == ord("k"): mainwin.rmove(0, -1)
      if event == ord("l"): mainwin.rmove(+1, 0)
      if event == ord(";"): mainwin.rmove(-1, 0)

      if event == ord("f"):       
         # need to convert between buffer and window
         ox, oy = get_point()
         nx, ny = basic_syntax.find("character",
                                    main_buffer.buf, 
                                    ox, 
                                    oy)
         if nx == None:
            logger.msg("move (%d,%d) -> None" % (ox, oy)) 
         else:
            logger.msg("move (%d,%d) -> (%d,%d)" % 
                       (ox, oy, nx, ny))

            set_point(screen, nx, ny)
            set_point(mainwin, nx, ny)
            mainwin.render()

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

if __name__ == '__main__':
    curses.wrapper(main)






















































































































































































































































































































































































































































































































































































































































