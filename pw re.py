
import re

pswd ='hnnj254DFD$%vffv'

reg ="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{16,20}$"

match_re = re.compile(reg)

res = re.search(match_re, pswd)

if res:
    print("Valid Password")
else:
    print("Invalid Password")

