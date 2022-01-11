from tkinter import *
from tkinter import messagebox
import pandas as pd

animal_df=pd.read_csv('animals.csv')
animal_df.drop(animal_df.columns[[0,4,6,7,9,10,11,13,14,16,17,18]], axis=1, inplace=True)

a=animal_df.to_numpy()
Animals=animal_df[['Animal Name']].to_numpy()
baslık = animal_df.columns

def Search(x):
  k=0
  for i in range (len(a)):
    for j in range(len(a[0])):
      if x == a[i][j]:
        return ('it is: ' + baslık[j])
        k=+1
        break
    if k==1:
      break
  if k==0:
    return ("It is not in tree")


def Compare(A, B):
  x = 6
  k = -1
  l = -1
  for i in range(len(Animals)):
    if Animals[i] == A:
      k = i
    if Animals[i] == B:
      l = i
  if k == -1 or l == -1:
    return ("Check the names. One of them is not in tree, or two??")

  for i in range(len(a[k]) - 1, -1, -1):
    if a[k][i] == a[l][i]:
      return ("they have same, " + baslık[i])
      break
      x = +1
    if x == 0:
      return ("they are tottaly difrent")


def gosterS():
    messagebox.showinfo("Search", Search(ekran1.get()))

def gosterC():
    messagebox.showinfo("Search", Compare(ekran2.get(),ekran3.get()))


main =Tk()
main.geometry("530x310")
main.title("Taxonomy")


explabel=Label(main,text="Some animals; \n "
                         "Arctic Wolf: Animalia, Chordata, Mammalia, Carnivora, Canidae, Canis \n"
                         "Pink Fairy Armadillo: Animalia, Chordata, Mammalia, Cingulata, Chlamyphoridae, Chlamyphorus \n"
                         "Antilopine Kangaroo: Animalia, Chordata, Mammalia, Diprotodontia, Macropodidae, Macropus \n"
                         "Collared Pika:Animalia,Chordata,Mammalia, Lagomorpha, Ochotonidae, Ochotona")
explabel.place(x=0,y=200)


ekran1 =Entry(main,width=40,borderwidth=5)
ekran1.place(x=100)

ekran2 = Entry(main,width=20,borderwidth=5)
ekran2.place(x=90,y=100)
ekran3 =Entry(main,width=20,borderwidth=5)
ekran3.place(x=230,y=100)


buttonS = Button(text="Search",command = gosterS)
buttonS.place(x=195,y=30)

buttonC = Button(main, text="Compare",command=gosterC)
buttonC.place(x=190,y=130)



main.mainloop()