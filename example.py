binip = input("Enter IP address in binary format:")
fcell = int(binip[:8], 2)
x = binip.split('.')

if fcell >= 1 and fcell <= 126:
    print("Class A")
    print(f"Network address :{x[0]}.0.0.0")
    print(f"Net id :{x[0]}")
    print(f"Host address : 0.{x[1]}.{x[2]}.{x[3]}")
    print(f"Host ID : {x[1]}.{x[2]}.{x[3]}")
    print(f"First address : {x[0]}.0.0.0")
    print(f"Last address : {x[0]}.255.255.255")
    print(f"Total number of address : {255*255*255}")

elif fcell >= 128 and fcell <= 191:
    print("Class B")
    print(f"Network address : {x[0]}.{x[1]}.0.0")
    print(f"Net id : {x[0]}.{x[1]}")
    print(f"Host address : 0.0.{x[2]}.{x[3]}")
    print(f"Host ID : {x[2]}.{x[3]}")
    print(f"First address : {x[0]}.{x[1]}.0.0")
    print(f"Last address : {x[0]}.{x[1]}.255.255")
    print(f"Total number of address : {255*255}")

elif fcell >= 192 and fcell <= 223:
    print("Class C")
    print(f"Network address : {x[0]}.{x[1]}.{x[2]}.0")
    print(f"Net id : {x[0]}.{x[1]}.{x[2]}")
    print(f"Host address : 0.0.0.{x[3]}")
    print(f"Host ID : {x[3]}")
    print(f"First address : {x[0]}.{x[1]}.{x[2]}.0")
    print(f"Last address : {x[0]}.{x[1]}.{x[2]}.255")
    print(f"Total number of address : {255}")
elif fcell >= 224 and fcell <= 239:
    print("Class D")
    print("No network address for class D")
    print("No net ID")
    print("No host address for class D")
    print("No host ID")
    print("First address and Last address not available")
    
elif fcell >= 240 and fcell <= 255:
    print("Class E")
    print("No network address available for class E")
    print("No net ID available")
    print("No host address available for class D")
    print("No host ID available")
    print("First address and Last address not available")
else:
    print("Invalid IP Address")
    
n = int(input("Enter the custom masking value:"))   
i = 0
b = 0
if n >= 0 and n <=32:
    if(n >= 24):
        i = n - 24
        for a in range(i):
            b = b + pow(2,7 - a)
        print(f"255.255.255.{str(b)}")
    
    elif(n >= 16):
        i = n - 16
        for a in range(i):
            b = b + pow(2,7 - a)
        print(f"255.255.{str(b)}.0")
    
    elif(n >= 8):
        i = n - 8
        for a in range(i):
            b = b + pow(2,7 - a)
        print(f"255.{str(b)}.0.0")
        
    elif(n <= 8):
        i = n 
        for a in range(i):
            b = b + pow(2,7 - a)
        print(f"{str(b)}.0.0.0")
else:
    print("Invalid Masking Value!!!")
    