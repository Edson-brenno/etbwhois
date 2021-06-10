#!/usr/bin/python3.9

#Author:Edson Brenno Ribeiro de Santana
#Data: 2021/04/02
#contact: bytegold64@gmail.com

import sys
import socket
import os
import pyfiglet

def intro(): #intro

    print ("=" * 100)
    print ("{}".format(pyfiglet.figlet_format("===== ETB ======== whois")))
    print ("=" * 100)

def ajuda(): #help without intro
    
    print ("=" * 100)
    print ("\n")

    print ("       __________________________________________________________________________________")
    print ("       |                              Whois Brenno Help                                 |")
    print ("       ----------------------------------------------------------------------------------")
    print ("                         |  Ex: {} wwww.whoisetb.com.br   |".format(sys.argv[0]))
    print ("                         ----------------------------------------------")
    print ("                            |     Try: {} [site]    |".format(sys.argv[0]))
    print ("                            -------------------------------------")

def help(): #help

    print ("=" * 100)
    print ("{}".format(pyfiglet.figlet_format("===== ETB ======== whois")))
    print ("=" * 100)
    print ("\n")

    print ("       __________________________________________________________________________________")
    print ("       |                              Whois Brenno Help                                 |")
    print ("       ----------------------------------------------------------------------------------")
    print ("                         |  Ex: {} wwww.whoisetb.com.br   |".format(sys.argv[0]))
    print ("                         ----------------------------------------------")
    print ("                            |     Try: {} [site]    |".format(sys.argv[0]))
    print ("                            -------------------------------------")

def whois(link): #This function will get all information about the site

    byte = "{} \r\n".format(link).encode() #encoding the link
     
    try: #Whois ianna
        
        c1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket
        c1.connect(("whois.iana.org",43)) #conecting to whois ianna

        c1.send(byte) #send link that it will be researched
        resp = c1.recv(1048).decode('UTF-8').split() #obtaining the response
        
        if ( resp[16] == "0" ) or ( resp[25] == "Registry" ): #if the url is invalid

            print ("                                          Invalid URL")
            ajuda()
            quit()
        
        
        who = resp[19] #obtaining responsible organ

        c1.close() #ending the socket

    

    except socket.error as erro:
        
        print ("                                    Had an Error! ({})".format(erro))
        exit
    
    #Whois at the responsible organ:

    c2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #socket
    c2.connect((who,43)) #Conecting at the responsible organ

    c2.send(byte) #send link that it will be researched
    resp2 = c2.recv(2048).decode('ISO-8859-1') #obtaining the response

    print(resp2) #showing what was found

    c2.close() #ending the socket

def main(link1): #main executation
    
    print ("=" * 100)
    print ("{}".format(pyfiglet.figlet_format("ETB Whois")))
    print ("=" * 100)
        
    whois(link1)

    print ("=" * 100)



if ( len(sys.argv) < 2 ): #case haven't enough
    
    help()
    

elif ( sys.argv[1] == "-h" ): #case the user ask for help
    
    help()
    

elif ( sys.argv[1] == "--help"): #case the user ask for help

    help()
    
elif ( len(sys.argv[1].split(".")) == 1 ): #case the user pass an invalid link

    help()

elif ( len(sys.argv[1].split(".")) > 1): #case the user pass an valid link

    main(sys.argv[1])

else:

    help()
