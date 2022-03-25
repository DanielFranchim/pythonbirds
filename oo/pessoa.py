class Pessoa:
    olhos = 2

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
    daniel.sobrenome = 'Franchim'
    del daniel.filhos
    daniel.olhos = 1
    del daniel.olhos
    print(daniel.__dict__)
    print(ignnis.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(daniel.olhos)
    print(ignnis.olhos)
    print(id(Pessoa.olhos)), print(id(daniel.olhos)), print(id(ignnis.olhos)),
