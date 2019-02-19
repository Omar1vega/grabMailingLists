import requests
import sys


def main():
    if len(sys.argv) < 4:
        print('\nERROR: Missing Arugments\n')
        print('Usage:     filename.py <MaillistName> <AdminEmail@uci.edu> <AdminPswd>')
        print('Ex)    cmdArgEmails.py   soe-staff       hssoeit@uci.edu     ********  ')
        print('\nQuitting...')
        exit()

    email_list = sys.argv[1]
    email = sys.argv[2]
    password = sys.argv[3]

    emails = []
    file_name = email_list + '.txt'

    print('MailList: ', email_list)
    print('Password: ', password)

    r = requests.get('https://department-lists.uci.edu/mailman/roster/' + email_list
                     + '?language=en&roster-email=' + email + '&roster-pw='
                     + password + '&SubscriberRoster=Visit+Subscriber+List')
    data = r.text
    data = data.split('\n')

    for line in data:
        if '<li><a href=' in line:
            email_string = line.strip('</a>')
            start = email_string.rfind('>') + 1
            email_string = email_string[start:]
            email_string = email_string.replace(' at ', '@')

            emails.append(email_string)
            print(email_string)

    print('\nDone retrieving emails')
    emails = sorted(list(set(emails)))
    if len(emails) == 0:
        print("No emails retrieved, check maillist/credential spelling and try again")
        exit(1)

    print('\n\nWriting to File:', file_name)

    with(open(file_name, 'w')) as file:
        file.write('\n'.join(emails))

    print(file_name, ' saved!')


main()
