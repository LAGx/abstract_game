

def plusLists(list1, list2):

	for i in range(0, len(list1)):
		list1[i] += list2[i]

	return list1

def constPlusList(list1, const):

	for i in range(0, len(list1)):
		list1[i] += const

	return list1