import statistics
#Stala dla foldera z plikami
FOLDER = 'daneztreningow/'


def read_swim_data(filename):
    """Funkcja zwraca imie i wiek plywaka, 
    dystans jaki przeplynal i styl plywacki 
    A takze czasy i ich srednia
    Wszystko to na bazie nazwy pliku bedacej paramtrem 'filename'"""

    swimmer, age, distance, stroke = filename.removesuffix('.txt').split('-')   #Zwraca dane z nazwy pliku
    
    with open(FOLDER + filename) as file:   #Otwiera rzeczywisty plik i pobiera z niego wiersze
        lines = file.readlines()
        times = lines[0].strip().split(';')

    converts = []   
    for t in times:     #Zamiana stringow na wartosci liczbowe czasow
        if ':' in t:    #Warunek pozwalajacy podzielic stringa jezeli nie ma w nim minut
            minutes, rest = t.split(':')
            seconds, hundredths = rest.split(',')
        else:
            minutes = 0
            seconds, hundredths = t.split(',')
        converts.append((int(minutes) * 60 * 100) + (int(seconds) * 100) + int(hundredths))

    
    average = statistics.mean(converts)     #wyliczanie sredniej i przerabianie jej na stringa
    mins_secs, hundredths = str(round(average / 100, 2)).split('.')
    mins_secs = int(mins_secs)
    minutes = mins_secs // 60
    seconds = mins_secs - minutes * 60
    average = str(minutes) + ':' + str(seconds) + ',' + hundredths
    return swimmer, age, distance, stroke, times, average #krotka zwrotna z danymi