import tabula
from tabula import read_pdf
import pandas as pd
tables3=read_pdf("D:\\camelot_pdf_extract\\India.pdf",pages='4')

# creating data frame
first_table=tables3[0]

# spiltting the colums
nfhs5_split=first_table['NFHS-5'].str.split(' ', expand=True)

#storing the relevant columns
Col1=nfhs5_split[0]
col2=nfhs5_split[2]
col3=nfhs5_split[4]

# entering data manually for disoriented rows
col2[0,]="(2019-21)"
col2[1,]="Rural"

col3[0,]="(2019-21)"
col3[1,]="Total"

nfhs_final = pd.concat([first_table.reset_index(drop=True), Col1,col2,col3], axis=1)

nfhs_final.rename(columns={'0': 'NFHS-5', '2': 'NFHS-5', '4': 'NFHS-5'}, inplace=True)

nfhs_final.to_csv("India2.csv")