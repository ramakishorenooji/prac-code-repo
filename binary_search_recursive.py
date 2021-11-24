def bsearch(list, start, end, val):
   if (end < start):
      return None
   else:
      midval = start + ((end - start) // 2)
# Compare the search item with middle most value
   if list[midval] > val:
      return bsearch(list, start, midval-1,val)
   elif list[midval] < val:
      return bsearch(list, midval+1, end, val)
   else:
      return midval

list = [8,11,24,56,88,131]
print(bsearch(list, 0, 5, 24))
#print(bsearch(list, 0, 5, 51))