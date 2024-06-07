class Restaurante:
    nome = ""
    categoria = ""
    status = False

restaurante_praca = Restaurante()
restaurante_praca.nome = "Bistrô"
restaurante_praca.categoria = "Italiana"
restaurante_praca.status = True

restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"
restaurante_pizza.status = True

restaurantes = [restaurante_praca,restaurante_pizza]

print("")
print(vars(restaurante_praca))

if restaurante_praca.status == True:
    print(f"O restaurante {restaurante_praca.nome} está ativo\n")

else:
    print(f"O restaurante {restaurante_praca.nome} está inativo\n")

print(vars(restaurante_pizza))

