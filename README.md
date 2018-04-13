myPDDL - A Modular Knowledge Engineering Tool for PDDL
=======================================================

[![Join the chat at
https://gitter.im/Pold87/myPDDL](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Pold87/myPDDL?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Download accompanying paper:

[Planning in the Wild: Modeling Tools for
PDDL](https://raw.githubusercontent.com/Pold87/myPDDL/master/mypddl.pdf). The
final publication is available at Springer via
[http://dx.doi.org/10.1007/978-3-319-11206-0_27](http://dx.doi.org/10.1007/978-3-319-11206-0_27).

myPDDL is a highly customizable and extensible modular system,
designed for supporting knowledge engineers in the process of writing,
analyzing and expanding PDDL files and thereby promoting the
collaboration between knowledge engineers and the use of PDDL in
real-world applications. It consists of the following integral parts:

- _myPDDL-new_: Create a myPDDL project folder structure with PDDL
  domain and problem skeletons.
- _myPDDL-syntax_: A context-aware syntax highlighting feature.
- _myPDDL-snippet_: Code snippets (templates), which can be inserted
in myPDDL files.
- _myPDDL-distance_: Automated distance calculation for PDDL
  locations, specified in a problem file.
- _myPDDL-diagram_: A type diagram generator for analyzing the
  structure of myPDDL type hierarchies.
- _myPDDL-IDE_: An integrated development environment for the use
of myPDDL in Sublime Text.

Supported file types
-------------------

- .pddl

Installation
------------

Requirements:
- Graphviz (command line tool `dot`)
- Java
- ...

Simply place this repository into your Sublime text packages folder (Preferences \-\> Browse Packages...). You have three possibilities to do so:
- Via Sublime Text Package Control (search for myPDDL) (RECOMMENDED!)
- *git clone https://github.com/Pold87/myPDDL.git myPDDL* 
- Download the ZIP and unzip it to your packages folder.


IMPORTANT
----------

You have to take a few more steps to enjoy all functionalities of myPDDL. I assume you are using Linux:

1. Go to the Sublime Text Packages folder (Preferences -> Browse Packages ...) and change to the myPDDL folder.
2. Ensure that the file myPDDL (inside the folder myPDDL) is executable (type `chmod a+x myPDDL` in your shell).
3. Place the file myPDDL somewhere on your $PATH (e.g. ~/bin) or add the folder myPDDL to your $PATH (e.g. add `export PATH=$PATH:~/.config/sublime-text-2/Packages/myPDDL` to your .bashrc).

4. Open the file myPDDL in a text editor and customize it: While most options are for advanced users can should set the variable "path" to match the corresponding myPDDL folder. The default is probably right for you: "~/.config/sublime-text-2/Packages/myPDDL".
5. Enjoy (in Sublime Text):

    1. Create new projects -  open the command palette (*ctrl+shift+p*) and choose myPDDL-new. Specify the name for the project and press enter -> A new project structure with templates will be generated in your PDDL project directory (the project directory defaults to ~/Documents/myPDDL but you can choose a different folder by setting "pddl_project_folder": "~/Documents/myPDDL/". You should also customize the command for running Sublime Text (normally one of subl, sublime, sublime-text) "sublime_shell_cmd": "subl"). 
    2. Switch to PDDL syntax highlighting: View -> Syntax -> PDDL  
    3. Use snippets: type domain and press *tab* -> a domain skeleton appears (you can find all snippets below)
    4. Display a PDDL type diagram: open the command palette (`ctrl`+`shift`+`p` and choose myPDDL-diagram)
    5. Calculate distances between PDDL predicates in a problem file specified by a predicate 'location' (you can choose a different name for this predicate in the myPDDL (NOT myPDDL.py) file in your $PATH). 

### Customization

You can customize almost anything. Use a different image viewer by changing the variable "viewer" in the myPDDL file on your $PATH or customize the templates for the domain files of myPDDL-new (in the folder templates). 

### Usage

You can also use myPDDL via a command-interface (type `myPDDL` in a shell to see further information).

### Use Snippets

This package contains some often used PDDL constructs. Try one of the following, to see how they work:

* template: `domain`, `problem`
* types: `t1`, `t2`, `t3`, etc.
* predicates: `p1`, `p2`, `p3`, etc.
* functions: `f1`, `f2`, `f3`, etc.
* action: `action`, `durative-action`

Examples
-----------

### Create PDDL Projects (myPDDL-new)

Within the project folder, the domain file domain.pddl and
the problem file p01.pddl (within the folder
problems/) initially contain corresponding PDDL skeletons
which can also be also customized. Additionally the project name is
used as the domain name within the files domain.pddl and p01.pddl.

### Syntax Highlighting (myPDDL-syntax)

![alt
 text](https://raw.githubusercontent.com/Pold87/myPDDL/master/examples/coffee_errors_img.png
 "PDDL syntax highlighting - Theme: Monokai")

A deliberately erroneous domain. Constructs not specified by PDDL are not highlighted.

### Type Diagram Generation (myPDDL-diagram)

![alt
 text](https://raw.githubusercontent.com/Pold87/myPDDL/master/examples/diagram.png
 "An automatically generated type diagram of the Hacker World using
 myPDDL-diagram")

Automatically generated type diagram of the [Hacker
World](https://github.com/Pold87/myPDDL/blob/master/examples/hacker-world.pddl)

Every time myPDDL-diagram is invoked, the names of the saved files are
extended by an ascending revision number. Thus, one cannot only
identify associated PDDL and diagram files, but also use this feature
for basic revision control.

### Distance Calculation (myPDDL-distance)

Before using the calculator the problem file looks like this (p01.pddl):
```
(:init ...
       (location gary 4 2)
       (location pizza 2 3))
```

After the application, the distances have been added in a new file (p01-location.pddl):
```
(:init ...
       (location gary 4 2)
       (location pizza 2 3)
       (distance gary gary 0.0)
       (distance gary pizza 2.2361)
       (distance pizza gary 2.2361)
       (distance pizza pizza 0.0))
```

Volker Strobel - <volker.strobel87@gmail.com> - 2014 
