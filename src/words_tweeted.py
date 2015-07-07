# example of program that calculates the total number of times each word has been tweeted.
import sys
# word count for each file
# call function word_count_line
def word_count_file(input_filename):
  word_map = {}
  input_file = open(input_filename, 'r')
  for line in input_file:
	word_count_line(line, word_map)
  input_file.close()
  return word_map

# word count for each tweet
# used for words.tweeted.py & median_unique.py
# input: certain line in file, global word_map(reference) 
def word_count_line(line, word_map):
  words = line.split()
  for word in words:
	if not word in word_map:
		word_map[word] = 1
	else:
		word_map[word] = word_map[word] + 1
  
# sorted word_map and output to file
def word_count(input_filename, output_filename, output_length):
  word_map = word_count_file(input_filename)
  words = sorted(word_map.keys())
  output_file = open(output_filename, 'w')
  count = 0
  for word in words:
	if count != 0:
		output_file.write("\n")
	count = count + 1
	output_file.write(word + ("{0}".format(word_map[word])).rjust(output_length-len(word)))

# main
def main():
  if len(sys.argv) != 3:
	print 'usage:  ./src/words_tweeted.py input_file output_file'
	sys.exit(1)
  input_filename = sys.argv[1]
  output_filename = sys.argv[2]
  output_length = 30 # for output_file format
  word_count(input_filename, output_filename, output_length)

if __name__ == '__main__':
  main()