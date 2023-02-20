from model import repository
from model import note


class Controller:
    def __init__(self, _repository):
        self.__repository = _repository

    def read_note(self, note_id):
        if isinstance(self.__repository, repository.Repository):
            notes = self.__repository.get_all_notes()
            for _note in notes:
                if isinstance(_note, note.Note):
                    if _note.get_id() == note_id:
                        return _note
                else:
                    print('Internal error!')
        else:
            print('Internal error!')
        print('Note not found!')

    def read_notes(self):
        if isinstance(self.__repository, repository.Repository):
            return self.__repository.get_all_notes()
        else:
            print('Internal error!')

    def validate_note_data(self, _note):
        if isinstance(_note, note.Note):
            if not _note.get_title() or not _note.get_msg() or not _note.get_date():
                print('Fields are empty')
                return False
            else:
                return True
        else:
            print('Internal error!')
            return False

    def save_note(self, _note):
        if Controller.validate_note_data(self, _note):
            if isinstance(self.__repository, repository.Repository):
                self.__repository.create_note(_note)
                print('Done')
            else:
                print('Internal error!')

    def delete_note(self, note_id):
        if isinstance(self.__repository, repository.Repository):
            self.__repository.delete_note(note_id)
        else:
            print('Internal error!')

    def edit_note(self, _note):
        if Controller.validate_note_data(self, _note):
            if isinstance(self.__repository, repository.Repository):
                self.__repository.edit_note(_note)
            else:
                print('Internal error!')
