from __future__ import annotations
import copy
import random

class Candidate:

	def __init__(self, genotype: [int]):
		super().__init__()
		self.genotype = genotype
		self.score = 0

	def get_genotype(self) -> [int]:
		return self.genotype

	def set_genotype(self, genotype: [int]) -> Candidate:
		self.genotype = genotype
		return self

	def mutation(self, probability: int = 0.8) -> Candidate:
		"""Mutation

		This mutation is a SWAP Mutation

		Args:
			probability (int, optional): Probability that mutation occurs. Defaults to 0.8.

		Returns:
			Candidate: A new candidate solution
		"""
		new = copy.deepcopy(self)
		if random.random() <= probability:
			genotype = new.get_genotype()
			i1 = random.randint(0, len(genotype) - 1)
			i2 = random.randint(0, len(genotype) - 1)
			c = genotype[i1]
			genotype[i1] = genotype[i2]
			genotype[i2] = c
			new.set_genotype(genotype)
		return new

	def crossover(self, c2: Candidate) -> [Candidate]:
		"""Single point crossovef

		Args:
			c2 (Candidate): Second candidate used to recombination

		Returns:
			[Candidate]: List of news candidate (Size should be 2)
		"""

		new_candidates = []
		g1 = self.get_genotype()
		g2 = c2.get_genotype()
	
		if len(g1) != len(g2):
			raise IndexError("Les deux génotypes sont de tailles différentes: {} != {}".format(len(g1), len(g2)))
		
		index_point = random.randint(0, len(g1) - 1)
		new_candidates.append(Candidate(g1[:index_point] + g2[index_point:]))
		new_candidates.append(Candidate(g2[:index_point] + g1[index_point:]))
		
		return new_candidates

	def __len__(self):
		return len(self.genotype)

	def __str__(self):
		# return "str(self.genotype)"
		return str(self.genotype)
	def __repr__(self):
		# return super().__repr__()(self.genotype)
		# return "str(self.genotype)"
		return str(self.genotype)

		