import random

n=25
catalog=[]

#populate array with random prices for 25 items between $1-$20
item=0
while item <25:
	catalog.append(random.randint(1,20))
	item+=1
print catalog
print '\nSorted...\n'
catalog.sort()
print str(catalog)
i=0
for i in range(len(catalog)):
	i+=1
	if i <=len(catalog)/2:
		if catalog[i-1]+catalog[-i]<=25:
			print str(catalog[i-1])+'  +  '+str(catalog[-i])+'  =  '+str(catalog[i-1]+catalog[-i])+'     Valid combination - $'+ str(25-(catalog[i-1]+catalog[-i]))+' left'
		else:
			#over credit
			print str(catalog[i-1])+'  +  '+str(catalog[-i])+'  =  '+str(catalog[i-1]+catalog[-i])+'     Not valid combination - $'+ str((catalog[i-1]+catalog[-i])-25)+' over'

######Need to handle length of array and different permutations
	'''
	if len(catalog)%2==1:
		#odd number of indicies	
		if i <=len(catalog)/2:
			print str(catalog[i-1])+'  +  '+str(catalog[-i])+'  =  '+str(catalog[i-1]+catalog[-i])
	else:
		#even
		#only go up to len(catalog)/2
		if i <=len(catalog)/2:
			print str(catalog[i-1])+'  +  '+str(catalog[-i])+'  =  '+str(catalog[i-1]+catalog[-i])
'''
