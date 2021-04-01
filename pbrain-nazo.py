#!/usr/bin/env python3

import sys, os
import random
import time
from math import exp

random.seed()

def checkMask(board, i, j, mask):
	for k in range(len(mask)):
		for l in range(len(mask[k])):
			if board[i+k][j+l] != mask[k][l] and mask[k][l] != -1:
				return False
	return True
def zeroIJ(mask, offsetIJ):
	for i in range(len(mask)):
		for j in range(len(mask[i])):
			if mask[i][j]==0:
				return i+offsetIJ[0],j+offsetIJ[1]
	return 'NO ZERO ERROR'
def findMask(board, maskTemp):
	mask1 = rotateMaskThisMuch(maskTemp, 90)
	mask2 = rotateMaskThisMuch(maskTemp, 180)
	mask3 = rotateMaskThisMuch(maskTemp, 270)
	masks = [maskTemp, mask1, mask2, mask3]
	for mask in masks:
		for i in range(len(board)-(len(mask)-1)):
			for j in range(len(board[i]) - len(mask[0])):
				if checkMask(board,i,j,mask) == True:
					return zeroIJ(mask,(i,j))
	return 'notfound'
def rotateMaskThisMuch(mask, howMuch):
	if howMuch == 90:
		return list(rotateMask(mask))
	elif howMuch == 180:
		return list(rotateMask(list(rotateMask(mask))))
	else:
		return list(rotateMask(list(rotateMask(list(rotateMask(mask))))))
def rotateMask(mask):
	return zip(*mask[::-1])


