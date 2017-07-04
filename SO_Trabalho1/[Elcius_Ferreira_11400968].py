"""
Aluno: Elcius Ferreira Barbosa Junior
Matrícula: 11400968
Professor: Fernando Menezes
Disciplina: Sistemas Operacionais
Engenharia de Computação - CI - UFPB
"""

""" Função que lê o arquivo de entrada."""
def lerArquivo():
	fila_processos = []

	with open("entradas.txt") as arquivo:
		arq_linhas = arquivo.readlines()		

	for i in range(len(arq_linhas)):

		fila_processos.append([]) 						
		if(i != len(arq_linhas)-1):							
			linha = arq_linhas[i][:-1]	
		else:
			linha = arq_linhas[i]		
		espaco_indx = linha.index(" ")

		tc = int(linha[:espaco_indx])
		td = int(linha[espaco_indx+1:])

		fila_processos[i].append(tc)	
		fila_processos[i].append(td)


	return fila_processos

""" Função que utiliza o algoritmo FCFS para selecionar o processo que utiliza a CPU."""
def fcfs(processos):
	fcfs_temp_completo = []
	fcfs_temp_retorno=[]
	fcfs_temp_espera=[]
	fcfs_temp_espera.append(0)

	aux = 0
	tempo_total = processos[0][0]
	for i in range(1,len(processos)):
		tempo_total += processos[i-1][1]
		aux = tempo_total - processos[i][0]
		fcfs_temp_espera.append(aux)


	tempo_total = 0
	for j in range(len(fcfs_temp_espera)):
		tempo_total += fcfs_temp_espera[j]

	fcfs_temp_espera_medio = float(tempo_total / (len(processos)))

	tempo_total = 0
	tempo_total += (processos[0][0] + processos[0][1])
	fcfs_temp_retorno.append(processos[0][1])

	aux = 0
	for k in range(1,len(processos)):
		tempo_total += processos[k][1]
		fcfs_temp_retorno.append(tempo_total - processos[k][0])

	tempo_total = 0
	for q in range(len(fcfs_temp_retorno)):
		tempo_total += fcfs_temp_retorno[q]

	fcfs_temp_retorno_medio = float(tempo_total / (len(processos)))

	print("FCFS %.1f %.1f %.1f" %(fcfs_temp_retorno_medio, fcfs_temp_espera_medio, fcfs_temp_espera_medio))

""" Função que utiliza o algoritmo SJF para selecionar o processo que utiliza a CPU."""
def sjf(lista_processos):
	sjf_temp_completo = []
	sjf_temp_retorno=[]
	sjf_temp_espera=[]
	sjf_temp_espera.append(0)
	fila_prontos = []
	aux = []

	processos = lista_processos
	processos_copia = processos
	processos_copia.sort(key = lambda processos_copia:processos_copia[0])

	primeiro_pros = processos_copia[0]

	index_primeiro_proc = primeiro_pros[0]

	aux.append(processos_copia[0])
	for i in range(1,len(processos_copia)):
		if(processos_copia[i][0] == index_primeiro_proc):
			aux.append(processos_copia[i])

	aux.sort(key = lambda aux:aux[1])

	fila_prontos.append(aux[0])

	processos.remove(aux[0])
	tempo_exec_total = fila_prontos[0][1]

	aux2 = []
	aux2 = fila_prontos[0]

	fila_provisoria = []
	
	k = 0
	control = False
	tam = len(processos)
	while (len(processos) >= 0):

		while (tam>=0) and (processos[k][0] <= tempo_exec_total):
			control = True

			fila_provisoria.append(processos[k])

			k += 1
			tam -= 1

			if tam == 0:
				break

		if control == True:
			fila_provisoria.sort(key = lambda fila_provisoria:fila_provisoria[1])

			if tam == 0:
				for numb in range(len(fila_provisoria)):
					fila_prontos.append(fila_provisoria[numb])
			else:
				fila_prontos.append(fila_provisoria[0])

			tempo_exec_total += fila_provisoria[0][0]
			processos.remove(fila_provisoria[0])

			fila_provisoria = []
			k = 0
			control = False
			if tam == 0:
				break
			
		else:
			tempo_exec_total += processos[k][0]
			k = 0

	aux = 0
	tempo_total = fila_prontos[0][0]

	for i in range(1,len(fila_prontos)):
		tempo_total += fila_prontos[i-1][1]
		aux = tempo_total - fila_prontos[i][0]
		sjf_temp_espera.append(aux)


	tempo_total = 0
	for j in range(len(sjf_temp_espera)):
		tempo_total += sjf_temp_espera[j]

	sjf_temp_espera_medio = float(tempo_total / (len(fila_prontos)))

	tempo_total = 0
	tempo_total += (fila_prontos[0][0] + fila_prontos[0][1])
	sjf_temp_retorno.append(fila_prontos[0][1])

	aux = 0
	for k in range(1,len(fila_prontos)):
		tempo_total += fila_prontos[k][1]
		sjf_temp_retorno.append(tempo_total - fila_prontos[k][0])

	tempo_total = 0
	for q in range(len(sjf_temp_retorno)):
		tempo_total += sjf_temp_retorno[q]

	sjf_temp_retorno_medio = float(tempo_total / (len(fila_prontos)))

	print("SJF %.1f %.1f %.1f" %(sjf_temp_retorno_medio, sjf_temp_espera_medio, sjf_temp_espera_medio))


