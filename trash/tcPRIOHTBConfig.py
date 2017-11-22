#!/usr/bin/python
 
# We construct the following queue system
#
#                               1:
#               _________________|
#              /      
#             /      
#           1:1              
#     _______|_______  
#    |   |   |   |   |   
# 111:112:113:114:115:
#
# root 1: htb
# GW classes: 1:1  
# classes
 
# Amount of available priorities
AMOUNT_PRIOS = 2 
 
# gateways
GW = {"GW1" : "1:1" 
    }
 
# bandwidth of gateways (maximum)
GW_bandwidth = {"GW1" : "1440kbit"}
        
# gateways IP
GW_IPs = {"GW1" : "132.187.12.97" }
 
MIN_BW = "51kbit"
BURST = "5kB"
DEFAULT_PRIO = 2
        
GW_PRIORITY = {"GW1_PRIORITY_1" : "flowid 1:11",
        "GW1_PRIORITY_2" : "flowid 1:12"
        }
 
PFIFO_LIMIT = [1000,1000]; 
