def Add(x):
    if " " in x:
        raise ValueError
    if ",\n" in x or "\n," in x:
        raise ValueError
    if x.endswith(",") or x.endswith("\n"):
        raise ValueError
    x=x.replace("\n",",")
    if x=="":
        return 0;
    numbers=x.split(",")
    if len(numbers)==1:
        return int(numbers[0])
    else:
        total=0
        for i in numbers:
            total+=int(i)
        return total