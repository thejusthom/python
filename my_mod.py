print('Import module created by me')

def find_index(str,tar) :
	for i,val in enumerate(str):
		if val == tar:
			return i

	return -1 	