class Car:

	def __init__(self, number_of_street, road_map: []):
		super().__init__()
		self.number_of_street = number_of_street
		self.road_map = road_map

	def __repr__(self):
		return "{} {}".format(self.number_of_street, self.road_map)
