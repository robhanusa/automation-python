# automation-python
Basic automated report generation tasks with python

failureModeExcelReport.py: 
This takes an input of an excel log hypothetical failures on a manufacturing line, compares
it to pre-determined severity and occurrence rankings, and outputs a formatted excel report
of the failures, giving each failure mode an 'RPN' value of occurrence X severity, for
time periods of 1 month and 1 year. Note that despite my use of the 'RPN' as 'risk priority
number' terminology, this falls short of being a true FMEA. For that, other parameters
such as detection would need to be considered.

errorLogReportGenerator.py:
Demonstrates reading a log file (.log or .txt) line by line, generating a summary by 
summing the event type per user, sorting the summary, and creating .csv files as output. 
Also a good example of regex, re.search() function to search through text. Uses syslog.log
as input.

pdfReportGenerator.py:
Loads data from a json file (here, fruits.json) generates a pdf report including title, 
body, and a pie chart.

Image_flip_resize.py:
Flips and resizes all images in a folder, as long as they're .jpg or .tiff, and renames the 
pictures. If the picture is .tiff, it converts it to .jpg.

