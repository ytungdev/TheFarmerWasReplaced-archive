def get(dict, key, default):
	if key in dict:
		return dict[key]
	return default

def sort(arr, rev=False):
	def merge(L,R, rev):
		neg = 1
		if rev:
			neg = -1
		i,j = 0,0
		temp = []
		while i < len(L) and j < len(R):
			if L[i]*neg < R[j]*neg:
				temp.append(L[i])
				i += 1
			else:
				temp.append(R[j])
				j+=1
		temp += L[i:]
		temp += R[j:]
		return temp
	length = len(arr)
	if length <= 1:
		return arr
	mid = len(arr)//2
	L = sort(arr[0:mid], rev)
	R = sort(arr[mid:], rev)
	return merge(L,R, rev)
