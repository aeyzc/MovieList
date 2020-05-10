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
    select=int(input('\n\n1-İzlenecek Filmler\n2-İzlediğim Filmler\n3-Cıkıs'))
    system('cls')
    #ToDo List

    if select==1:
        selectToDoList=int(input('İZLENECEK FİLMLER\n\n1-İzlenecekler Listesini Göster\n2-Listeye Film Ekle\n3-Listeden Film Sil\n4-Rastgele Film Seç\n5-Ana Menüye Dön\n\n'))
        system('cls')
        if selectToDoList==1:
            print('İZLENİLECEKLER LİSTESİ\n')
            counter=1
            for i in liste:
                print(str(counter)+'-'+i,end='')
                counter+=1

        elif selectToDoList==2:
            eklenen=input('Ekleyeceğiniz Filmin İsmini Girin: ')
            liste.append(eklenen+'\n')
            print(eklenen+' Listenize Eklendi!')

        elif selectToDoList==3:
            try:
                deletingToDo=input('(LÜTFEN BÜYÜK KÜÇÜK HARFLERE DİKKAT EDİN!)\nSilinecek Filmin İsmini Girin: ')
                liste.remove(deletingToDo+'\n')
            except Exception:
                print('Film Bulunamadı!')
            else:
                print(deletingToDo+' Listenizden Silindi!')

        elif selectToDoList==4:
            randomMovie=random.choice(liste)
            print('Seçilen Film: '+randomMovie)

        elif selectToDoList==5:
            continue

        else:
            print('Hatalı Seçim Yaptınız!')
            continue

    #Watched List        

    if select==2:
        selectWatched=int(input('İZLEDİĞİM FİLMLER\n\n1-Eklenme Tarihine Göre Göster\n2-Puanıma Göre Göster\n3-Listeye Film Ekle\n4-Listeden Film Sil\n5-Ana Menüye Dön'))
        system('cls')
        if selectWatched==1:
            print('İZLEDİĞİM FİLMLER (EKLENME SIRASINA GÖRE)\n')
            counter=1
            for k,v in watchedList.items():
                print(str(counter)+'-'+k+'('+str(v)+')')
                counter+=1

        elif selectWatched==2:
            print('İZLEDİĞİM FİLMLER (PUANLARIMA GÖRE)\n')
            counter=1
            for k,v in sorted(watchedList.items(), key=itemgetter(1),reverse=True):
                print(str(counter)+'-'+k+'('+str(v)+')')
                counter+=1

        elif selectWatched==3:
            while True:
                title=input('Ekleyeceğiniz Filmin Adını Girin: ')
                if len(title)<=1:
                    print('\nLütfen Geçerli Film İsmi Girin!\n')
                else:
                    break

            while True:
                try:
                    points=float(input('\nEkleyeceğiniz Filme Puanınızı Girin (Örn:4.2): '))
                    if (points>10 or points<0):
                        raise Exception('\nlütfen 0-10 arası sayı giriniz!\n')
                except Exception:
                    print('\nlütfen 0-10 arası sayı giriniz!\n')
                else:
                    break

            watchedList.update({title : float(points)})
            print(title+' Listenize Eklendi!')

        
        elif selectWatched==4:
            try:
                deleting=input('(LÜTFEN BÜYÜK KÜÇÜK HARFLERE DİKKAT EDİN!)\nLütfen Silinecek Filmin İsmini Girin: ')
                del watchedList[deleting]
            except Exception:
                print('Film Bulunamadı!')
            else:
                print(deleting+' Listenizden Silindi!')

        elif selectWatched==5:
            continue
            
        else:
            print('Hatalı Seçim Yaptınız!')
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

    wait=input('\n1-Ana Menü\n2-Çıkış')
    system('cls')
    if wait=='2':
        break
    
    