class Handler:
	def __init__(self):
		self.infos = {}
		self.size = 0
		self.boarding = False
		self.masks = [
			{'board':[	[0,1,1,1,1]		], 'prio':10},
			{'board':[	[0,-1,-1,-1,-1],
						[-1,1,-1,-1,-1],
						[-1,-1,1,-1,-1],
						[-1,-1,-1,1,-1],
						[-1,-1,-1,-1,1]	], 'prio':10},
			{'board':[	[1,1,0,1,1]		], 'prio':10},
			{'board':[	[1,-1,-1,-1,-1],
						[-1,1,-1,-1,-1],
						[-1,-1,0,-1,-1],
						[-1,-1,-1,1,-1],
						[-1,-1,-1,-1,1]	], 'prio':10},
			{'board':[	[1,1,1,0,1]		], 'prio':10},
			{'board':[	[1,-1,-1,-1,-1],
						[-1,1,-1,-1,-1],
						[-1,-1,1,-1,-1],
						[-1,-1,-1,0,-1],
						[-1,-1,-1,-1,1]	], 'prio':10},
			{'board':[	[0,2,2,2,2]		], 'prio':9},
			{'board':[	[0,-1,-1,-1,-1],
						[-1,2,-1,-1,-1],
						[-1,-1,2,-1,-1],
						[-1,-1,-1,2,-1],
						[-1,-1,-1,-1,2]	], 'prio':9},
			{'board':[	[2,2,0,2,2]		], 'prio':9},
			{'board':[	[2,-1,-1,-1,-1],
						[-1,2,-1,-1,-1],
						[-1,-1,0,-1,-1],
						[-1,-1,-1,2,-1],
						[-1,-1,-1,-1,2]	], 'prio':9},
			{'board':[	[2,2,2,0,2]		], 'prio':9},
			{'board':[	[2,-1,-1,-1,-1],
						[-1,2,-1,-1,-1],
						[-1,-1,2,-1,-1],
						[-1,-1,-1,0,-1],
						[-1,-1,-1,-1,2]	], 'prio':9},
			{'board':[	[0,1,1,1,0]		], 'prio':8},
			{'board':[	[0,-1,-1,-1,-1],
						[-1,1,-1,-1,-1],
						[-1,-1,1,-1,-1],
						[-1,-1,-1,1,-1],
						[-1,-1,-1,-1,0]	], 'prio':8},
			{'board':[	[0,1,0,1,1,0]		], 'prio':8},
			{'board':[	[0,-1,-1,-1,-1,-1],
						[-1,1,-1,-1,-1,-1],
						[-1,-1,0,-1,-1,-1],
						[-1,-1,-1,1,-1,-1],
						[-1,-1,-1,-1,1,-1],
						[-1,-1,-1,-1,-1,0]	], 'prio':8},
			{'board':[	[0,2,2,2,0]		], 'prio':7},
			{'board':[	[0,-1,-1,-1,-1],
						[-1,2,-1,-1,-1],
						[-1,-1,2,-1,-1],
						[-1,-1,-1,2,-1],
						[-1,-1,-1,-1,0]	], 'prio':7},
			{'board':[	[2,2,0,0,2]		], 'prio':7},
			{'board':[	[2,-1,-1,-1,-1],
						[-1,2,-1,-1,-1],
						[-1,-1,0,-1,-1],
						[-1,-1,-1,0,-1],
						[-1,-1,-1,-1,2]	], 'prio':7},
			# {'board':[	[-1,-1,-1,-1,-1],
			# 			[-1,-1,-1,-1,-1],
			# 			[-1,-1,-1,-1,-1],
			# 			[-1,-1,-1,-1,-1],
			# 			[-1,-1,-1,-1,-1]	], 'prio':7},
			{'board':[	[0,-1,-1,2,2],
						[-1,-1,-1,-1,-1],
						[-1,-1,-1,-1,-1],
						[2,-1,-1,-1,-1],
						[2,-1,-1,-1,-1]	], 'prio':6},
			{'board':[	[0,-1,2,2],
						[-1,-1,-1,-1],
						[2,-1,-1,-1],
						[2,-1,-1,-1]	], 'prio':6},
			{'board':[	[2,-1,-1,-1,2],
						[-1,2,-1,2,-1],
						[-1,-1,0,-1,-1]	], 'prio':7},
			{'board':[	[2,0,2,2]		], 'prio':7},
			{'board':[	[2,-1,-1,-1],
						[-1,0,-1,-1],
						[-1,-1,2,-1],
						[-1,-1,-1,2]	], 'prio':7},
			{'board':[	[2,0,2]		], 'prio':6},
			{'board':[	[2,-1,-1],
						[-1,0,-1],
						[-1,-1,2]	], 'prio':6},
			{'board':[	[2,2,0]		], 'prio':6},
			{'board':[	[2,-1,-1],
						[-1,2,-1],
						[-1,-1,0]	], 'prio':6},
			{'board':[	[2,-1],
						[-1,0]	], 'prio':2},
			{'board':[	[1,-1],
						[-1,0]	], 'prio':1},
			{'board':[	[1,0]		], 'prio':1},
			{'board':[	[2,0]		], 'prio':1},
		]
	def run(self):
		end = False
		while not end:
			cmd = input().rstrip()
			end = self.handleCommand(cmd)
	def highestPrio(self, founds):
		prio, index = 0,0
		for i,found in enumerate(founds):
			if found[1] > prio:
				index = i
				prio = found[1]
		return index
	def nextMove(self):
		founds = []
		for mask in self.masks:
			f = findMask(self.board, mask['board'])
			if f != 'notfound':
				founds.append([f, mask['prio']])
		if len(founds):
			ind = self.highestPrio(founds)
			self.board[founds[ind][0][0]][founds[ind][0][1]] = 1
			return str(founds[ind][0][0])+','+str(founds[ind][0][1])
		i,j = random.randint(0,19),random.randint(0,19)
		while self.board[i][j] != 0:
			i,j = random.randint(0,19),random.randint(0,19)
		self.board[i][j] = 1
		return str(i)+','+str(j)
	def handleCommand(self, cmd):
		if self.boarding and not cmd.startswith('DONE'):
			spl = [int(v) for v in cmd.split(',')]
			self.board[spl[0]][spl[1]] = spl[2]
			return False
		if cmd.startswith('END'):
			return True
		elif cmd.startswith('START'):
			if int(cmd[6:]) != 20:
				print('ERROR unsupported size must be square of 20')
			else:
				self.size = int(cmd[6:])
				self.board = [[0 for i in range(self.size)] for j in range(self.size)]
				print('OK')
			return False
		elif cmd.startswith('INFO'):
			spl = cmd.split(' ')
			self.infos[spl[1]] = spl[2]
			return False
		elif cmd.startswith('TURN'):
			spl = cmd[5:].split(',')
			self.board[int(spl[0])][int(spl[1])] = 2
			print(self.nextMove())
			return False
		elif cmd.startswith('BEGIN'):
			print(self.nextMove())
			return False
		elif cmd.startswith('RESTART'):
			self.board = [[0 for i in range(self.size)] for j in range(self.size)]
			print('OK')
			return False
		elif cmd.startswith('BOARD'):
			self.boarding = True
			return False
		elif cmd.startswith('DONE'):
			self.boarding = False
			print(self.nextMove())
			return False
		elif cmd.startswith('ABOUT'):
			print('name="nazo", version="15.6.8", author="Najo", country="FR"')
			return False
		return False

handler = Handler()
try:
	handler.run()
except KeyboardInterrupt:
	print("\nUser pressed Ctrl-c.")
except Exception as e:
	print('Main error :' + str(e))
