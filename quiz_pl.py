import json


def questionDef(tresc, a, b, c, d, poprawna):
    wpisz_odpowiedz = 'Wpisz odpowiedź: '

    # Wyświetla pytanie i jego opcje
    print('\n> ' + tresc)
    print('\na: {} \nb: {} \nc: {} \nd: {}'.format(a, b, c, d))
    odpowiedz = input(wpisz_odpowiedz)
    if odpowiedz.lower() == poprawna:
        return 1
    else:
        return 0


# Określanie IDE do dodatkowego pytania
ides = ['atom', 'vim', 'codeblocks', 'visualstudiocode',
        'codelite', 'dialogblocks', 'eclipse', 'netbeans',
        'komodo', 'aptanastudio', 'geany', 'shiftedit',
        'squad', 'visualstudio', 'monodevelop', 'pycharm',
        'kate', 'gedit', 'sublimetext', 'vscode', 'visualstudio'
        'what am I even doing here ;_;', 'vs']

print('Witamy w quizie o pythonie!')

# Wybór języka pytań
while True:
    język = input('Wybierz język [en/pl]: ').lower()
    if język == 'en':
        # (do przetestowania) prawdopodobnie na windowsie trzeba będzie zmienić '/' na '\' w ścieżce pliku.
        with open('question_sets/questions_en.json', 'r') as f:
            questionsets = json.load(f)
            questionlist = []
        break
    elif język == 'pl':
        # (do przetestowania) prawdopodobnie na windowsie trzeba będzie zmienić '/' na '\' w ścieżce pliku.
        with open('question_sets/questions_pl.json', 'r') as f:
            questionsets = json.load(f)
            questionlist = []
        break
#   elif język == 'wpisz skrót do twojego zestawu pytań':
#       # (do przetestowania) prawdopodobnie na windowsie trzeba będzie zmienić '/' na '\' w ścieżce pliku.
#       with open('question_sets/nazwa twojego zestawu pytań.json', 'r') as f:
#           questionsets = json.load(f)
#           questiondict = []
#       break
    else:
        print('Przepraszamy, ten język nie jest obecnie w bazie danych. Spróbuj Ponownie.')
        continue

try:
    with open('data.json') as f:
        data_store = json.load(f)
# Jeżeli plik nie istnieje, bądź jest zepsuty stwórz nowy
except (FileNotFoundError, json.decoder.JSONDecodeError):
    data_store = []

# Robienie listy z pliku json
for item in questionsets:
    question = item['Question']
    a = item['a']
    b = item['b']
    c = item['c']
    d = item['d']
    answer = item['answer']
    questionlist.append((question, a, b, c, d, answer))

# Quiz pętla
while True:
    name = input('Enter your name: ')
    punkty = 0

    # Za każde pytanie w questionsets przywołuje funkcję questionDef,
    # i dodaje punkty za każdą dobrą odpowiedź.
    for q in questionlist:
        punkty += questionDef(*q)

    print('\n(-1 punkt, jeżeli udzielisz złej odpowiedzi w dodatkowym pytaniu)')
    extra = input("Czy chcesz dodatkowe pytanie? [t/n] ")
    if extra == 't':
        ide_extra = input(
            'Wpisz nazwę jednego z popularnych IDE. (bez spacji, sam tekst)\n').lower()
        if ide_extra in ides:
            punkty += 1
        else:
            punkty -= 1
    data_store.append({'Name: ': name, 'Score: ': punkty})
    od_nowa = input('Jeszcze raz? [t/n] ').lower()
    if od_nowa == 't':
        continue
    else:
        # Zapisuje dane do pliku json
        with open('data.json', 'w') as f:
            json.dump(data_store, f, indent=2)
        break
