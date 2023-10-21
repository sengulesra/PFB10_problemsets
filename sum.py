#!/usr/bin/env python3
#In terminal/ interpreter, type python3 to start coding in python. 
import sys
print("Hello, PFB!")
#If you want to run your .py file in terminal but don't want to type python3, you can make it executable by chmod and change the permissions on it:
#			>>chmod +x hello.py
#			ls -l hello.py
# -rwxr-xr-x  |  - for a normal file type, d directory and l if for link. rwx stands for read, write and execute. The sequence represents the permissions for you, your group and everyone else, respectively.
# In terminal, you can simply type ./yourscript.py to run it. NO space between the ./ and the filename.

message = '' #make an empty variable and make sure that the block of code by lines will be denited with the same level of indentation. 
for x in (1,2,3,4,5):
		if x > 4:
				print("Hello")
				message = 'x is big'
		else:
				print(x)
				message = 'x is small'
		print(message)
print('All Done!')

##Data types and variables!
#Literal numbers are immutable
gene_count = 5
#But you can define them in a variable and variables can change
gene_count = 10
#you can assign integers to variables:
gene_count = 10
#you can assign floats to variables, floating point numbers:
average = 2.531
#and here is a string:
message = "Welcome to Python"
#there are lists that you can store data, all indexed SQUARE BRACKETS& COMMAS
[ 'atg' , 'aaa' , 'agg' ]
#there are tuples which are also indexed data but they are immutable PARANTHESES & COMMAS
( 'Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , 'Jun' , 'Jul' , 'Aug' , 'Sep' , 'Oct' , 'Nov' , 'Dec' )
#there are dictionaries, two-column table data storing. unordered collections of key/ value pairs
{ 'TP53' : 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC' , 'BRCA1' : 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA' }


friend1 = sys.argv[1] # get first command line parameter
friend2 = sys.argv[2] # get second command line parameter
# now print a message to the screen
print(friend1,'and',friend2,'are friends')
#type names for friend1 and friend2 after ./xx.py: ./sum.py Joe Anita
#to remember what kind of object you're dealing with:
data = [2,4,6]
type(data)
data = 5
type(data)
id(data)
dir(data)

#Python1 ProblemSet
print("Hello New York")
name = "esra"
print(name)
name = "esra"
color = "blue"
activity = "broomball"
print(name, color, activity)
animal = "cat"
print(name, color, activity, animal)
print(f'My name is: {name} andmy fav color is {color} and my fav activity is {activity} and lastly I love my {animal}.')
#try sys.argv from the command line
#ADD/COMMIT/PUSH

#PYTHON2

dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
'TCT' in dna
'ATG' in dna
'ATG' not in dna
codons = [ 'atg' , 'aaa' , 'agg' ]
'atg' in codons
'ttt' in codons
bool(True)
bool('True')
bool(False)
bool('False')
bool(0)
bool('0')
bool('')
bool(' ')
bool(())
bool([])
bool({})

#if to test for truth and execute the lines of code if true
#else the first block is xecuted if the condition is true

dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
if 'AGC' in dna:
  print('found AGC in your dna sequence')
else:
	print('did not find ATG in your dna sequence')

#if/elif if it's false, the indented block after elif is executed if the first elif condition is true. any remaining elif will be tested until one is found to be true
count = 60
if count < 0:
  message = "is less than 0"
  print(count, message)
elif count < 50:
  message = "is less than 50"
  print (count, message)
elif count > 50:
  message = "is greater than 50"
  print (count, message)
else:
  message = "must be 50"
  print(count, message) 

count = 20
if count < 0:
  message = "is less than 0"
  print(count, message)
elif count < 50:
  message = "is less than 50"
  print (count, message)
elif count > 50:
  message = "is greater than 50"
  print (count, message)
else:
  message = "must be 50"
  print(count, message)

count = 50
if count < 0:
  message = "is less than 0"
  print(count, message)
elif count < 50:
  message = "is less than 50"
  print (count, message)
elif count > 50:
  message = "is greater than 50"
  print (count, message)
else:
  message = "must be 50"
  print(count, message)

#integer can be pos or neg and that function will convert 2.3 to a plain int because integer does not contain a decimal point or exponent
int(2.3)

#floating point number can be pos or neg and the following will convert it into a floating number
float(2)

#complex number is a form of a+bi where bi is an imaginary part. The following converts 2.3 and 2 to a complex number with real part and an imaginary part 
complex(2.3,2)

abs(2.3)

abs(-2.9)

round(2.3)

round(2.5)

round(2.9)

round(-2.9)

round(-2.3)

round(-2.009,2)

round(2.675, 2)  # note this rounds down

max(4,-5,5,1,11)

min(4,-5,5,1,11)

#Python2 Problem set

cavefish = 34
if cavefish<20:
	message = ("1.5 million years ago, Astyanax mexicanus diverged into 19 caves")
	print(message)
elif cavefish == 31:
	message = ("1.5 million years ago, Astyanax mexicanus diverged into 31 caves")
	print(message)
else:
	message = ("1.5 million years ago, Astyanax mexicanus diverged into 34 caves")
	print(message)

#Python3 
#Different types of data
len('ACGTGA') # length of a string
len( (0.23, 9.74, -8.17, 3.24, 0.16) )   # length of a tuple, needs two parentheses (( ))
len(['dog', 'cat', 'bird'])  # length of a list

'ACGTGA'.rstrip('A')
'ACGTG'
#you'll get an error now if you run that as it's a list. not a string > ['dog', 'cat', 'bird'].rstrip()

#To search object specifc functions or methods
dir('ACGTGA')

#Strings
#Series of characters ending with " or '
#f'' or f-strings are useful for variable interpolation in python
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences. And goes
on and on.
"""


#print a string
print("ATG")
#assign a string to a variable and print that variable
dna = 'ATG'




#Python6 Problem set
mySet = set('ATGTGGG')
mySet2 = {'ATGCCT'}
print(mySet)
print(mySet2)

Set_A = {'3', '14', '15', '9', '26', '5', '35', '9'}
Set_B = {'60', '22', '14', '0', '9'}

print(Set_A)
print(Set_B)

print(Set_A - Set_B) #difference
print(Set_A | Set_B) #union
print(Set_A & Set_B) #intersection
print(Set_A ^ Set_B) #symmetric difference

dnaseq_set_ = set('GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTNNGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACX')
print(dnaseq_set_)

p6p4_ntcount = {}
dna_p6p4 = ('GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA')
unique = set(dna_p6p4)

print('unique nt: ', unique)
for nt in unique:
	count = dna_p6p4.count(nt)
	p6p4_ntcount[nt] = count
print('nt count:', p6p4_ntcount)
total_ntcount = 370 + 206 +227 +360
print(total_ntcount)

#store each count in a dictionary. example: nt_comp['A']=2

#when you are done counting each character calculate and report the nucleotide composition and the GC content.


#Python10
#built-in functions like len and print can work default but you can also write your own functions, you can define your own functions using def

#here's the code for how to find the GC content
dna = 'GTACCTTCTGAGAGGCTGCTGCT'
c_count = dna.count('C')  # count is a string method
g_count = dna.count('G')
dna_len = len(dna) # len is a function
gc_content = (c_count + g_count) / dna_len # fraction from 0 to 1
print(gc_content)

#let's define our function to calculate the GC content
def gc_content(dna):
	c_count = dna.count('C')
	g_count = dna.count('G')
	dna_len = len(dna)
	gc_content = (c_count + g_count) / dna_len 
	return gc_content #return the value of the result to the code
	print(gc_content(dna)) 

#to convert the GC fraction to %GC ?? We can use f''
dna_2 = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCT'
dna2_gc = gc_content(dna_2)
print(f'This sequence is {dna2_gc:.2%} GC')

#keyword arguments
dna_string = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCT'
print(gc_content(dna_string))
print(gc_content(dna=dna_string)) #gc content here expects a dna argument, remember where you put the dna value when defining your function

def team(name, project, computer, gitname):
		print(name, "is working on", project, "using", computer, "computer and her github profile name is", gitname)
team( project= "Python3", computer = "PF10", name = "Esra", gitname = "sengulesra")

#lambda expressions?? you can use them to define simple one line functions
def get_first_codon(dna):
  return dna[0:3]
print(get_first_codon('ATGTTT'))

#lambda <the bariable you pass into the function> : <the expression that operates on your variable>
get_first_codon = lambda dna : dna[0:3]  # pass data into 'dna' then extract 
                                         # the first 3 characters
print(get_first_codon('ATGTTT'))


#Scope
#Control blocks like if statements do not count and the variables used or initialized inside the block of an if statement can also be used and accessed outside of its scope. Python variable is in scope for the whole of the function where it appears, not just in the innermost "block". Sooo, anything declared in an if block has the same scope as anything declared outside of the block. 

a = 2
if(a==2):
	b = a+2
	print(b)


print('Before if block')
x = 100
print('x=',x)
if True:  # this if condition will always be True 
  # we want to make sure the block gets executed
  # so we can show you what happens
  print('Inside if block')
  x = 30
  y = 10
  print("x=", x)
  print("y=", y)

print('After if block')
print("x=", x)
print("y=", y)








