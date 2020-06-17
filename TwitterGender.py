import csv


twitter_data = open("gender-classifier-DFE-791531.csv")
reader = csv.reader(twitter_data)

males = 0
females = 0

next(reader, None) #skipping the header

for line in reader:

	if line[5].lower() == 'male' and float(line[6]) == 1.0:

		males+=1

	elif line[5].lower() == 'female' and float(line[6]) == 1.0:

		females+=1

print("males are: ", males)
print("females are: ", females)
