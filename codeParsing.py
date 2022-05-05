import re


def parsePython(text):
    final_text = ''
    followed_empty_lines = 0

    for line in text.splitlines():
        # remove multiple spaces
        if len(line.strip()) == 0:
            followed_empty_lines += 1
            if followed_empty_lines >= 2:
                continue
            else:
                final_text += '\n'
                continue
        elif followed_empty_lines > 0:
            followed_empty_lines = 0

        new_line = line.replace('inport', 'import')
        new_line = new_line.replace('fron', 'from')
        new_line = new_line.replace('nuspy', 'numpy')
        new_line = new_line.replace('“', '"')
        new_line = new_line.replace('. ', '.')

        # if the line starts with (for,while,if) it needs ':' in the end
        if re.match(r'^(for|while|if|def)\s', new_line) and new_line[-1] != ':':
            new_line += ':'

        # if the line starts with two words and the first is not (while,from,if,for,import) then there's a missing underscore between them
        elif re.match(r'^(?!for|while|if|from|import|return|def)\w+\s+\w+', new_line):
            new_line = new_line.replace(' ', '_', 1)

        final_text += f'{new_line}\n'

    return final_text


# txt_file = open("assets/frame2.txt", "r")
# text = txt_file.read()
# print(parsePython(text))

# print(re.match(r'^(?!for\b|while\b)\w+\s+\w+', 'for path in video paths'))
# print(re.search(r'^(?!for\b|while\b)\w+\s+\w+', 'aa path in video paths'))

# print('This is asasas asasasasa'.replace(' ', '_', 1))
