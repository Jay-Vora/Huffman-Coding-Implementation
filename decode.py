'''
 -------------------------------------
 Huffman Decoding Assignment 06
 Name:  Jay Vora
 Student ID: 203321900
 -------------------------------------
''' 
from encode import frequencyCode
# Removing the bit manipulation done in encoding the text
def removePad(encodedTxt):
    info = encodedTxt[:8]
    extra = int(info, 2)
    encodedTxt = encodedTxt[8:] 
    byteCode = encodedTxt[:-1*extra]
    return byteCode
# Decoding to string from binary

def decodeTxt(encodedTxt):
    byteCode = ""
    decodedTxt = ""

    for bit in encodedTxt:
        byteCode += bit
        if(byteCode in frequencyCode.values()):
            character = list(frequencyCode.keys())[list(frequencyCode.values()).index(byteCode)]
            decodedTxt += character
            byteCode = ""

    return decodedTxt



# Reading the compressed.bin file
file4 = open("compressed.bin", "rb")
byteStr = ""

singleByte = file4.read(1)
while(len(singleByte) > 0):
    singleByte = ord(singleByte)
    bit = bin(singleByte)[2:].rjust(8, '0')
    byteStr += bit
    singleByte = file4.read(1)

encodedTxt = removePad(byteStr)
decodedTxt = decodeTxt(encodedTxt)
# Writing the results into decoded.txt
file5 = open("decoded.txt", "w")
file5.write(decodedTxt)
file5.close()
