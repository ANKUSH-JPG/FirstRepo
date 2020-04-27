import os
# THIS IS TUI PROGRAM
os.system("tput setaf 1")
print("""                     TUI PROGRAM 
      ---------------------------------------""")
print("ENTER THE IP YOU WANT TO CONNECT:" , end=" ")
getip=input()

while(1):
	os.system("tput setaf 5")
	print(""" 
	1. DATE
	2. CAL
	3. CONFIGURE WEBSERVER
	4. CREATE NEW USER
	5. CREATE FILE
	6. CREATE DIRECTORY
	7. CHANGE DIRECTORY
	8. LIST DATA
	
	""")

	print("ENTER YOUR CHOICE" , end=" ")
	n=int(input())

	if n==1:
		
    		os.system("ssh {} date".format(getip))
	elif n==2:
		
    		os.system("ssh {} cal".format(getip))
	elif n==4:
		
    		print("ENTER NEW USERNAME:" , end=" ")
    		createUser=input()
    		os.system("ssh {0} useradd {1}".format(getip,createUser))
    		print("NEW USER {} CREATED".format(createUser))
	elif n==5:
		
    		print("ENTER FILE NAME:" , end=" ")
    		fileName=input()
    		os.system("ssh {0} touch {1}".format(getip,fileName))
	elif n==6:
		
    		print("ENTER DIRECTORY NAME:" , end=" ")
    		directoryName=input()
    		os.system("ssh {0} mkdir {1}".format(getip,directoryName))
	elif n==7:
		
		print("NAME:" , end=" ")
		moveDirectory=input()
		os.system("ssh {0} cd {1}".format(getip,moveDirectory))
	elif n==8:
		
		os.system("ssh {} ls".format(getip))
	
