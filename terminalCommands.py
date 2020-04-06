# input arguments:
# 1: filename.yaml
# 2: module#
# 3: exercise#

import yaml, sys, os

#loading assets for the specified question
file = open(sys.argv[1], 'r')
modules = yaml.load( file )
mod = sys.argv[2]
ex = sys.argv[3]
commands = modules.get(mod).get(ex).get('commands')
repeated = modules.get(mod).get(ex).get('repeated')

#loading in student bash history and comparing
bash_history = open(os.path.expanduser('~/.bash_history') ,'r')
commandCount = 0
repeatedCount = 0
duplicateCount = 0 #lines that were unexpectedly duplicated

for line in commands:
    if line in bash_history:
        if bash_history.count(line) > 1:
            commandCount+=1
            if line in repeated:
                repeatedCount+= (bash_history.count(line) - 1)
            else:
                duplicateCount+= (bash_history.count(line) - 1)
        else:
            commandCount+=1
            
#print out results
print("For " + mod + " " + ex +": ")
print("-----------------------------------------")
print("Percent of commands run: " + str(commandCount / len(commands) * 100.0) )
print("Number of repeated commands: " + str(repeatedCount) )
print("Number of unexpectedly duplicated commands: " + str(duplicateCount) )