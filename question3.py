def balance(string): 
	list = [] 
	for char in string: 
		if char in ["(", "{", "["]: 
			list.append(char) 
		else: 
			if not list: 
				return False
			poped = list.pop() 
			if poped == '(': 
				if char != ")": 
					return False
			if poped == '{': 
				if char != "}": 
					return False
			if poped == '[': 
				if char != "]": 
					return False

	if list: 
		return False
	return True

string = input("Enter the string with brakets: ")
print(balance(string))