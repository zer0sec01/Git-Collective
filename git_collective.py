#!/usr/bin/python3
from git import Repo
import sys
import time


#clone multiple git repositories


def choices():
    choice = input('how many links do you want to clone? 2 or 3? ')
    if choice == '2':
        link2()
    elif choice == '3':
        link3()
    else:
        print('invalid number')
        sys.exit

def link2():
    link1 = input('link1: ')
    where1 = input('what directory should link 1 go? ')
    link2 = input('link2: ')
    where2 = input('what directory should link 2 go? ')
    
    Repo.clone_from(link1, where1)
    print('cloned first link...')
    time.sleep(5)
    Repo.clone_from(link2, where2)
    print('Done')

def link3():
    link1 = input('link1: ')
    which1 = input('what directory should link 1 go? ')
    link2 = input('link2: ')
    which2 = input('what directory should link 2 go? ')
    link3 = input('link3: ')
    which3 = input('what directory should link 3 go? ')
    Repo.clone_from(link1, which1)
    print ('Cloned first link...')
    time.sleep(5)
    Repo.clone_from(link2, which2)
    print ('Cloned Second link...')
    time.sleep(5)
    Repo.clone_from(link3, which3)
    print ('Done')



choices()

