import atexit


__all__ = ['txt_format', 'rtf_format', 'pdf_format', 'docx_format',
           'avro_format', 'csv_format', 'json_format', 'parsing']

__version__ = '1.1'


@atexit.register
def goodbye():
    print('I hope we will meet soon!')
