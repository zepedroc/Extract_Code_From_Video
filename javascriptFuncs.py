import re


# Method that helps translate the text to javascript code
def parseJavascript(text):
    final_text = ''    
    followed_enters = 0

    for line in text.splitlines():
        # remove spaces in the beginning and the end of the line
        new_line = line.strip()

        # if the line is empty, don't even bother parsing it
        if len(line) == 0:
            followed_enters += 1
            # don't add more than one followed enter
            if followed_enters > 1:
                continue
            else:
                final_text += '\n'
                continue

        # remove non-sense expressions like '7)' or 'ad)'
        new_line = re.sub(r'^[0-9A-Za-z]+\)', '', new_line)

        # if the line is not javascript, skip it
        if not javascriptCheck(new_line):
            continue

        # removes the numbers of the editor lines
        new_line = re.sub(r'^[0-9]+\s*', '', new_line)


        new_line = new_line.replace('. ', '.')
        new_line = new_line.replace('fonsole', 'console')
        new_line = new_line.replace('.Log', '.log')
        new_line = new_line.replace('. log', '.log')
        new_line = new_line.replace('. Log', '.log')
        new_line = new_line.replace('og (', 'og(')
        new_line = new_line.replace(') ;', ');')

        final_text += f'{new_line}\n'
        followed_enters = 0

    return final_text



# Method that checks if a string has javascript keywords, function calls or assignments
def javascriptCheck(text):
    if re.match(r'^(var|const|let|if|while|for|else|break|//|import|return|async|await|export)', text):
        return True

     # if it starts or ends with a '=' then it's not javascript
    if re.search(r'^=|=$', text):
        return False

    # if it starts with a ')' and has a word or number after
    if re.search(r'^\)\s\w', text):
        return False   


    if re.search(r'\(|\)|=|\{|\}|\[|\]', text):
        return True

    return False