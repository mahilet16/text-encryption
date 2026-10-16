
import ceasr_cipher
logo=ceasr_cipher.logo
print(logo)
alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
again="yes"
while again=="yes":
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))

    if shift>26:
            quotient=shift//26
            shift=shift-(26*quotient)
    def cipher(code=text,num=shift,todo=direction):

        cipher_text=[]
        for i in range(len(text)):
            cipher_text.append("")
            letter=text[i]
            if direction=="encode":
                entry=alphabet.index(letter)+shift
                if entry>25:
                    entry-=26
            elif direction=="decode":
                entry=alphabet.index(letter)-shift
                if entry<0:
                    entry+=26
            else:
                print("you passed wrong entry!")
            cipher_text[i]=alphabet[entry]
            result="".join(cipher_text)
        print(f"the {direction}d  text is {result}")
    cipher(text,shift,direction)
    again=input("type yes if u want to continue:\n")
print("Goodbye!")