def main():
	k = 3 #Number of clusters.
	
	id = 0
	arr = []
	
	my_file = open("data.txt","r")
	
	for line in my_file:
		if(line.find("#")==-1):
			x, y = (int(s) for s in line.split())
			arr.append([id, x, y, 0]) #last element is the associated cluster, 0 means none.
			id = id + 1
		
	my_file.close()
	print(arr)


if __name__ == "__main__":
	main()
