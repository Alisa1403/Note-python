from datetime import datetime

from controller import controller
from model import note


class View:
    def __init__(self, _controller):
        self.__controller = _controller

    def run(self):
        while True:
            command = str(input('Enter the command (help - list of all commands): '))
            if command.lower() == 'exit':
                return

            if command.lower() == 'create':
                title = str(input('Enter note title: '))
                msg = str(input('Enter note text: '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.save_note(note.Note('0', title, msg, str(datetime.now().strftime("%Y.%m.%d %H:%M:%S"))))
                else:
                    print('Internal error!')


            elif command.lower() == 'list':
                if isinstance(self.__controller, controller.Controller):
                    notes = self.__controller.read_notes()
                    notes.sort()
                    for _note in notes:
                        print(_note)
                else:
                    print('Internal error')


            elif command.lower() == 'delete':
                note_id = str(input('Enter ID: '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.delete_note(note_id)
                else:
                    print('Internal error!')

            elif command.lower() == 'edit':
                note_id = str(input('Enter ID: '))
                title = str(input('Enter note title: '))
                msg = str(input('Enter note text: '))
                if isinstance(self.__controller, controller.Controller):
                    self.__controller.edit_note(note.Note(note_id, title, msg, str(datetime.now().strftime("%Y.%m.%d %H:%M:%S"))))

            elif command.lower() == 'help':
                print('List of commands:')
                print('list - display list of all notes')
                print('create - create new note')
                print('edit - edit note by ID')
                print('delete - delete note by ID')
                print('exit - exit from program')
            else:
                print('Command not found!')