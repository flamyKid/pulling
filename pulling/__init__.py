import atexit


__all__ = ['Txt', 'Rtf', 'Pdf', 'Docx', 'Csv', 'Avro', 'Json']

__version__ = '1.4.2'


@atexit.register
def goodbye():
    print('I hope we will meet soon!')
