import random
from time import sleep
from models import Samples
from database import Database
import signal



class GracefulKiller:
	kill_now = False
	def __init__(self):
		signal.signal(signal.SIGINT, self.exit_gracefully)
		signal.signal(signal.SIGTERM, self.exit_gracefully)

	def exit_gracefully(self, signum, frame):
		self.kill_now = True

def main(session):
	killer = GracefulKiller()
	while (True):
		temperature = random.randint(-30,40)
		humidity = random.randint(0,101)
		pressure = random.randint(1011,1014)
		windspeed = random.randint(0,200)

		sample = Samples(temperature=temperature,humidity=humidity,pressure=pressure,windspeed=windspeed)
		session.add(sample)
		session.commit()

		sleep(1)
		if killer.kill_now:
			session.close()
			break

if __name__ == '__main__':  
	db = Database()
	session = db.get_session()  
	main(session)