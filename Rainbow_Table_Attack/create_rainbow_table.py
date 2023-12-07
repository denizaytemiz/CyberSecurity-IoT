import hashlib

fp = open("10K_PLAINTEXT_PASSWORDS.txt", "r") # open for reading

# Read existing file with plaintext passwords
lines = [line.rstrip() for line in fp.readlines()]
fp.close()

# OPEN FILE TO STORE HASHED PASSWORDS HERE
outputfile = open("RAINBOW_TABLE.txt", 'w')

# loop through each entry in lines
for i in lines:
    # Call the md5 function in hashlib and pass it the password string in bytes. See http://pythoncentral.io/hashing-strings-with-python/
    res = bytes(i,'utf-8')
    md5_hashed = hashlib.md5(res)
    print(md5_hashed.hexdigest())
    # Write the hexdigest of the md5_hashed object to the outfile.
    outputfile.write(md5_hashed.hexdigest()+'\n')    
outputfile.close()
