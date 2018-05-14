import requests
import re
import sys
import json

class KwiCon:

    client = requests.Session()

    def __init__(self, user, password):
        self.login(user, password)

    def login(self, user, password):
        print('Logging in %s' %user)
        r = self.client.post('https://www.kwikku.com/auth_login.php', {
            'user': user,
            'pass': password,
            'remember': 'true'
        })
        # Check if login success
        rDecoded = json.loads(r.text);
        result_code = rDecoded[0]['result']
        if result_code == '1':
            print('Incorrect username')
            sys.exit()
        elif result_code == '2':
            print('You are logged in!')
        elif result_code == '3':
            print('Incorrect password!')
            sys.exit()
        else:
            print('Login Failed: %s' % rDecoded[0]['result'])
            sys.exit()

    def get_all_userid_in_find_friends(self):
        r = self.client.get('https://www.kwikku.com/i/settings/findfriends')
        return re.findall('<div class=\'boxchat nolink\'><a href=\'https://www.kwikku.com/(.*?)\'', r.text)

    def get_all_user_id_in_discover(self, keyword, page):
        r = self.client.post('https://www.kwikku.com/core/core_ajax_data/get_search_pages.php', {
            'act': 'users',
            'keyword': keyword,
            'loaddata': page * 21
        })
        rList = []
        if r.text == 'null':
            return rList
        rDecoded = json.loads(r.text);
        for user in rDecoded:
            rList.append(user['username'])
        return rList
            

    def send_message(self, user_id, message_body):
        """
        Send message to user

        Args:\n
        `user_id` (:str:): the user id to send the message\n
        `message_body` (:str:): the message to send\n

        Returns:\n
        :Bool: : True; if sent\n
        Otherwise:\n
        :Bool: : False
        """
        response = self.client.post('https://www.kwikku.com/core/core_actions/post_message.php', {
            'action': '1',
            'to': user_id,
            'body': message_body,
            'tipe': '0'
        })

        # Check if send message success
        if response.text == '[{"result":"1"}]':
            return True
        else:
            return False

    def get_user_online(self, userid):
        """
        Get all of the user detail information from the Kwikku web

        Args:\n
        `userid` (:str:): the user id to get the detail information

        Returns:\n
        :Dictionary: {userid, username, dateofbirth, gender, status, city, aboutme}; if found\n
        Otherwise:\n
        :None:
        """
        response = self.client.get('https://www.kwikku.com/%s/aboutme' % userid)
        if re.search('back_404.png', response.text):
            return None
        else:
            parsed = re.findall('<div class=\'list\'>\s*<p></p>\n(.*?)</div>.*?</p>\n(.*?)</div>.*?</p>\n(.*?)</div>.*?</p>\n(.*?)</div>.*?</p>\n(.*?)</div>.*?</p>\n(.*?)</div>',
                                    response.text,
                                    re.DOTALL)[0]
            user_detail = {
                'userid': userid,
                'username': parsed[0],
                'dateofbirth': parsed[1],
                'gender': parsed[2],
                'status': parsed[3],
                'city': parsed[4],
                # need to fix aboutme : messy (some html tag still appear)
                'aboutme': parsed[5]
            }

            return user_detail
