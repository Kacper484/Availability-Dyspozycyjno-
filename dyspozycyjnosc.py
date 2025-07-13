#Importy
import calendar
from tkinter import *
from tkinter import messagebox  # dodaj na górze pliku

#0 defuniuje zmienne globalne

#1. Tworzenie gui
gui = Tk()
gui.title("Dyspozycyjność")
gui.configure(background="black")
gui.geometry("740x600")


#1.1 Tworzenie 1 elementu wpisanie roku i miesiąca

#rok
labelRok = Label(gui, text="Wpisz rok:", font=("Arial", 10, "bold"), bg="black", fg="white")
labelRok.grid(row=0, column=0, padx=5, pady=5, sticky="w")

rok_var = StringVar()
entryRok = Entry(gui, font=("Arial", 10), bd=10, insertwidth=2, width=5, justify="left", textvariable=rok_var)
entryRok.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky="w")


#miesiąc
labelMies = Label(gui, text="Wpisz Miesiąc:", font=("Arial", 10, "bold"), bg="black", fg="white")
labelMies.grid(row=1, column=0, padx=5, pady=5, sticky="w")

miesiac_var = StringVar()
entryMies = Entry(gui, font=("Arial", 10), bd=10, insertwidth=2, width=5, justify="left", textvariable=miesiac_var)
entryMies.grid(row=1, column=1, padx=5, pady=5, columnspan=2, sticky="w")

# Podawanie Imienia
labelName = Label(gui, text="Wpisz Imie:", font=("Arial", 10, "bold"), bg="black", fg="white")
labelName.grid(row=2, column=0, padx=5, pady=5, sticky="w")

name_var = StringVar()
entryName = Entry(gui, font=("Arial", 10), bd=10, insertwidth=2, width=25, justify="left", textvariable=name_var)
entryName.grid(row=2, column=1, padx=5, pady=5, columnspan=2, sticky="w")

# Podawanie Nazwiska
labelSurname = Label(gui, text="Wpisz Nazwisko:", font=("Arial", 10, "bold"), bg="black", fg="white")
labelSurname.grid(row=3, column=0, padx=5, pady=5, sticky="w")

surname_var = StringVar()
entrySurname = Entry(gui, font=("Arial", 10), bd=10, insertwidth=2, width=25, justify="left", textvariable=surname_var)
entrySurname.grid(row=3, column=1, padx=5, pady=5, columnspan=2, sticky="w")



