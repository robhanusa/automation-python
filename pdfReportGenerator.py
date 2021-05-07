#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import json
from reportlab.lib import colors

today = datetime.date.today()

report = SimpleDocTemplate(r"processed.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("Processed Update on {} <br/><br/>".format(today.strftime('%b %d, %Y')), styles["h1"])

#fruits.json is basically a list of dictionaries. So, the fruits variable
#will become a list of dictionaries
with open('fruits.json', 'r') as fruits_json:
    fruits = json.load(fruits_json)

body_string = ""
for dict in fruits:
    body_string += "Name: {} <br/>Weight: {} lbs<br/><br/>".format(dict['name'],
                                                                   dict['weight'])

body =  Paragraph(body_string, styles["Normal"])

#table for pdf
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
table = [[fruits[i]['name'] for i in range(3)], ["{} lbs".format(fruits[i]['weight']) for i in range(3)]]
report_table = Table(data=table, style=table_style, hAlign="LEFT")

#adding graphics to the pdf:
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
report_pie = Pie(width=3, height=3)
# To add data to our Pie chart, we need two separate lists: One for data, and one for labels.
report_pie.data = [fruits[i]['weight'] for i in range(3)]
report_pie.labels = [fruits[i]['name'] for i in range(3)]
# The Pie object isn’t Flowable, but it can be placed inside of a Flowable Drawing.
report_chart = Drawing()
report_chart.add(report_pie)

report.build([report_title, body, report_table, report_chart])