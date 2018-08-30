# Imports
from flask import Flask
from flask import render_template
from flask import jsonify
from database import Database
from aux_pro import Process

app = Flask(__name__)

db = Database()
pro = Process()


# Ruta inicio
@app.route('/')
def index():
	return render_template('index.html',is_running=pro.is_running()) # Envía el estado del proceso al html

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888)

# Ruta ultima muestra estatica
@app.route('/ultima/')
def ultima():
	sample = db.get_samples(1) # Ejecuta metodo get, devolviendo la ultima muestra
	return render_template('ultima.html',sample = sample[0]) # Envía la muestra al html

# Ruta ultima muestra en vivo
# A diferencia de la anterior, utiliza vivo.js para actualizar la vista
@app.route('/vivo/')
def vivo():
	sample = db.get_samples(1) # Ejecuta metodo get, devolviendo la ultima muestra
	return render_template('vivo.html',sample = sample[0]) # Envía la muestra al html

# Ruta promedios
@app.route('/promedios/')
def promedios():
	tprom = 0
	hprom = 0
	pprom = 0
	wprom = 0
	samples = db.get_samples(10) # Ejecuta metodo get, devolviendo las ultimas 10 muestras
	length = len(samples) 
	if (length > 0): # Si se devolvieron muestras
		for s in samples: # Acumula en cada variable
			tprom += s["temperature"]
			hprom += s["humidity"]
			pprom += s["pressure"]
			wprom += s["windspeed"]

		# Calcula los promedios
		tprom = round(tprom / length , 2)
		hprom = round(hprom / length , 2)
		pprom = round(pprom / length , 2)
		wprom = round(wprom / length , 2)

	return render_template('promedios.html', samples = samples, tprom = tprom, hprom = hprom, pprom = pprom, wprom = wprom, length = length) # Envía la muestra y los promedios al html

# Ruta para activar y desactivar el proceso
@app.route("/toggle-process/")
def toggle_process():
	if pro.is_running(): 	# Si ya esta iniciado
		pro.stop_process() 	# Lo para
	else:					# Si no
		pro.start_process() # Lo inicia
	return index() # Muestra el index

# Ruta para obtener la ultima muestra como json, para su uso en vivo.js
@app.route('/last-sample/', methods = ["GET"])
def get_last_sample():
    sample = db.get_samples(1) # Ejecuta metodo get, devolviendo la ultima muestra
    return jsonify(sample[0])  # Convierte la ultima muestra json

