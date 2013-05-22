#!/usr/bin/python

## Import #############
#######################

import time
import os
import random
import sys

#######################
## Intro ##############

print ""
print ""
print "############################################"
print "## FAST WEBSERVER Installer By Zero         "
print "############################################"
print "##  ABOUT THE AUTHOR                      ##"
print "##  ___________________________           ##"
print "##  Name       : Jay                      ##"
print "##  Job        : Web Graphic Designer     ##"
print "##  Job        : IT Management            ##"
print "##  Job        : Linux & Mac Maintenance  ##"
print "##  mail       : zerolinuxx@gmail.com     ##"
print "##  facebook   : Itachi Sama              ##"
print "##  website    : coming soon              ##"
print "##                                        ##"
print "############################################"
print ""
print ""


## Install ############
#######################

os.system("sudo apt-get install apache2")
os.system("sudo apt-get install php5 libapache2-mod-php5 php5-cli php5-cgi php5-mysql ")
os.system("sudo apt-get install mysql-client mysql-common mysql-server phpmyadmin")
os.system("sudo /etc/init.d/apache2 start")

## create a log file ##
#######################

os.system("echo ...:: Zero Webserver installed successfully ::... > fastwww-report.log")
