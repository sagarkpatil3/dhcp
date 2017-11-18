import sys
import csv

with open("ip-list.csv") as fd:
	data=[list(line) for line in csv.reader(fd)]
	ldata=len(data)

with open("fixed-ip-list.csv") as fd:
	global data1
	data1=[list(line) for line in csv.reader(fd)]
	global ldata1
	ldata1=len(data)
	
	
	for i in range(0,ldata):
		for j in range(0,ldata1):
			if(data[i]==data1[j]):
				#i=+1
				break
		    	#elif(data[i]!=data1[j]):
			    #j=+1
			if(j==ldata1-1):
				#print("not matched")
#--------********************----------------------------******************************--------------------------*************************
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
				
			#	writer=[]
			#	with open('eggs.csv', 'wb') as csvfile:
    		#		 writer.writerow((sn),(mc))
	
                                                                     

ip_data_config_file = "ip-list.csv"
dhcpd_conf_file = "dhcpd.conf"
def add_rule_to_conf(sys_name, sys_mac, next_ip):
	#add logic to append new rule to conf file

def get_next_sequence_ip(dhcpd_conf_file):
	ip_addr = get_last_ip_configured(dhcpd_conf_file)

	next_ip = genarate_next_sequence_ip(ip_addr)

	return (next_ip)

def add_rule_by_system(sys_config):
	next_ip = get_next_sequence_ip(dhcpd_conf_file)
	add_rule_to_conf(sys_name, sys_mac, next_ip)


def get_configuration_data(ip_data):
	with open("ip-list.csv") as fd:
		data=[list(line) for line in csv.reader(fd)]
		return (data, len(data))

def main():
	print ("I am in main")

	(data, dlen) = get_configuration_data(ip_data_config_file)

	for line in data:
		add_rule_by_system(line)



	
if (__name__ == '__main__'):
	main()

