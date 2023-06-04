def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
        
    punctuations = ['.', '?',':'
    lines = text.splitlines()
    output = []
    
    for line in lines:
        line = line.strip()  # Remove leading and trailing whitespace
        if line.endswith(tuple(punctuations)):
            output.append(line + '\n\n')
        else:
            output.append(line + '\n')
