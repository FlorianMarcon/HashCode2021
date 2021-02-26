import argparse
from project.hash_code.parse_file import parse_file
from project.hash_code.game import Game
from project.hash_code.evolutionary.candidate import Candidate
from project.hash_code.intersection import Intersection


def write_candidate(path: str, candidate: [Candidate], intersections: [Intersection]):
	with open(path, "w+") as f:
		f.write("{}\n".format(len(intersections)))
		genotype = candidate.get_genotype()
		j = 0

		for intersection in intersections:
			f.write("{}\n".format(intersection.id))
			size = len(intersection.incoming)
			f.write("{}\n".format(size))

			for i in range(0, size):
				street = intersection.incoming[i]
				f.write("{} {}\n".format(street.name, genotype[j + i]))

			j += size

if __name__ == "__main__":
	# Parse arguments
	parser = argparse.ArgumentParser(description='Hash code 2021.')
	parser.add_argument('-i', dest='input', metavar='input', type=str, help='File containing data', required=True)
	parser.add_argument('-o', dest='output', metavar='output',  type=str, help='Output file', default="out.txt")
	parser.add_argument('--max-rounds', dest='max_rounds',type=int, help="Maximun cycles", default=10000)
	args = parser.parse_args()

	# Generate objects
	print("Parse file")
	game: Game = parse_file(args.input)

	score = 0
	candidate = None
	# while score == 0:
	print("Generate candidates solution")
	candidates: [Candidate] = game.generate_candidate_solutions(4)
	# candidate = candidates[0]
	# print(candidate)
	# print("Score")

	print("Run")
	candidate = game.run(candidates, args.max_rounds)
	# print("Score is {} pts".format(score))


	write_candidate(args.output, candidate, game.intersections)
	
	# print(game)
	# print(candidates)
		