import api



api.corrigir()
confirmacoes = []
val = [
  ('Baile da Colômbia', '2020-04-25', "1228059454920413189"),
  # ('Baile do Zé', '2020-04-04', "1219621891830403074"),
]

api.create_evento(val)
# # pessoas = []
# api.create_pessoa(pessoas_evento)
# pessoas.append(tuple([pessoas_evento[0][1]]))
# pessoas.append(tuple([pessoas_evento[1][1]]))
# api.update_tweet_evento("1218278690351697920", 5)
# for i in confirmacoes:
#   pessoas.append(tuple([i[1]]))
# api.create_pessoa(pessoas_evento)
# api.confirmar_pessoa(pessoas_evento)
# for e in api.get_eventos():
#   print(e[0])
#   api.destroy_evento(e[0])

# api.destroy_evento(9)
# api.destroy_confirmar_pessoa('111111111')
print("Eventos")
eventosdb = api.get_eventos()
for i in eventosdb:
  print(i)

print("Pessoas e Eventos")
pessoasbdeve = api.get_pessoa_evento()
for i in pessoasbdeve:
  print(i)


# eventoinput = [('NITRO FOLIA', '2020-01-25', '1215441869829738501'),]

# api.create_evento(eventoinput)
