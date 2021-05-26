import sys

from cheapest_module import calculate_cheapest_carrier
from fastest_module import calculate_fastest_carrier

def open_read(file_name):
	try:
		return open(file_name).read().split('\n')[1:] #Retirando a linha de cabeçalho
	except FileNotFoundError:
		print("O arquivo que você tentou acessar não existe.")

def create_table(carriers):
	table = []
	
	for line in carriers:
		for field in line:
			table.append(field.split(','))
	
	return table[:len(table)-1] #Retirando a última linha que é vazia
	
def main(args):
	if len(args) < 2:
		print('Consulte o PROJECT.md para saber como executar o programa')
	else:
		city = ''
		
		if args[0].endswith('.csv'):
			file = args[0]
			
			try:
				weight = float(args[1])
			except:
				print("O peso digitado não foi um valor numérico")
			
			for name in args[2:]:
				city += name.lower()
		else:
			file = 'transportadoras.csv'
			
			try:
				weight = float(args[0])
			except:
				print("O peso digitado não foi um valor numérico")
			
			for name in args[1:]:
				city += name.lower()
				
				if len(args[1:]) > 1:
					city += ' '
					
			if len(args[1:]) > 1:
				city = city[:-1]
		
		carriers = list(map(open_read, [file]))
		
		table = create_table(carriers)
		
		cheapest = calculate_cheapest_carrier(table, weight, city)	
		fastest = calculate_fastest_carrier(table, weight, city)
		
		if fastest == [] or cheapest == -1:
			print("A cidade digitada não foi encontrada. Confira se digitou o nome da cidade corretamente")
	
if __name__ == "__main__":
   main(sys.argv[1:]) #Retirando o primeiro parâmetro que é o próprio nome do arquivo
