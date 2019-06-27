from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/SmartParking')
def SmartParking():
	return render_template('SmartParking.html')

@app.route('/Form')
def Form():
	
	return render_template('FormPage.html' )

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
