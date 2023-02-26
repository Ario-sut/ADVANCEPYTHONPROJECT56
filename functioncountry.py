def nameofcountries(country): #Fungsi perkenalan otomatis dari suatu negara
    for i in country: #Mengambil satu per satu varibel dari list country
        print("I am from " + i)

listCountry = ["China", "Japan", "Mongolia"] # daftar negara-negara
nameofcountries(listCountry) #Eksekusi fungsi