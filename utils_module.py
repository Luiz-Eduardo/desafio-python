""" utils_module.py
This module contains utils stuff such as conversion functions, return-indexes function, etc
"""
	
def get_index(field):
	index = {
		"name": 0,
		"cost_leq_100": 1,
		"cost_ge_100": 2,
		"city": 3,
		"time": 4
	}
	
	return index[field]

def calculate_weight_index(weight):
	if weight <= 100:
			index = "cost_leq_100"
	else:
		index = "cost_ge_100"
	
	return index
	
def convert_currency_to_float(money):
	return float(money.strip('R$ '))
