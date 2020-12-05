import re
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


class PDF:

    def get_text(self, path):
        # возвращаемый список с текстом
        text_list = list()

        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle)
        page_interpreter = PDFPageInterpreter(resource_manager, converter)

        with open(path, 'rb') as fh:
            for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()

        converter.close()
        fake_file_handle.close()

        if text:
            text_list = text.split('. ')

        return text_list

    def find_text(self, path, pattern_list):
        # возвращаемый словарь с совпадениями
        match_dict = dict()

        # получение текста из файла
        text_list = self.get_text(path)

        for string in text_list:
            for pattern in pattern_list:
                match = re.search(pattern.lower(), string.lower())
                if match:
                    match_dict[string] = pattern

        return match_dict


if __name__ == '__main__':
    path = 'C:\\Users\\Samsung\\Desktop\\игры\\DnD\\книги\\Книга Игрока.pdf'
    pdf = PDF()

    result_text = pdf.get_text(path)
    print(result_text)

    found_text = pdf.find_text(path, ['Опыт'])
    for elem in found_text:
        print(elem)
