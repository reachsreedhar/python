#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys

print("=============================================")

print("Running main.py - module name: {0}".format(__name__))

import module1

module1.pprint_dict('main.globals', globals())

print(sys.path)

del globals()['module1']
module1.pprint_dict('main.globals', globals())
print(sys.modules['module1'])

#print("Importing module1 again")
#import module1
print("=============================================")
