import requests
import sys


def main():
    if (len(sys.argv) < 4):
        print('\nERROR: Missing Arugments\n')
        print('Usage:     filename.py <MaillistName> <AdminEmail@uci.edu> <AdminPswd>')
        print('Ex)    cmdArgEmails.py   soe-staff       hssoeit@uci.edu     ********  ')
        print('\nQuitting...')
        exit()

    emailList = sys.argv[1]
    email = sys.argv[2]
    pwd = sys.argv[3]

    emails = []
    fname = emailList + '.txt'

    print('MailList: ', emailList)
    print('Password: ', pwd)

    r = requests.get(
        'https://department-lists.uci.edu/mailman/roster/' + emailList + '?language=en&roster-email=' + email + '&roster-pw=' + pwd + '&SubscriberRoster=Visit+Subscriber+List')
    data = r.text
    data = data.split('\n')

    for i in range(len(data)):
        if ('<li><a href=' in data[i]):
            emailString = data[i]
            emailString = emailString.strip('</a>')
            start = emailString.rfind('>') + 1
            emailString = emailString[start:]
            emailString = emailString.replace(' at ', '@')

            emails.append(emailString)
            print(emailString)

    print('\nDone retrieving emails')
    emails = sorted(list(set(emails)))
    if (len(emails) == 0):
        print("No emails retrieved, check maillist/credential spelling and try again")
        exit(1)

    print('\n\nWriting to File:', fname)

    with(open(fname, 'w')) as file:
        file.write('\n'.join(emails))

    print(fname, ' saved!')


main()
