import statistics
import pyrg_funkcje
#Stala dla foldera z plikami
FOLDER = 'daneztreningow/'
#Stala dla foldera na pliki z wykresami
CHARTS = 'wykresy/'


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
    mins_secs, hundredths = f"{(average / 100):.2f}".split('.')
    mins_secs = int(mins_secs)
    minutes = mins_secs // 60
    seconds = mins_secs - minutes * 60
    average = f'{minutes}:{seconds:0>2},{hundredths}'
    return swimmer, age, distance, stroke, times, average, converts #krotka zwrotna z danymi


def produce_bar_chart(fn):
    """Na podstawie nazwy pliku pływaka generuje wykres słupkowy, używając HTML i SVG
    
    Wykres jest zapisywany w katalogu określonym przez stałą CHARTS. Funkcja zwraca 
    ścieżkę dostępu do pliku wykresu
    """

    swimmer, age, distance, stroke, times, average, converts = read_swim_data(fn)
    from_max = max(converts)
    times.reverse()
    converts.reverse()
    title = f'{swimmer} (ponizej {age} lat), {distance}, styl: {stroke}'
    header = f"""<!DOCTYPE html>
                    <html>
                        <head>
                            <title>{title}</title>
                        </head>
                        <body>
                            <h3>{title}</h3>"""
    body = ''
    for n, t in enumerate(times):
        bar_width = pyrg_funkcje.convert2range(converts[n], 0, from_max, 0, 300)
        body = body + f"""
                        <svg height="30" width="400">
                            <rect height="30" width="{bar_width}" style="fill:rgb(0,0,255);" />
                        </svg>{t}<br />"""
    footer = f"""
                        <p>Sredni czas: {average}</p>
                    </body>
                </html>"""
    page = header + body + footer
    save_to = f"{CHARTS}/{fn.removesuffix(".txt")}.html"
    with open(save_to, 'w') as sf:
        print(page, file=sf)
    return save_to

                

    """Funkcja konwertuje przekazaną wartość (v) z zakresu od f_min
    do f_max, na odpowiadającą jej wartość z zakresu t_min do t_max.

    Kod bazuje na technic opisanej na stronie:
        http://james-ramsden.com/map-a-value-from-one-number-scale-to-another-formula-and-c-code/
    """
    return round(t_min + (t_max - t_min) * ((v - f_min) / (f_max - f_min)), 2)