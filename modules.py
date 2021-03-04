


def rm_duplicates(df):
    subset_status = str(input("Do you want to specify a subset of columns?(Y/N):"))
    print(df)
    if subset_status.capitalize() == "N":
        num_of_duplicates = str(df.duplicated().count())
        print("There is " + num_of_duplicates + " duplicated rows.\n")
        remove_or_not = str(input("Do you want to remove them?:"))
        if remove_or_not.capitalize() == "Y":
            df.drop_duplicates(inplace = True)
            print(num_of_duplicates + "rows removed")
            export_path = input("Please Specify path to new csv file")
            df.to_csv(export_path)
        else:
            print("Okay!")
    elif subset_status.capitalize == "Y":
        raw_subset = input("Specify your subset of columns. delimit them by ,:")



