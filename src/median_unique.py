# example of program that calculates the median number of unique words per tweet.
import sys
import os
import words_tweeted

def word_median_file(input_filename, output_filename):
  input_file = open(input_filename, 'r')
  output_file = open(output_filename, 'w')
  sorted_unique_count = []
  unique_median = []
  count = 0
  for line in input_file:
	if count != 0:
		output_file.write("\n")
	count = count + 1
	word_map = {}
	words_tweeted.word_count_line(line, word_map)
	unique = len(word_map)
	
	pos = sorted_list(sorted_unique_count, 0, len(sorted_unique_count)-1, unique)
	sorted_unique_count.insert(pos, unique)
	cnt = len(sorted_unique_count)
	median = 0.0
	if cnt%2 == 1:
		median = sorted_unique_count[cnt/2]
	else:
		median = 0.5*(sorted_unique_count[(cnt+1)/2] + sorted_unique_count[(cnt-1)/2]) 
	output_file.write("{0}".format(median))
	print count
	
	print unique
  input_file.close()
  output_file.close()

# find the position in sorted array of new element using binary search
# input: original sorted array, begin index, end index, new element
# output: position  
def sorted_list(sorted_unique_count, b, e, unique):
  if len(sorted_unique_count) == 0:
	return 0
  pivot = (e + b)/2 
  if e <= b: 
	pos = min(b,e)
	key = sorted_unique_count[pos]
	if key > unique:
		return pos
	else:	
		return pos + 1	
  key = sorted_unique_count[pivot]	
  if key > unique:
	return sorted_list(sorted_unique_count, b, pivot-1, unique)
  elif key < unique:
	return sorted_list(sorted_unique_count, pivot+1, e, unique)
  else:
	return pivot  

# main
def main():
  if len(sys.argv) != 3:
    print 'usage:  ./src/median_unique.py input_file output_file'
    sys.exit(1)
  input_filename = sys.argv[1]
  output_filename = sys.argv[2]
  word_median_file(input_filename, output_filename)


if __name__ == '__main__':
  main()