# # importing modules 
# from reportlab.pdfgen import canvas 
# from reportlab.pdfbase.ttfonts import TTFont 
# from reportlab.pdfbase import pdfmetrics 
# from reportlab.lib import colors 

# # initializing variables with values 
# fileName = 'sample.pdf'
# documentTitle = 'sample'
# title = 'Technology'
# subTitle = 'The largest thing now!!'
# textLines = [ 
# 	'Technology makes us aware of', 
# 	'the world around us.', 
# ] 
# image = 'test.png'

# # creating a pdf object 
# pdf = canvas.Canvas(fileName) 

# # setting the title of the document 
# pdf.setTitle(documentTitle) 

# # registering a external font in python 
# pdfmetrics.registerFont( 
# 	TTFont('abc', 'OpenSans-VariableFont_wdth,wght.ttf') 
# ) 

# # creating the title by setting it's font 
# # and putting it on the canvas 
# pdf.setFont('abc', 36) 
# pdf.drawCentredString(300, 770, title) 

# # creating the subtitle by setting it's font, 
# # colour and putting it on the canvas 
# pdf.setFillColorRGB(0, 0, 255) 
# pdf.setFont("Courier-Bold", 24) 
# pdf.drawCentredString(290, 720, subTitle) 

# # drawing a line 
# pdf.line(30, 710, 550, 710) 

# # creating a multiline text using 
# # textline and for loop 
# text = pdf.beginText(40, 680) 
# text.setFont("Courier", 18) 
# text.setFillColor(colors.red) 
# for line in textLines: 
# 	text.textLine(line) 
# pdf.drawText(text) 

# # drawing a image at the 
# # specified (x.y) position 
# # pdf.drawInlineImage(image, 130, 400) 

# # saving the pdf 
# pdf.save() 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch

def create_enhanced_pdf(output_path, image_path):
    # Create a canvas for the PDF
    pdf = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter  # Letter page dimensions

    # Set PDF metadata
    pdf.setTitle("Enhanced Beautiful PDF Document")
    pdf.setAuthor("Your Name")
    pdf.setSubject("Enhanced Python PDF Example")
    pdf.setKeywords("Python, ReportLab, PDF, Enhanced, Image, Text")

    # Add a background color to the page
    pdf.setFillColor(colors.lightblue)
    pdf.rect(0, 0, width, height, fill=1)

    # Add a white panel for content
    pdf.setFillColor(colors.white)
    pdf.rect(40, 40, width - 80, height - 80, fill=1, stroke=0)

    # Add a decorative title with border
    pdf.setFont("Helvetica-Bold", 24)
    pdf.setFillColor(colors.darkblue)
    pdf.drawCentredString(width / 2, height - 60, "Enhanced Beautiful PDF Document")

    # Add a subtitle
    pdf.setFont("Helvetica-Oblique", 14)
    pdf.setFillColor(colors.gray)
    pdf.drawCentredString(width / 2, height - 90, "Generated with Python and ReportLab")

    # Draw a line below the title
    pdf.setStrokeColor(colors.darkblue)
    pdf.setLineWidth(1)
    pdf.line(50, height - 100, width - 50, height - 100)

    # Add some body text with padding
    pdf.setFont("Helvetica", 12)
    pdf.setFillColor(colors.black)
    text_lines = [
        "Welcome to this beautifully enhanced PDF document.",
        "This version includes an elegant layout with backgrounds and borders.",
        "",
        "Features included in this version:",
        "- A decorative title with borders",
        "- Embedded image with a frame",
        "- Improved text layout and spacing",
        "- Background colors for better aesthetics",
        "",
        "Python makes it easy to create professional PDFs!"
    ]

    text_x = 60
    text_y = height - 140
    for line in text_lines:
        pdf.drawString(text_x, text_y, line)
        text_y -= 15  # Adjust line spacing

    # Add an image with a border
    image_width = 4 * inch
    image_height = 3 * inch
    image_x = (width - image_width) / 2  # Center the image
    image_y = height - 400  # Adjust vertical position

    # Draw a border for the image
    pdf.setStrokeColor(colors.darkblue)
    pdf.setLineWidth(2)
    pdf.rect(image_x - 5, image_y - 5, image_width + 10, image_height + 10, fill=0)

    # Draw the image
    pdf.drawImage(image_path, image_x, image_y, width=image_width, height=image_height)

    # Add a footer
    pdf.setFont("Helvetica", 10)
    pdf.setFillColor(colors.darkgray)
    pdf.drawCentredString(width / 2, 30, "Generated using Python | Enhanced ReportLab Example")

    # Save the PDF
    pdf.save()

# Example usage
output_pdf = "enhanced_beautiful_document.pdf"
image_file = "test.png"  # Use the uploaded image file path
create_enhanced_pdf(output_pdf, image_file)

print(f"Enhanced PDF successfully created: {output_pdf}")
