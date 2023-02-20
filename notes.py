from model import file_operation
from model import repository
from controller import controller
from view import view


if __name__ == '__main__':
    file = file_operation.FileOperation('notes.csv')
    repo = repository.Repository(file)
    _controller = controller.Controller(repo)
    _view = view.View(_controller)
    _view.run()