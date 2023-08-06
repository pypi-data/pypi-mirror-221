import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import os


def generate(invoices_path, pdfs_path, image_path, product_id, product_name, amount_purchased, price_per_unit, total_price):
    """This file converts invoices Exel files into PDF invoices """
    file_paths = glob.glob(f"{invoices_path}/*.xlsx")

    for file_path in file_paths:

        pdf = FPDF(orientation="P", unit="mm", format="A4")

        pdf.add_page()
        file_name = Path(file_path).stem
        invoice_number = file_name.split('-')

        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_number[0]}", ln=1)

        pdf.cell(w=50, h=8, txt=f"Date {invoice_number[1]}", ln=1)

        df = pd.read_excel(file_path, sheet_name="Sheet 1")

        # blank line
        pdf.cell(w=0, h=5, txt="", ln=1)

        pdf.set_font(family="Times", size=10, style="B")
        pdf.set_text_color(40, 40, 40)
        columns_name = [name.replace('_', ' ').title() for name in df.columns]
        # Add a header
        pdf.cell(w=10, h=8, txt="-", border=1, align="C")
        pdf.cell(w=30, h=8, txt=columns_name[0], border=1)
        pdf.cell(w=45, h=8, txt=columns_name[1], border=1)
        pdf.cell(w=35, h=8, txt=columns_name[2], border=1)
        pdf.cell(w=30, h=8, txt=columns_name[3], border=1)
        pdf.cell(w=30, h=8, txt=columns_name[4], border=1, ln=1)

        total_prices = df[total_price].sum()
        for index, row in df.iterrows():
            # Add rows to the table
            pdf.set_font(family="Times", size=10)
            pdf.set_text_color(80, 80, 80)
            index_row = str(index + 1)
            pdf.cell(w=10, h=8, txt=index_row, border=1, align="C")
            pdf.cell(w=30, h=8, txt=str(row[product_id]), border=1)
            pdf.cell(w=45, h=8, txt=str(row[product_name]), border=1)
            pdf.cell(w=35, h=8, txt=str(row[amount_purchased]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[price_per_unit]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[total_price]), border=1, ln=1)

        pdf.cell(w=10, h=8, txt="", border=1, align="C")
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=45, h=8, txt="", border=1)
        pdf.cell(w=35, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt=str(total_prices), border=1, ln=1)

        # blank line
        pdf.cell(w=0, h=5, txt="", ln=1)

        # Add total sum sentence
        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=30, h=8,
                 txt=f"The total due amount is {total_prices} Euros.", ln=1)

        # Add Company name and logo
        pdf.cell(w=25, h=8, txt="PythonHow")
        pdf.image(name=image_path, w=8, h=8, type="png")
        
        if not os.path.exists(pdfs_path):
            os.makedirs(pdfs_path)
        pdf.output(f"{pdfs_path}/{file_name}.pdf")
