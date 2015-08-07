
			PypeR

Please refer to http://www.webarray.org/softwares/PypeR/ for bug fixes.

Requirements:
	Python 2.3 or later. 
	PypeR can run with different Python implementations: 
		Python 2.X.X
		Python 3.X.X
		Jython
		IronPython

For installation:
	# python setup.py install
	  or
	# easy_install PypeR
	  or
	# pip install PypeR

To upgrade to the newest version:
	# python setup.py install
	  or
	# easy_install --upgrade PypeR
	  or
	# pip install --upgrade PypeR

Known issues:
	1. Problem: cannot run with IronPython on mono.
	   Platform: tested on Ubuntu-10.04, mono 2.4.4, IronPython 2.6 Beta 2
		   DEBUG (2.6.0.20) on .NET 2.0.50727.1433
	   Behavior: report "TypeError: Cannot cast from source type to desination type."
	   Reason: This happens when call a function found in the dict "str_func",
		   e.g. "str_func[type(obj)](obj)".  Most likely it is caused by a bug
		   of IronPython (or mono?). 
	   Solution: It is possible to use IF...ELIF...ESLE to replace the dict
		   "str_func". However it will make the function "Str4R" much longer
		   than it is now.

For Help:
	Please see the documents of the module, class, and methods

For example:
	The script "test.py" covers all the typical uses of PypeR

Citation:
	@article{Xia:McClelland:Wang:2010:JSSOBK:v35c02,
	  author =	"Xiao-Qin Xia and Michael McClelland and Yipeng Wang",
	  title =	"PypeR, A Python Package for Using R in Python",
	  journal =	"Journal of Statistical Software, Code Snippets",
	  volume =	"35",
	  number =	"2",
	  pages =	"1--8",
	  day =  	"30",
	  month =	"7",
	  year = 	"2010",
	  CODEN =	"JSSOBK",
	  ISSN = 	"1548-7660",
	  bibdate =	"2010-03-23",
	  URL =  	"http://www.jstatsoft.org/v35/c02",
	  accepted =	"2010-03-23",
	  acknowledgement = "",
	  keywords =	"",
	  submitted =	"2009-10-23",
	}


FAQs:

1.	Q: I got error message when trying to use PypeR:
		>>> from pyper import *
		>>> r = R()

		Traceback (most recent call last):
		......
		"WindowsError: [Error 2] The system cannot find the file specified"
		>>>

	A: Usually this means PypeR cannot find the R program on Windows. There is
		two ways to tell PypeR where R is. E.g., R is installed at 
		"C:\Program Files\R\R-2.11.1".

		method 1 - initialize R with full path:
			>>>  r = R(RCMD="C:\\Program Files\\R\\R-2.11.1\\bin\\R")

		method 2 - add "C:\\Program Files\\R\\R-2.11.1\\bin" into the PATH
			environmental variable:

			(1) Right click "My Computer" on Windows XP (or "Computer" on
				Windows 7), either on your desktop or in your start menu.
			(2) Click "Properties"
			(3) In Windows 7, click "Advanced System Settings" on the left.
			(4) In the "Advanced" tab, click the "Environment Variables" button.
			(5) Double-click the PATH variable, and add your R path to the list.
				Entries are separated by semicolons.  For example:
				%WinDir%\System32;C:\Program Files\R\R-2.11.1\bin

2.	Q: What is the differences between r("myvar"), r["myvar"], r.myvar,
		r.get("myvar", "a wild value"), and r.assign("myvar", "a new value")?

	A: These forms serve for different purpose:
		(1) r("myvar")
			Here "myvar" is a R variable name or a complex R expression. This
			equals to type myvar on the R terminal. The information displayed
			on the terminal will be returned as a Python string.

		(2) r["myvar"] 
			This form can be used to get values from R, or set value for a R
			variable. 

			If it is used to get value from R, "myvar" can be a R variable name
			or a complex R expression, and this will return the value of
			"myvar" instead of the output on STDOUT. 

			To set value for the R variable, the form is:
				r["myvar"] = "something"
			here "myvar" should be valid R variable name.

		(3) r.myvar
			This form is similar to r["myvar"], but diffs in two aspects:
			a) myvar have to following Python's name convention too.
			b) IMPORTANT: if myvar is a attribute of the python object r, it
				will override (shield) the variable myvar in R!

		(4) r.get("myvar", "a wild value")
			This form is similar to r["myvar"], but it can only be used to get
			values from R. If there is no variable "myvar" in R, the value "a
			wild value" will be returned

		(5) r.assign("myvar", "a new value") 
			This form is used to assign value ("a new value") to a R variable
			("myvar"). Here "myvar" should be a valid R variable name.

3.	Q: How can I get a named list in R returned as a dict, - just as been done
		in RPy?

	A: Due to named R list allows replicated names, while Python dictionary
		does not, conversion of R named list to Python dictionary may lead to
		lost of data. That is why PypeR return a list of tuples (name, value)
		for R named list. However it is possible to get dictionary returned
		since PypeR 1.0.2:
			method 1:
				>>> r.get("myvar", use_dict=True)
			method 2:
				>>> r.use_dict = True
				>>> r.myvar
		If this failed, please update your PypeR with the newest version.

