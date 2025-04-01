# using symmetrical encrption, encrpt the data. Ask user for data and shift of characters.

def enc(data,shift):
    enc_data = []
    for i in data:
        i = (ord(i)) + shift
        enc_data.append(chr(i))
    print(''.join(enc_data))

data = input("enter the data to be encrypted: ")
shift = int(input("enter the shift to happen by how many alphabets: "))
enc(data,shift)