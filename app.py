# Import flask module. 
from flask import Flask, render_template

# Create app using flask. 
app = Flask(__name__)

# Define basic route `/`. 
@app.route("/")

# Define basic route request handler. 
def main():
	return render_template('homepage.html')

'''
Check if executed file is the main program. 
If it is, run the app. 
'''
if __name__ == "__main__": 
	app.run(debug=True)

