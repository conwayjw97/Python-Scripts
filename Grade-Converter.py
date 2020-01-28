# Use this script to convert between UoG grades and bands.

def chooseConversion():
    print("\n1 - Band to Grade")
    print("2 - Grade to Band")
    print("3 - Percentage to Grade")
    print("4 - Grade to Percentage")
    print("Other - Exit")
    choice = input("Insert choice: ")
    return choice

grades = ("H", "G2", "G1", "F3", "F2", "F1", "E3", "E2", "E1", "D3", "D2", "D1",
            "C3", "C2", "C1", "B3", "B2", "B1", "A5", "A4", "A3", "A2", "A1")
percentages = ((0, 9), (10, 14), (15, 19), (20, 23), (24, 26), (27, 29), (30, 33),
            (34, 36), (37, 39), (40, 43), (44, 46), (47, 49), (50, 53), (54, 56),
            (57, 59), (60, 63), (64, 66), (67, 69), (70, 73), (74, 78), (79, 84),
            (85, 91), (92, 100))

print("Use this script to convert between UoG grades and bands.")
conversionChoice = chooseConversion()
while((conversionChoice == "1") or (conversionChoice == "2")
        or (conversionChoice == "3") or (conversionChoice == "4")):
    if(conversionChoice == "1"):
        band = int(input("\nBand: "))
        if(band >= 0 and band <= 22):
            print("Corresponding grade:", grades[band])
        else:
            print("Band must be between 0 and 22.")
    elif(conversionChoice == "2"):
        grade = input("\nGrade: ")
        if(grade in grades):
            for i in range(len(grades)):
                if(grades[i] == grade):
                    print("Corresponding band:", i)
                    break
        else:
            print("Grade invalid.")
    elif(conversionChoice == "3"):
        percentage = int(input("\nPercentage: "))
        if(percentage >= 0 and percentage <= 100):
            for i in range(len(percentages)):
                lower = percentages[i][0]
                upper = percentages[i][1]
                if(percentage >= lower and percentage <= upper):
                    print("Corresponding grade:", grades[i])
                    break
        else:
            print("Percentage must be between 0 and 100.")
    elif(conversionChoice == "4"):
        grade = input("\nGrade: ")
        if(grade in grades):
            for i in range(len(grades)):
                if(grades[i] == grade):
                    lower = percentages[i][0]
                    upper = percentages[i][1]
                    print("Corresponding percentage: %d%% - %d%%" % (lower, upper))
                    break
        else:
            print("Grade invalid.")
    conversionChoice = chooseConversion()
