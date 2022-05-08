import re

# Method that helps translate the text to python code
def parsePython(text):
    final_text = ''
    followed_enters = 0

    for line in text.splitlines():
        # remove spaces in the beginning and the end of the line
        line = line.strip()

        # if the line is empty, don't even bother parsing it
        if len(line) == 0:
            followed_enters += 1
            # don't add more than one followed enter
            if followed_enters > 1:
                continue
            else:
                final_text += '\n'
                continue

        new_line = line.replace('inport', 'import')
        new_line = new_line.replace('fron', 'from')

        # if the line is not python, skip it
        if not pythonCheck(new_line):
            continue

        new_line = new_line.replace('nuspy', 'numpy')
        new_line = new_line.replace('“', '"')
        new_line = new_line.replace('. ', '.')

        # if the line starts with (for,while,if) it needs ':' in the end
        if re.match(r'^(for|while|if|def|try|except|else|elif|finally|with|class)\s', new_line) and new_line[-1] != ':':
            new_line += ':'

        # if the line starts with two words and the first is not (while,from,if,for,import) then there's a missing underscore between them
        elif re.match(r'^(?!for|while|if|from|import|return|def|except|with|class)\w+\s+\w+', new_line):
            new_line = new_line.replace(' ', '_', 1)

        final_text += f'{new_line}\n'
        followed_enters = 0

    return final_text


# Method that checks if a string has python keywords, function calls or assignments
def pythonCheck(text):
    if re.search(r'^(for|while|if|def|try|except|else|elif|with|continue|break|#|from|import|return|pass|async|await|yield|raise|del|class|global|finally|assert)', text):
        return True

    # if it starts with a '(' then it's not python
    if re.search(r'^\(', text):
        return False

     # if it starts or ends with a '=' then it's not python
    if re.search(r'^=|=$', text):
        return False

    if re.search(r'\(|=', text):
        return True

    return False

