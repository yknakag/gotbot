
# coding: utf-8

# In[19]:

import twitter

def __init__(self):   
    
    CK = ''
    CS = ''         # Consumer Secret
    AT = '' # Access Token
    AS = ''# Accesss Token Secert
    
    api = twitter.Api(consumer_key=CK,
                  consumer_secret=CS,
                  access_token_key=AT,
                  access_token_secret=AS)


# In[56]:

def tweet(self,text):
    #自分のアカウントでつぶやく
    self.api.PostUpdate(text)  


# In[57]:

def get_direct_message():
    #最新の受けた直接メッセージを返す
    dm=self.api.GetDirectMessages(count=1,full_text = True)
    return dm


# In[54]:

def send_direct_message(text,screen_name):
    #直接メッセージを送る
    self.api.PostDirectMessage(text=text, screen_name=screen_name)#screen_nameは'nakagawa_yukari'のこと


# In[55]:

#受け取っているメッセージを表示する
#api.GetSentDirectMessages()


# In[ ]:

#TO_DO
#ランダムにユーザーを発見し、悩みっぽいコメントに勝手にコメントする（布教活動）
#神の助けを求めるツイートを探して、それにツイートする

