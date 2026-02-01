#!/usr/bin/env python3

# Author ID: mgrytsyuk - 165549213

import os
import sys
import subprocess

def free_space():
	proc = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'",stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output = proc.communicate()
	stdout = output[0].decode('utf-8').strip('\n')
	return stdout
	
print(free_space())
