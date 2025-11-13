import os
from PyPDF2 import PdfMerger

merger = PdfMerger()

pdf_files = [f for f in os.listdir() if f.endswith(".pdf") and f != "combinedPDF.pdf"]

pdf_files.sort(key=lambda x: os.path.getmtime(x))

for file in pdf_files:
    print(f"Merging: {file}")
    merger.append(file)

merger.write("combinedPDF.pdf")
merger.close()

print("Done! Merged", len(pdf_files), "PDFs into combinedPDF.pdf")
