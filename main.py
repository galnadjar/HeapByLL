import constants
import foreignList
import sortedList
import unsortedList

#handles getting the users choice of list from the console
def get_cons_list_type():

    listType = ""
    while listType == "":
        print("Which type of list do you choose,options are:\n 1- Sorted\n 2- UnSorted\n 3- Foreign")
        userInput = int(input("Please enter your choice: "))
        print()

        if userInput == 1:
            listType = "Sorted"

        elif userInput == 2:
            listType = "UnSorted"

        elif userInput == 3:
            listType = "Foreign"

        else:
            print("theres no such type of list, please try again")

    return listType


#handles the file opening and close, and also returning its info
def file_open():
    file = None

    while file is None:
        fileName = input("Please specify the correct file name: ")
        fileName += ".txt"
        try:
            with open(fileName) as f:
                file = f.readlines()

        except FileNotFoundError:
            print("input file given is not valid\n")

    return file


def main():

    textStartWrap = "\n \x1b[4m" + "\033[1m"
    textEndWrap = "\033[0m" + "\x1b[24m \n"
    file = None
    fileInd = 0
    listType = 0


    print("Select your input source ,options are:\n 1- File\n 2- Console ")
    inputSrc = int(input("Please enter your choice: "))
    print(textStartWrap + "Source chosen was Option " + str(inputSrc) + textEndWrap )

    #User Input for the type of list


    if inputSrc == constants.FILE_SOURCE: #file Option
        file = file_open()
        listTypeInput = file[fileInd].rstrip()
        fileInd += 1

    else: #console Option
        listTypeInput = get_cons_list_type()


    if listTypeInput == "Sorted":
        listType = constants.SORTED_LIST

    elif listTypeInput == "UnSorted":
        listType = constants.UNSORTED_LIST

    elif listTypeInput == "Foreign":
        listType = constants.FOREIGN_LIST


    listOfLists = []

    print(textStartWrap + listTypeInput + " list has been selected" + textEndWrap)

    #Getting user input for type of operation and operating it until EOF or exit command is given
    while True:

        if inputSrc == constants.FILE_SOURCE:
            try:
                opTypeInput = file[fileInd].rstrip()
                fileInd += 1
            except (IndexError, EOFError):
                break

        #case input source is from console
        else:
            print("Select the type of operation you want to use,options are: MakeHeap,Insert,Union,ExtractMin,Minimum or exit to quit")
            opTypeInput = input("Please enter your choice: ")



        if opTypeInput == "MakeHeap":

            if listType == constants.SORTED_LIST: Lst = sortedList.SortedList()

            elif listType == constants.UNSORTED_LIST: Lst = unsortedList.UnSortedList()

            else: Lst = foreignList.ForeignList()

            listOfLists.append(Lst)
            print("A new Heap has been created")


        elif "Insert" in opTypeInput:
            listOfLists[-1].insert(int(opTypeInput.split(" ")[-1]))
            listOfLists[-1].print()



        elif opTypeInput == "ExtractMin":
            print(str(listOfLists[-1].extract_min()) + " has been extracted")
            listOfLists[-1].print()

        elif opTypeInput == "Minimum":
            print("The heap current minimum : " + str(listOfLists[-1].minimum()))

        elif opTypeInput == "Union":
            Lst = listOfLists.pop(-1)
            newLst = Lst.union(listOfLists[-1])
            listOfLists.append(newLst)
            print("Sets have been Unionised")
            newLst.print()

        elif opTypeInput == "exit":
            break
        print()


if __name__ == '__main__':
    main()
