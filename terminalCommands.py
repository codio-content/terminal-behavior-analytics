import yaml

# change file name
file = open('facebook.yaml', 'r')

modules = yaml.load( file )

# module name to access
mod = 'module2'

# exercise name to access 
ex = 2

print(modules)