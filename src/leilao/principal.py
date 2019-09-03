from src.leilao.dominio import Usuario, Leilao, Lance


rafael = Usuario('Rafael')
luana = Usuario('Luana')

lance_do_rafael = Lance(rafael, 100.0)
lance_da_luana = Lance(luana, 150.0)


leilao = Leilao('Celular')

leilao.lances.append(lance_do_rafael)
leilao.lances.append(lance_da_luana)


for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

#avaliador = Avaliador()
#avaliador.avalia(leilao)

#print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')
