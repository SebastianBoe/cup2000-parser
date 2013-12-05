cup2000-parser
==============

Some code for parsing the output of cup2000 (www.cup2000.dk) and generating some informative match statistics in html/css. First used during UBM 2013 in Trondheim.

Dependencies
==============
It is bash and Python (2.7?/3.0?) dependent.

Usage
==============
It is meant to be started by executing "run".
The program assumes there will be a file called resultater.csv that will be regularly updated. 
resultater.csv needs to be periodically manually exported from cup2000 by clicking buttons in the cup2000 GUI.

The intended usage is that you have one machine in the secretary running cup2000 and another machine running this script connected to some screens. They both need to be connected to the internet and running some file synchronization program e.g. Dropbox to transfer the resultater.csv file to the "display" machine.

The display machine needs to execute "run" e.g. like ./run and it needs to open the html files with some browser.
The browser should be doing auto-refresh to show the newest version of the html file, Opera supported this in 2012.
Remember to turn off the screen saver and auto-sleep on the display machine!

Development
==============
It is the wish of the author that other programmers/badminton players will help out with future development.
