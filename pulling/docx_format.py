import re
try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile


class DOCX:

    def get_text(self, path):
        # возвращаемый список с текстом
        text_list = list()

        word_namespace = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        para = word_namespace + 'p'
        text = word_namespace + 't'

        document = zipfile.ZipFile(path)
        xml_content = document.read('word/document.xml')
        document.close()
        tree = XML(xml_content)

        raw_text_list = list()
        for paragraph in tree.iter(para):
            texts = [node.text for node in paragraph.iter(text) if node.text]
            if texts:
                raw_text_list.append(''.join(texts))

        all_text = '\n\n'.join(raw_text_list)  # весь текст в одной строке

        strings = all_text.split('. ')  # разбиение по предложениям
        for line in strings:
            lines = line.split('\n')  # разбиение по абацам
            for string in lines:
                text_list.append(string)

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
    path = 'test/test.docx'
    docx = DOCX()

    result_text = docx.get_text(path)
    print(result_text)

    found_text = docx.find_text(path, ['file'])
    print(found_text)
