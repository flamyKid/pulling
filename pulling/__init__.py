import atexit


__all__ = ['Txt', 'Rtf', 'Pdf', 'Docx', 'Csv', 'Avro', 'Json']

__version__ = '1.4.post1'


@atexit.register
def goodbye():
    print('I hope we will meet soon!')
