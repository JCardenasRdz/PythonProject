import string
punctuations = set(string.punctuation)

def cleanup(raw_text):
    cleaned_up = ""
    for char in raw_text:
       if char not in punctuations:
           cleaned_up = cleaned_up + char
    return cleaned_up