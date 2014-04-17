PDDL Sublime Text Plugin
=========================

*View my [Project site](http://pold87.github.io/myPDDL/) for current developments and further information.*

Supported filetypes
-------------------

- .pddl

Installation
------------

Simply place this repository into your Sublime text packages folder (Preferences \-\> Browse Packages...). You have three possibilities to do so:
- Via Sublime Text Package Control (search for myPDDL) (RECOMMENDED!)
- *git clone https://github.com/Pold87/myPDDL.git myPDDL* 
- Download the ZIP and unzip it to your packages folder.



Usage
-----

### Enable Syntax Highlighting

There are several ways to enable PDDL syntax highlighting:

* Open a PDDL file (.pddl) in Sublime Text
* Click the Plain Text label at the bottom right of the sublime text window and select PDDL
* Show the Command Palette (press *Ctrl+Shift+P* in Windows / Linux or *Command+Shift+P* in Mac OS X) and choose *Set Syntax: PDDL*.

### Use Snippets

This package contains some often used PDDL constructs. Try one of the following, to see how they work:

* template: `domain`, `problem`
* types: `t1`, `t2`, `t3`, etc.
* predicates: `p1`, `p2`, `p3`, etc.
* functions: `f1`, `f2`, `f3`, etc.
* action: `action`, `durative-action`

Screenshots
-----------

![alt text](https://raw.githubusercontent.com/Pold87/myPDDL/master/examples/coffee_errors_img.png "PDDL syntax highlighting - Theme: Monokai")

A deliberately erroneous domain. Constructs not specified by PDDL are not highlighted.

