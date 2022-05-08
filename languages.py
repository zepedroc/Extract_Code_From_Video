from javascriptFuncs import parseJavascript
from pythonFuncs import parsePython


NORMAL_TEXT = 0
PYTHON = 1
JAVASCRIPT = 2

ACCEPTED_LANGUAGES = ['Normal Text', 'Python', 'Javascript']

# Method that lets user decide in which language the text will be provided in
def chooseLang():
    print()
    for idx, lang in enumerate(ACCEPTED_LANGUAGES):
        print(str(idx) + '. ' + lang)

    chosen_lang = -1

    while chosen_lang not in range(0, len(ACCEPTED_LANGUAGES)):
        try:
            chosen_lang = int(input('Choose language above (number):'))
        except ValueError:
            print('Please only input digits.')

    return chosen_lang


# Method that decides which parsing should be applied to the text
def handle_lang(text, lang):
    if lang == NORMAL_TEXT:
        return text
    if lang == PYTHON:
        return parsePython(text)
    if lang == JAVASCRIPT:
        return parseJavascript(text)
