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
	print(arr)
	
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
			
	print("\nCENTROIDS")
	print(centroids)
	
	for x in arr:
		x[4] = x[3]
		a = 0
		b = 0
		c = 0
		
		a = eucl_dist(centroids[0][0],centroids[0][1],x[1],x[2])
		b = eucl_dist(centroids[1][0],centroids[1][1],x[1],x[2])
		c = eucl_dist(centroids[2][0],centroids[2][1],x[1],x[2])
		
		x[3] = compare(a,b,c)
		
	print("\nRESULTS")
	print(arr)
		
def eucl_dist(x2,y2,x1,y1):
	return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
		
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
