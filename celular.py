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


    def verificar_entreterimento(self):
        if self.eletronico_entreterimento:
            print(f'É um eletronico de entreterimento')
        else:
            print(f'Não é um eletronico de entreterimento')


    def verificar_estudo(self):
        if self.eletronico_estudo:
            print(f'É um eletronico de estudo')
        else:
            print(f'Não é um eletronico de estudo')

    def estudar(self, status):
        if self.eletronico_estudo and status:
            print("Ele já é um eletronico de estudo")
        elif not self.eletronico_estudo and not status:
            print("Não é um eletronico de estudo")
            self.eletronico_estudo()
        elif not self.eletronico_estudo and status:
            self.eletronico_estudo = status
            print("Agora é um eletronico de estudo")
        else:
            self.eletronico_estudo = status
            self.eletronico_estudo()



    def entreter(self, status):
        if self.eletronico_entreterimento and status:
            print("É um eletronico de entreterimento")
        elif not self.eletronico_entreterimento and not status:
            print("Não é um eletronico de entreterimento")
            self.eletronico_entreterimento()
        elif not self.eletronico_entreterimento and status:
            self.eletronico_entreterimento = status
            print("É um eletronico de entreterimento")
        else:
            self.eletronico_entreterimento = status
            self.eletronico_entreterimento()



e1= Eletronico("R$400,00", "rosa", "pequeno")
e1.apresentar()
e1.estudar(True)
e1.estudar(True)
e1.entreter(True)
e1.entreter(True)

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



    def carregar(self, status):
        if self.bateria and status:
            print("O celular já esta com bateria")
        elif not self.bateria and not status:
            print("O celular esta sem bateria")
            self.bateria()
        elif not self.bateria and status:
            self.bateria = status
            print("Agora o celular esta com bateria")
        else:
            self.bateria = status
            self.bateria()





    def armazenamento(self, status):
        if self.memoria and status:
            print("O celular esta com memoria")
        elif not self.memoria and not status:
            print("O celular esta sem memoria")
            self.memoria()
        elif not self.memoria and status:
            self.memoria = status
            print("Agora o celular esta com memoria")
        else:
            self.memoria = status
            self.memoria()



c1 = Celular("R$400,00", "rosa", "medio")
c1.apresentar()
c1.carregar(True)
c1.carregar(True)
c1.armazenamento(True)


