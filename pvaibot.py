import auth, api
import datetime, time, random
import tweepy
from colorama import Fore
from colorama import Style

def bot():
  bot1 = auth.bot1()
  # bot2 = auth.bot2()

  tweets_id = []
  dtnow = datetime.date.today()
  count = 0
  op = 1
  let_post = 0

  confirmados = []

  eventos = api.get_eventos()
  eventoscount = api.get_pessoa_evento_count()

  for i in eventoscount:
    confirmados.append(i[0])
  print(confirmados)

  texto = "Lista de Rolês [{}]\n\n".format(dtnow.strftime("%d/%m"))
  texto_1 = ""
  texto_2 = ""

  for i in eventos:
    data_splitt = str(i[2]).split('-')
    data = "{}/{}".format(data_splitt[2], data_splitt[1], data_splitt[0])

    count += 1

    confirmado = confirmados.count(i[0])

    try:
      tweets_id.append(i[3])
    except KeyError:
      print("faltou tweet id")
    
    # if count == len(eventos):
    #   print(count)
    #   texto += "[{}] #{} - {} ({} confirmados)\n\n".format(data, i[0], i[1], confirmado)
    #   break;

    if op == 1:
      textoold = texto
      #  ({} confirmados)
      texto += "[{}] - {}\n".format(data, i[1], confirmado)
      if len(texto) >= 271:
        print(len(texto))
        texto = textoold
        op = 2
    if op == 2:
      textoold = texto_1
      texto_1 += "[{}] - {}\n".format(data, i[1], confirmado)
      if len(texto_1) >= 272:
        print(len(texto_1))
        texto_1 = textoold + "\n\n[ + ]"
        op = 3
    if op == 3:
      textoold = texto_2
      texto_2 += "[{}] - {}\n".format(data, i[1], confirmado)
      if len(texto_2) >= 272:
        print(len(texto_2))
        texto_2 = textoold + "\n\n[ + ]"
        op = 3
  # edoido(tweets_id)
  texto += "\n\n[ + ]"
  print(texto)
#   texto_confirmacao = """\nPara confirmar presença no rolê digite "#rolepvai x"
# # Onde X é o id do role, o numero anterior ao nome, ex: \n-->#123 - Evento em Paranavaí; digite: #rolepvai 123"""

  status = bot1.update_status(status=texto)

  if op == 2:
    print(texto_1)
    textoold = texto_1
    texto_1 += texto_confirmacao

    if len(texto_1) > 280:
      print("Bateu 280 no segundo texto")
      print(len(texto_1))
      texto_1 = textoold 
      let_post = 1

    bot1.update_status(status=texto_1, in_reply_to_status_id=status.id_str)

    # if let_post == 1:
    #   print("Postou texto confirmacao separado")
    #   bot1.update_status(status=texto_confirmacao, in_reply_to_status_id=status.id_str)

  if op == 3:
    print(texto_1)
    print(texto_2)
    bot1.update_status(status=texto_1, in_reply_to_status_id=status.id_str)
    bot1.update_status(status=texto_2, in_reply_to_status_id=status.id_str)

  status = bot1.update_status(status="@roleparanavai Detalhes atualizados em {}\nhttps://twitter.com/roleparanavai/status/{}".format(dtnow.strftime("%d/%m"), 1218975227339776000), in_reply_to_status_id=status.id_str)

  #Bot respostas

# def edoido(tweets_id):
#   bot1 = auth.bot1()
#   for i in tweets_id:
#     try:
#       random_sleep = random.randrange(10, 20)
#       print("Sleep: {}".format(random_sleep))
#       time.sleep(5)
#       print(i)
#       bot1.update_status(status='https://twitter.com/roleparanavai/status/{}'.format(i), in_reply_to_status_id=1218975227339776000)
#     except tweepy.error.TweepError: 
#       print("Erro")
#   input("acabou")

bot()