import re

# Method that helps translate the text to python code
def parsePython(text):
    final_text = ''

    for line in text.splitlines():
        # remove multiple spaces
        line = line.strip()

        # don't allow more than one space between
        if len(line) == 0:
            final_text += '\n'
            continue

        new_line = line.replace('inport', 'import')
        new_line = new_line.replace('fron', 'from')
        new_line = new_line.replace('nuspy', 'numpy')
        new_line = new_line.replace('“', '"')
        new_line = new_line.replace('. ', '.')

        # if the line starts with (for,while,if) it needs ':' in the end
        if re.match(r'^(for|while|if|def|try|except|else|elif|finally|with|class)\s', new_line) and new_line[-1] != ':':
            new_line += ':'

        # if the line starts with two words and the first is not (while,from,if,for,import) then there's a missing underscore between them
        elif re.match(r'^(?!for|while|if|from|import|return|def|except|with|class)\w+\s+\w+', new_line):
            new_line = new_line.replace(' ', '_', 1)

        if pythonCheck(new_line):
            final_text += f'{new_line}\n'

    return final_text


# Method that checks if a string has python keywords, function calls or assignments
def pythonCheck(text):
    if re.match(r'^(for|while|if|def|try|except|else|elif|with|continue|break|#|from|import|return|pass|async|await|yield|raise|del|class|global|finally|assert)', text):
        return True

    if re.search(r'\(|=', text):
        return True

    return False
