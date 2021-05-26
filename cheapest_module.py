""" cheapest_module.py
This module calculates and print the cheapest carrier of the tabular data contained in a CSV file 
"""

from utils_module import *

def get_cheapest_carrier(carriers, weight, city):
	index = calculate_weight_index(weight)
	
	minimum_cost = -1
	minimum = -1
	
	for line in carriers:
		current_cost = convert_currency_to_float(line[get_index(index)])
		
		if minimum_cost == -1 and line[get_index('city')].lower() == city:
			minimum_cost = current_cost
			minimum = line
		else:
			if current_cost < minimum_cost and line[get_index('city')].lower() == city:
				minimum_cost = current_cost
				minimum = line
	
	return minimum
	
def print_cheapest_carrier(cheapest, weight):
	index = calculate_weight_index(weight)
		
	print('Opção mais barata')
	print(f'Nome:{cheapest[get_index("name")]}, cidade de destino: {cheapest[get_index("city")]}, peso da carga: {weight} kg, tempo de entrega: {cheapest[get_index("time")]}, custo total do frete: R$ { convert_currency_to_float(cheapest[get_index(index)]) * weight}') 
	
def calculate_cheapest_carrier(table, weight, city):
	cheapest = get_cheapest_carrier(table, weight, city)
	
	if cheapest != -1:
		print_cheapest_carrier(cheapest, weight)

	return cheapest
