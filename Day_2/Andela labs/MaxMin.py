def find_max_min(listOfNums):
	listOfNums.sort()
	return [listOfNums[0], listOfNums[-1]] if (listOfNums[0] != listOfNums[-1]) else [listOfNums[0]]
