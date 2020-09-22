import sys

sys.path.append('../skeletoy')

# Modules
print( skeletoy.__plugins__ )

# Class
skeletoy.__demo__.Plugin().hello()

# Def
skeletoy.__demo__.hello()
