import auth, api
import tweepy

bot1 = auth.bot1()

texto = ""

status = bot1.update_status(status=texto)