#2.Funkcja generuj kalendarz
def generuj_kalendarz():

      #2.1 Walidacja dla błędów dania danych

      #sprawdzanie roku i miesiąca
      rok_text = entryRok.get()
      miesiac_text = entryMies.get()
      if not (rok_text.isdigit() and miesiac_text.isdigit()):
            messagebox.showerror("Błąd","Rok i miesiąc muszą być liczbami całkowitymi!")
            return



      if len(rok_text) != 4 or not (1<= int(miesiac_text) <=12):
            messagebox.showerror("Błąd", "Rok musi miec 4 cyfry, a  miesiąc od 1 do 12!")
            return

      #sprawdaznie imienia i nazwiska
      imie = name_var.get().strip()
      nazwisko = surname_var.get().strip()
      if not imie or not nazwisko:
            messagebox.showerror("Błąd", "Imię i nazwisko nie mogą być puste!")
            return


      #2.2 Usuwamy Label i entry:
      labelRok.destroy()
      labelMies.destroy()
      entryRok.destroy()
      entryMies.destroy()
      labelName.destroy()
      entryName.destroy()
      labelSurname.destroy()
      entrySurname.destroy()
      genKal.destroy()

      #2.3 Obliczanie ilości dni w miesiącu i powiadomienie kiedy zaczyna się mieisąc

      year = int(rok_var.get())
      month = int(miesiac_var.get())

      dni_tygodnia = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']

      miesiace = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień",
                  "Wrzesień", "Październik", "Listopad", "Grudzień"]

      first_day, num_days = calendar.monthrange(year, month)

      #2.4 Wyświetlanie  Dzni tygodnia na gorze


      dni_tygodnia_skrocone = ["PON", "WT", "ŚR", "CZW", "PT", "SOB", "NIEDZ"]

      for col, dzien in enumerate(dni_tygodnia_skrocone):
            label = Label(gui, text=dzien, font=("Arial", 10, "bold"), bg="black", fg="white")
            label.grid(row=0, column=col, padx=5, pady=5)

      zmiany_lista = ["00"] * num_days

      #2.5 Funkcja która obilicza zmiany

      class ZmianaButton:
            def __init__(self, master, index, zmiany_lista):
                  self.index = index
                  self.zmiany_lista = zmiany_lista
                  self.cykle = ["00", "10", "01", "11"]
                  self.curent_index = 0
                  self.koloryZmian = {
                        "00": ("Brak zmian", "lightgray"),
                        "10": ("1. zmiana", "green"),
                        "01": ("2. zmiana", "dodgerblue"),
                        "11": ("Cały dzień", "red")
                  }
                  self.button = Button(master, height=3, width=10, text=str(index + 1), font=("Arial", 9),
                                       command=self.klik)
                  self.ustaw_przycisk()

            def klik(self):
                  self.curent_index = (self.curent_index + 1) % len(self.cykle)
                  self.ustaw_przycisk()

            def ustaw_przycisk(self):
                  kod = self.cykle[self.curent_index]
                  tekst, kolor = self.koloryZmian[kod]
                  self.button.config(bg=kolor, text=f"{self.index + 1}\n{tekst}")
                  self.zmiany_lista[self.index] = kod

      #2.6 pętla wyśwetlająca kalędarz
      for day in range(num_days):
            row = (day + first_day) // 7 + 1
            column = (day + first_day) % 7
            zmiana_btn = ZmianaButton(gui, day, zmiany_lista)
            zmiana_btn.button.grid(row=row, column=column, padx=5, pady=5)

      # 3. Funkcja podsumuj

      row_end = (num_days + first_day) // 7 + 2  # +2 żeby było pod kalendarzem
      col_end = (num_days + first_day) // 7 + 2  # +2 żeby było pod kalendarzem

      #3.1 wypisanie podsumowania
      def wypisz_podsumowanie():
            ciąg_zmian = " ".join(" ".join(kod) for kod in zmiany_lista)

            # Entry + Scrollbar poziomy
            entry_podsumowanie_var = StringVar()
            entry_podsumowanie_var.set(ciąg_zmian)

            frame_entry = Frame(gui)
            frame_entry.grid(row=row_end + 1, column=0, columnspan=7, padx=5, pady=5)

            scrollbar_x = Scrollbar(frame_entry, orient=HORIZONTAL)
            entry = Entry(frame_entry, textvariable=entry_podsumowanie_var, font=("Arial", 10),
                          xscrollcommand=scrollbar_x.set, width=80, state="readonly")
            scrollbar_x.config(command=entry.xview)

            entry.pack(side=TOP, fill=X)
            scrollbar_x.pack(side=BOTTOM, fill=X)

            # Przycisk kopiowania do schowka
            def kopiuj_do_schowka():
                  gui.clipboard_clear()
                  gui.clipboard_append(ciąg_zmian)
                  gui.update()
                  messagebox.showinfo("Skopiowano", "Ciąg zmian został skopiowany do schowka!")

            btn_kopiuj = Button(gui, text="Kopiuj do schowka", font=("Arial", 10, "bold"), command=kopiuj_do_schowka)
            btn_kopiuj.grid(row=row_end + 2, column=0, columnspan=3, pady=5)

            # Przycisk zapisu do pliku
            def zapisz_do_pliku():
                  try:
                        miesiac = int(miesiac_var.get())
                        rok = int(rok_var.get())
                        imie = name_var.get().strip()
                        nazwisko = surname_var.get().strip()

                        if not imie or not nazwisko:
                              raise ValueError("Imię i nazwisko są wymagane.")

                        if not (1 <= miesiac <= 12):
                              raise ValueError("Miesiąc poza zakresem")

                        imie_caps = imie.upper()
                        nazwisko_caps = nazwisko.upper()

                        nazwa_pliku = f"{nazwisko_caps}_{imie_caps}_{miesiac:02d}_{rok}_OD.txt"

                        with open(nazwa_pliku, "w") as plik:
                              plik.write(ciąg_zmian)

                        messagebox.showinfo("Zapisano", f"Ciąg zmian zapisany do pliku '{nazwa_pliku}'")
                  except Exception as e:
                        messagebox.showerror("Błąd", f"Nie udało się zapisać pliku:\n{e}")

            btn_zapisz = Button(gui, text="Zapisz do pliku", font=("Arial", 10, "bold"), command=zapisz_do_pliku)
            btn_zapisz.grid(row=row_end + 2, column=4, columnspan=3, pady=5)





      # 3.2 button podsumowanie


      btn_podsumuj = Button(gui, text="Podsumuj", font=("Arial", 10, "bold"), command=wypisz_podsumowanie)
      btn_podsumuj.grid(row=row_end, column=col_end, columnspan=7, pady=10)



#2.7 przycisk do generowania kalendarza
genKal = Button(gui, text="Generuj kalendarz", font=("Arial", 10, "bold"), bg="grey", fg="white", command=generuj_kalendarz)
genKal.grid(row=5, column=1, padx=5, pady=5, sticky="w")


# konczymy na tym zawsze loopawnie gui
gui.mainloop()

