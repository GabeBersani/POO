class Eletronico:
    def __init__(self, preco, cor, tamanho, eletronico_entreterimento=True, eletronico_estudo=False ):
        self.preco = preco
        self.cor = cor
        self.tamanho = tamanho
        self.eletronico_entreterimento = eletronico_entreterimento
        self.eletronico_estudo = eletronico_estudo


    def apresentar(self):
        print(f'Preço: {self.preco}')
        print(f'Cor: {self.cor}')
        print(f'Tamanho: {self.tamanho}')
        print(f'Entreterimento: {self.eletronico_entreterimento}')
        print(f'Estudo: {self.eletronico_estudo}')


    def entretar(self):
        if self.eletronico_entreterimento and self.eletronico_estudo:
            print(f'É um eletronico de multitarefas')
        elif self.eletronico_entreterimento:
            print(f'É um eletronico de entreterimento')
        else:
            print(f'Não é um eletronico de entreterimento')


    def estudar(self):
        if self.eletronico_estudo:
            print(f'Não é um eletronico de estudo')

        else:
            print(f'É um eletronico de estudo')
            self.eletronico_estudo = True



e1= Eletronico("R$400,00", "rosa", "pequeno")
e1.apresentar()
e1.estudar()
e1.estudar()
print("-" * 30)


class Celular(Eletronico):
    def __init__(self, preco, cor, tamanho):
        super().__init__( preco, cor, tamanho)
        self.bateria = False
        self.memoria = True


    def apresentar(self):
        print(f'O preço do Celular é: {self.preco}')
        print(f'A cor do Celular é: {self.cor}')

        if  self.bateria:
            print(f'O Celular esta com bateria')
        else:
            print(f'O Celular esta sem bateria')

        if  self.memoria:
            print(f'O Celular esta com memoria')
        else:
            print(f'O Celular esta sem memoria')


    def carregar(self):
        if self.bateria and self.memoria:
            print(f'O Celular esta com bateria e memoria')

        elif self.bateria:
            print("O Celular esta sem bateria")
        else:
            print(f'O Celular esta com bateria')
            self.bateria = True

    def mamoria(self):
        if self.memoria:
            print("O Celular esta sem memoria")
            self.memoria = False
        else:
            print(f'O Celular esta com memoria')
            self.memoria = True



c1 = Celular("R$400,00", "rosa", "medio")
c1.apresentar()
c1.carregar()
c1.carregar()


