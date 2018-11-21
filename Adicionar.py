class Adicionar():
    def perguntamarca():
        global marca
        marca = input("\nDigite a marca do veículo:\n")
        return marca

    def perguntamodelo():
        global modelo
        modelo = input("Digite o modelo do veículo:\n")
        return modelo

    def perguntastatus(self,status):
        self.status = status
        #print ("Adicione o status do veículo:\n")
        #print ("1 p/ alugado:")
        #print ("2 p/ reservado:")
        #print ("3 p/ disponível:")
        #print ("4 p/ em atraso:")
        #status = int(input())
        if self.status == 1:
            self.status = "Alugado"
            
        elif self.status == 2:
            self.status = "Reservado"

        elif self.status == 3:
            self.status = "Disponível"

        elif self.status == 4:
            self.status = "Em atraso"

        return self.status

    def perguntaano():
        global ano
        ano = int(input("Digite o ano do veículo:\n"))
        return ano

    def perguntavalordiaria():
        global valordiaria
        valordiaria = float(input("Digite o valor da diária:\n"))
        return valordiaria
