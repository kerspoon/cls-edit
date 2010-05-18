make a text editor just for editing cls files with tab completion syntax highlighting etc. 


Todo
====

 + Get movement working

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


