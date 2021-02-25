import unittest
from project.evolutionary.candidate import Candidate

class TestCandidate(unittest.TestCase):

	def test_get_set_genotype(self):
		genotype = [1, 2, 3, 4, 5]
		candidate = Candidate(genotype)
		self.assertEqual(genotype, candidate.get_genotype())
		candidate.set_genotype([42])
		self.assertNotEqual(candidate.get_genotype(), genotype)

	def test_mutation(self):
		genotype = [1, 2, 3, 4, 5]
		candidate = Candidate(genotype)
		mutated_candidate = candidate.mutation(probability=1)
		self.assertListEqual(genotype, candidate.get_genotype())
		self.assertNotEqual(genotype, mutated_candidate.get_genotype())

	def test_mutation(self):
		c1 = Candidate([1, 2, 3, 4, 5])
		c2 = Candidate([6, 7, 8, 9, 10])
		new_candidates = c1.crossover(c2)
		self.assertEqual(len(new_candidates), 2)
		for c in new_candidates:
			self.assertNotEqual(c.get_genotype(), c1.get_genotype())
			self.assertEqual(len(c.get_genotype()), len(c1.get_genotype()))
			self.assertNotEqual(c.get_genotype(), c2.get_genotype())
			self.assertEqual(len(c.get_genotype()), len(c2.get_genotype()))

