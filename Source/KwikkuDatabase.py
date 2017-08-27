import json
import os


class KwiDB:
    user_db = {}

    def __init__(self):
        self.load_db()

    def add_user(self, user):
        self.user_db[user['userid']] = user

    def load_db(self):
        if os.path.exists('../DB/user_db.json'):
            with open('../DB/user_db.json', "r") as f:    
                self.user_db = json.load(f)

    def save_db(self):
        directory = '../DB'
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(directory + '/user_db.json', "w") as f:
            json.dump(self.user_db, f)

    def get_user(self, userid):
        """
        Get all of the user detail information

        Args:\n
        `userid` (:str:): the user id to get the detail information

        Returns:\n
        :Dictionary: {userid, username, dateofbirth, gender, status, city, aboutme}; if found\n
        Otherwise:\n
        :None:
        """

        if userid in self.user_db.keys():
            return self.user_db[userid]
        else:
            return None
