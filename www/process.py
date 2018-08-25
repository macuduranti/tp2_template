import random
from time import sleep
from models import Samples
from database import Database

# temperature=Column('temperature', Integer)
# humidity=Column('humidity', Integer)
# pressure=Column('pressure', Integer)
# windspeed=Column('windspeed', Integer)

def main(session):
	while (True):
		temperature = random.randint(-30,40)
		humidity = random.randint(0,101)
		pressure = random.randint(1011,1014)
		windspeed = random.randint(0,200)

		sample = Samples(temperature=temperature,humidity=humidity,pressure=pressure,windspeed=windspeed)
		session.add(sample)
		session.commit()

		sleep(1)

if __name__ == '__main__':  
    db = Database()
    session = db.get_session()  
    main(session)