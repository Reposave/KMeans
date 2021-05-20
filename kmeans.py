def main():
	k = 3 #Number of clusters.
	
	id = 0
	arr = []
	
	my_file = open("data.txt","r")
	
	for line in my_file:
		if(line.find("#")==-1):
			x, y = (int(s) for s in line.split())
			arr.append([id, x, y, 0, 4]) #element 3 is the associated cluster, 0 means none. element 4 is the previous cluster the point was in.
			id = id + 1
			
	centroids=[[]]*3 #array of cluster centres. 
	
	#Set initial centroids.
	for x in arr:
		if(x[0]==0):
			centroids[0]= [x[1],x[2]]
		elif(x[0]==3):
			centroids[1]= [x[1],x[2]]
		elif(x[0]==6):
			centroids[2]= [x[1],x[2]]
	
	print(centroids)
	
	my_file.close()
	print(arr)


if __name__ == "__main__":
	main()
