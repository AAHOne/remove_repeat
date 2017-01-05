#!/usr/bin/env python
#coding=utf-8
import sys
import getopt

def page():
    print "[+]**Please input -f Example:chek_repeat.py -f 1.txt**[+]"

def chek_repeat(filename):
    chek = []
    f = open(filename,'r')
    print "Checking Repeat Content ....."
    try:
        for i in f.readlines():
            i = i.strip("\n")
            if i not in chek:
                if i !="":
                    chek.append(i)
    except:
        pass
    f.close()
    print "Start Delte Repeat Content....."
    with open(filename,"w") as f:
        for password in chek:
            f.write(password)
            f.write("\n")
        f.close()
    print "Successful!"

def main(argv):
    try:
        opts,args=getopt.getopt(argv[1:],'hf:')
    except getopt.GetoptError,err:
        print str(err)
        page()
        sys.exit()
    for o,a in opts:
        if o in ('-h'):
            page()
            sys.exit(1)
        elif o in ('-f'):
            chek_repeat(a)
            sys.exit(0)
        else:
            print "Please Input Correct Parameters!"
            sys.exit(3)    

if __name__=='__main__':
    main(sys.argv)