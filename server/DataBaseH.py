import os
import md5
#os.path.join
#os.path.exists
#os.makedirs

path = os.path.dirname(__file__)
basedir = os.path.join(path, 'DATA')
if not os.path.exists(basedir):
    os.mkdir(path+'\\DATA')

def addNew(user, passw):
    hashed = md5.md5(passw).hexdigest()
    userSP = [user[1]+user[0],user[3]+user[2]]
    cdir = os.path.join(basedir,userSP[0])
    cdir = os.path.join(cdir,userSP[1])
    if not os.path.exists(cdir):
        os.makedirs(cdir)
    fileName = os.path.join(cdir,user[4:]+'.txt')
    if os.path.exists(fileName):
        return -1
    f = open(fileName,'w')
    f.write(hashed)
    f.close()
def getPassw(user):
    userSP = [user[1]+user[0],user[3]+user[2]]
    cdir = os.path.join(basedir,userSP[0])
    cdir = os.path.join(cdir,userSP[1])
    fileName = os.path.join(cdir,user[4:]+'.txt')
    if not os.path.exists(fileName):
        return -1
    f = open(fileName,'r')
    c = f.read()
    f.close()
    return c
def changePassw(user, newpass):
    hashed = md5.md5(passw).hexdigest()
    userSP = [user[1]+user[0],user[3]+user[2]]
    cdir = os.path.join(basedir,userSP[0])
    cdir = os.path.join(cdir,userSP[1])
    fileName = os.path.join(cdir,user[4:]+'.txt')
    if not os.path.exists(fileName):
        return -1
    f = open(fileName,'w')
    f.write(hashed)
    f.close()
    return c
def userExists(user):
    userSP = [user[1]+user[0],user[3]+user[2]]
    cdir = os.path.join(basedir,userSP[0])
    cdir = os.path.join(cdir,userSP[1])
    fileName = os.path.join(cdir,user[4:]+'.txt')
    if os.path.exists(fileName):
        return True
    return False
def removeUser(user):
    userSP = [user[1]+user[0],user[3]+user[2]]
    cdir = os.path.join(basedir,userSP[0])
    cdir = os.path.join(cdir,userSP[1])
    fileName = os.path.join(cdir,user[4:]+'.txt')
    if os.path.exists(fileName):
        os.remove(fileName)
    
    
if __name__ == '__main__':
    print path
    #addNew('jonathan', 'somepass')
    #print getPassw('jonathan')
    #print getPassw('henry')
    #print userExists('jonathan')
    removeUser('jerryy')
