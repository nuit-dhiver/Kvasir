


def rm_duplicates(df):

    subset_status = str(input("Do you want to specify a subset of columns?(Y/N): "))
    
    if subset_status.capitalize() == "N":

        num_of_duplicates = str(df.duplicated().sum())
        print("There is " + num_of_duplicates + " duplicated rows.\n")
        remove_or_not = str(input("Do you want to remove them?(Y/N): "))

        if remove_or_not.capitalize() == "Y":
            df.drop_duplicates(inplace = True)
            print(num_of_duplicates + "rows removed")
            export_path = input("Please Specify path to new csv file: ")
            df.to_csv(export_path)

        else:
            print("Okay!")
            main()

    elif subset_status.capitalize == "Y":

        raw_subset = input("Specify your subset of columns. delimit them by ,:")
        subset = raw_subset.split(",")
        num_of_duplicates = str(df.duplicated(subset = subset).sum())
        print("There is " + num_of_duplicates + " duplicated rows.\n")
        remove_or_not = str(input("Do you want to remove them?(Y/N): "))

        if remove_or_not.capitalize() == "Y":
            df.drop_duplicates(subset = subset, inplace = True)
            print(num_of_duplicates + "rows removed")
            export_path = input("Please Specify path to new csv file: ")
            df.to_csv(export_path)

        else:
            print("Okay!")
            main()
        
    else:
        print("Input is incorrct.")
        main()





