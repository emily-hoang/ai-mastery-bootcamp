# with - allows file to be opened and close automatically after operation
# Open file with different mode: r - read, w - write, a - append, r+ - read and write
# .read() - read the entire file, .readline()- read line by line, .readlines() - read all lines

try:
  with open("test.txt", "r+") as file:
    lines = file.readline()
    word_count = sum(len(line.split()) for line in lines)
    print("number of line is ", len(lines))
    print("number of word is ", word_count)
except FileNotFoundError:
  print("File doesn't exist")
    