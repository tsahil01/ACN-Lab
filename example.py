def get_ip_class(binary_ip):
    first_octet = int(binary_ip[:8], 2)

    if first_octet >= 1 and first_octet <= 126:
        return 'Class A'
    elif first_octet >= 128 and first_octet <= 191:
        return 'Class B'
    elif first_octet >= 192 and first_octet <= 223:
        return 'Class C'
    elif first_octet >= 224 and first_octet <= 239:
        return 'Class D'
    elif first_octet >= 240 and first_octet <= 255:
        return 'Class E'
    else:
        return 'Invalid IP Address'

binary_ip = input("Enter IP address in binary format (e.g., 11000000.10101000.00000001.00000001): ")
ip_class = get_ip_class(binary_ip)
print("IP Class:", ip_class)

inp = input("Enter new ip address ")
x = inp.split('.')

if(int(x[0])>=1 and int(x[0])<=126):
    print(f"Network address :{x[0]}.0.0.0")
    print(f"Net id :{x[0]}")
    print(f"Host address : 0.{x[1]}.{x[2]}.{x[3]})
    print("Host ID : ", x[1]+"."+x[2]+"."+x[3])
    print("First address : ",x[0] + ".0.0.0")
    print("Last address : ",x[0]+"."+"255.255.255")
    print("Total number of address : ", 255*255*255)

elif (int(x[0])>=128 and int(x[0])<=191):
    print("Network address : ", x[0] +"."+ x[1]+".0.0")
    print("Net id : ",x[0]+"."+x[1])
    print("Host address : 0.0"+"."+x[2]+"."+x[3])
    print("Host ID : ", +x[2]+"."+x[3])
    print("First address : ",x[0] +"."+ x[1]+".0.0")
    print("Last address : ",x[0]+"."+x[1]+"."+"255.255")
    print("Total number of address : ", 255*255)

elif(int(x[0])>=192 and int(x[0])<=223):
    print("Network address : ", x[0] +"."+ x[1]+"."+ x[2]+"."+"0")
    print("Net id : ",x[0]+"."+x[1]+"."+x[2])
    print("Host address : 0.0.0"+"."+x[3])
    print("Host ID : ", x[3])
    print("First address : ",x[0] +"."+ x[1]+"."+ x[2]+"."+"0")
    print("Last address : ",x[0]+"."+x[1]+"."+x[2]+"."+"255")
    print("Total number of address : ", 255)

elif(int(x[0])>=224 and int(x[0])<=239):
    print("No network address available for class D")
    print("No net ID available")
    print("No host address available for class D")
    print("No host ID available")
    print("No first address and last address available")
    
elif(int(x[0])>=240 and int(x[0])<=255):
    print("No network address available for class E")
    print("No net ID available")
    print("No host address available for class D")
    print("No host ID available")
    print("No first address and last address available")


def cusmask(num):
    i = 0
    byte = 0

    if(num>=24):
        i=num-24
        for idx in range(i):
            byte = byte+pow(2,7-idx)
        return "255.255.255."+ str(byte)

    elif(num>=16):
        i=num-16
        for idx in range(i):
            byte = byte+pow(2,7-idx)
        return "255.255."+ str(byte)+".0"

    elif(num>=8):
        i=num-8
        for idx in range(i):
            byte = byte + pow(2,7-idx)
        return "255."+str(byte)+".0.0"

num = int(input("Enter the custom masking value"))
res=cusmask(num)
print(res)