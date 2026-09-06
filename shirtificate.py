from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 40)
        self.cell(0, 30, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")


def main():
    name = input("Name: ")
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x=10, y=70, w=190)
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=55, y=140, text=f"{name} took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
