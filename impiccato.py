'''
Autore: Pulga Luca
Classe: 5^L
Data di inizio: 2021-10-08
Data di termine: 2021-10-22
Scopo: Gioco dell'impiccato

'''
import csv # Libreria in aiuto per l'estrazione delle parole dal csv fornito.
import time # Libreria per gestione del tempo (thread.sleep()).
import random # Libreria necessaria per la scelta casuale della parola.
import sys # Libreria che servirà per terminare il programma quando voluto dall'utente (sys.exit()).

parole = [] # Lista delle parole che saranno estratte dal csv.
viteGiocatore = 10 # Vite a disposizione del giocatore.
parolaDaIndovinare = "" # Parola da indovinare.
lettereIndovinate = [] # Lettere indovinate inserite dall'utente, serve per la costruzione della parola.

# Ascii dell'impiccato a seconda delle vite a disposizione del giocatore.
def impiccato(viteGiocatore):
        if viteGiocatore==0:
                print('       ______  ')
                print('      |     |  ')
                print('      |     O  ')
                print('      |    /|\ ')
                print('      |    / \ ')
                print('      |        ')
                print('     _|________')
                return
        if viteGiocatore==1:
                print('       ______  ')
                print('      |     |  ')
                print('      |     O  ')
                print('      |    /|\ ')
                print('      |    /   ')
                print('      |        ')
                print('     _|________')
                return
        if viteGiocatore==2:
                print('       ______  ')
                print('      |     |  ')
                print('      |     O  ')
                print('      |    /|\ ')
                print('      |        ')
                print('      |        ')
                print('     _|________')
                return
        if viteGiocatore==3:
                print('       ______  ')
                print('      |     |  ')
                print('      |     O  ')
                print('      |    /|  ')
                print('      |        ')
                print('      |        ')
                print('     _|________')
                return
        if viteGiocatore==4:
                print('       ______  ')
                print('      |     |  ')
                print('      |     O  ')
                print('      |     |  ')
                print('      |        ')
                print('      |        ')
                print('     _|________')
                return
        if viteGiocatore==5:
                print('       ______  ')
                print('      |     |  ')
                print('      |     O  ')
                print('      |        ')
                print('      |        ')
                print('      |        ')
                print('     _|________')
                return
        if viteGiocatore==6:
                print('       ______  ')
                print('      |     |  ')
                print('      |        ')
                print('      |        ')
                print('      |        ')
                print('      |        ')
                print('     _|________')
                return
        if viteGiocatore==7:
                print('       ______  ')
                print('      |        ')
                print('      |        ')
                print('      |        ')
                print('      |        ')
                print('      |        ')
                print('     _|________')
                return
        if viteGiocatore==8:
                print('               ')
                print('      |        ')
                print('      |        ')
                print('      |        ')
                print('      |        ')
                print('      |        ')
                print('     _|________')
                return
        if viteGiocatore==9:
                print('               ')
                print('               ')
                print('               ')
                print('               ')
                print('               ')
                print('               ')
                print('     _|________')
                return

# Lettura del file csv ed estrazione parole.
def ReadingCsvFile():
        with open('italian-word-list-total.csv', newline='') as csvfile: # Apertura file csv.
                data = csv.DictReader(csvfile) # Lettura file.
                for row in data:
                        parole.append(row['word form'].upper()) # Aggiungo alla lista da cui verrà scelta la parola, tutte le parole del csv.

# Visualizza la parola aggiornata a seconda delle lettere indovinate.
def VisualizzaParola(listaLettere):
    print(' '.join(lettera for lettera in listaLettere))

# Se la lettera digitata dall'utente (letteraInput) è presente nella parola,
# prendo l'indice in cui si trova la lettera e sostituisco il '+' o il '_' 
# presente in lettereIndovinate con la nuova lettera.
def AggiornaLettere(letteraInput, parola, lettereIndovinate):
    for indiceLettera, lettera in enumerate(parola): # Funziona come il FOR in c#
        if lettera == letteraInput:
            lettereIndovinate[indiceLettera] = lettera # Assegnazione alla parola in un determinato indice della lettera indovinata.
    return lettereIndovinate

# Conversione della parola da indovinare in formato "impiccato": '+' per vocali, '_' per consonanti.
def ConversioneParolaDaIndovinare(choice, wordToFind):
        for indiceLettera, lettera in enumerate(wordToFind):
                if(choice == 2 or choice == 4):
                        if lettera == wordToFind[0] and indiceLettera == 0: # Lascio la prima lettera in chiaro. 
                                lettereIndovinate.append(lettera) 
                        elif lettera == wordToFind[len(wordToFind) - 1] and indiceLettera == len(wordToFind) - 1: # Lascio l'ultima in chiaro. 
                                lettereIndovinate.insert(len(wordToFind) - 1, lettera)
                        else:
                                if(lettera == 'A' or lettera == 'E' or lettera == 'I' or lettera == 'O' or lettera == 'U' or lettera == 'à'.upper() or lettera == 'é'.upper() or lettera == 'è'.upper() or lettera == 'ì'.upper() or lettera == 'ò'.upper() or lettera == 'ù'.upper()): # Se vocale, +
                                        lettereIndovinate.append('+')
                                else: # Altrimenti, -            
                                        lettereIndovinate.append('_')
                else:
                        if(lettera == 'A' or lettera == 'E' or lettera == 'I' or lettera == 'O' or lettera == 'U' or lettera == 'à'.upper() or lettera == 'é'.upper() or lettera == 'è'.upper() or lettera == 'ì'.upper() or lettera == 'ò'.upper() or lettera == 'ù'.upper()): # Se vocale, +

                                        lettereIndovinate.append('+')
                        else: # Altrimenti, -            
                                        lettereIndovinate.append('_')

