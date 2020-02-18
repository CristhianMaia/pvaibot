import auth
import tweepy
import time, datetime, random

bot1 = auth.bot1()

pessoa = "layguerra"

followerids =[]
for user in tweepy.Cursor(bot1.followers_ids, id=pessoa,count=5000).items():
  followerids.append(user)    
print (len(followerids))

#Below function could be used to make lookup requests for ids 100 at a time leading to 18K lookups in each 15 minute window
def get_usernames(userids, bot1):
    fullusers = []
    u_count = len(userids)
    print(u_count)
    print(userids)
    print("")
    print("")
    count = 0
    try:
        for i in range(int(u_count/100) + 1):            
            end_loc = min((i + 1) * 100, u_count)
            fullusers.extend(
                bot1.lookup_users(user_ids=userids[i * 100:end_loc])                
            )

            print(len(fullusers))
        return fullusers
    except:
        import traceback
        traceback.print_exc()
        print ('Something went wrong, quitting...')

#Calling the function below with the list of followeids and tweepy api connection details

def get_friends():
  ids_me =[]
  for user in tweepy.Cursor(bot1.friends_ids, id='roleparanavai',count=5000).items():
    ids_me.append(user)
  print (len(ids_me))
  return ids_me

def get_followers():
  ids_me_who = []
  for user in tweepy.Cursor(bot1.followers_ids, id='roleparanavai',count=5000).items():
    ids_me_who.append(user)
  print (len(ids_me_who))
  return ids_me_who


fullusers = get_usernames(followerids,bot1)
ids = []
ids_by_fl = []
ids_for =[]
value_follower = 500

ids_me = get_friends()
ids_no_followed = []
ids_no_followed_seguidores = []
ids_me_who = get_followers()

for friend in fullusers:
  location = friend.location.split(',')
  locationh = friend.location.split(' - ')
  location_string = friend.location

  if (location[0] == "pvai" or location[0] == 'Paranavaí' or locationh[0] == "Paranavaí - PR" or 
    (('p' in location_string or 'P' in location_string) and 
    ('v' in location_string or 'V' in location_string) and 
    ('a' in location_string or 'A' in location_string) and
    (('i' in location_string or 'I' in location_string) or
    ('í' in location_string or 'Í' in location_string))) and not
    (location_string[1] == "o" or location_string[2] == 'o') and not
    friend.id in ids_me_who):
    print("")
    print("{}({}) em {} seguidores: {}".format(friend.name, friend.id, friend.location, friend.followers_count))
    ids.append(friend.id)

    if friend.id in ids_me:
      print("Bot ja segue")
    else:
      if friend.id in ids_me_who:
        print("esse usuario ja te segue")
      else:
        print("Esse usuario NÃO te segue")
        ids_no_followed.append(friend.id)

    if friend.followers_count >= value_follower:
      ids_by_fl.append(friend.id)
      if friend.id in ids_me:
        continue;
      else:
        ids_no_followed_seguidores.append(friend.id)

print("\n{} ids encontrados em Paranavai de {} seguidores.".format(len(ids), len(fullusers)))
print("e {} com mais de {} seguidores".format(len(ids_by_fl), value_follower))

print("\nde {}, {} voce ainda não segue .".format(len(ids), len(ids_no_followed)))
print("e {} com mais de {} seguidores\n".format(len(ids_no_followed_seguidores), value_follower))
print("@{}".format(pessoa))
op = input("seguir? [todos 1] [{} seguidores 2]\n".format(value_follower))
count = 0

if op == '1':
  try:
    bot1.create_friendship(id=pessoa)
  except:
    print("Não foi possivel seguir a pessoa principal")
  ids_for = ids_no_followed
if op == '2':
  try:
    bot1.create_friendship(id=pessoa)
  except:
    print("Não foi possivel seguir a pessoa principal")
  ids_for = ids_no_followed_seguidores

for id in ids_for:
  print("seguindo {}".format(id))
  # if count >=82:
  try:
    bot1.create_friendship(id=id)
  except tweepy.error.TweepError as error:
    print(error)
    print("Erro ao seguir {}".format(count))
  count += 1
  print(count)
  # if count%50==0:
  #   input("Continuar?")
  # if count >= 130:
  #   date_now = datetime.datetime.now()
  #   ano = int(str(date_now.date()).split('-')[0])
  #   mes = int(str(date_now.date()).split('-')[1])
  #   dia = int(str(date_now.date()).split('-')[2])
  #   horario_1 = datetime.datetime(ano, mes, dia, 12, 0 ,0)
  #   horario_2 = datetime.datetime(ano, mes, dia, 18, 0, 0)
  #   horario_3 = datetime.datetime(ano, mes, dia, 22, 0, 0)
  #   if date_now <= horario_1:
  #     diferenca = (horario_1 - date_now).seconds
  #   elif date_now <= horario_2:
  #     diferenca = (horario_2 - date_now).seconds
  #   elif date_now <= horario_3:
  #     diferenca = (horario_3 - date_now).seconds
  #   time.sleep(diferenca+5)
  #   count=0
  # if count >=82:
  random_sleep = random.randrange(15, 30)
  print("Sleep: {}".format(random_sleep))
  time.sleep(random_sleep)

    # 153 - MPmendees