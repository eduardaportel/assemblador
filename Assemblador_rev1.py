file1 = open('C:\\Users\\edbrag\\OneDrive - SAS\Desktop\\Git\\Maua\\Arquitetura\\Assemblador\\codigo7.txt', 'r')
Lines = file1.readlines()

result = open('C:\\Users\\edbrag\\OneDrive - SAS\Desktop\\Git\\Maua\\Arquitetura\\Assemblador\\asmimt.cdm', 'w')

conversion = {"HLT":" : 00",
              "STO":" : 1",
              "LD":" : 2",
              "LDI":" : 3",
              "ADD":" : 4",
              "ADDI":" : 5",
              "SUB":" : 6",
              "SUBI":" : 7",
              "JUMP":" : 8",
              "NOP":" : 9"}

count = 0
n = 0
# Strips the newline character
for line in Lines:
    try:
        split = line.strip().split(" ")

        if len(split[1]) == 1:
            s = "00" + split[1]
        elif len(split[1]) == 2:
            s = "0" + split[1]
        else:
            s = split[1]
        
        result.write(str(hex(n)).upper()[2:] + conversion[split[0].upper()] + s + "\n")
        print(line.strip())
        n = n+1
    except:
        pass
result.close()
