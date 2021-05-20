import math

def main():
	k = 3 #Number of clusters.
	
	id = 0
	arr = []
	
	my_file = open("data.txt","r")
	
	for line in my_file:
		if(line.find("#")==-1):
			x, y = (int(s) for s in line.split())
			arr.append([id, x, y, 0, 0]) #element 3 is the associated cluster, 0 means none. element 4 is the previous cluster the point was in.
			id = id + 1
	
	my_file.close()
	#print(arr)
	
	centroids=[[]]*3 #array of cluster centres. 
	
	#Set initial centroids.
	for x in arr:
		if(x[0]==0):
			centroids[0]= [x[1],x[2]]
			x[3] = 1
		elif(x[0]==3):
			centroids[1]= [x[1],x[2]]
			x[3] = 2
		elif(x[0]==6):
			centroids[2]= [x[1],x[2]]
			x[3] = 3
			
	#print("\nCENTROIDS")
	#print(centroids)
	
	check = 0
	iteration = 1
	
	while(check < id):
	
		check = 0 #Reset check counter.
		
		cluster1 = []
		cluster2 = []
		cluster3 = []
			
		#Find the cluster.
		for x in arr:
		
			x[4] = x[3]
			
			a = 0
			b = 0
			c = 0
			
			a = eucl_dist(centroids[0][0],centroids[0][1],x[1],x[2])
			b = eucl_dist(centroids[1][0],centroids[1][1],x[1],x[2])
			c = eucl_dist(centroids[2][0],centroids[2][1],x[1],x[2])
			
			x[3] = compare(a,b,c)
			
			if(x[3] == 1):
					cluster1.append([x[1],x[2],x[0]])
			elif(x[3] == 2):
					cluster2.append([x[1],x[2],x[0]])
			else:
					cluster3.append([x[1],x[2],x[0]])
			
			if(x[4] == x[3]):
				check = check + 1 #count the number of points that haven't changed clusters. If it is 8, then we have reached convergence.
				
		print("Iteration " + str(iteration) + "\n")
		iteration = iteration + 1
		
		print("Cluster 1: ", end = '')
		output(cluster1, centroids[0])
		
		print("Cluster 2: ", end = '')
		output(cluster2, centroids[1])
		
		print("Cluster 3: ", end = '')
		output(cluster3, centroids[2])
		
		if(check < id):
				centroids[0] = mean_cent(cluster1)
				centroids[1] = mean_cent(cluster2)
				centroids[2] = mean_cent(cluster3)
				
		

def output(cluster, centroid):
	for i in range(0, len(cluster)):
		if(i==(len(cluster)-1)):
			print(cluster[i][2]+1)
		else:
			print(cluster[i][2]+1, end = ',')
			
	print("Centroid: ", end ='')
	print(centroid)
	print()
		
		
#Calculate the new Mean centroid.
def mean_cent(cluster):

	i = len(cluster)
	
	x = 0
	y = 0
	
	for m in cluster:
		x = x + m[0]
		y = y + m[1]
		
	x = x/i
	y = y/i
	
	return [x,y]
	
def eucl_dist(x2,y2,x1,y1):
	return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

#Function to find the shortest distance.	
def compare(a,b,c): 
	if (a <= b) and (a <= c):
   		shortest = 1
	elif (b <= a) and (b <= c):
   		shortest = 2
	else:
   		shortest = 3
   
	return shortest
	

if __name__ == "__main__":
	main()
