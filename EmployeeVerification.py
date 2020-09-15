import re
 
class Verification:
 
    def verifyemail(self):
        pattern = re.compile(r"\w+[^_][.]{0,1}\w+@[^0-9]\w+\.{0,1}\w+\.{0,1}\w+") 
        while 1:
            email = input("enter email: ")
            if pattern.match(email):           
                return email
            print("<< Invalid email >>")
 
    def verifyid(self):
        pattern = re.compile(r"[a-zA-Z]*[1-9]*")  
        while 1:
            enr = input("enter Id: ")
            if pattern.match(enr):          
                return enr
            print("<< Invalid ID >>")
            
    def verifynumber(self):
        pattern = re.compile(r"[0-9]")  
        while 1:
            no = input("enter Number: ")
            if (len(pattern.findall(no))==10):          
                return no
            print("<< Invalid Number >>")        
            