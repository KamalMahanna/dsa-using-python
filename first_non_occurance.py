def first_non_occurance(s):
    a={}
    b=[]
    for i in s:
        curr_occur = a.get(i,0)

        if curr_occur == 0:
            b.append(i)
        elif curr_occur==1:
            b.remove(i)

        a[i]=curr_occur+1

    return  b[0] if b else -1