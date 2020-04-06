class Pessoa:
    def __init__(self,  *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Hello {id(self)}'

if __name__== '__main__':
    # p = Pessoa('Bábara')
    barba = Pessoa(nome='Barba')
    barbara = Pessoa(barba, nome='Bábara')
    print(Pessoa.cumprimentar(barbara))
    print(id(barbara))
    print(barbara.cumprimentar())
    print(barbara.nome)
    # p.nome = 'Ben'
    # print(p.nome)
    print(barbara.idade)
    for filho in barbara.filhos:
        print(filho.nome)