""" Função que utiliza o algoritmo RR para selecionar o processo que utiliza a CPU."""
def rr(processos):
	qnt = len(processos)
	tempo_total = 0
	quantum = 2
	
	processos_copia = processos
	for processo in range(len(processos_copia)):
		dur = processos_copia[processo][1]
		processos_copia[processo].append(dur)

	qnt_processos = len(processos)
	fila_prontos = []
	fila_prontos.append(2)
	rr_temp_retorno = []
	rr_temp_espera = []
	rr_temp_resposta = []
	i = 0
	j = 0
	primeira = True
	anterior = []
	fim = False
	cpu_ociosa = True
	
	
	while qnt_processos > 0:
		if primeira == True:
			fila_prontos.remove(2)

		if j != len(processos_copia):
			novo_processo = False
			while processos_copia[j][0] <= tempo_total:
				novo_processo = True
				fila_prontos.append(processos_copia[j])
				j += 1

				if j == len(processos_copia):
					fim = True
					break

		if novo_processo == True or (processos_copia[i][0] <= tempo_total):
			if primeira == False and cpu_ociosa == False:
				if (processo_cpu[1] > 0):
					fila_prontos.append(processo_cpu)

			processo_cpu = fila_prontos[i]
			cpu_ociosa = False
			fila_prontos.remove(processo_cpu)

			if processo_cpu[1] == processo_cpu[2]:
				tmp_res = tempo_total - processo_cpu[0]
				rr_temp_resposta.append(tmp_res)

			processo_cpu[1] -= 2
			controle = True

			if processo_cpu[1] <= 0:
				qnt_processos -= 1

				if processo_cpu[1] < 0:
					tempo_total += 1
					tmp_ret = tempo_total - processo_cpu[0]
					tmp_espera = tmp_ret - processo_cpu[2]

					rr_temp_retorno.append(tmp_ret)
					rr_temp_espera.append(tmp_espera)

				else:
					tempo_total += 2
					tmp_ret = tempo_total - processo_cpu[0]
					tmp_espera = tmp_ret - processo_cpu[2]

					rr_temp_retorno.append(tmp_ret)
					rr_temp_espera.append(tmp_espera)



			else:
				tempo_total += 2

		else:
			tempo_total += (processos_copia[j][0] - tempo_total)

		primeira = False


	tmp = 0
	for tempo in range(len(rr_temp_retorno)):
		tmp += rr_temp_retorno[tempo]

	rr_temp_retorno_medio = float(tmp / (len(processos)))

	tmp = 0
	for tempo in range(len(rr_temp_retorno)):
		tmp += rr_temp_espera[tempo]

	rr_temp_espera_medio = float(tmp / (len(processos)))
	
	tmp = 0
	for tempo in range(len(rr_temp_resposta)):
		tmp += rr_temp_resposta[tempo]

	rr_temp_resposta_medio = float(tmp / (len(processos)))

	print("RR %.1f %.1f %.1f" %(rr_temp_retorno_medio, rr_temp_resposta_medio, rr_temp_espera_medio))



fila_processos = lerArquivo()
fcfs(fila_processos)
fila_processos = lerArquivo()
sjf(fila_processos)
fila_processos = lerArquivo()
rr(fila_processos)


