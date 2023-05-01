#This is my python code
# importing sys 
import sys  
def main():     
# check for the shift value 
    k = check(sys.argv) 
    plain = input("plaintext: \n") 
    print() 
    print("Cipher output: \n") 
    cipher_txt = cipher(plain, k)      
# get the first index value of lines which consist of 10 blocks of 5 
    for line_start in range(0, len(cipher_txt), 50):         
        current_line = cipher_txt[line_start : line_start + 50]          
        for block_start in range(0, len(current_line), 5): 
            block = cipher_txt[line_start + block_start : line_start + block_start + 5]             
# making spaces between the blocks
            print("".join(block), end=" ")         
        print() 
#the encrytion function        
def cipher(plain, k):     
# make the plain text into uppercase  
    plain = plain.upper()    
# storing the cipher txt 
    cipher_txt = [] 
    for letter in plain:         
# check if the letters are alphabets 
        if not letter.isalpha(): 
            continue         
# the ascii value of A is 65 
        base = 65         
# ord() gives the ascii of a letter 
        pi = ord(letter) - base         
# if the value goes more than 26 it can circle back between the range 0 to 26 
        ci = (pi + k) % 26        
# chr() gives the ascii character corresponding to its number 
        cipher_txt.append(chr(ci + base)) 
    return cipher_txt   
# check function whether the CLI argument for the caesar key K is given or not 
def check(arg):     
# if only there are no two arguments or the second argument ie K is not an integer then exit 
    if len(arg) != 2 or arg[1].isalpha(): 
        exit()     
# if exits correctly then return K value 
    return int(arg[1])   
# call main function 
if __name__ == "__main__":     main()
