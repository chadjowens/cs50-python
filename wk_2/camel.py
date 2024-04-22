def main():
    # ltr = ""
    name = input(("camelCase: "))
    # while ltr in name.isupper():
    #     convert(name, ltr)
    # else:
    #     print("done")
    for ltr in name:
      if ltr.isupper():
        indx = []
        print("Type of indx:", type(indx))
        print("Index is:", name.index(ltr))
        indx = indx.append(ltr)
        # indx = name.index(ltr)
        print("Values of indx:", indx)
        print("Type of indx:", type(indx))
        # print("Size of indx:", len(indx))
        convert(name, ltr)

    #   else:
    #      print("-")
        #  convert

        # convert(name, ltr)

def convert(name, ltr):
    print("camelCase: " + name)
#     # for ltr in name:
#     #   if ltr.isupper():
#     indx = int(name.index(ltr))
#     wrd1 = name[0:indx]
#     wrd2 = name[indx:].lower()
#     print('snake_case: '+ wrd1+'_'+ wrd2)

    # ltr = ""
    # while ltr.isupper() in name == True:
    #   # if ltr.isupper():
    #     indx = int(name.index(ltr))
    #     wrd1 = name[0:indx]
    #     wrd2 = name[indx:].lower()
    #     print('snake_case: '+ wrd1+'_'+ wrd2)
    #     continue
    # else:
    #     print('error')

main()