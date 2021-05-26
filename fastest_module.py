""" fastest_module.py
This module calculates and print the fastest carrier of the tabular data contained in a CSV file 
"""

from utils_module import *

def get_fastest_carrier(carriers, city):
	minimum_cost = -1
	minimum = []
	
	for line in carriers:
		current_cost = float(line[get_index("time")].strip('h'))
		
		if minimum_cost == -1 and line[get_index('city')].lower() == city:
			minimum_cost = current_cost
			minimum.append(line)
		else:
			if current_cost < minimum_cost and line[get_index('city')].lower() == city:
				minimum_cost = current_cost
				minimum = []
				minimum.append(line)
				
			elif current_cost == minimum_cost and line[get_index('city')].lower() == city:
				minimum.append(line)
				
	return minimum
	
def print_fastest_carrier(fastest, weight):
	index = calculate_weight_index(weight)
	
	if len(fastest) > 1:
		print('\nOpções mais rápidas')
	else:
		print('\nOpção mais rápida')
	
	for line in fastest:
		print(f'Nome:{line[get_index("name")]}, cidade de destino: {line[get_index("city")]}, peso da carga: {weight} kg, tempo de entrega: {line[get_index("time")]}, custo total do frete: R$ { convert_currency_to_float(line[get_index(index)]) * weight}')

def calculate_fastest_carrier(table, weight, city):
	fastest = get_fastest_carrier(table, city)
	
	if fastest != []:
		print_fastest_carrier(fastest, weight)
	
	return fastest
