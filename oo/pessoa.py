class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    ignnis = Pessoa(nome='Ignnis')
    daniel = Pessoa(ignnis, nome='Daniel')
    print(Pessoa.cumprimentar(daniel))
    print(id(daniel))
    print(daniel.cumprimentar())
    print(daniel.nome)
    print(daniel.idade)
    for filho in daniel.filhos:
        print(filho.nome)

