def swapFileData():
    file1 = input("Enter The File Name")
    file2 = input("Enter The File Name")
    data_A = open(file1,'r')
    data_b = open(file2,'r')
    with open(file1,'w') as f:
        f.write("hi, my name is saumya")
    with open(file2,'w')as f:
        f.write("hi, my name is hem")
    
swapFileData()