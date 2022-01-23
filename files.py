# python has afunction for creating, reading and updating files 
# open a file 
myfile= open('mtTxt.txt','w')

# get an information from the files 
print('name', myfile.name)
print('is closed:', myfile.close)
print('opening mode:', myfile.mode)

# lets write to file 
myfile.write('i love python ')
myfile.write('and javascript')
myfile.close()

# lets append to the files 
myfile= open('mtTxt.txt','a')
myfile.write(' i prayed to God to clear my debt and He did')
myfile.close()

# to read from 
myfile= open('mtTxt.txt','r+')
text = myfile.read(100)
print(text)
