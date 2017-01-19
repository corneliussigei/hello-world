def find_missing(a, b):
	#find the symm. diff (items that are in one or the other but not both)
	the_list = list(set(a) ^ set(b))
	return the_list[0] if the_list != [] else 0