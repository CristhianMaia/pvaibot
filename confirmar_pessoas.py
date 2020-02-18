import auth, api
import tweepy

def main():

  bot1 = auth.bot1()

  perfil = 1214542399596302337

  list = []

  search = tweepy.Cursor(bot1.search, q="#rolepvai", result_type='recent', include_entities=False).items()

  for results in search:
    print(results.text)
    list_results = []
    perfil_id = results.in_reply_to_user_id
    id_evento_texto = results.text
    id_evento = ""
    user = results.user.id_str

    if perfil_id != 1214542399596302337:
      continue

    try:
      id_evento_texto = id_evento_texto.split('#rolepvai ')[1]

      for i in id_evento_texto:
        if i.isdigit() == False:
          break;
        id_evento += i

      list_results.append(int(id_evento))
      list_results.append(user)

      list.append(list_results)
      
    except IndexError as error:
      print(error)
      print(Fore.RED + "sem ID de role" + Style.RESET_ALL)

  print(Fore.GREEN)
  print(list)
  print(Style.RESET_ALL)
  api.confirmar_pessoa(list)
  # print(perfil)
  # print(id_evento_texto)
  # print(user)
     
main()
            # item = (results.text).encode('utf-8').strip()