while True:
    ip = input("Enter the IPv4 address string: ")
    arr = [""] * 6
    j = 0
    leng = 1

    for i in range(len(ip)):
        if ip[i] != '.':
            arr[j] = arr[j] + ip[i]
            len += 1
        else:
            j += 1

    while True:
        print()
        print("Enter input:")
        input_value = int(input())

        if input_value == 1:
            a = 0
            for j in range(4):
                if arr[j][0] == '0':
                    print(f"Error: There should be no leading zeros in the IPv4 address string: {arr[j]}")
                    a += 1
            if a == 0:
                print("There are no leading zero errors")
            break

        elif input_value == 2:
            a = 0
            b = 0
            for j in range(4):
                try:
                    value = int(arr[j])
                    if not (0 < value < 255):
                        print(f"ERROR: {value} should be between the range of 0-255")
                        a += 1
                        break
                except ValueError:
                    print("ERROR: The entered IPv4 does not contain only integer values")
                    b += 1
                    break
            if a == 0:
                print("No range error.")
            if b == 0:
                print("The cell values have only integer values.")
            break

        elif input_value == 3:
            a = 0
            if len != 4:
                a += 1
                print("ERROR: The IP address should have exactly 4 cells")
            if a == 0:
                print("IP address has 4 cells")
            break

        elif input_value == 5:
            a = 0
            for i in range(len(ip)):
                if not (ord(ip[i]) == 46 or 47 <= ord(ip[i]) <= 58):
                    a += 1
                    print(f"ERROR: Each IP cell value should be separated by dot/period only. Error: {ip[i]}")
            if a == 0:
                print("Each IP cell is separated by dot/period.")
            break

        elif input_value == 6:
            if 0 < int(arr[0]) < 127:
                print("Class A")
            if 127 < int(arr[0]) < 191:
                print("Class B")
            if 191 < int(arr[0]) < 223:
                print("Class C")
            if 223 < int(arr[0]) < 239:
                print("Class D")
            if 240 < int(arr[0]) < 255:
                print("Class E")
            break

        else:
            print("Enter correct option")
            break