# Visualizzazione del Menù.
def Menu():
        print('\t\t####################')
        print('\t\t#        The       #')
        print('\t\t#      Hangman     #')
        print('\t\t#       Game       #')
        print('\t\t####################')
        print("\t\t\tPulga Luca - 5^L - 2021-10-08 - IMPICCATO IN PYTHON")    
        print("\t\t\tBenvenuto nel gioco dell'impiccato!")
        print("\t[1] Versione + (vocali) - (consonanti) senza prima ed ultima lettera in chiaro & parola scelta dall'utente;")
        print("\t[2] Versione + (vocali) - (consonanti) con prima ed ultima lettera in chiaro & parola scelta dall'utente;")
        print("\t[3] Versione + (vocali) - (consonanti) senza prima ed ultima lettera in chiaro & parola scelta casualmente;")
        print("\t[4] Versione + (vocali) - (consonanti) con prima ed ultima lettera in chiaro & parola scelta casualmente;")
        print("\t[5] Per uscire dal gioco.")

# Scelta della versione a cui l'utente vuole giocare. 
def Choice():
        while True:
                try:
                        choice = int(input("> Scegli la versione dell'impiccato a cui vuoi partecipare:")) # Scelta.
                        lettereIndovinate.clear() # Ad ogni nuova partita, devo pulire la lista delle lettere indovinate.
                        viteGiocatore = 10
                        if choice ==  1:
                                print("\n\t> [1] Versione + (vocali) - (consonanti) senza prima ed ultima lettera in chiaro & parola scelta dall'utente;")
                                parolaDaIndovinare = Alpha()
                                ConversioneParolaDaIndovinare(1, parolaDaIndovinare)
                                VisualizzaParola(lettereIndovinate)
                                Main(lettereIndovinate, parolaDaIndovinare) # Esecuzione Main in cui si svolge il gioco.
                        
                        elif choice == 2:
                                print("\n\t> [2] Versione + (vocali) - (consonanti) con prima ed ultima lettera in chiaro & parola scelta dall'utente;")
                                parolaDaIndovinare = Alpha()
                                ConversioneParolaDaIndovinare(2, parolaDaIndovinare)
                                VisualizzaParola(lettereIndovinate)
                                Main(lettereIndovinate, parolaDaIndovinare) # Esecuzione Main in cui si svolge il gioco.

                        elif choice == 3:
                                print("\n\t> [3] Versione + (vocali) - (consonanti) senza prima ed ultima lettera in chiaro & parola scelta casualmente;")
                                ReadingCsvFile() # Lettura del csv.
                                parolaDaIndovinare = random.choice(parole) # Estrazione casuale della parola da indovinare.
                                ConversioneParolaDaIndovinare(3, parolaDaIndovinare) # Conversione.
                                VisualizzaParola(lettereIndovinate)
                                Main(lettereIndovinate, parolaDaIndovinare) # Esecuzione Main in cui si svolge il gioco.

                        elif choice == 4:
                                print("\n\t> [4] Versione + (vocali) - (consonanti) con prima ed ultima lettera in chiaro & parola scelta casualmente;")
                                ReadingCsvFile()
                                parolaDaIndovinare = random.choice(parole) # Estrazione casuale della parola da indovinare.
                                ConversioneParolaDaIndovinare(4, parolaDaIndovinare) # Conversione.
                                VisualizzaParola(lettereIndovinate)
                                Main(lettereIndovinate, parolaDaIndovinare) # Esecuzione Main in cui si svolge il gioco.

                        elif choice == 5:
                                sys.exit() # Chiusura del programma.

                except ValueError:
                                print("\t> Inserisci una versione valida del gioco.")
                                continue

# Svolgimento del gioco.
def Main(correctLetters, wordToFind):
        viteGiocatore = 10
        while viteGiocatore > 0: # Il gioco continua finchè il giocatore non termina le vite a disposizione.
                letteraInput = input("\t> Inserisci una lettera -> ").upper() # Lettera inserita dall'utente da confrontare se la parola da indovinare, la contiene.
                if letteraInput in wordToFind: # Se la contiene
                        correctLetters = AggiornaLettere(letteraInput, wordToFind, correctLetters) # Aggiornamento lettere.
                        if wordToFind == ''.join(lettera for lettera in correctLetters): # Se la parola da indovinare è uguale a tutte le lettere inserite dall'utente, allora ha vinto.
                                print("\t> Sei salvo dall'impiccagione! :) \nComplimenti! La parola è: " + wordToFind.upper())
                                time.sleep(2.0)
                                break
                else: # Se la lettera inserita, non è contenuta nella parola da indovinare.
                        viteGiocatore = viteGiocatore - 1 # Decremento le vite.
                        print(impiccato(viteGiocatore)) # Animazione impiccato
                VisualizzaParola(correctLetters) # Visualizza la parola aggiornata, cioè nello stato in cui era prima.
        else: # Se il giocatore ha speso le 10 vite, ha perso il gioco.
                print("\t> Sei stato impiccato! :( \nLa parola era: " + wordToFind.upper())
                time.sleep(2.0)

def Alpha():
        ok = False
        while ok == False:
                ok = True
                parola = str(input("\nInserisci la parola da indovinare: ")).upper() # Inserimento dell'utente della parola da indovinare.
                controllo = parola.isalpha() # Controlla se la parola appena inserita è effettivamente composta da sole lettere e non numeri o simboli.
                if(controllo == False):
                        print("\t\t Inserire una parola valida da indovinare! ")
                        ok = False
                elif(len(parola) < 3):
                        print("\t\t Inserire una parola maggiore di 3 caratteri! ")
                        ok = False
        return parola


Menu()
Choice()
