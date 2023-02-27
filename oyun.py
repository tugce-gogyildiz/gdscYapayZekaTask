# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:54:00 2023

@author: tugce
"""


import os
class Oyun():

    def __init__(self):

        self.ilk_işlemler()

        self.oyunu_baslat() 

    def ilk_işlemler(self):

        self.tahta = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']    
        self.oyuncu = 1  

        self.Galibiyet = 1    
        self.Beraberlik = -1    
        self.Devam = 0    
            
        self.Oyun = self.Devam      
        self.İşaret = 'A' 
    
    def tahtayı_çiz(self): 
        os.system('cls')
        
        print("   |   |   ") 
        print(" {} | {} | {} ".format(self.tahta[1], self.tahta[2], self.tahta[3]))    
        print("___|___|___")
        print("   |   |   ")     
        print(" {} | {} | {} ".format(self.tahta[4], self.tahta[5], self.tahta[6]))    
        print("___|___|___") 
        print("   |   |   ")    
        print(" {} | {} | {} ".format(self.tahta[7], self.tahta[8], self.tahta[9]))    
        print("   |   |   ") 
        
    def boşluk_kontrol(self,A): 
        
        if(self.tahta[A] == ' '):    
            return True    
        else:    
            return False 

    def durum_kontrol(self):
        if(self.tahta[1] == self.tahta[2] and self.tahta[2] == self.tahta[3] and self.tahta[1] != ' '): 
            self.Oyun = self.Galibiyet 
        
          
        elif(self.tahta[4] == self.tahta[5]  == self.tahta[6] != ' '):    
            self.Oyun = self.Galibiyet

        elif(self.tahta[7] == self.tahta[8]  == self.tahta[9] != ' '):    
            self.Oyun = self.Galibiyet 
            
        elif(self.tahta[1] == self.tahta[4] == self.tahta[7] != ' '):    
            self.Oyun = self.Galibiyet    

        elif(self.tahta[2] == self.tahta[5] == self.tahta[8] != ' '):    
            self.Oyun = self.Galibiyet   
 
        elif(self.tahta[3] == self.tahta[6] == self.tahta[9] != ' '):    
            self.Oyun = self.Galibiyet 
            
            
        elif(self.tahta[1] == self.tahta[5] == self.tahta[9] and self.tahta[5] != ' '):    
            self.Oyun = self.Galibiyet    

        elif(self.tahta[3] == self.tahta[5] == self.tahta[7] and self.tahta[5] != ' '):    
            self.Oyun = self.Galibiyet  

    
        elif(self.tahta[1] != ' ' and self.tahta[2] != ' ' and self.tahta[3] != ' ' and self.tahta[4] != ' ' and self.tahta[5] != ' ' and self.tahta[6] != ' ' and self.tahta[7] != ' ' and self.tahta[8] != ' ' and self.tahta[9] != ' '):
                        
            self.Oyun = self.Beraberlik
        else:

            self.Oyun = self.Devam



    def oyunu_baslat(self):
        
        print("\n ---  Oyuna Hoş Geldiniz --- \n")

        oyuncu_1 = input("1.oyuncunun adını giriniz: ")
        oyuncu_2 = input("2.oyuncunun adını giriniz: ")

        print(f"{oyuncu_1} [A] --- {oyuncu_2} [B]\n")    

        input("Başlamak İçin enter'a basın ")


        while(self.Oyun == self.Devam):
           

            if(self.oyuncu % 2 != 0): 
                print(f"Sıradaki oyuncu {oyuncu_1}")    
                self.İşaret = 'A'    

            else:   
                print(f"Sıradaki oyuncu {oyuncu_2}")    
                self.İşaret = 'B'    

            seçim = int(input("İşaretlemek için 1 ve 9 arasında bir sayı girin : "))   

            if(self.boşluk_kontrol(seçim)): 

                self.tahta[seçim] = self.İşaret   
                self.oyuncu += 1   
                self.durum_kontrol() 
                self.tahtayı_çiz()    

        if(self.Oyun == self.Beraberlik):    
            print("* OYUN BERABERE *")    

        elif(self.Oyun == self.Galibiyet):    
            self.oyuncu -= 1    

            if(self.oyuncu % 2 != 0):    
                print(f"* {oyuncu_1} KAZANDI *")    
                
            else:    
                print(f"* {oyuncu_2} KAZANDI *")  

            Oyun()








