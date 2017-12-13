def CPass(pss):
    err = ''
    capital = 0
    numbers = 0
    if len(pss)<=6:
        err+= "password must be longer then 6 letters\n"
    if pss.find(' ')!=-1:
        err += 'must not contain spaces\n'
    for i in pss:
        if i.isupper():
            capital+=1
    if capital==0:
        err+='You must use at least one capital letter\n'
    for i in pss:
        if i.isdigit():
            numbers+=1
    if numbers ==0:
        err+="you must use at least one number\n"
    if err!='':
        return err
    return True
            
def CUser(user):
    err=''
    if len(user)<=6:
        err+= "user name must be longer then 6 letters"
    if user.find(' ')!=-1:
        err += 'must not contain spaces\n'
    if err!='':
        return err
    return True

if __name__ == '__main__':
    print CPass('matan kriel # %')
    print CPass('Aan1')
    print CPass('matan 2')
    print CUser("jnkjnjndf")
    print CUser("sdf")









    
