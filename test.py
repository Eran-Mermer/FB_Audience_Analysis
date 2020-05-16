from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
import hmac
import hashlib
import base64

def generate_appsecret_proof(access_token, app_secret):
    dig = hmac.new(app_secret.encode('utf-8'), msg=access_token.encode('utf-8'), digestmod=hashlib.sha256).digest()
    return base64.b64encode(dig).decode()

my_app_id = '685049868955715'

# Taken from - https://developers.facebook.com/apps/685049868955715/settings/basic/
my_app_secret = ''

# Access Token generated using - https://developers.facebook.com/tools/explorer?method=GET&path=me%3Ffields%3Did%2Cname&version=v7.0
my_access_token = ''

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
#me = AdUser(fbid='me')
#my_account = me.get_ad_accounts()[0]
my_account = AdAccount('act_58886378')
#campaigns = my_account.get_campaigns()
#print(campaigns)

#m = hashlib.sha256()
#m.update('EAAHqOU5xIQUBAAIYwB7o4jfeWGYn6ZCiButBZBZC8oVzZAlR0NOXv8063yLe74W5rRKES3AWbZB17f0uZCcKtBkLUMJpCmJMrpLcR4vfN21eZB842JnXAa6gj0ZBF9I8WnRrkLqLgSVLxtZCgrvjnr5E2nZAbCNnLyoZCMioJbXTjwOhkCWXtuel9GBQnnK6BVipbf5pDo8qVuAG10iIT4qy26ncppITfKRSKIZD'.encode('utf-8')+'05d41524b4dae350b5501c2c33f8c6ee'.encode('utf-8'))
#dig = m.digest()
#base64.b64encode(dig).decode()
#'vqMeVJCXcsJdgzPJNWs4roeqD29a8gjnHJpmKbXiQCk='


# appsecret_proof = generate_appsecret_proof(my_access_token, my_app_secret)
# print(appsecret_proof)
