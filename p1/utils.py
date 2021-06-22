# This file is intended as a "utils" library for the specific purposes in IPM's p1
# Authors:
# Christian David Outeda García
# Miguel Blanco Godón

# Retuns a dictionary or list(depends of the code) with the parsed json answer in a dictionary
def get_json_from_url(url) :
	import urllib.request
	import json
	http_answer = urllib.request.urlopen(url)
	answer =  http_answer.read()
	# the answer is inputted to the json decoder
	# the answer is decoded in utf8, so that can be compatible with python < 3.7
	data = json.loads(answer.decode('utf8'))
	# returning the dictionary (the intresting part)
	return data["data"]

# ATTENTION. VALID ONLY IF THE PARSER RETURNS A DICTIONARY
# Returns the list of keys of the dictionary
def get_key_list(dictionary) :
	return list(dictionary.keys())

# Returns the list of values of the dictionary
def get_value_list(dictionary) :
	return list(dictionary.values())

# Returns the value of the key in the dictionary
def get_value(dictionary, key) :
	return dictionary[key]

# Returns a list of tuples(key, value) from the dictionary
def get_dict_list(dictionary) :
	keys = get_key_list(dictionary)
	values = get_value_list(dictionary)
	dict_list = []
	for i in range(len(keys)) :
		dict_list.append((keys[i], values[i]))
	return dict_list


# ATTENTION. IF THE PARSER RETURNS A LIST(/songs/x/y case) only access the list normally
