from struct import pack, unpack
import os
import sys



##################for me ##########################

#to be removed later #

#print int('00000110', 2)

############################



######Variable byte Encoding ################

############function ######################
def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
   # os.system('cls')
              
    print("\t**********************************************")
    print("\t***  Greeter - Variable Byte !  ***")
    print("\t**********************************************")


####referecne https://nlp.stanford.edu/IR-book/html/htmledition/variable-byte-codes-1.html

def vb_encode(number):
    bytes = []
    while True:
        bytes.insert(0, number % 128)
        if number < 128:
            break
        number /= 128
    bytes[-1] += 128
    # print len(bytes)
    # print bytes
    return pack('%dB' % len(bytes), *bytes)



def vb_decode(bytestream):
    n = 0
    numbers = []
    bytestream = unpack('%dB' % len(bytestream), bytestream)
    for byte in bytestream:
        if byte < 128:
            n = 128 * n + byte
        else:
            n = 128 * n + (byte - 128)
            numbers.append(n)
            n = 0
    return numbers

#greeting message ;
display_title_bar();


#taking the input from the console , the number is saved in string
option =raw_input("\t Option for encode/decode \n\t 1 to Encode  \n\t 2 to Decode \n ")
num = raw_input("Input the posting list   ")  

# print int(num)/128;  --->qotient
# print int(num)%128;  --->reminder


#print vb_encode(int(num));
def byte_vb_encode(number):
    bytestream = vb_encode(number)
   # print bytestream
    # print unpack('%dB' % len(bytestream), bytestream)
    print ([format(b, '08b') for b in unpack('%dB' % len(bytestream), bytestream)])



if int(option)==1:
	print "Bytes of input number is :"
	print ('{0:08b}'.format(int(num)))
	print "Variable Bytes of input number is :"
	byte_vb_encode(int(num))
elif int(option)==2:
	print "Decoding the input number ";
	
	n=8;
	line=num;
	if len(line)%8==0:
		# print "Input length is Good"
		bytes =[]
		bytes= [int(line[i:i+n],2) for i in range(0, len(line), n)]
		bytestream=pack('%dB' % len(bytes), *bytes)
		result= vb_decode(bytestream);
		print result
	else:
		print "Input bytes number"		
	

	
else:
	print 'Unrecognized Action number please input the correct number'	;
