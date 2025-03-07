class Eletronico:
    def __init__(self, preco, cor, tamanho, eletronico_entreterimento=True, eletronico_estudo=False ):

        self.__preco = preco
        self.__cor = cor
        self.__tamanho = tamanho
        self._eletronico_entreterimento = eletronico_entreterimento
        self._eletronico_estudo = eletronico_estudo

    def get_preco(self):
        return self.__preco

    def get_cor(self):
        return self.__cor

    def get_tamanho(self):
        return self.__tamanho

    def get_eletronico_entreterimento(self):
        return self._eletronico_entreterimento

    def get_eletronico_estudo(self):
        return self._eletronico_estudo


    def apresentar(self):
        print(f'O preço do eletronico definido é {self.get_preco()}, sua cor é {self.get_cor()} e seu tamanho é '
              f'{self.get_tamanho()}')
        print(f'Entreterimento: {self.get_eletronico_entreterimento()}')
        print(f'Estudo: {self.get_eletronico_estudo()}')

    def verificar_entreterimento(self):
        if self._eletronico_entreterimento:
            print(f'É um eletronico de entreterimento')
        else:
            print(f'Não é um eletronico de entreterimento')

    def verificar_estudo(self):
        if self._eletronico_estudo:
            print(f'É um eletronico de estudo')
        else:
            print(f'Não é um eletronico de estudo')


    def set_estudar(self, status):
        if self._eletronico_estudo and status:
            print("Ele já é um eletronico de estudo")
        elif not self._eletronico_estudo and not status:
            print("Não é um eletronico de estudo")
            self._eletronico_estudo()
        elif not self._eletronico_estudo and status:
            self._eletronico_estudo = status
            print("Agora é um eletronico de estudo")
        else:
            self._eletronico_estudo = status
            self._eletronico_estudo()

    def set_entreter(self, status):
        if self._eletronico_entreterimento and status:
            print("É um eletronico de entreterimento")
        elif not self._eletronico_entreterimento and not status:
            print("Não é um eletronico de entreterimento")
            self._eletronico_entreterimento()
        elif not self._eletronico_entreterimento and status:
            self._eletronico_entreterimento = status
            print("É um eletronico de entreterimento")
        else:
            self._eletronico_entreterimento = status
            self._eletronico_entreterimento()

    def set_preco(self, valor):
        if valor >= 0:
            self.__preco = valor
        else:
            print("salario deve ser positivo")

    def set_cor(self, cor):
        if cor == "":
            print("Deve digitar uma cor")
        else:
            self.__cor = cor

    def set_tamanho(self, valor):
        if valor >= 0:
            self.__tamanho = valor



e1= Eletronico("R$100,00", "rosa", "pequeno")
e1.apresentar()
e1.set_estudar(True)
e1.set_estudar(True)
e1.set_entreter(True)

print("-" * 40)


class Celular(Eletronico):
    def __init__(self, preco, cor, tamanho):
        super().__init__( preco, cor, tamanho)
        self.bateria = False
        self.memoria = True


    def apresentar(self):
        print(f'O preço do Celular é: {self.get_preco()}')
        print(f'A cor do Celular é: {self.get_cor()}')

        if  self.bateria:
            print(f'O Celular esta com bateria')
        else:
            print(f'O Celular esta sem bateria')

        if  self.memoria:
            print(f'O Celular esta com memoria')
        else:
            print(f'O Celular esta sem memoria')



    def set_carregar(self, status):
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


    def set_armazenamento(self, status):
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
c1.set_carregar(True)
c1.set_carregar(True)
c1.set_armazenamento(True)


