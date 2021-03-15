import pandas as pd
import modules

task_list = """
1- Manage Duplicates
2- Dealing with missing Data
"""

def import_df():
    
    file_path = input("Please specify the path to your excel or csv file: ")
    extension = file_path.split('.')
    
    if extension[-1] == "csv":
        df = pd.read_csv(file_path)
        #df.reset_index(inplace=True)
        return df
    elif extension[-1] == "xlsx" or extension[-1] == "xls":
        df = pd.read_excel(file_path)
        #df.reset_index(inplace=True)
        return df
    else:
        print("Only .csv .xlsx and .xls files are supported.")
        main()
        


def switch(df):

    print(task_list)
    user_task = int(input("What do you want to do?: "))

    if user_task == 1:
        modules.rm_duplicates(df)
        main()
    elif user_task ==2:
        modules.missing_data(df)
        main()
    else:
        print("Pleas choose a number from list above!")
        main()




def main():
    df = import_df()
    switch(df)

while(True):
    main()
    
    