import os
print "enter the path where the folders should be created "
s=raw_input()
for i in range(1,101):
	os.mkdir(s+"/folder"+str(i))
	with open(s+"/folder"+str(i)+"/file"+str(i)+".txt", "wt") as myfile:
		os.chmod(s+"/folder"+str(i)+"/file"+str(i)+".txt", 0700)
		
