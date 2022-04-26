from fileinput import close
import selenium
import time
import urllib.request, json 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import ssl
import logging

def start():
    #SSL Error Handling
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    #Farben

    #Websites abrufen
    with urllib.request.urlopen("https://json.jurka.ch/websites.json") as url:
        data = json.loads(url.read().decode())

    #Blacklist abrufen
    with urllib.request.urlopen("https://json.jurka.ch/blacklist.json") as blacklist:
        bldata = json.loads(blacklist.read().decode())


    #-------------Bomber Schleife----------------
    def bomb():
        x = 0
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('log-level=3')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        while x < len(data):
            driver.get(data[x]["url"])
            print(str(x+1) + " Eintragungen wurden vorgenommen")
            

    #Vorname
            if len(data[x]["vorname"]) > 0:
                try:
                    driver.find_element(by=By.XPATH, value=data[x]["vorname"]).clear()
                    driver.find_element(by=By.XPATH, value=data[x]["vorname"]).send_keys(vorname)
                except:
                    #print("Ein Fehler wurde bei der URL " + (data[x]["url"]) + " beim Feld Vorname übersprungen")
                    pass
            else:
                pass
    
    #Nachname
            if len(data[x]["nachname"]) > 0:
                try:
                    driver.find_element(by=By.XPATH, value=data[x]["nachname"]).clear()
                    driver.find_element(by=By.XPATH, value=data[x]["nachname"]).send_keys(nachname)
                except:
                    #print("Ein Fehler wurde bei der URL " + (data[x]["url"]) + " beim Feld Nachname übersprungen")
                    pass
            else:
                pass

    #Strasse
            if len(data[x]["strasse"]) > 0:
                try:
                    driver.find_element(by=By.XPATH, value=data[x]["strasse"]).clear()
                    driver.find_element(by=By.XPATH, value=data[x]["strasse"]).send_keys(strasse)
                except:
                    #print("Ein Fehler wurde bei der URL " + (data[x]["url"]) + " beim Feld Strasse übersprungen")
                    pass
            else:
                pass

    #Strassennummer
            if len(data[x]["strassennummer"]) > 0:
                try:
                    driver.find_element(by=By.XPATH, value=data[x]["strassennummer"]).clear()
                    driver.find_element(by=By.XPATH, value=data[x]["strassennummer"]).send_keys(strassennummer)
                except:
                    #print("Ein Fehler wurde bei der URL " + (data[x]["url"]) + " beim Feld Strassennummer übersprungen")
                    pass
            else:
                pass

    #Postleitzahl
            if len(data[x]["plz"]) > 0:
                try:
                    driver.find_element(by=By.XPATH, value=data[x]["plz"]).clear()
                    driver.find_element(by=By.XPATH, value=data[x]["plz"]).send_keys(plz)
                except:
                    #print("Ein Fehler wurde bei der URL " + (data[x]["url"]) + " beim Feld Postleitzahl übersprungen")
                    pass
            else:
                pass

    #Ort
            if len(data[x]["ort"]) > 0:
                try:
                    driver.find_element(by=By.XPATH, value=data[x]["ort"]).clear()
                    driver.find_element(by=By.XPATH, value=data[x]["ort"]).send_keys(nachname)
                except:
                    #print("Ein Fehler wurde bei der URL " + (data[x]["url"]) + " beim Feld Ort übersprungen")
                    pass
            else:
                pass

    #E-Mail
            if len(data[x]["email"]) > 0:
                try:
                    driver.find_element(by=By.XPATH, value=data[x]["email"]).clear()
                    driver.find_element(by=By.XPATH, value=data[x]["email"]).send_keys(email)
                except:
                    #print("Ein Fehler wurde bei der URL " + (data[x]["url"]) + " beim Feld E-Mail übersprungen")
                    pass
            else:
                pass

    #Passwort    
            if len(data[x]["pass"]) > 0:
                try:    
                    driver.find_element(by=By.XPATH, value=data[x]["pass"]).clear()
                    driver.find_element(by=By.XPATH, value=data[x]["pass"]).send_keys(passwort)
                except:
                    #print("Ein Fehler wurde bei der URL " + (data[x]["url"]) + " beim Feld Passwort übersprungen")
                    pass
            else:
                pass

    #Passwort wiederholen   
            if len(data[x]["passwiederholen"]) > 0:
                try:    
                    driver.find_element(by=By.XPATH, value=data[x]["passwiederholen"]).clear()
                    driver.find_element(by=By.XPATH, value=data[x]["passwiederholen"]).send_keys(passwort)
                except:
                    #print("Ein Fehler wurde bei der URL " + (data[x]["url"]) + " beim Feld Passwort wiederholen übersprungen")
                    pass
            else:
                pass

    #AGB    
            if len(data[x]["agb"]) > 0:
                try:
                    driver.find_element(by=By.XPATH, value=data[x]["agb"]).click() 
                except:
                    #print("Ein Fehler wurde bei der URL " + (data[x]["url"]) + " beim Feld Checkbox übersprungen")
                    pass
            else:
                pass

        
    #Absenden
            if len(data[x]["submit"]) > 0:
                try:
                    driver.find_element(by=By.XPATH, value=data[x]["submit"]).click()
                    #time.sleep(0.5) 
                except:
                    #print("Ein Fehler wurde bei der URL " + (data[x]["url"]) + " beim Submit übersprungen")
                    pass
            else:
                pass

            x = x + 1  
        print("Der Bomber hat seine Aufgabe erfolgreich erledigt!") 
    #--------------------------------------------

    #Endabfrage
    def end():
        todo = int(input("Was möchtest du tun? \n 1. Andere E-Mail Adresse zumüllen \n 2. Programm beenden \n"))
        if todo == 1:
            start()
        elif todo == 2:
            exit()
        else: 
            print("Ungültige Eingabe")
            end()


    #Eingaben vom Benutzer

    print("======================================================================\n")
    print("----Willkommen beim Newsletter Massenmail Script von Jurka Brunner----\n")
    print("======================================================================\n")

    vorname = input("Vorname eigeben:")
    nachname = input("Nachname eingeben:")
    email = input("E-Mail Adresse eingeben:")
    strasse = "Luzernerstrasse"
    strassennummer = "15"
    plz = "6015"
    ort = "Luzern"
    passwort = "I8c!Pdei382"



    #Blacklist
    counter = 0
    while counter < len(bldata):
        counter = counter + 1
        if bldata[counter-1]["email"] == email:
            print("Sorry, du verwendest eine für den Bomber gesperrte E-Mail Adresse! \nDas Programm wurde abgebrochen!")
            end()
        
            
    bomb()
    end()



start()
