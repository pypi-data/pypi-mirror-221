import os

import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


def generate(invoices_path, pdfs_path, image_path, col1, col2, col3, col4, col5):
    """
    This function converts invoice Excel files into PDF invoices
    :param invoices_path:
    :param pdfs_path:
    :param image_path:
    :param col1:
    :param col2:
    :param col3:
    :param col4:
    :param col5:
    :return:
    """
    filepaths = glob.glob(f'{invoices_path}/*.xlsx')

    for filepath in filepaths:
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        filename = Path(filepath).stem
        invoice_no, date = filename.split("-")

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Invoice no.{invoice_no}")
        pdf.ln()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Date: {date}")
        pdf.ln()

        df = pd.read_excel(filepath, sheet_name='Sheet 1')

        columns = df.columns
        cols = [item.replace("_", " ").title() for item in columns]

        rows = [row for row in df.itertuples(index=False, name=None)]

        col_row_widths = [20, 65, 35, 30, 20]
        col_row_range = range(len(col_row_widths))

        total_sum = df[df.columns[-1]].sum()

        for i, col in zip(col_row_range, cols):
            pdf.set_font("Times", size=10, style="B")
            pdf.cell(w=col_row_widths[i], h=8, txt=f"{col}", border=1)
        pdf.ln()

        for i, row in zip(col_row_range, rows):
            for j, cell in zip(col_row_range, row):
                pdf.set_font("Times", size=10)
                pdf.cell(w=col_row_widths[j], h=8, txt=f"{cell}", border=1)
            pdf.ln()

        for k, cell in zip(col_row_range, range(4)):
            pdf.cell(w=col_row_widths[k], h=8, txt="", border=1)

        pdf.set_font("Times", size=10, style="B")
        pdf.cell(w=col_row_widths[-1], h=8, txt=f"{total_sum}", border=1)
        pdf.ln()

        # Add total sum sentence
        pdf.set_font(family="Times", size=10, style="B")
        pdf.cell(w=50, h=8, txt=f"The total due amount is {total_sum} Euros.")
        pdf.ln()

        # Add company name and logo
        pdf.set_font(family="Times", size=12, style="B")
        pdf.cell(w=25, h=8, txt="PythonHow")
        pdf.image(image_path, w=10)

        if not os.path.exists(pdfs_path):
            os.makedirs(pdfs_path)
        pdf.output(f"{pdfs_path}/{filename}.pdf")