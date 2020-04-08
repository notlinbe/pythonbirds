class Pessoa:
    olhos = 2

    def __init__(self,  *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Hello {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    barbara.sobrenome = 'Ramalho'
    del barbara.filhos
    # barbara.sobrenome
    # print(barbara.sobrenome)
    barbara.olhos = 1
    del barbara.olhos
    print(barbara.__dict__)
    print(barba.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(barbara.olhos)
    print(barba.olhos)
    print(id(Pessoa.olhos), id(barbara.olhos), id(barba.olhos))
    print(Pessoa.metodo_estatico(), barbara.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), barbara.nome_e_atributos_de_classe())







