import pandas as pd
import modules

task_list = """
1- Manage Duplicates
2- Remove NULL
"""

def import_df():

    csv_path = input("Please specify the path to you csv file:")
    df = pd.read_csv(csv_path)
    df.reset_index(inplace = True)
    return df


def switch():

    print(task_list)
    user_task = int(input("What do you want to do?"))

    if user_task == 1:
        modules.rm_duplicates(import_df())
        main()
    else:
        print("Pleas choose a number from list above!")
        main()




def main():
    #import_df()
    switch()

while(True):
    main()
    
    