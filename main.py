import string as str
import random as ran

pw = []

pw_len = int(input('password length: '))

for i in range(pw_len):
    pw.append(ran.choice(str.digits + str.ascii_letters + str.punctuation))

pw = ''.join(pw)

print(pw)