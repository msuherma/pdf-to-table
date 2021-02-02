'''
Converting Tables in PDF into csv
by Mukhamad Suhermanto

This code is used to convert table in PDF file into csv format
'''

from tabula import read_pdf
import pandas as pd

pdfFileName = input("Enter your file name here:")
pdfFolderName = input("Enter your folder name where the PDF from here:")
pageNum = input("Enter the page number where the table you want to extract is, here:")
pageNum = int(pageNum)
'''
def pdf2table(pdfFileName, pdfFolderName, pageNum):
    read_pdf(pdfFolderName/pdfFileName+".pdf", pages= pageNum)
    input("Enter the csv file name you want to save:")
    input("Enter the name of the folder where you want to save your created csv file:")
    return df_idn.to_csv(csvFolderName/csvFileName+".csv", index = False)

'''
df = read_pdf(pdfFolderName+"/"+pdfFileName+".pdf", pages= pageNum)
df = pd(df)
csvFileName = input("Enter the csv file name you want to save:")
csvFolderName = input("Enter the name of the folder where you want to save your created csv file:")
df.to_csv(csvFolderName+"/"+csvFileName+".csv", index = False)