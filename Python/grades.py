from numpy import *

# Each of our grades
kristen_grades = [90, 85, 100, 77, 94]
clarisse_grades = [96, 83, 89, 97, 86]
sapna_grades = [82, 91, 94, 87, 99]

# Class grade book
grade_book = [kristen_grades, clarisse_grades, sapna_grades]

'''
This is what our grade book looks like
[	[90, 85, 100, 77, 94]
	[96, 83, 89, 97, 86]
	[82, 91, 94, 87, 99] ]

'''

# Traverse through the grade book and print all the indivdual grades
print ("GRADES:")
for x in grade_book:
	print (x)
print()
# Extensions: Find the class average, median, and standard deviation
#average
grade_sum = 0
count = 0
for x in grade_book:
	for y in x:
		count+=1
		score = y
		grade_sum = grade_sum + score
average = grade_sum/count
print("THE AVERAGE IS: ")
print(average)
print()
#standard deviation
new_list = []
counter=0
for x in grade_book:
	for y in x:
		counter+=1
		diff = 90 - y
		squared_diff = diff*diff
		new_list.append(squared_diff)

diff_sum = 0
for z in new_list:
	diff_sum = diff_sum + z
sd = (diff_sum/count)**0.5
print("THE STANDARD DEVIATION IS:")
print (sd)
# (For the extentions google for hints!)

# Super extra extensions: calculate the student with highest/lowest average
