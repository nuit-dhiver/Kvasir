import pandas as pd
import modules

task_list = """
1.Explore Dataset
2.Manage Duplicates
3.Dealing with missing Data
4.Import another dataset
100.Quit
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
        modules.explore(df)
        main()
    elif user_task == 2:
        modules.rm_duplicates(df)
        main()
    elif user_task ==3 :
        modules.missing_data(df)
        main()
    elif user_task == 4:
        df = import_df()
        main
    elif user_task == 100:
        print("Come here again.")
        quit()
    else:
        print("Pleas choose a number from list above!")
        main()




def main():
    switch(df)

df = import_df()

while(True):
    main()
    
    