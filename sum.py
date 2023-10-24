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

#Python11
#Classes: They have similar advantages to the functions, they make our functions easier to read. It sets a list of rules for creating a new custom object, everytime I use classes I will create an instance of a type of an object. I.e., let's use the #open function to create two instances of a file object. 
#		fa_input = open("somedata.fa")
#		gff_input = open("somedata.gff")

#Let's create a class DNArecord and define series of rules that DNARecord object must follow
# Start w class, then the name of your class, them the name of the base class in () object
class DNARecord(object):

#define class attributes
  sequence = 'ACGTAGCTGACGATC' 
  gene_name = 'ABC1'
  species_name = 'Drosophila melanogaster'
  
#define methods
  def reverse_complement(self): 
    replacement1 = self.sequence.replace('A', 't') 
    replacement2 = replacement1.replace('T', 'a')
    replacement3 = replacement2.replace('C', 'g')
    replacement4 = replacement3.replace('G', 'c') 
    reverse_comp = replacement4[::-1]
    return reverse_comp.upper()
  
  def get_AT(self): 
    length = len(self.sequence)
    a_count = self.sequence.count('A') 
    t_count = self.sequence.count('T') 
    at_content = (a_count + t_count) / length 
    return at_content

###END of CLASS DNARecord ###


### Outside class defintion ###
## Create a new DNARecord Object
dna_rec_obj = DNARecord() 

## Use New DNARecord object
print('Created a record for ' + dna_rec_obj.gene_name + ' from ' + dna_rec_obj.species_name) 
print('AT is ' + str(dna_rec_obj.get_AT()))
print('complement is ' + dna_rec_obj.reverse_complement())






#some stuff that will help with the assembly problems

import os


for bin_lower in range(100,1000,100):
    bin_upper = bin_lower + 99
    bin_folder_name = str(bin_lower) + "_" + str(bin_upper)
    os.mkdir(bin_folder_name)

def process_sequence(line, number):
    dna = line.rstrip("\n")
    length = len(dna)
    print("sequence length is " + str(length))
    for bin_lower in range(100,1000,100):
        bin_upper = bin_lower + 99
        if length >= bin_lower and length < bin_upper:
            print("bin is " + str(bin_lower) + " to " + str(bin_upper))
            bin_folder_name = str(bin_lower) + "_" + str(bin_upper)
            output_path = bin_folder_name + '/' + str(seq_number) + '.dna'
            output = open(output_path, "w")
            output.write(dna)
            output.close()

seq_number = 1
for file_name in os.listdir("."):
    if file_name.endswith(".dna"):
        print("reading sequences from " + file_name)
        dna_file = open(file_name)
        for line in dna_file:
            process_sequence(line, seq_number)
            seq_number = seq_number+1    






#!/usr/bin/env python3
  #class ContigObject(object):
 # sequence = import(ecoli_0.25.contigs.fasta)
  #def contig_number(self):
  #contig_nu = len(self.sequence)
  #return contig_number


gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def translate_dna(dna):
    last_codon_start = len(dna) - 2
    protein = ""
    for start in range(0,last_codon_start,3):
        codon = dna[start:start+3]
        aa = gencode.get(codon, 'X')
        protein = protein + aa
    return protein

# input sequence is easy
assert(translate_dna("ATGTTCGGT")) == "MFG"

# input sequence has incomplete codons at the end
assert(translate_dna("ATCGATCGAT")) == "IDR"

# input sequence contains N
assert(translate_dna("ACGANCGAT")) == "TXD" 



#XXXXXXXXXXXXXXXXXXXXX

from __future__ import division

def get_aa_percentage(protein, aa):
	protein = protein.upper()
	aa = aa.upper()
	aa_count = protein.count(aa)
	protein_length = len(protein)
	percentage = aa_count * 100 / protein_length
	return percentage

assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert get_aa_percentage("msrslllrfllfllllpplp", "L") == 50
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", "Y") == 0



#XXXXXXXXXXXXXXXXXXXXXX


dna = "AATGATGAACGAC"
bases = ['A','T','G','C']
all_counts = {}
for base1 in bases:
    for base2 in bases:
        dinucleotide = base1 + base2
        count = dna.count(dinucleotide)
        if count > 0:
            all_counts[dinucleotide] = count

#XXXXXXXXXXXXXXXXXXXXXXXXXXX


dna = "AATGATGAACGAC"
dinucleotides = ['AA','AT','AG','AC',
                 'TA','TT','TG','TC',
                 'GA','GT','GG','GC',
                  'CA','CT','CG','CT']
all_counts = []
for dinucleotide in dinucleotides:
    count = dna.count(dinucleotide)
    print("count is " + str(count) + " for " + dinucleotide)
    all_counts.append(count)
print(all_counts)




#XXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import os
import sys

# convert command line arguments to variables
kmer_size = int(sys.argv[1])
count_cutoff = int(sys.argv[2])

# define the function to split dna
def split_dna(dna, kmer_size):
    kmers = []
    for start in range(0,len(dna)-(kmer_size-1),1):
        kmer = dna[start:start+kmer_size]
        kmers.append(kmer)
    return kmers

# create an empty dictionary to hold the counts
kmer_counts = {}

# process each file with the right name
for file_name in os.listdir("."):
    if file_name.endswith(".dna"):
        dna_file = open(file_name)

        # process each DNA sequence in a file
        for line in dna_file:
            dna = line.rstrip("\n")

            # increase the count for each k-mer that we find
            for kmer in split_dna(dna, kmer_size):
                current_count = kmer_counts.get(kmer, 0)
                new_count = current_count + 1
                kmer_counts[kmer] = new_count

# print k-mers whose counts are above the cutoff
for kmer, count in kmer_counts.items():
    if count > count_cutoff:
        print(kmer + " : " + str(count))



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


