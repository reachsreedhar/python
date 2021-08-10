#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'searchSuggestions' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY repository
#  2. STRING customerQuery
#

def searchSuggestions(repository, customerQuery):
    # Write your code here
    result = []
    if len(customerQuery) < 2:
      return []
    
    for i in range(len(repository)):
      matches = 1
      repo = repository[i]
      for j in range(len(customerQuery)):
        if customerQuery[j] != repo[j]:
          matches = 0
          break
      if matches == 1:
        result.append(repo)
      if len(result) == 3:
        break
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    repository_count = int(input().strip())

    repository = []

    for _ in range(repository_count):
        repository_item = input()
        repository.append(repository_item)

    customerQuery = input()

    result = searchSuggestions(repository, customerQuery)

    print('\n'.join([' '.join(x) for x in result]))
    fptr.write('\n'.join([' '.join(x) for x in result]))
    fptr.write('\n')

    fptr.close()

