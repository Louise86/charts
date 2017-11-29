"""A quick demo to show how to dynamically generate a webpage using the Google
Charts API with the Flask web framework.

Run charts.py and then connect to http://localhost:5000/charts/ in your
browser."""

from flask import Flask, render_template
app = Flask(__name__)

# ages = [('John',10),('Pat',12),('Sophie',14)]
# John is 10
# Pat is 12
# Sophie is 14

@app.route("/age")
def age ():
	x = [('john', 10,"address"), ('pat', 12), ('sophie', 14)]
	return render_template('age.html', boysAges=x)


@app.route("/quotes/<string:name>")
def quote(name):
    return render_template('quote.html', name=name)

@app.route('/chart/')
def chart():
	# The data can come from anywhere you can read it; for instance, a SQL
	# query or a file on the filesystem created by another script.
	# This example expects two values per row; for more complicated examples,
	# refer to the Google Charts gallery.
	data = [('Sunday', 48), ('Monday', 27), ('Tuesday', 32), ('Wednesday', 42),
			('Thursday', 38), ('Friday', 45), ('Saturday', 52)]
	return render_template('chart.html', data=data)

if __name__ == '__main__':
	# Automatically detect changes to charts.py and reload the server as
	# necessary.
	app.run(debug=True)
