from KwikkuConnection import KwiCon
from KwikkuDatabase import KwiDB
import sys
import getpass

# Create client

username = input('Username:')
passwd = getpass.getpass('Password:')

KWICON = KwiCon(username, passwd)
KWIDB = KwiDB()
while True:
    print('\nWhat do you want to do?\n1. Send Message\n2. List All Local User Id\n3. Get User Detail Information\n4. Exit')

    user_choice = input()

    if user_choice == '1':
        # Send message
        print("\nEnter the recipient user id:")
        userid = input()
        print("\nEnter the message that you want to send:\n")
        message = input()
        if KWICON.send_message(userid, message):
            print('\nSend message to %s (Success)\n' % userid)
        else:
            print('\nSend message to %s (Failed)\n' % userid)

    elif user_choice == '2':
        print(KWIDB.user_db.keys())
    elif user_choice == '3':
        # Get User Detail Information
        print("\nEnter user id to get the detail information:")
        userid = input()
        #Get from local db
        user = KWIDB.get_user(userid)
        if user == None:
            #Get from online
            user = KWICON.get_user_online(userid)
            if user == None:
                print('\nuser not found\n')
            else:
                #Add to local db
                KWIDB.add_user(user)
        if user != None:
            print('\nuser id : %s\nusername : %s\nDate of birth : %s\ngender : %s\nstatus : %s\ncity : %s\nabout me : %s' %
                (user['userid'], user['username'], user['dateofbirth'], user['gender'], user['status'], user['city'], user['aboutme']))

    else:
        KWIDB.save_db()
        sys.exit()

# KWIKKU.SendMessage('VIPQIUQIU99', 'Kamu jual aqua yah')
# ids = GetallIdInFindFriends()

# for id in ids:
# SendMessage(id,'hi')
