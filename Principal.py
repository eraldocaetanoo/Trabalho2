from Adicionar import Adicionar
from AvancarData import avancarData
from datetime import datetime, timedelta

lista_codigo = []
lista_marca = []
lista_modelo = []
lista_status = ["Alugado", "Reservado", "Disponível", "Em atraso"]
lista_st = []
lista_ano = []
lista_valordiaria = []
data_loc = []
disponivel = "Disponível"

class principal:
        def __init__(self):
                data_atual = datetime.today()
                data_em_texto = data_atual.strftime('%d/%m/%Y')
                quantidade_cadastrados = len(lista_codigo)
                quantidade_alugados = len(lista_st)
                print ("\n*----- Data atual: ",data_em_texto," -----*\n")
                print ("Quantidade de veículos cadastrados  --> ",quantidade_cadastrados)
                print ("Quantidade de veículos alugados     --> ",quantidade_alugados)
                print ("\nEscolha uma opção:")
                print ("1 p/ Consultar veículos:")
                print ("2 p/ Adicionar veículos:")
                print ("3 p/ Alugar/reservar veículos:")
                print ("4 p/ Devolver/liberar veículos:")
                print ("5 p/ Excluir veículos:")
                print ("6 p/ Avançar data atual:")
                print ("0 p/ Sair:")

                try:
                        d = int(input())
                        if d == 1:
                                if not lista_codigo:
                                        print ("\nNenhum veículo cadastrado! Primeiro adicione um veículo!\n")
                                else:
                                        a = len(lista_codigo)-1
                                        i = 0
                                        while i <= a:
                                                print ("\nCódigo: ",lista_codigo[i])
                                                print ("Marca: ",lista_marca[i])
                                                print ("Modelo: ",lista_modelo[i])
                                                
                                                if not lista_st:
                                                        print ("Status: ",lista_status[2])
                                                
                                                        
                                                else:
                                                        i2 = 0
                                                        b = len(lista_st)
                                                        while i2 < b:
                                                                if lista_st[i2] == "Disponível":
                                                                        print ("Status: ",lista_status[2])
                                                                        
                                                                else:
                                                                        lista_st[i2] = lista_status[0]
                                                                        print ("Status: ",lista_status[i2])
                                                                        t = len(data_loc)-1
                                                                        dt = data_loc[t]
                                                                        print ("Prazo alugado: ",dt.strftime('%d/%m/%Y'))
                                                                i2 = i2 + 1
                                                print ("Ano: ",lista_ano[i])
                                                print ("Valor da diária: ",lista_valordiaria[i]," reais")
                                                #lista.append(a)
                                                i = i + 1
                                        
                                principal()
        
                        elif d == 2:
                                lista_codigo.append(len(lista_codigo)+1)
                                marcainformada = Adicionar.perguntamarca()
                                lista_marca.append(marcainformada)
                                modeloinformado = Adicionar.perguntamodelo()
                                lista_modelo.append(modeloinformado)
                                
                                #lista_st.append(lista_status[2])
                                                
                                anoinformado = Adicionar.perguntaano()
                                lista_ano.append(anoinformado)
                                valordiariainformado = Adicionar.perguntavalordiaria()
                                lista_valordiaria.append(valordiariainformado)
                            
                                principal()

                        elif d == 3:
                                if not lista_codigo:
                                        print ("\nNenhum veículo cadastrado! Primeiro adicione um veículo!\n")
                                else:
                                        nome_locatario = input("Nome do locatário:\n")
                                        prazo_locacao = int(input("Prazo de locação:\n"))
                                        if prazo_locacao > 0:
                                                codigov = int(input("Digite o código do veículo que deseja alugar:\n"))
                                                data_loc.append(avancarData.avancardt(self,prazo_locacao))
                                                if codigov in lista_codigo:
                                                        #status = 1
                                                        st = lista_status[0]
                                                        lista_st.append(st)
                                                        print ("\nVeículo ",st,"!")
                
                                                else:
                                                        print ("Código inválido!")
                                        else:
                                                print ("Prazo inválido!\n")
                                principal()

                        elif d == 5:
                                if not lista_codigo:
                                        print ("Nenhum veículo cadastrado! Primeiro adicione um veículo!\n")
                                else:
                                        codigoremover = int(input("\nDigite o código do veículo que deseja remover:\n"))
                                        if codigoremover in lista_codigo:
                                                ind = lista_codigo.index(codigoremover)
                                                del lista_codigo[ind]
                                                del lista_marca[ind]
                                                del lista_modelo[ind]
                                                del lista_status[ind]
                                                del lista_ano[ind]
                                                del lista_valordiaria[ind]
                                                
                                        else:
                                                print ("Código inválido!")
                                        principal()
                        elif d == 6:
                                print("\nA data foi avançada em 1 dia!")
                                data_av = avancarData.avancardt(self,1)
                                data_em_texto = data_av.strftime('%d/%m/%Y')
                                print(data_em_texto)
                        elif d == 0:
                                exit()
                        else:
                                print ("\nOpção inválida!\n")
                        principal()
                        
                except ValueError:
                        print ("\nOpção inválida!\n")
                        principal()
                
principal()
