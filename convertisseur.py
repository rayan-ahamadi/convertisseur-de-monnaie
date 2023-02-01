from tkinter import *
from tkinter import ttk 
from tkinter import messagebox


window = Tk()
window.title("Convertisseur de Monnaie")
window.geometry("420x350")
window.iconbitmap("icon.ico")
value = ["Euros","Dollars Américain","Yens","Livres Sterling"]


def isNumerique(chaine): 
    for i in str(chaine):
        #si c'est pas un chiffre
        if ord(i) < 48 or ord(i) > 57 : 
            return False
    #si c'est un chiffre        
    return True 




def convert():
    global resultat
    if devise1.get() == "" or devise2.get() == "":
        messagebox.showerror("Erreur", "manque une ou plusieurs devises")
        return 0
    elif isNumerique(str(montant.get())) == False : 
        messagebox.showerror("Erreur", "Pas une valeur numérique")
        clear()
        return 0 

    valeurDepart = float(montant.get())
    deviseDepart = devise1.get()
    deviseDeConversion = devise2.get() 
    
    match deviseDepart:
        case "Euros":
            if deviseDeConversion == "Euros": 
                valeurConverti = float(valeurDepart)
            elif deviseDeConversion == "Dollars Américain":
                valeurConverti = float(valeurDepart) * 1.09
            elif deviseDeConversion == "Yens":
                valeurConverti = float(valeurDepart) * 141.90
            elif deviseDeConversion == "Livres Sterling":
                valeurConverti = float(valeurDepart) * 0.88
        case "Dollars Américain":
            if deviseDeConversion == "Dollars Américain": 
                valeurConverti = float(valeurDepart)
            elif deviseDeConversion == "Euros":
                valeurConverti = float(valeurDepart) * 0.92
            elif deviseDeConversion == "Yens":
                valeurConverti = float(valeurDepart) * 130.46
            elif deviseDeConversion == "Livres Sterling":
                valeurConverti = float(valeurDepart) * 0.81
        case "Yens":
            if deviseDeConversion == "Yens": 
                valeurConverti = float(valeurDepart)
            elif deviseDeConversion == "Dollars Américain":
                valeurConverti = float(valeurDepart) * 0.0077
            elif deviseDeConversion == "Euros":
                valeurConverti = float(valeurDepart) * 0.0071
            elif deviseDeConversion == "Livres Sterling":
                valeurConverti = float(valeurDepart) * 0.0062
        case "Livres Sterling":
            if deviseDeConversion == "Livres Sterling": 
                valeurConverti = float(valeurDepart)
            elif deviseDeConversion == "Dollars Américain":
                valeurConverti = float(valeurDepart) * 1.23
            elif deviseDeConversion == "Yens":
                valeurConverti = float(valeurDepart) * 160.68
            elif deviseDeConversion == "Euros":
                valeurConverti = float(valeurDepart) * 1.14
    resultat.insert(0,round(valeurConverti,4))
    return 0

def clear(): 
    resultat.delete(0,END)
    montant.delete(0,END)

Label(window,text="Convertisseur de monnaie",font=("Arial",10)).grid(row=0,columnspan=2,padx=50,pady=15)
Label(window,text="Montant : ").grid(row=1,column= 0,padx=50)
montant = Entry(window)
Label(window,text="Devise de départ : ").grid(row=2,column= 0,padx=50)
devise1 = ttk.Combobox(window,values=value,state="readonly")
Label(window,text="Devise de fin : ").grid(row=3,column= 0,padx=50)
devise2 = ttk.Combobox(window,values=value,state="readonly")
boutonConvert = Button(window,text="Convertir",command= lambda : convert())
Label(window,text="Somme converti : ").grid(row=5,column= 0,padx=50)
resultat = Entry(window)
boutonClear = Button(window,text="Annuler",command= lambda : clear())


montant.grid(row=1,column=1,pady=10,padx=10)
devise1.grid(row=2,column=1,pady=10,padx=10)
devise2.grid(row=3,column=1,pady=10,padx=10)
boutonConvert.grid(row=4,column=1,pady=10,padx=10)
resultat.grid(row=5,column=1,pady=10,padx=10)
boutonClear.grid(row=6,column=1,pady=10,padx=10)


window.mainloop()