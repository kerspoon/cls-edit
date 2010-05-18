make a text editor just for editing cls files with tab completion, syntax 
highlighting, etc. 
              
Todo
====

 + Get forward char movement using `syntaxclass` working by testing 
   without curses. 
 + get forward line movement ...

Long Term Todo
----

 + Movement 
 + Deletion
 + Text Entry
 + Saving
 + Transpose, Copy, Paste, Extend-Selection

    noun -> character, word, line, sentence, function, class, block
    selection -> from <noun> to <noun>
                 from caret to next <noun>
                 from caret to previous <noun>
    verb -> move-forward <noun> 
            move-backward <noun>
            transpose-forward <selection>
            transpose-backward <selection>
            delete <selection>
            duplicate <selection>
            copy <selection>
            paste <paste-history-number>

select-block :: move-backwards <verb> select move-forwards <verb>
select-line :: move-backwards line select move-forwards line 

`hjkl;` :: char word line sentence/function header/class  
ctrl - `hjkl;` select an additional <verb>



Notes
====

curses movement. each window and the screen have a point. it is moved with 
`move(y,x)` the visual caret is determined by `screen.move`  wheras the 
point at which each window will write to is determined by its own one.

to move we need the point in buffer. to pass into `syntaxclass.find`. this is 
different to `curses.getyx` so it might make sense to have a separate caret var
for each window. 

It looks like curses caret moves to where ever it last wrote to. We don't want 
this. 

    window.getyx
    window.getmaxyx
    window.move


"because we want to have separate views of one buffer it cannot have one caret
it would make much more sense to have one caret per window"

"we are assuming that every SyntaxClass can be parsed by regexp. Much later 
this can be replaced by proper parsing but for now leave it."

Links
====


 1. <http://excess.org/urwid/examples.html>

 1. <http://www.catch22.net/tuts/neatpad/1>

 1. Data Structures For Text Sequences <http://www.cs.unm.edu/~crowley/papers/sds/sds.html> Compares and describes many different text editor data structures. The author (Charles Crowley) has done a very good job, although no sample code is available. The one that stands out is the "Piece Table" method which is where the original idea for my HexEdit design originated. This will be the method we will use for our own text editor. The link above is quite old and is no longer accessible from the main page. Also the images are missing. However the complete PostScript version may be downloaded here. I also have a PDF version which can be downloaded directly.

 1. The Craft of Text Editing <http://www.finseth.com/craft/craft.pdf> Discusses issues related to the design of the EMACS text editor. Although a very well-known editor (primarily for it's user-interface) it appears to use a "buffer gap" method so presumably EMACS is not too good for larger files.

 1. Design and Implementation of an Advanced Text Editor <http://mclauchlan.site.net.au/scott/C=Hacking/C-Hacking11/zedace.html> Whilst the text editor described is not advanced at all (calling it "basic" would be an overstatement), the document does contain some interesting ideas about text editors and user interfaces.

 1. <http://ned.rubyforge.org> Contains a nice selection of links to other text-editing documents and websites.


Ideas
====


Mode List
----

Defines a list of regexps that tell you which filenames belong to which mode.

Syntax Class
----

Defines some classes of things for simple parsing of a file.
For instance you might have a function point-to-next-sentance
which works regardless of which mode you are in as long as the 
concept of sentance exists here. Best is probably that they are 
a list of regexps. Not all need to be defined by all modes, they 
can overlap. 

 + *character*
 + *line*
 + *whitespace*
 + *word*
 + *comment starter*
 + *comment ender*
 + *string starter*
 + *string ender*
 + *parenthesis starter*
 + *parenthesis ender*
 + *keyword*
 + *title*

A few functions to move around in blocks. Where XXX is any item 
defined in syntax-class: 

 + point-forward-start : move to start of next XXX 
 + point-forward-end : move to end of next/current XXX
 + point-backward-start : move to start of previous/current XXX
 + point-backward-end : move to end of previous XXX
 + point-to-nth : move to nth XXX, e.g. 10th line
 + hide-section : display '...' instead of the bit between previous XXX and next YYY.
 + show-section : show text of previously hidden bit.
 + show-all : show all bits hidden by XXX, YYY. e.g. show all comments
 + hide-all : hide every instance of XXX to YYY. e.g. hide all comments
 + show-everything : make sure nothing is hidden
 + transpose-next - move selected region to after next XXX
 + transpose-previous - move selected region to before previous XXX
 + duplicate - make a copy of selected region
 + select : if we are in an XXX or XXX,YYY make it the selected region.
 + delete-syntax-class : if we are in an XXX or XXX,YYY delete it.
 + delete-to : delete everything up to the next instance of XXX
 + delete-from : delete everything up to the previous instance of XXX

Syntax Highlight
----

A list of items defined in syntax-class matched to font-faces. 
So a comment might have a red font and a keyword might be blue.

Keymap
----

Defines what all the keys do in this mode. A list of chars and the 
function to call when those are pressed.

Other Ideas
----

 + Snippets
 + Validate (spelling, parse, compile)
 + Line numbers, word wrapping, window management, file management.


Util Functions
----

 + delete-to-char : delete everything up to the next char matching XXX
 + delete-from-char : delete everything up to the previous char matching XXX
 + set-region-start
 + set-region-end
 + search

