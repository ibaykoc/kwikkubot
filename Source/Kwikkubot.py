from KwikkuConnection import KwiCon
import sys
import getpass

# Create client

username = input('Username:')
password = getpass.getpass('Password:')

KWICON = KwiCon(username, password)

while True:
    print('\n'
          '1. Send Message\n'
          '2. List All Local User Id\n'
          '3. Get User Detail Information\n'
          '4. Exit')

    user_choice = input()

    if user_choice == '1':
        # Send message
        user_id = input('User id: ')
        message = input('Message: ')
        if KWICON.send_message(user_id, message):
            print('\nSend message to %s (Success)\n' % user_id)
        else:
            print('\nSend message to %s (Failed)\n' % user_id)

    else:
        sys.exit()
