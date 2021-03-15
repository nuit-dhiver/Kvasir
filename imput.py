import numpy as np

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

    df[imput_column] = df[imput_column].replace({',':''}, regex=True)
    df[imput_column] = df[imput_column].replace({'NAN':np.nan}).astype(float)
    
    if m_imputation_methode == 1:
        df[imput_column] = df[imput_column].fillna(value=df[imput_column].mean())
        print("Values in " + imput_column + " imputed with mean values of the columns")
    elif m_imputation_methode == 2:
        df[imput_column] = df[imput_column].fillna(value=df[imput_column].median())
        print("Values in " + imput_column + " imputed with median values of the columns")
    elif m_imputation_methode == 3:
        df[imput_column] = df[imput_column].fillna(value=df[imput_column].mode())
        print("Values in " + imput_column + " imputed with mode values of the columns")
    else:
        print("Please choose a number from above: ")
        m_imputation(df)
    

    print(df.isna().sum())
    another_column = input("Do you want to imput another column?(y/n): ")
    if another_column.capitalize() == "Y":
        m_imputation(df)
    else:
        export_path = input("Please Specify path to new csv file: ")
        df.to_csv(export_path, index=False)

    
