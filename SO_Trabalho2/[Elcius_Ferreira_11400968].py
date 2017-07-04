"""
Aluno: Elcius Ferreira Barbosa Junior
Matrícula: 11400968
Professor: Fernando Menezes
Disciplina: Sistemas Operacionais
Engenharia de Computação - CI - UFPB
"""

referencias = []

""" Função que lê o arquivo de entrada."""
def lerArquivo():
	global qnt_quadros

	with open("entrada.txt") as arquivo:
		arq_linhas = arquivo.readlines()

	qnt_quadros = int(arq_linhas[0])
	aux = 0
	for linhas in arq_linhas:
		if aux != 0:
			referencias.append(int(linhas[0]))
		aux += 1

""" Função que procura um determinado número em um array/lista."""
def procurar(numb,quadros):
	for i in (range(len(quadros))):
		if numb == quadros[i]:
			return True

	return False

""" Função que procura o maior elemento em um array/lista."""
def maiorValor(lista):
	valor = 0
	idx_max_valor = 0
	for i in range(len(lista)):
		if valor < lista[i]:
			idx_max_valor = i
			valor = lista[i]

	return idx_max_valor

""" Função que procura o menor elemento em um array/lista."""
def menorValor(lista):
	valor = lista[0]
	idx_min_valor = 0
	for i in range(1,len(lista)):
		if valor > lista[i]:
			idx_min_valor = i
			valor = lista[i]

	return idx_min_valor

""" Função que procura a página que não será acessada pelo maior período de tempo."""
def pagMaiorPeriodo(quadros, referencias_restantes):
	tempos = []
	found = []
	max_indx = None

	for i in range(len(quadros)):
		found.append(None)

	for k in range(len(quadros)):
		for q in range(len(referencias_restantes)):
			if quadros[k] == referencias_restantes[q]:
				tempos.append(q)
				found[k] = True
				break
			else:
				found[k] = False

		if found[k] == False:
			max_indx = k

	if max_indx == None:
		max_indx = maiorValor(tempos)

	return max_indx			


def pagMenosRecente(quadros, referencias_anteriores):
	distancias = []
	for k in range(len(quadros)):
		for q in range(len(referencias_anteriores)):
			if quadros[k] == referencias_anteriores[q]:
				dist = q
		distancias.append(dist)

	idx_min_dist = menorValor(distancias)

	return idx_min_dist			


def FIFO():
	quadros = []
	index = 0
	faltas = 0

	for i in range(qnt_quadros):
		quadros.append(0)

	for j in range(len(referencias)):
		if j < qnt_quadros:
			quadros[index] = referencias[j]
			faltas += 1
			index = (index + 1) % qnt_quadros
		else:
			found = procurar(referencias[j],quadros)
			if found == False:
				quadros[index] = referencias[j]
				faltas += 1
				index = (index + 1) % qnt_quadros

	print("FIFO %i" %faltas)


def OTM():
	quadros = []
	index = 0
	faltas = 0

	for i in range(qnt_quadros):
		quadros.append(0)

	for j in range(len(referencias)):
		if j < qnt_quadros:
			quadros[index] = referencias[j]
			faltas += 1
			index = (index + 1) % qnt_quadros
		else:
			found = procurar(referencias[j],quadros)
			if found == False:
				referencias_restantes = referencias[j+1:len(referencias)]
				max_index = pagMaiorPeriodo(quadros, referencias_restantes)
				quadros[max_index] = referencias[j]
				faltas += 1

	print("OTM %i" %faltas)


def LRU():
	quadros = []
	index = 0
	faltas = 0
	fila = []

	for i in range(qnt_quadros):
		quadros.append(0)

	for j in range(len(referencias)):
		if j < qnt_quadros:
			quadros[index] = referencias[j]
			faltas += 1
			index = (index + 1) % qnt_quadros
		else:
			found = procurar(referencias[j],quadros)
			if found == False:
				referencias_anteriores = referencias[0:j]
				min_index = pagMenosRecente(quadros, referencias_anteriores)
				quadros[min_index] = referencias[j]
				faltas += 1

	print("LRU %i" %faltas)
		


lerArquivo()
FIFO()
OTM()
LRU()
