def PSC():
    # Explain purpose and use of Calculator
    print(
        "This Punnet Square Calculator determines the Genotypes and Phenotypes for a given set of parent alleles. This includes when one allele for each parent is present, when two alleles for the same gene from each parent are present and when two alleles from two different genes are present for each parent. When inputing more than one gene, the genes must correspond for each parent!")
    # Ask for input of Maternal and Paternal Genotypes
    mGeno = input("What is the Maternal Genotype?")
    fGeno = input("What is the Paternal Genotype?")

    # Create List for offspring
    offGeno = []
    offDihyb = []
    MdiHyblist = []
    FdiHyblist = []

    # Combine Parental Genotypes with Consideration for length
    if len(mGeno) == 1:
        for i in range(len(mGeno)):
            offGeno.append(mGeno[i] + fGeno[0])

    elif len(mGeno) == 2:
        for i in range(len(mGeno)):
            offGeno.append(mGeno[i] + fGeno[0])
            offGeno.append(mGeno[i] + fGeno[1])

    elif len(mGeno) == 4:
        MdiHyblist.append(mGeno[0] + mGeno[2])
        MdiHyblist.append(mGeno[0] + mGeno[3])
        MdiHyblist.append(mGeno[1] + mGeno[2])
        MdiHyblist.append(mGeno[1] + mGeno[3])
        FdiHyblist.append(fGeno[0] + fGeno[2])
        FdiHyblist.append(fGeno[0] + fGeno[3])
        FdiHyblist.append(fGeno[1] + fGeno[2])
        FdiHyblist.append(fGeno[1] + fGeno[3])
        for i in range(len(MdiHyblist)):
            offDihyb.append(MdiHyblist[i] + FdiHyblist[0])
            offDihyb.append(MdiHyblist[i] + FdiHyblist[1])
            offDihyb.append(MdiHyblist[i] + FdiHyblist[2])
            offDihyb.append(MdiHyblist[i] + FdiHyblist[3])

    # Determine Phenotype for 1 Allele or a gene from each Parent
    GenoCap = 0
    if len(mGeno) == 1:
        Trait1 = offGeno[0]
        Pheno = Trait1[0]
        if Trait1[0].isupper() or Trait1[1].isupper():
            GenoCap = GenoCap + 1
    if GenoCap > 0:
        Pheno = Pheno.upper()
    elif GenoCap < 0:
        Pheno = Pheno.lower()

    # Determine Offspring Phenotypes for when two alleles for a single gene from each parent are inputted
    if len(mGeno) == 2:
        offGenoElem1 = offGeno[0]
        offGenoElem2 = offGeno[1]
        offGenoElem3 = offGeno[2]
        offGenoElem4 = offGeno[3]
        if offGenoElem1[0].isupper() or offGenoElem1[1].isupper():
            GenoCap = GenoCap + 1
        elif offGenoElem2[0].isupper() or offGenoElem2[1].isupper():
            GenoCap = GenoCap + 1
        elif offGenoElem3[0].isupper() or offGenoElem3[1].isupper():
            GenoCap = GenoCap + 1
        elif offGenoElem4[0].isupper() or offGenoElem4[1].isupper():
            GenoCap = GenoCap + 1

    # Determine Phenotypes for Dihybrid Cross
    if len(mGeno) == 4:
        A = mGeno[0].capitalize()
        a = mGeno[0].lower()
        B = mGeno[2].capitalize()
        b = mGeno[2].lower()
        AB = 0
        aB = 0
        Ab = 0
        ab = 0
        for i in range(len(offDihyb)):
            if offDihyb[i].count(A) >= 1 and offDihyb[i].count(B) >= 1:
                AB = AB + 1
            elif offDihyb[i].count(A) == 0 and offDihyb[i].count(B) >= 1:
                aB = aB + 1
            elif offDihyb[i].count(A) >= 1 and offDihyb[i].count(B) == 0:
                Ab = Ab + 1
            elif offDihyb[i].count(A) == 0 and offDihyb[i].count(B) == 0:
                ab = ab + 1

    # Print Genotypes
    print("The Maternal Genotype is " + mGeno)
    print("The Paternal Genotype is " + fGeno)

    # What to print in case of 1 Allele from each Parent
    if len(mGeno) == 1:
        print("The offspring Genotype will be " + str(offGeno))
        print("The Offspring Phenotype will be " + Pheno)

    # What to print in case of 2 alleles for s single gene from each parent
    elif len(mGeno) == 2:
        print("The potential Genotypes for the Offspring are " + str(offGeno))
        print("The number of potential Offspring with the Dominant trait will be " + str(
            GenoCap) + " out of 4" + " (" + str((GenoCap / 4) * 100) + "%)")
        print("The number of potential Offspring with the Recessive trait will be " + str(
            4 - GenoCap) + " out of 4" + " (" + str(((4 - GenoCap) / 4) * 100) + "%)")

    # What to print in case of Dihybrid Cross
    elif len(mGeno) == 4:
        print("The potential Genotypes for the Offspring are " + str(offDihyb))
        print("The phenotypes for the potential offspring are: ")
        print(str(A + B) + "=" + str(AB) + "(" + str((AB / len(offDihyb)) * 100) + "%)")
        print(str(A + b) + "=" + str(Ab) + "(" + str((Ab / len(offDihyb)) * 100) + "%)")
        print(str(a + B) + "=" + str(aB) + "(" + str((aB / len(offDihyb)) * 100) + "%)")
        print(str(a + b) + "=" + str(ab) + "(" + str((ab / len(offDihyb)) * 100) + "%)")
    restart = input("Would you like to enter new Parental Genotypes?")
    if restart == "yes" or restart == "y":
        PSC()
    if restart == "n" or restart == "no":
        print
        "Script terminating. Goodbye."


PSC()
