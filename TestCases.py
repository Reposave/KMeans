#Ardo Dlamini
#Python Testing Code
#09 March 2020

from random import randint
import os

# generate some integers
	
def CreateRandom(count,UsedEntries,output_file,my_file,num_of_trials,random_amount):

	for line in my_file:
		value = randint(0, 100)

		if count > num_of_trials:
			break
		else:
			if line in UsedEntries:
				pass
				#if this entry was already used, do nothing.
			else:	
				if value >= random_amount:
				#helps randomise outputs to the file.
					output_file.write(line)	
					UsedEntries[line] = 1
					count=count+1
				else:	
					pass
					#Do nothing.
	pass
	return count

def Average(lst): 
    return sum(lst) / len(lst)
 
def IsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def main():
	try:
		cases =	True
		#default should be false

		num_of_trials = eval(input("How many trials to perform: "))
		if not (num_of_trials >= 0 and num_of_trials <= 2976):
			#To avoid infinite loops.
			num_of_trials = 0
		else:
			pass

		random_amount = eval(input("How much randomness (0-100): "))

		if not (random_amount >=0 and random_amount <= 100):
				random_amount = 60
		else:
			pass

		my_file = open("../LoadShedding_Data/Load_Shedding_All_Areas_Schedule_and_Map.clean.final.txt","r")
		output_file = open("../LoadShedding_Data/trials"+str(num_of_trials)+".txt","w")
		count = 1;

		UsedEntries = {}
			
		while not(count>num_of_trials):
			count = CreateRandom(count,UsedEntries,output_file,my_file,num_of_trials,random_amount)
			my_file = 0
			my_file = open("../LoadShedding_Data/Load_Shedding_All_Areas_Schedule_and_Map.clean.final.txt","r")
			#resets file pointer.
				
		my_file.close()
		output_file.close()

		os.system("java LSBSTApp s e a r c h "+str(num_of_trials) +" > "+"../Outputs/LSBSTtrials"+str(num_of_trials) + ".txt")
		os.system("java LSAVLApp s e a r c h "+str(num_of_trials) +" > "+"../Outputs/LSAVLtrials"+str(num_of_trials) + ".txt")

		my_file_LSBST = open("../Outputs/LSBSTtrials"+str(num_of_trials) + ".txt","r")
		my_file_LSAVL = open("../Outputs/LSAVLtrials"+str(num_of_trials) + ".txt","r")
		
		outputLSBST = []
		outputLSAVL = []
			
		for line in my_file_LSBST:
			number = line.split(" ")
			if(IsInt(number[0])):
				outputLSBST.append(eval(number[0]))

		for line in my_file_LSAVL:
			number = line.split(" ")
			if(IsInt(number[0])):
				outputLSAVL.append(eval(number[0]))

		my_file_LSBST = open("../Outputs/LSBSTtrials"+str(num_of_trials) + ".txt","a")
		my_file_LSAVL = open("../Outputs/LSAVLtrials"+str(num_of_trials) + ".txt","a")

		print("\nBest case: "+ str(min(outputLSBST,default=0)), file = my_file_LSBST)
		print("Worst case: "+ str(max(outputLSBST,default =0)), file = my_file_LSBST)
		print("Average Case: "+ str(Average(outputLSBST)), file = my_file_LSBST)
			
		print("\nBest case: "+ str(min(outputLSAVL,default = 0)), file = my_file_LSAVL)
		print("Worst case: "+ str(max(outputLSAVL,default = 0)), file = my_file_LSAVL)
		print("Average Case: "+ str(Average(outputLSAVL)), file = my_file_LSAVL)

		my_file_LSBST.close()
		my_file_LSAVL.close()

	except FileNotFoundError as errno:
		print("File not found")
	finally:
		pass


if __name__ == "__main__":
	main()
