from timeit import default_timer as timer

file1 = open("RECOVERED_PASSWORD_HASHES.txt")

recovered_hashes = file1.readlines()

file1.close()

file2 = open("RAINBOW_TABLE.txt")

# https://docs.python.org/3/library/functions.html#enumerate
indexed_hashes = list(enumerate(file2))

file2.close()

file3 = open("10K_PLAINTEXT_PASSWORDS.txt")

plaintext_passwords = file3.readlines()

file3.close()

# for each candidate hash in recovered_hashes
for candidate in recovered_hashes:
   # you'll need some way to stop the inner for loop search
   # maybe use a flag variable (True/False)
   myflag = 0
   startTime = timer()
   for i,hash in indexed_hashes:
       if candidate.rstrip() == hash.rstrip():
          myflag = 1
          endTime = timer()
          print("MATCH: hash # " + hash + " = " + plaintext_passwords[i])
          print ('It took ', (endTime - startTime)*1000000, ' microseconds.')
          
   if myflag == 0:
   # this part of the code is to be executed if there is no match after a search through
   # the entire list of indexed_hashes. maybe condition on your flag variable
       endTime = timer()
       print("NO MATCH FOUND FOR ", candidate.rstrip())
       print ('It took ', (endTime - startTime)*1000000, ' microseconds.')
