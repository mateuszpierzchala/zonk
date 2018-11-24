#!/usr/bin/env python3
from random import shuffle, randrange

class Door(object):
	def __init__(self,prize):
		self.prize =prize

class Show(object):		
	def __init__(self):
		self.picked = None
		self.revealed = None
		self.alternate = None

	#ukryj nagrode za losowymi drzwiami
		self.prizes=[1,0,0]
		shuffle(self.prizes)

		self.doors = []
		for prize in self.prizes:
			self.doors.append(Door(prize))

	def pick(self):
	#uczestnik wybiera drzwi
		idx = randrange(0, len(self.doors))
		self.picked = idx

	def reveal(self):
	#prowadzacy otwiera kolejne drzwi
		for idx,door in enumerate(self.doors):
			if door.prize or self.picked ==idx :
				continue
			if self.revealed is None:
				self.revealed = idx

	#okreslenie pozostalych drzwi
		for idx, door in enumerate(self.doors):
			if self.picked != idx and self.revealed != idx:
				self.alternate = idx


	def prize_idx(self):
		for idx,door in enumerate(self.doors):
			if door.prize:
				return idx


print ("wybrane, ujawnione,alternatywne, nagroda");


my_data = []
for i in range(1000):
	show=Show()
	show.pick()
	show.reveal()


	single_data = []
	
	single_data.append(show.picked) 
	single_data.append(show.revealed)
	single_data.append(show.alternate)
	single_data.append(show.prize_idx())

	my_data.append(single_data)

	print ("{0},{1}, {2}, {3}".format(show.picked, show.revealed, show.alternate,show.prize_idx()))
print(type(print()))
print(my_data)
import csv
with open('shows.csv', 'w', newline = '', encoding = 'utf-8') as f:
	writer = csv.writer(f)
	writer.writerows(my_data)