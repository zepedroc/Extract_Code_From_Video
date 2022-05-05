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
        if re.match(r'^(for|while|if|def|try|except|else|elif)\s', new_line) and new_line[-1] != ':':
            new_line += ':'

        # if the line starts with two words and the first is not (while,from,if,for,import) then there's a missing underscore between them
        elif re.match(r'^(?!for|while|if|from|import|return|def|except)\w+\s+\w+', new_line):
            new_line = new_line.replace(' ', '_', 1)

        final_text += f'{new_line}\n'

    return final_text
