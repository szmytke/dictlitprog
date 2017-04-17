import csv

choise = True

while choise != '0':
    choise = input('''Dictionary for a little programmer:\n
    1) search explanation by appellation\n
    2) add new definition\n
    3) show all appellations alphabetically\n
    4) show available definitions by first letter of appellation \n
    0) exit\n''')
    if choise == '1':
        infile = open('dict.csv','r')
        reader = csv.reader(infile)
        appel = input('search appellation\n')
        for row in reader:
            dict_prog = {row[0]:(row[1],row[2])}
            if appel == row[0]:
                print(dict_prog[row[0]])
        infile.close()
        break
    elif choise == '2':
        ofile  = open('dict.csv', 'a')
        writer = csv.writer(ofile)  
        def_appel = input('write appellation \n')
        def_value = input('write value \n')
        def_source = input('write source \n')
        list_av = [def_appel,def_value,def_source]
        writer.writerow(list_av)
        break
    elif choise == '3':
        infile = open('dict.csv','r')
        reader = csv.reader(infile)
        list_appel = []
        for i in reader:
            list_appel = list_appel + [i[0]]
        list_appel.sort(key=lambda s: s.lower())
        for i in list_appel:
            print(i)
        break
    elif choise == '4':
        infile = open('dict.csv','r')
        reader = csv.reader(infile)
        letter = input('search appellation by firs letter\n')
        for row in reader:
            dict_prog = {row[0]:(row[1],row[2])}
            if letter == row[0][0] or letter.upper() == row[0][0]:
             print(dict_prog[row[0]])
        infile.close()
        break
    elif choise == '0':
        exit() 
    else:
        print('invalid number, please choose again')