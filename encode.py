'''
 -------------------------------------
 Huffman Encoding Assignment 06
 Name:  Jay Vora
 Student ID: 203321900
 -------------------------------------
 '''
 
class HeapTree(object):

    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

    def child(self):
        return (self.left, self.right)

    def node(self):
        return (self.left, self.right)

def HuffmanTree(node, left = True, binStr = ''):
    if type(node) is str:
        return {node: binStr}
    
    (l, r) = node.child()
    dictionary = dict()
    dictionary.update(HuffmanTree(l, True, binStr + '1'))
    dictionary.update(HuffmanTree(r, False, binStr + '0'))
    return dictionary

file1 = open("test1.txt", "r")
line = file1.readline()
# Counting the Characters
counter = [0] * 39
chars = [" ", ",", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
while line:
    for i in line:
        if (ord(i) == 32 or ord(i) == 9 or ord(i) == 10 or ord(i) == 13):
            counter[0] += 1
        elif ord(i) == 44:
            counter[1] += 1
        elif ord(i) == 46:
            counter[2] += 1
        elif ord(i) >= 48 and ord(i) <= 57:
            counter[ord(i)-48+3] += 1
        elif ord(i.lower()) >= 97 and ord(i.lower()) <= 122:
            counter[ord(i.lower()) - 97 + 13] += 1
    line = file1.readline()
file1.close()
# Saving the no. of Characters in frequency.txt
file2 = open("frequency.txt", "w")
for i in range(39):
    file2.write(chars[i] + ":" + str(counter[i]) + "\n")
file2.close()
# Converting the Frequency into Dynamic Huffman Code for each character
frequency = {}
file2 = open("frequency.txt", "r")
line = file2.readline()
while line:
    lineSplited = line.split(":")
    frequency[lineSplited[0]] = int(lineSplited[1][:-1])
    line = file2.readline()
file2.close()
frequency = sorted(frequency.items(), key = lambda x: x[1], reverse = True)

node = frequency

while len(node) > 1:
    (key1, c1) = node[-1]
    (key2, c2) = node[-2]
    node = node[:-2]
    node2 = HeapTree(key1, key2)
    node.append((node2, c1 + c2))

    node = sorted(node, key=lambda x: x[1], reverse=True)

hCode = HuffmanTree(node[0][0])
# Saving the Huffman Codes into codes.txt
file3 = open("codes.txt", "w")
for (char, freq) in frequency:
    file3.write(char + ":" + hCode[char] + "\n")
file3.close();
# Using frequencyCode dictionary for Huffman Codes to Encode
frequencyCode = {}
binCode = ""
for (char, freq) in frequency:
    frequencyCode[char] = hCode[char]

file1 = open("test1.txt", "r")
file1.seek(0)
line = file1.readline()
while line:
    for i in line:
        if i.lower() not in frequencyCode.keys():
            binCode += frequencyCode[' ']
        else:
            binCode += frequencyCode[i.lower()]
    line = file1.readline()
file1.close()
# Performing bit manipulation for compression
byteCode = bytearray()
binCodeLen = len(binCode)
byte = ""
for i in range(0, binCodeLen, 8):
    if (binCodeLen < i + 8):
        byte = binCode[i:]
    else:
        byte = binCode[i:i + 8]
    byteCode.append(int(byte, 2))
# Saving the code to compressed.bin file
file4 = open("compressed.bin", "wb")
file4.write(bytes(byteCode))
file4.close()