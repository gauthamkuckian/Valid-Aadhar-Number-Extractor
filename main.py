def FindAadhaar(txt):
    my_file = open(txt, "r")
    data = my_file.read()
    data= data.split()
    a=[]
    for i in range(len(data)-2):
        if (len(data[i])==4 and len(data[i+1])==4 and len(data[i+2])==4):
            a.append(data[i]+" "+data[i+1]+" "+data[i+2])
        if (len(data[i])==8 and len(data[i+1])==4):
            a.append(data[i]+" "+data[i+1])
        if (len(data[i])==12):
            a.append(data[i])

    for i in a:
        if "VID" in i:
            a.remove(i)
#AADHAAR NUMBER NEVER STARTS FROM 0 OR 1
    for i in a:
        if i[0]=='0'or'1':
            a.remove(i)
        
    replace={"B":"8","Z":"2","O":"0","I":"1","l":"1"," ":""}
    for i in range(len(a)):
        for j in replace.keys(): 
            a[i]=a[i].replace(j,replace[j])

    for i in a:
        if any(c.isalpha() for c in i)==True:
            a.remove(i)

#verhoeff algorithm
    mult = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9, 5], [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
            [3, 4, 0, 1, 2, 8, 9, 5, 6, 7], [4, 0, 1, 2, 3, 9, 5, 6, 7, 8], [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
            [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], [7, 6, 5, 9, 8, 2, 1, 0, 4, 3], [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
    perm = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 5, 7, 6, 2, 8, 3, 0, 9, 4], [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
            [8, 9, 1, 6, 0, 4, 3, 5, 2, 7], [9, 4, 5, 3, 1, 2, 6, 8, 7, 0], [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
            [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]

    def Validate(aadharNum):
        try:
            i = len(aadharNum)
            j = 0
            x = 0

            while i > 0:
                i -= 1
                x = mult[x][perm[(j % 8)][int(aadharNum[i])]]
                j += 1
            if x == 0:
                return 1
            else:
                return 0

        except ValueError:
            return 'Invalid Aadhaar Number'
        except IndexError:
            return 'Invalid Aadhaar Number'
    
    count=0
    for i in a:
        if Validate(i)==1:
            return(print("Valid Aadhaar Number found is: "+i[0:4]+" "+i[4:8]+" "+i[8:]))
            count=1
    if count==0:
        return(print("No Valid Aadhaar Number"))
            
#TESTING FUNCTION
FindAadhaar("Sample1.txt")