#from sys import argv
#from os.path import exists

#script, from_file, to_file = argv

#print(f"Copying from {from_file} to {to_file}")
#open(argv[2], 'w').write(open(argv[1].read()))

# we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()

#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}")
#print(f"Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

#out_file = open(to_file, 'w')
#out_file.write(indata)

#print("Alright, all done.")

#out_file.close()
#in_file.close()

#This is a simpler way to write the above code while minimizing redundancy
from sys import argv ; open(argv[2], 'w').write(open(argv[1]).read())
