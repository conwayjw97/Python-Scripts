# Use this script to convert between UoG grades and bands.

def chooseConversion():
    print("\n1 - Band to Grade")
    print("2 - Grade to Band")
    print("Other - Exit")
    choice = input("Insert choice: ")
    return choice

grades = ("H", "G2", "G1", "F3", "F2", "F1", "E3", "E2", "E1", "D3", "D2", "D1",
            "C3", "C2", "C1", "B3", "B2", "B1", "A5", "A4", "A3", "A2", "A1")
            
print("Use this script to convert between UoG grades and bands.")
conversionChoice = chooseConversion()
while((conversionChoice == "1") or (conversionChoice == "2")):
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
        else:
            print("Grade invalid.")
    conversionChoice = chooseConversion()
