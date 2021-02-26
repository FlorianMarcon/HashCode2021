from .street import Street
from .car import Car
from .intersection import Intersection
from .evolutionary.candidate import Candidate
import numpy
import copy

from random import randint
# DEBUG=True
DEBUG=False
class Game:

	def __init__(self, duration: int, streets: [Street], cars: [Car], intersections: [Intersection], fixed_point: int):
		super().__init__()
		self.duration = duration 
		self.streets = streets 
		self.intersections = intersections
		self.cars = cars 
		self.fixed_point = fixed_point


	def generate_candidate_solutions(self, quantity) -> [Candidate]:
		size = len(self.streets)
		candidates = []
		print('Candidate size {}'.format(size))
		for j in range(0, quantity):
			print('j {}'.format(j))
			candidate = []
			for i in range(0, size):
				print('\ti {}'.format(i))
				candidate.append(randint(0, self.duration / 2))

			candidates.append(Candidate(candidate))

		return candidates

	def score_candidate(self, candidate: Candidate):
		intersections = self.generate_phenotype(candidate)

		t = 0 #Time
		score = 0
		self.print("--- Score candidate ---")
		while t < self.duration:
			self.print("Time {}".format(t))
			for intersection in intersections:
				self.print("\tIntersection {}".format(intersection.id))
				street = intersection.run_incoming[0]
				if street != None:
					self.print("\tCurrent Street {} with time {}".format(street.name, street.time))

					for car in street.cars:
						self.print("\tCar {} has {} seconds of delay".format(car[1], car[0]))

				self.print()
				s = intersection.next()
				if s > 0:
					self.print("\t add score {} * {} + {} - {}".format(s,  self.fixed_point, self.duration, t))
					score += s * self.fixed_point + (self.duration - t)
			t += 1
		
		self.print("--- Score {}".format(score))
		return score

	def score_candidates(self, candidates: [Candidate]):
		return [(self.score_candidate(candidate), candidate) for candidate in candidates]

	def generate_phenotype(self, candidate: Candidate):
		
		genotype = candidate.get_genotype()
		j = 0

		self.print("--- Generate Phenotype ---")
		for intersection in self.intersections:
			self.print("Intersection {}".format(intersection.id))
			intersection.reset_run()

			size = len(intersection.incoming)
			for i in range(0, size):
				street = intersection.incoming[i]
				street.set_delay(genotype[j + i])
				street.reset_cars()
				self.print("\tStreet {} have {} cars and delay {}".format(street.name, len(street.cars), street.delay))

			j += size

		self.print("--- Phenotype is generated ---")
		return self.intersections

	def run(self, candidates: [Candidate], rounds: int):

		scored_candidates = self.score_candidates(candidates)
		print(scored_candidates)
		while rounds >= 0:
			print("Rounds remainding {}:\t {}".format(rounds, scored_candidates[-1][0]))
			def getKey(item):
				return item[0]
			scored_candidates = sorted(scored_candidates, key=getKey)
			b1 = (scored_candidates[-1])[1]
			b2 = (scored_candidates[-2])[1]
			b1_mutate = b1.mutation()
			b2_mutate = b2.mutation()

			scored_candidates += self.score_candidates([b1, b2])
			scored_candidates = sorted(scored_candidates, key=getKey)
			
			scored_candidates = scored_candidates[2:]

			rounds -= 1

		return (scored_candidates[-1])[1]


	def print(self, message: str = ""):
		if DEBUG:
			print(message)
	# 	pass
