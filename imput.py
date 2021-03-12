#import numpy as np

def main(df):

    imputation_methode = int(input("""which methode of imputation do you want to use?
    1.Mean/Median/Mode
    (No other imputation methode is supported at the time.)
    Please Specify the number :
    """))

    if imputation_methode == 1:
        m_imputation(df)
    else:
        print("Please choose a number from above: ")
        main(df)

def m_imputation(df):

    imput_column = input("Please specify a column: ")

    m_imputation_methode = int(input("""which methode of imputation do you want to use?
    1.Mean imputation
    2.Median imputation
    3.Mode imputation
    Specify the number:
    """))
    
    if m_imputation_methode == 1:
        df[imput_column] = df[imput_column].fillna(value=df[imput_column].mean())
    elif m_imputation_methode == 2:
        df[imput_column] = df[imput_column].fillna(value=df[imput_column].median())
    elif m_imputation_methode == 3:
        df[imput_column] = df[imput_column].fillna(value=df[imput_column].mode())
    else:
        print("Please choose a number from above: ")
        m_imputation(df)

    another_column = input("Missing values imputed with mean value of the column, do you want to imput another column?(yes/no): ")
    if another_column.capitalize == "YES":
        m_imputation(df)
    else:
        export_path = input("Please Specify path to new csv file: ")
        df.to_csv(export_path)
