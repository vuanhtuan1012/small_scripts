# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-11-26 15:06:28
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-11-26 15:29:46

import time

class Profiler():
	def __init__(self, name=None):
		self.name = name
		self.start = time.time()
		self.checkpoints = dict()

	def setCheckpoints(self, name):
		elapsed = time.time() - self.start
		self.checkpoints.update({name: elapsed})

	def elapsed(self, cp1, cp2):
		if cp1 not in self.checkpoints or cp2 not in self.checkpoints:
			return None
		return abs(self.checkpoints[cp1] - self.checkpoints[cp2])

	def getCheckpoints(self):
		return self.checkpoints

	def printCheckpoints(self):
		for c, e in self.checkpoints.items():
			print('[{name}] Checkpoint {checkpoint} took {elapsed} seconds'.format(name=self.name, checkpoint=c, elapsed=e))


'''
Example
'''
def expensive_function():
	for x in range(5000000):
		i = x^x^x

def main():
	pf = Profiler()
	expensive_function()
	pf.setCheckpoints('c1')
	expensive_function()
	expensive_function()
	pf.setCheckpoints('c2')
	pf.printCheckpoints()
	cp = pf.getCheckpoints()
	print('[{pf}] Elapsed time between c1 and c2 is: {el} seconds'.format(pf=pf.name, el=pf.elapsed('c1', 'c2')))

if __name__ == '__main__':
	main()