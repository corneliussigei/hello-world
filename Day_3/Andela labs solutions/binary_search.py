class BinarySearch(list):

	def __init__(self, a , b):
		for i in range(1, a+1):
			list.append(self, (i*b))
		self.length = a

	def search(self,numToSearch):
	    firstIndexValue = 0
	    lastIndex = self.length-1
	    found = False
	    count = 0
	    in_list = False
	    try:
	      index = self.index(numToSearch)
	      in_list = True
	    except ValueError:
	      index = -1
	      in_list = False

	    while firstIndexValue <= lastIndex and not found and in_list and numToSearch != self[lastIndex]:
	        middleIndex = (firstIndexValue+lastIndex)//2
	        mid_value = self[middleIndex]
	        if mid_value == numToSearch:
	            found = True
	            count +=1
	            index = middleIndex
	        else:
	            if numToSearch < mid_value:
	                lastIndex = middleIndex - 1
	                count +=1
	            else:
	                firstIndexValue = middleIndex + 1
	                count +=1
	    return {"count": count, "index": index}