""" Question ::
    Print reverse input
    ex. 'I read this book' >> print 'book this read I'
"""

from ast import literal_eval

def inputReverse(sentence):
    rev_input = ""
    text = sentence.split(" ")
    text.reverse()
    
    for x in text:
        rev_input += x
        rev_input += " "

    print("-------------------------------")
    print("Original: ", sentence)
    print("\n")
    print("Reverse: ", rev_input)
    print("-------------------------------")

def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str

s = input ("Enter string :") 
""" print(get_type(s))  """
inputReverse(s)