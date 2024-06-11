import PyPDF2

# Open the PDF file in binary mode
with open('first.pdf', 'rb') as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)
    
    # Get the number of pages in the PDF
    num_pages = len(reader.pages)
    print(num_pages)
    
    # Get the first page of the PDF
    page = reader.pages[0]
    
    # Rotate the page clockwise by 90 degrees
    page.rotate(90)
    
    # Create a PDF writer object
    writer = PyPDF2.PdfWriter()
    
    # Add the rotated page to the writer object
    writer.add_page(page)
    
    # Write the rotated page to a new PDF file
    with open("rotated.pdf", "wb") as output:
        writer.write(output)
