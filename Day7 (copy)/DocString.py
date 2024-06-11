# to document the python code in python we have one package called docstring
# to define docstring use triple quotes
# also we need blank line after one line

# """One line description.

#    A more detailed explanation
# """


"""This module provides functions to convert a PDF to text"""


def convert(path):
    """ 
    Convert the given PDF to text

    Parameters:
    path(str): The path to a PDF file.

    Returns:
    str: The content of the PDF file as text.
    """
    print("pdf2text")
