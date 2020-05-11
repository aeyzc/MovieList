import random
from operator import itemgetter, attrgetter
import ast
from os import system

# txt dosyalarından alınan verileri listelere attım.
with open('WList.txt','r+',encoding='utf-8') as file1:
    watchedListTake=file1.read()
    watchedList=ast.literal_eval(watchedListTake)

with open('TDList.txt','r',encoding='utf-8') as file1:
    liste=file1.readlines()

######################################################

while True:
    print(''' __ __            _        _    _        _   
|  \  \ ___  _ _ <_> ___  | |  <_> ___ _| |_ 
|     |/ . \| | || |/ ._> | |_ | |<_-<  | |  
|_|_|_|\___/|__/ |_|\___. |___||_|/__/  |_| 
                                   by aeyzc''')
    select=int(input('\n\n1-Movie List to Watch\n2-Movie List the Watched\n3-Exit'))
    system('cls')
    #ToDo List

    if select==1:
        selectToDoList=int(input('MOVIE LIST TO WATCH\n\n1-Show List\n2-Add a Movie\n3-Delete a Movie\n4-Choose Random Movie\n5-Return to Main Menu\n\n'))
        system('cls')
        if selectToDoList==1:
            print('MOVIE LIST TO WATCH\n')
            counter=1
            for i in liste:
                print(str(counter)+'-'+i,end='')
                counter+=1

        elif selectToDoList==2:
            eklenen=input('Movie Name to Add: ')
            liste.append(eklenen+'\n')
            print(eklenen+' Added to Your List!')

        elif selectToDoList==3:
            try:
                deletingToDo=input('(PLEASE PAY ATTENTION TO UPPER AND LOWER CASE!)\nMovie Name to Delete: ')
                liste.remove(deletingToDo+'\n')
            except Exception:
                print('Movie not Found!')
            else:
                print(deletingToDo+' Deleted to Your List!')

        elif selectToDoList==4:
            randomMovie=random.choice(liste)
            print('Random Movie: '+randomMovie)

        elif selectToDoList==5:
            continue

        else:
            print('Wrong Choice!')
            continue

    #Watched List        

    if select==2:
        selectWatched=int(input('MOVIE LIST THE WATCHED\n\n1-Show List by Added Time\n2-Show List by Your Points\n3-Add a Movie\n4-Delete a Movie\n5-Return to Main Menu'))
        system('cls')
        if selectWatched==1:
            print('MOVIE LIST THE WATCHED (by Added Time)\n')
            counter=1
            for k,v in watchedList.items():
                print(str(counter)+'-'+k+'('+str(v)+')')
                counter+=1

        elif selectWatched==2:
            print('MOVIE LIST THE WATCHED (by Your Points)\n')
            counter=1
            for k,v in sorted(watchedList.items(), key=itemgetter(1),reverse=True):
                print(str(counter)+'-'+k+'('+str(v)+')')
                counter+=1

        elif selectWatched==3:
            while True:
                title=input('Movie Name to Add: ')
                if len(title)<=1:
                    print('\nInvalid Movie Name!\n')
                else:
                    break

            while True:
                try:
                    points=float(input('\nMovie Points (e.g:4.2): '))
                    if (points>10 or points<0):
                        raise Exception('\nPlease Enter a Number Between 0-10!\n')
                except Exception:
                    print('\nPlease Enter a Number Between 0-10!\n')
                else:
                    break

            watchedList.update({title : float(points)})
            print(title+' Added to Your List!')

        
        elif selectWatched==4:
            try:
                deleting=input('(PLEASE PAY ATTENTION TO UPPER AND LOWER CASE!)\nMovie Name to Delete: ')
                del watchedList[deleting]
            except Exception:
                print('Movie not Found!')
            else:
                print(deleting+' Deleted to Your List!')

        elif selectWatched==5:
            continue
            
        else:
            print('Wrong Choice!')
            continue

    #Exit

    if select==3:
        break

    #listeleri tekrar txt dosyalarına atadım

    with open('TDList.txt','w',encoding='utf-8') as file1:
            file1.writelines(liste)

    with open('WList.txt','w',encoding='utf-8') as file1:
        file1.write('{')
        for key, value in watchedList.items():
            file1.write('''"%s":%s,\n''' % (key, value))
        file1.write('}')

    ########################################

    wait=input('\n1-Main Menu\n2-Exit')
    system('cls')
    if wait=='2':
        break
    
    