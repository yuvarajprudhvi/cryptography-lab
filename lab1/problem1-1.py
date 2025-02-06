
file_name = input("Enter the file name: ")
with open(file_name, 'r') as file:
    text = file.read()  


words = text.split() 
char_count = len(text)  
word_count = len(words)  


print(f"Word Count: {word_count}")
print(f"Character Count: {char_count}")


print("\nASCII Values of Each Character:")
for char in text:
    print(f"Character: '{char}' - ASCII: {ord(char)}")

