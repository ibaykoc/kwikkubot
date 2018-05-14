from KwikkuConnection import KwiCon
import sys
import getpass

# Create client

username = input('Username:')
password = getpass.getpass('Password:')

KWICON = KwiCon(username, password)
while True:
    print('\n'
          '1. Do chat bot\n'
          '2. Exit')

    user_choice = input()
    if user_choice == '1':
        # Send message
        # user_id = input('User id: ')
        # message = input('Message: ')
        # if KWICON.send_message(user_id, message):
        #     print('\nSend message to %s (Success)\n' % user_id)
        # else:
        #     print('\nSend message to %s (Failed)\n' % user_id)
        keyword = input('Enter a keyword for specific user that you want chat bot to send message to: ')
        message = input('Enter a message that you want chat bot to send: ')
        page_index = 0
        while True:
            retrieved_user = KWICON.get_all_user_id_in_discover(keyword, page_index)
            for uid in retrieved_user:
                if KWICON.send_message(uid, message):
                    print('\nSend message to %s (Success)\n' % uid)
                else:
                    print('\nSend message to %s (Failed)\n' % uid)
            if len(retrieved_user) < 21:
                break

    else:
        sys.exit()
