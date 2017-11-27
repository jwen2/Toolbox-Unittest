def remove_neg(listofnegs):
    newlist = []
    for number in listofnegs:
        if number >= 0:
            newlist.append(number)
    return newlist

def longername(name1,name2):
    if len(name1) == len(name2):
        return 'They are they same length'
    else:
        if len(name1) > len(name2):
            return name1
        else:
            return name2
