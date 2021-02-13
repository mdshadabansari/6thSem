

months = ['06','07','08','09','10','10','11','12']
keywordList = ['social distancing ', 'quarantine', 'isolation ', 'community spread ', 'lockdown', 'W.H.O guideline', 'guideline', 'awareness ','covid-19 spread', 'Sanitization', 'PPE N95 mask', 'confirmed case', 'prevent', 'stay safe from corona', 'hygiene maintain', 'trauma', 'child affected']

searchList=[]

for mon in months:
	for day in range(1,30):
		for key in keywordList:			
			today=""
			tomorrow=""
			if day<9:
				today="0"+str(day)
				tomorrow="0"+str(day+1)
			elif day==9:
				today="0"+str(day)
				tomorrow=str(day+1)
			else:
				today=str(day)
				tomorrow=str(day+1)
			search=key+" since:2020-"+mon+"-"+today+" until:2020-"+mon+"-"+tomorrow
			#print(search)
			searchList.append(search)

	searchList.append("STOP")
#print(searchList)

 
# writing to file
file1 = open('searchFile.txt', 'w')

for search in searchList:
	file1.write(search+"\n")

#file1.writelines(searchList)
file1.close()
 


# Using readlines()
file1 = open('searchFile.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    #print("Line{}: {}".format(count, line.strip()))
    search=line.strip()
    print(search)