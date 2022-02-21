import csv

with open('x:/repos/GGReport/scripts/songs.csv') as csv_file:
    resultado = csv.reader(csv_file, delimiter=',')
    line_count = 0
    total_artistas=0
    for row in resultado:
        if  line_count == 0:
             print(f'los nombres de las columnas son  {", ".join(row)} \n')
             line_count += 1
            
        else:
            line_count += 1
            print(f"{row[0]} por {row[1]} es del género {row[3]} y se estreno en {row[2]}")

        total_artistas += 1
    print(f"\nEl total de los artistas es de: {total_artistas}")
