#KMeans
#How to Run
In the terminal, type 'make' to  automatically create a virtual environment and install required packages.

'make clean' to remove binary files.

to run, type the following:

```bash
	@python3 kmeans.py "filename"
```
where filename is the txt file with your data. The final clusters will be output to the terminal.

#To use the default set of data("data.txt"), type the following commands.

For terminal output
```bash
	make run
```

To pipe the output into a txt file called answers.txt
```bash
	make runtxt
```

#FILES
kmeans.py is the main program. It will take in a specified txt file with x,y points then organize them into clusters using the kmeans algorithm. At the moment it can only create 3 clusters. Data points must be 8 or more in total. 

requirements.txt lists the required packages to be installed (None are necessary in this case)

data.txt is the default set of data to be clustered. To test your own set of data, make sure it is in the required format.

answers.txt is the output of the cluster iterations.

.gitignore excludes binary files from the repository.

#REQUIRED FORMAT.
Lines with '#' will be skipped.
int int
int int
int int
