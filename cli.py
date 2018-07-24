#!/usr/bin/env python
"""
Trello CLI : Django/Python Assignment

Usage:
    trello board new <name>
    trello board show <Board ID>
    trello list new <name> <Board ID>
    trello list show <List ID>
    trello card new <name> <description> <List ID>
    trello card show <Card ID>
    trello (-i | --interactive)
    trello (-h | --help)

Options:
    -i, --interactive            Interactive Mode
    -h, --help                   Show this screen and exit.
"""

import sys
import cmd, getpass,requests,json
from docopt import docopt, DocoptExit
from requests.auth import HTTPBasicAuth
from pprint import pprint


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    print("Username:",end="")
    username=input()
    try:
        password = getpass.getpass()
    except Exception as error:
        print('ERROR', error)
    print(username)
    print(password)
    intro = 'Welcome to Trello CLI APP!' \
        + ' (type help for a list of commands.)'
    prompt = '(trello)'
    file = None

    @docopt_cmd
    def do_board(self, arg):
        """Usage: board [(-c <cmd>)] [(-n <name>)] [(-b <id>)] [--all]

Options:
    -c, --command   <cmd>   Enter 'new' to create and 'show' to show existing boards.
    -n, --name      <name>  Use this while creating new board.
    -b, --BoardID   <id>    Display lists and cards of the specific board with 'id'.
    -a, --all               Show all boards.
        """
        # print(arg)
        # print(self.username)
        # print(self.password)
        if arg['<cmd>']=="new":
            print("Creating new board with name: "+arg['<name>'])
            d1={'name':arg['<name>']}
            try:
                r = requests.post('http://127.0.0.1:8000/api/boards/', data=d1 ,auth=HTTPBasicAuth(self.username, self.password))
                pprint(json.loads(r.text))
            except Exception as e:
                print(e)
            # print(r)
        elif arg['<cmd>']=='show':
            print('Displaying board')
            if arg['--all']:
                try:
                    r=requests.get('http://127.0.0.1:8000/api/boards/',auth=HTTPBasicAuth(self.username, self.password))
                    print(r.status_code)
                    # print(type(r.text))
                    # print(r.text)
                    if r.status_code==200:
                        data=json.loads(r.text)
                        for board in data:
                            print("ID: "+str(board['id'])+" NAME: "+board['name'])
                except Exception as e:
                    print(e)
            elif arg['--BoardID']:
                try:
                    r=requests.get('http://127.0.0.1:8000/api/'+arg['<id>'],auth=HTTPBasicAuth(self.username, self.password))
                    # pprint(r.text)
                    print(r.status_code)
                    if r.status_code==200:
                        board=json.loads(r.text)
                        pprint(board)
                    # print("ID: "+str(board['id'])+" NAME: "+board['name'])
                except Exception as e:
                    print(e)
            else:
                print("Invalid command. See help board")

        else:
            print("Invalid command. See help board")

    @docopt_cmd
    def do_list(self, arg):
        """Usage: list [(-c <cmd>)] [(-n <name>)] [(-b <id>)] [--all]

Options:
    -c, --command   <cmd>   Enter 'new' to create and 'show' to show existing lists
    -n, --name      <name>  Use this while creating new list.
    -b, --BoardID   <id>    Use this while creating new list.
    -a, --all               Show all lists
        """

        # print(arg)
        if arg['<cmd>']=="new":
            print("Creating new list with name: "+arg['<name>']+" in board: "+arg['<id>'])
            d1={'board':arg['<id>'],'name':arg['<name>']}
            try:
                r = requests.post('http://127.0.0.1:8000/api/tl/', data=d1 ,auth=HTTPBasicAuth(self.username, self.password))
                pprint(json.loads(r.text))
            except Exception as e:
                print(e)
            # print(r)
        elif arg['<cmd>']=='show':
            print('Displaying lists')
            if arg['--all']:
                try:
                    r=requests.get('http://127.0.0.1:8000/api/tl/',auth=HTTPBasicAuth(self.username, self.password))
                    print(r.status_code)
                    if r.status_code==200:
                    # pprint(r.text)
                        data=json.loads(r.text)
                        # pprint(data)
                        for l in data:
                            print("ID: "+str(l['id'])+" NAME: "+l['name'])
                except Exception as e:
                    print(e)
            else:
                print("Invalid command. See help list")

        else:
            print("Invalid command. See help list")

    @docopt_cmd
    def do_card(self, arg):
        """Usage: card [(-c <cmd>)] [(-n <name>)] [(-d <desc>)] [(-l <id>)] [--all]

Options:
    -c, --command       <cmd>   Enter 'new' to create and 'show' to show existing cards
    -n, --name          <name>  Use this while creating new card.
    -l, --ListID        <id>    Use this while creating new card.
    -d, --description   <desc>  Use this while creating new card.
    -a, --all                   Show all cards.
        """

        # print(arg)
        if arg['<cmd>']=="new":
            print("Creating new card with name: "+arg['<name>']+" in list: "+arg['<id>']+" with description: "+arg['<desc>'])
            d1={'task_list':arg['<id>'],'name':arg['<name>'],'description':arg['<desc>']}
            try:
                r = requests.post('http://127.0.0.1:8000/api/card/', data=d1 ,auth=HTTPBasicAuth(self.username, self.password))
                pprint(json.loads(r.text))
            except Exception as e:
                print(e)
            # print(r)
        elif arg['<cmd>']=='show':
            print('Displaying cards')
            if arg['--all']:
                try:
                    r=requests.get('http://127.0.0.1:8000/api/card/',auth=HTTPBasicAuth(self.username, self.password))
                    print(r.status_code)
                    if r.status_code==200:
                        data=json.loads(r.text)
                        # pprint(data)
                        for card in data:
                            print("ID: "+str(card['id'])+" NAME: "+card['name']+" DESCRIPTION: "+card['description'])
                except Exception as e:
                    print(e)
            else:
                print("Invalid command. See help card")

        else:
            print("Invalid command. See help card")
    def do_logout(self, arg):
        """Logout of the session"""
        print('Logged out!')
        print("Username:",end="")
        self.username=input()
        try:
            self.password = getpass.getpass()
        except Exception as error:
            print('ERROR', error)
        # print(username)
        # print(password)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
