import socket
import struct

def int_to_binary_string(num):
    binary_str = format(num, '032b')
    return [binary_str[i:i + 8] for i in range(0, len(binary_str), 8)]

def ask_user_input():
    while True:
        input_type = input("Enter the type of input (binary or IP): ").lower()
        if input_type == "b" or input_type == "ip":
            break
        else:
            print("Invalid input. Please enter either 'binary' or 'IP'.")

    input_value = input(f"Enter the {input_type} value: ")
    return input_type, input_value

def main():
    input_type, input_value = ask_user_input()

    if input_type == "ip":
        # Convert IPv4 to binary
        ipv4_str = input_value
        ipv4_binary = struct.unpack('!I', socket.inet_aton(ipv4_str))[0]
        ipv4_binary_str = int_to_binary_string(ipv4_binary)

        print(f"IPv4: {ipv4_str} -> binary: ", end="")
        print(*[f"[{section}]" for section in ipv4_binary_str])
    else:
        # Convert binary to IPv4
        ipv4_binary_str = input_value.replace(" ", "").replace("[", "").replace("]", "")
        ipv4_binary_back = int(ipv4_binary_str, 2)
        ipv4_str_back = socket.inet_ntoa(struct.pack('!I', ipv4_binary_back))

        print(f"Binary: {input_value} -> IPv4: {ipv4_str_back}")


if __name__ == "__main__":
    main()