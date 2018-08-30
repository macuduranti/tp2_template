import random
from time import sleep
from models import Samples
from database import Database
import signal


# Método para parar correctamente el proceso
class GracefulKiller:
	kill_now = False
	def __init__(self):
		signal.signal(signal.SIGINT, self.exit_gracefully)
		signal.signal(signal.SIGTERM, self.exit_gracefully)

	def exit_gracefully(self, signum, frame):
		self.kill_now = True


# Main del proceso
def main(session):
	killer = GracefulKiller()
	while (True):
		temperature = random.randint(-30,40) # Crea valores aleatorios
		humidity = random.randint(0,101)
		pressure = random.randint(1011,1014)
		windspeed = random.randint(0,200)
		# Crea una muestra a partir de ellos
		sample = Samples(temperature=temperature,humidity=humidity,pressure=pressure,windspeed=windspeed)
		session.add(sample)
		session.commit() # Persiste en la db

		sleep(1) # Delay de un segundo
		if killer.kill_now:
			session.close()
			break

if __name__ == '__main__':  
	db = Database()
	session = db.get_session()  
	main(session)