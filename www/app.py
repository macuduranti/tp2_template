# Imports
from flask import Flask
from flask import render_template
from flask import jsonify
from database import Database
from aux_pro import Process

app = Flask(__name__)

db = Database()
pro = Process()

@app.route('/')
def index():
	return render_template('index.html',is_running=pro.is_running())

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888)

@app.route('/ultima/')
def ultima():
	sample = db.get_lastsample()
	return render_template('ultima.html',sample = sample)

@app.route('/vivo/')
def vivo():
	sample = db.get_lastsample()
	return render_template('vivo.html',sample = sample)

@app.route('/promedios/')
def promedios():
	tprom = 0
	hprom = 0
	pprom = 0
	wprom = 0
	samples = db.get_10samples()
	length = len(samples)
	if (length > 0):
		for s in samples:
			tprom += s["temperature"]
			hprom += s["humidity"]
			pprom += s["pressure"]
			wprom += s["windspeed"]

		tprom = round(tprom / length , 2)
		hprom = round(hprom / length , 2)
		pprom = round(pprom / length , 2)
		wprom = round(wprom / length , 2)

	return render_template('promedios.html', samples = samples, tprom = tprom, hprom = hprom, pprom = pprom, wprom = wprom, length = length)

@app.route("/toggle-process/")
def toggle_process():
	if pro.is_running():
		pro.stop_process()
	else:
		pro.start_process()
	return index()

@app.route('/last-sample/', methods = ["GET"])
def get_last_sample():
    sample = db.get_lastsample()
    return jsonify(sample)  

