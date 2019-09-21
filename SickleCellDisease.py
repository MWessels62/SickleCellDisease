#Task 25
#Compulsory Task 1 + 2

#1) The program will read in DNA sequences, and it will translate where 5 particular amino acids appear in the sequence, with the remainder marked as X
#2) Secondly it performs a 'mutation' where lowercase 'a' are found and two new files are created, one where 'a' is converted to 'A' and another where it is converted to 'T'
    #This simulates the effects of the Single Nucleotide Polymorphism that leads to Sickle Cell  disease


def translate(DNASequence):     #This function takes a DNA sequence of any length and converts each codon section into its SLC codes, in other words it returns the amino acid SLC code 
                                #(this is only done for codons I,L,V,F,M, all others are referred to as 'X')
    #Below stores the codons that relate to the first few SLC codes
    SLC_I = ["ATT","ATC","ATA"]
    SLC_L = ["CTT","CTC","CTA","CTG","TTA","TTG"]
    SLC_V = ["GTT","GTC","GTA","GTG"]
    SLC_F = ["TTT","TTC"]
    SLC_M = ["ATG"]

    aminoAcids = "" #initialising the final output variable
    iterations = int(len(DNASequence)/3)    #Determines the number of iterations for the loop (i.e. how many complete codons are present, a codon always has three characters)
                                            #Casting to int means that if the sequence is not divisible by 3 (i.e. there are one or two digits shorts), it will do one fewer iteration

    count = 0
    for i in range(iterations):
        codon = DNASequence[count:count+3]      #Reads in a codon, count:count+3 means that it will review the 3 characters (codon grouping) at a time 
        if codon in SLC_I: aminoAcids += "I"    #if a match is found for the codon it is applied an SLC code otherwise it is assigned the code "X"
        elif codon in SLC_L: aminoAcids += "L"
        elif codon in SLC_V: aminoAcids += "V"
        elif codon in SLC_F: aminoAcids += "F"
        elif codon in SLC_M: aminoAcids += "M"
        else: aminoAcids += "X"
        count += 3  #+3 to skip to the next codon
    return aminoAcids

#Function searches for the lowercase 'a' in the text file and writes the file content to two new files, one where 'a' is changed to 'A', the other where it is converted to 'T'
def mutate():
    f=open('DNA.txt','r')   
    f.read()
    f.seek(0)

    normalDNA = open('normalDNA.txt','w')
    mutatedDNA = open('mutatedDNA.txt','w')

    for lines in f:
        currentLine = lines
        for chars in lines:     #iterates through each character to write to two new files (and convert value if necessary)
            if chars == "a":
                normalDNA.write("A"+"")
                mutatedDNA.write("T"+"")
            else:
                normalDNA.write(chars+"")
                mutatedDNA.write(chars+"")

    f.close()
    normalDNA.close()
    mutatedDNA.close()


#function will read a text file with DNA sequences and pass it to the translate function to convert to SLC codes 
def txtTranslate(userInput):
    if userInput == 2:
        userFile = open('normalDNA.txt', 'r') 
    elif userInput == 3:
        userFile = open('mutatedDNA.txt','r')
    userFile.read()
    userFile.seek(0)
    translation = ""
    for lines in userFile:
        translation += translate(lines) + "\n"      #converts the full line of DNA sequencew
    print("The DNA sequence / amino acid SLC code translation has been completed!")
    userFile.close()
    print ("\n As you can see below the DNA sequence has been translated; the 'I', 'L', 'V', 'F', 'M' characters represent five of the different amino acid SLC codes, 'X' refers to all of the remaining SLC codes\n")
    return translation

print("\n\n")
print("This program converts a DNA sequence to its resulting amino acid SLC codes (for 5 amino acids), and performs a 'mutation' of genes")
print("This mutation simulates the effects of the Single Nucleotide Polymorphism that leads to Sickle Cell  disease\n")
mutate()
userInput = int(input("Type in 1 to read in the original DNA sequence, DNA.txt, 2 to read the translated amino acid codes in normalDNA.txt file or 3 to read the translated amino acid codes with mutatioins in mutatedDNA.txt: "))
print(txtTranslate(userInput)) #Runs the translation of the DNA sequence to the amino acid SLC codes (for five amino acids)

#From what I could see the lowercase 'a' that had to be replaced using the mutate function was an 'extra' character, i.e. it wasnt part of a grouping of 3, 
#Therefore it was excluded from Amino Acid conversions, and also a conversion on both the normalDNA.txt and mutatedDNA.txt would have produced the same results
