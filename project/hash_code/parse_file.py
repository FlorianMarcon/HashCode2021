import csv
from .street import Street
from .car import Car
from .game import Game
from .intersection import Intersection

def parse_file(path: str) -> Game:
	with open(path, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ')
		row1 = [int(x) for x in next(spamreader)]
		d = row1[0] #Duration
		i = row1[1] #Number of intersections
		s = row1[2] #Number of streets
		v = row1[3] #Number of cars
		f = row1[4] #Fixed point
		print("Duration:			{}".format(d))
		print("Number of intersections:	{}".format(i))
		print("Number of streets:		{}".format(s))
		print("Number of cars:			{}".format(v))
		print("Fixed point:			{}".format(f))

		# Parse streets
		streets = []
		for j in range(0, s):
			line = next(spamreader)
			streets.append(
				Street(
					int(line[0]), int(line[1]), line[2], int(line[3])
				)
			)

		# Parse cars
		cars = []
		for j in range(0, v):
			line = next(spamreader)
			roads: [str] = line[1:]
			road_map = [street for street in streets if street.name in roads]
			car = Car(int(line[0]), road_map)
			cars.append(car)
			street = road_map[0]
			if street != None:
				street.add_car_to_origin(car)

		# Create intersections
		intersections = []
		for j in range(0, i):
			incoming = [street for street in streets if street.i2 == j]
			intersections.append(
				Intersection(j, incoming)
			)

		# game = Game(int(setup_line[1]), int(setup_line[2]), int(setup_line[3]), pizzas)
		return Game(d, streets, cars, intersections, f)
	raise FileNotFoundError(path)
