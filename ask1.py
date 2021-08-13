#   Thomas Patsanis, A.M: 3318
#
#   1 Ergasthriakh Askhsh
#   Version: Python 3.8.5
#   How to run:
#   python3 ask1.py
#   Then follow menu instructions
#
#
from join import merge_join
from union import union
from intersection import intersect
from difference import set_difference
from groupby import group_by_and_sum


#open all files that program needs
def get_files():
    files = []
    file_1 = open("R_sorted.tsv", "r")
    file_2 = open("S_sorted.tsv", "r")
    file_3 = open("R.tsv", "r")
    files.append(file_1)
    files.append(file_2)
    files.append(file_3)
    return files


#simple "ui" for running all Algorithms
def show_menu():
    menu = "\nAPPLICATION MENU\n\n1: Join\n\n2: Union\n\n3: Intersection\n\n4: Set Difference\n\n5: Group By & Sum\n\n0: Exit\n"
    print(menu)
    selection = input("Choose a number from above: ");

    while(selection != '0'):
        files = get_files()
        if selection=='1':
            print("***Executing Join Algorithm***")
            merge_join(files[0],files[1])
            print("\nDone!")
        elif selection=='2':
            print("***Executing Union Algorithm***")
            union(files[0],files[1])
            print("\nDone!")
        elif selection=='3':
            print("***Executing Intersection Algorithm***")
            intersect(files[0],files[1])
            print("\nDone!")
        elif selection=='4':
            print("***Executing Set Difference Algorithm***")
            set_difference(files[0],files[1])
            print("\nDone!")
        elif selection=='5':
            print("***Executing Group By & Sum Algorithm***")
            group_by_and_sum(files[2])
            print("\nDone!")

        rerun = input("\nPress 0 for exit or anything for menu: ")
        if rerun=='0':
            selection = '0'
        else:
            print("\n")
            print(menu)
            selection = input("Choose a number from above: ");
        if selection=='0':
            for file in files:
                file.close()
            print("\nTerminating Program...")


def main():
    show_menu()


if __name__ == '__main__':
    main()
