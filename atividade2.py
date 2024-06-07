class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def __str__(self):
        return f"{self.modelo} | {self.cor} | {self.ano}"

carro_opala = Carro("Opala", "preto", "1996")

print((carro_opala))
print("")

class Restaurante:
    def __init__(self, nome, categoria, horario_atendimento, delivery, ativo):
        self.nome = nome
        self.categoria = categoria 
        self.horario_atendimento = horario_atendimento
        self.delivery = delivery
        self.ativo = False

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.horario_atendimento} | {self.delivery} | {self.ativo}"
    
restaurante_brasa = Restaurante("Brasa Livre", "Churrasco", "noite", "sem delivery", "")

print((restaurante_brasa))
print("")

class Pessoa:
    def __init__(self, nome, sobrenome, idade, profissao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"{self.nome} | {self.sobrenome} | {self.idade} | {self.profissao}"

pessoa_gilberto = Pessoa("Gilberto", "Mendes", "48", "pedreiro")
pessoa_claudia = Pessoa("Cláudia", "Soares", "31", "dentista")
pessoa_roberto = Pessoa("Roberto", "Matos", "17", "atendente")

print((pessoa_gilberto))
print((pessoa_claudia))
print((pessoa_roberto))
