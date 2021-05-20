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
	
	print(centroids)
	
	for x in arr:
		a = 0
		b = 0
		c = 0
		
		#a = euclidean(
		
def euclidean(x2,y2,x1,y1):
	return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
		
def compare(a,b,c):
	if (a >= b) and (a >= c):
   		greatest = 1
	elif (b >= a) and (b >= c):
   		greatest = 2
	else:
   		greatest = 3
   
	return greatest
	

if __name__ == "__main__":
	main()
