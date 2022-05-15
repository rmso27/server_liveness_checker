################################
#
#   Title: Server Liveness Checker
#   Description: Script to check the liveness status of a server
#   Version: 1.0
#   Author: rmso27
#
################################

## GENERAL ##

# Import modules
import json
import os
import pandas as pd
import tabulate
from termcolor import colored

# Main vars
hosts_file = 'hosts.json'

## FUNCTIONS ##

# Read hosts
def read_hosts(hosts_file):
    temp_hosts_list = open(hosts_file, 'r')
    hosts_list = json.load(temp_hosts_list)
    
    return hosts_list
    
# Check liveness
def check_liveness(hosts_list):

    liveness_results = ()
    hosts_entries = []
    descriptions_entries = []
    statuses_entries = []

    for host in hosts_list:
        hosts_entries += [host['host']]
        descriptions_entries += [host['description']]
        ping_status = ping_host(host['host'])
        if ping_status == 0:
            statuses_entries += [colored('UP', 'green')]
        else:
            statuses_entries += [colored('DOWN', 'red')]
        
    liveness_results = {'host': hosts_entries, 'description': descriptions_entries, 'status': statuses_entries}
        
    return liveness_results
        
# Ping servers
def ping_host(host):

    response = os.system('ping -c 1 ' + host)
    
    return response  

# Generate DataFrame and print it
def generate_dataframe(liveness_results):

    data_frame = pd.DataFrame(liveness_results)
    print(tabulate.tabulate(data_frame, tablefmt = 'grid', headers = ['', 'Host', 'Description', 'Status']))


## SCRIPT EXECUTION ##

list_of_hosts = read_hosts(hosts_file)
check_results = check_liveness(list_of_hosts)
generate_dataframe(check_results) 