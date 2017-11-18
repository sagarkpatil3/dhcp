import sys
import csv

with open("fixed-ip-list.csv") as fd:			#opens the -csv- file as fd:file descriptor
    data=[list(line) for line in csv.reader(fd)]		#reads the line and stores to variable data
    l1=len(data)						#l1 returns the length of data
    l=len(data[0]) 						#l returns the length of dat[0]
    z=0

#----------comparing duplicate names in the csv file----------------------
for i in range(0,l1):					
	for j in range(i,l1):
		if(data[i]==data[j]):
			i=i+1
		else:
#			print("not matched")   
			sn=data[i][0]
			mc=data[i][1]
#--------------opening DHCPD Config File for finding last ip address and increment the new ip--------------------------  
			fd=open("dhcpd.conf","r")
			b=fd.read()
			a=0
			z=0
			a=(b.rfind('fixed-address'))    #finding ip address 
			z=b.find(';',a)				#finding semicolon in that line
			v=[]
			for i in range(z-1,a,-1):		#range from reverse in the same line
			    if(ord(b[i])==ord('.')):		# when it reaches (.) dot it breaks
			        break
			    else:
			        v+=b[i]  			#else add the number to list
			x=v[::-1]   				#reverse the list
			ip1="".join(x)				#removes the space and joins
			ip=int(ip1)				#convert the list into integer
			ip=ip+1					#increment the ip address
			if(ip>254):				#if ip is greater than 254 it ill start from 3
			    ip=3
			str(ip)					#converting the ip into string
			fd.close()
		
#--------------- appending to the file-----------------------------------------
			fd=open("dhcpd.conf","a")
			sys.stdout=fd
			#print("host",sys.argv[1],"{")   for command line arguments
			
			print("host %s {" % (sn))
			#print('        hardware ethernet %s;' %(sys.argv[2])) for command line arguments

			print('        hardware ethernet %s;' % (mc))
			print('        fixed-address 192.168.1.%s;' %(ip))
			print('        option routers 192.168.1.1;')
			print('}')
			print(" ")
		
			fd.close()			

	
#name=row[0]
#mac=row[1]
#print(name)
#print(mac)
'''                                                                                                            
#finding the last ip address from main file

	fd=open("dhcpd.conf","r")
	b=fd.read()
	a=0
	z=0
	a=(b.rfind('fixed-address'))
	z=b.find(';',a)
	v=[]
	for i in range(z-1,a,-1):
	    if(ord(b[i])==ord('.')):
	        break
	    else:
	        v+=b[i]  
	x=v[::-1]
	ip1="".join(x)
	ip=int(ip1)
	ip=ip+1
	if(ip>254):
	    ip=3
	str(ip)
	fd.close()
	
	# appending to the file
	fd=open("dhcpd.conf","a")
	sys.stdout=fd
	#print("host",sys.argv[1],"{")   for command line arguments
	print("host %s {" % name)
	#print('        hardware ethernet %s;' %(sys.argv[2])) for command line arguments
	print('        hardware ethernet %s;' % mac)
	print('        fixed-address 192.168.1.%s;' %(ip))
	print('        option routers 192.168.1.1;')
	print('}')
	print(" ")
	
	fd.close()
'''									
