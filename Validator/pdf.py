from fpdf import FPDF

#take save path, dictionary, project name
class PDF(FPDF):

    def header(self):
        
        self.set_font('Arial', 'B', 20)
        # Move to the right
        # self.cell(80)
        # Title

        self.set_text_color(1,1,0)
        self.text( 10,20,'12 FACTOR CC REPORT')
        self.line(10,25,200,25)
        # Line break
        # self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class
pdf = PDF()
# pdf.alias_nb_pages()
# pdf.add_page()
# pdf.set_font('Times', '', 12)

pdf.output('s.pdf')