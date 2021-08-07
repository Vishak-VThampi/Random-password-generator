import string as s
from random import*
char= s.ascii_letters + s.digits + s.punctuation
password= "".join(choice(char) for x in range(randint(8,16)))
print(password)
