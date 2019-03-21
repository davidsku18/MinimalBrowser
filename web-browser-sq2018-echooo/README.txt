Simple Browser

In-class activity on March 27, 2018:
- Top quality attributes reflected in your browser:
	1. simplicity (our browser is made to be intuitive and simple for users)
	2. transparency (we're really honest about what failures there are) 
	3. timeliness (the amount of time that it takes to load webpages does not take too long for our web browser)
	4. affordability (our web browser is currently free-to-download from GitHub)
	5. testability (we have been working on making tests to cover our code)
	6. fault tolerance (at least our web browser doesn't crash when something fails to execute)

- Most obvious missing / poorly reflected quality attributes:
	1. security (our current web browser is simply focused on displaying 
		     and images without regards to making the web browser secure)
	2. robustness (need to handle more error cases)
	3. modularity (almost all of our functions are jammed into the code for BasicUI, as opposed to organizing functions into
		       separate "super-functions" that can be eventually used by BasicUI)
	4. deployability (app is able to be distributed to the audience as a workable application)
	5. tailorability (user is able to customize their personal application of the web browser)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suggested Sites:

	https://library.up.edu
	


Dependencies:
	basicUI:	
		from tkinter import *
		from PIL import Image, ImageTk
		from io import BytesIO
		import sys, getURL, requests, urllib.request, LinkedList, textDisplay, caching
		import base64
	caching:
		import time, sqlite3
	parseCSS:
		import re
	textDisplay:
		import math

Minimum python version:
-Python 3

Known bugs/issues:
	Bugs when url is not in proper https:// format.

Features:
	Ability to customize: 
		- Font style
		- Font size
		- Back display with CSS 

Comparison to SRS:
	Our main product features highlighted in our SRS document are 
	-Displaying text in web-pages in a font style and size that is easily readable by users. 
		This is well implemented in our version. For furture versions we hope to be able to adjust font size. 
	-Allowing ease of viewing a previously visited web page and reloading a web page that is currently being viewed. 
		Navigation is well implemented with moving forward, backward, and reloading. 
	-Enabling users to have the freedom to customize the web browser's settings and features to fit their own specific needs and desires for surfing the web. 
		Customization is currently in the works for being able to select different fonts but is not fully implemented in this version. Future versions will be more customizable. 

Performance testing:
	Site:					Load time:
	http://google.com				0.12489676475524902
	http://youtube.com				2.193676710128784
	http://up.edu					0.3375873565673828
	http://amazon.com				Not able to load
	http://en.wikipedia.org/wiki/Main_Page		0.5468103885650635

Test coverage: 
	Unfortunatley, Travis CI which we have been using to test most of our functions has trouble running our basicUI tests because travis-CI itself cannot open the browser to be tested. 
	With that said, we still have tests that test the navigation and the text display in the basicUI but we have to run them directly from python in order for them to pass. 
	Therefore, our coverage on Travis-CI shows up as virtually none, but we do have passing tests for basicUi, caching, getURL, parseCSS, and stripHTML. The textDisplay combines parts from placeholderImageVideoLinks which we have passing tests for. 
