#!/usr/bin/python

# We construct the following queue system
#
#                                       1:
#               _________________|_________________
#              /                         |                          \
#             /                          |                            \
#           1:1                      1:2                         1:3
#            |                           |                             |
#    100 ... 199           200 ... 299             300 ... 399
#
# root 1: htb
# GW classes: 1:1, 1:2, 1:3 
# GW1 sub_classes: 1:100 ... 1:199
# GW2 sub_classes: 1:200 ... 1:299
# GW3 sub_classes: 1:300 ... 1:399


# gateways
GW = {"GW1" : "1:1", 
    }

# gateways IP
GW_IPs = {"GW1" : "132.187.12.97" }
        
# defines the number of application prio classes, currently must be < 300
App_QueueSize = 99 
# defines the number of maximum youtube classes
YouTube_QueueSize = 3


# bandwidth of gateways
#GW_bandwidth = {"GW1" : "1960kbit",  "GW2" : "1960kbit",  "GW3" : "1960kbit" }
GW_bandwidth = {"GW1" : "5000kbit"}

# for all gateways map priority to flowid
GW_PRIORITY = {"GW1_PRIORITY_1" : "flowid 11:1",
        "GW1_PRIORITY_2" : "flowid 11:2",
        "GW1_PRIORITY_3" : "flowid 11:3",
        "GW1_PRIORITY_4" : "flowid 11:4",
        "GW1_PRIORITY_5" : "flowid 11:5"
        }

minBW = "51kbit"
burst = "2kB"
