#!/usr/bin/env python

#
# GS.py - an implementation of the Gale-Shapley algorithm in Python
# Copyright (C) Yavor Stoychev 2011 <stoychev.yavor@gmail.com>
# 
# GS is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# GS is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

#Input Format Example Follows
#######################
#V B A D E C
#W D B A C E
#X B E C D A
#Y A D C D E
#Z B D A E C
 
#A Z V W Y X
#B X W Y V Z
#C W X Y Z V
#D V Z Y X W
#E Y W Z X V
#######################
#End of Input Format


#entry point  	
if __name__ == "__main__":
	menArr = [] 		#all men in the format [arrIndex, name, matchIndex ,choice1@index(2) ,..., choiceN@index(N+2)]
	womenArr = [] 		#all women in the format [arrIndex, name, matchIndex ,choice1@index(2) ,..., choiceN@index(N+2)]


	line = raw_input().split(" ")

	matrixSize = len(line)
	line.insert(1, None)
	line.insert(0, len(menArr))
	menArr.append(line)
	
	for i in range(1, matrixSize - 1):
		prefs = raw_input().split(" ")
		prefs.insert(1, None)
		prefs.insert(0, len(menArr))
		menArr.append(prefs)

	raw_input()

	for i in range(0, matrixSize - 1):
		prefs = raw_input().split(" ")
		prefs.insert(1, None)
		prefs.insert(0, len(womenArr))
		womenArr.append(prefs)
	
	while 1:
		m = False
		for man in menArr:
			if man.count(None) and len(man) > 3: #if man free and hasn't proposed to all
				m = man	#he's our man!
				break
		
		if m == False: #if no one is selected
			break	#exit

		for wom in womenArr:
			if wom[1] == m[3]: # select first woman in preference
				w = wom
				break

		if w.count(None):
			womenArr[w[0]][2] = m[0] #engage woman to man
			menArr[m[0]][2] = w[0] #engage man to woman
		
		elif w.index(m[1]) < w.index(menArr[w[2]][1]):
			menArr[w[2]][2] = None	#dump old man
			womenArr[w[0]][2] = m[0] #engage woman to man
			menArr[m[0]][2] = w[0] #engage man to woman

		else:
			menArr[m[0]].pop(3)

	for man in menArr:
		if man[2] != None: #if he is matched
			print man[1] + " " + womenArr[man[2]][1] #print matching
