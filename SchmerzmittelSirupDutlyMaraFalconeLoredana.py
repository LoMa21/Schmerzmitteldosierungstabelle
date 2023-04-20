# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 12:46:31 2023

@author: LoReF
"""

#Quellen: Streamlit.io, ChatGPT und Google
#Wir haben zum Teil bei Fehlermeldungen Chatgpt gefragt oder gegoogelt. 
#Von Streamlit.io haben wir teils auch gewisse Befehle nachgeschaut.


import streamlit as st
import pandas as pd
import os
import DosierungsrechnerDMLF as dosre
import json
from datetime import date
import altair as alt


st.title('Schmerzmitteldosierungstabelle für Kinder')

    
tab1, tab2 = st.tabs(["Fachperson", "Elternteil"])

with tab1:
    
    st.write("Unten finden Sie 4 verschiedene Schmerzmittelsirupe für Kinder im Alter von 1 bis 16 Jahren und einem Gewicht von 5 bis 60 kg, welche die Dosierung für das kranke Kind berechnen.")
    
    # Definierung einer Liste mit verfügbaren Sirup-Optionen
    sirup_options = ["Algifor Sirup", "Ben U Ron Sirup", "Dafalgan Sirup", "Irfen Sirup"]
    # Erstellung von Optionenfeld für den Sirup
    selected_sirup = st.selectbox("Wählen Sie ein Schmerzmittelsirup:", sirup_options)
   
    single_dose=()
    age = (0)
    weight = (0)
    
    if selected_sirup == 'Algifor Sirup':
        dosre.main_algifor(age, weight)
        dosre.calculate_max_dosage_algifor(single_dose) 
        dosre.calculate_single_dose_algifor(age, weight)
        
    if selected_sirup == 'Ben U Ron Sirup':

        dosre.calculate_max_dosage_benuron(single_dose)
        dosre.calculate_single_dose_benuron(age, weight)
        dosre.main_benuron(age, weight)
        
    if selected_sirup == 'Dafalgan Sirup':

        dosre.calculate_max_dosage_dafalgan(single_dose)
        dosre.calculate_single_dose_dafalgan(age, weight)
        dosre.main_dafalgan(age, weight)
        
    if selected_sirup == 'Irfen Sirup':

        dosre.calculate_max_dosage_irfen(single_dose)
        dosre.calculate_single_dose_irfen(age, weight)
        dosre.main_irfen(age, weight)


with tab2:
    st.write('Liebe Eltern, mit dieser App wird die Dosierung von Schmerzmittelsirupen für Ihr Kind berechnet.')
    ('Ausserdem gibt es ein Schmerzmitteltagebuch, welches Ihre Daten in einem Diagramm speichern kann. Dadurch können Sie sehen, wie viel Mililiter insgesamt Ihr Kind pro Tag an Schmerzmittelsirup eingenommen hat. Dies kann hilfreich sein, um den Fachleuten bei einem nächsten Arztbesuch oder Apothekenbesuch Informationen mitzuteilen.')

    tab3, tab4= st.tabs(["Schmerzmittelsirupe", "Schmerzmitteltagebuch"])

 
with tab3:
    st.header("Schmerzmittelsirupe")
    st.write("Unten finden Sie 4 verschiedene Schmerzmittelsirupe für Kinder im Alter von 1 bis 16 Jahren und einem Gewicht von 5 bis 60 kg, welche die Dosierung für das kranke Kind berechnen.")
    
    # Definierung einer Liste mit verfügbaren Sirup-Optionen
    sirup_options = ["Algifor Sirup ", "Ben U Ron Sirup ", "Dafalgan Sirup ", "Irfen Sirup "]
    # Erstellung von Optionenfeld für den Sirup
    selected_sirup = st.selectbox("Wählen Sie ein Schmerzmittelsirup:", sirup_options)
    
   
    if selected_sirup == 'Algifor Sirup ':

        dosre.calculate_max_dosage_algifor1(single_dose) 
        dosre.calculate_single_dose_algifor1(age, weight)
        dosre.main_algifor1(age, weight)


    if selected_sirup == 'Ben U Ron Sirup ':

        dosre.calculate_max_dosage_benuron1(single_dose)
        dosre.calculate_single_dose_benuron1(age, weight)
        dosre.main_benuron1(age, weight)
        

    if selected_sirup == 'Dafalgan Sirup ':

        dosre.calculate_max_dosage_dafalgan1(single_dose)
        dosre.calculate_single_dose_dafalgan1(age, weight)
        dosre.main_dafalgan1(age, weight)

   
    if selected_sirup == 'Irfen Sirup ':

        dosre.calculate_max_dosage_irfen1(single_dose)
        dosre.calculate_single_dose_irfen1(age, weight)
        dosre.main_irfen1(age, weight)
 
with tab4:
    st.header("Schmerzmitteltagebuch")
    st.write("Für einen neuen Tagebucheintrag notieren Sie den Namen des Kindes, wählen Sie das Einnahmedatum aus, bestimmen Sie den verwendeten Schmerzmittelsirup und tragen Sie die berechnete Schmerzmitteldosierung ein. Um den Tagebucheintrag zu überprüfen, wählen Sie den Namen des Kindes aus.")

    # Tabebucheingaben
    # Eingabefelder für den Namen der Person, den Tag, den Sirup und die Dosierung
    name_tagb = st.text_input('Name')
    datum_tagb = st.date_input('Datum', value=date.today())
    sirup_tagb = st.selectbox('Sirup', ('Algifor', 'Ben U Ron', 'Dafalgan', 'Irfen'))
    dosierung_tagb = st.number_input('Dosierung in ml')
    
    # Button zum Abspeichern des JSON-Objekts hinzufügen
    if st.button('Speichern'):
        # Dateiname erstellen (basierend auf dem Namen)
        tagebuch_name = f"{name_tagb.replace(' ', '_')}.json"
    
        # Prüfen, ob die Datei bereits vorhanden ist
        try:
            with open(tagebuch_name, 'r') as f:
                daten = json.load(f)
        except FileNotFoundError:
            daten = {}
    
        # Aktuallisierung oder neuen Eintrag im JSON-Objekt hinzufügen
        if sirup_tagb in daten and datum_tagb.strftime("%d.%m.%Y") in daten[sirup_tagb]:
            # Wenn der Eintrag bereits vorhanden ist, Dosierung aktuallisieren
            daten[sirup_tagb][datum_tagb.strftime("%d.%m.%Y")].append(dosierung_tagb)
        elif sirup_tagb in daten:
            # Wenn der Sirup-Eintrag bereits vorhanden ist, aber das Datum nicht übereinstimmt neur Datumseintrag hinzufügen
            daten[sirup_tagb][datum_tagb.strftime("%d.%m.%Y")] = [dosierung_tagb]
        else:
            # Wenn der Sirup-Eintrag noch nicht vorhanden ist, einen neuen Sirup-Eintrag erstellen
            daten[sirup_tagb] = {datum_tagb.strftime("%d.%m.%Y"): [dosierung_tagb]}
    
        # JSON-Datei speichern
        with open(tagebuch_name, 'w') as f:
            json.dump(daten, f)
    
        st.success('Informationen erfolgreich gespeichert!')
 
    # Tagebuchübersicht               
    st.subheader("Tagebuch Übersicht")
    
    # JSON-Dateien in aktuellem Verzeichnis suchen und nur diese anzeigen
    names = [filename for filename in os.listdir() if filename.endswith('.json')]
    
    # Liste von Dateinamen ohne ".json" Erweiterung
    options = [os.path.splitext(filename)[0] for filename in names]  
    
    if options:
        selected_name = st.selectbox('Name auswählen', options)
        with open(selected_name + ".json", 'r') as f:
            daten = json.load(f)

        # DataFrame erstellen
        data = []
        for sirup_tagb in ['Algifor', 'Ben U Ron', 'Dafalgan', 'Irfen']:
            if sirup_tagb in daten:
                for datum_tagb in daten[sirup_tagb].keys():
                    dosierung_tagb = sum(daten[sirup_tagb][datum_tagb])
                    data.append([pd.to_datetime(datum_tagb, format='%d.%m.%Y'), sirup_tagb, dosierung_tagb])
        df = pd.DataFrame(data, columns=['Datum', 'Sirup', 'Dosierung'])
                
        # Bar-Chart anzeigen
        bars = alt.Chart(df).mark_bar().encode(
            x=alt.X('Datum:T', axis=alt.Axis(title='Datum')),
            y=alt.Y('Dosierung:Q', axis=alt.Axis(title='Dosierung in ml')),
            color=alt.Color('Sirup:N', scale=alt.Scale(domain=['Algifor', 'Ben U Ron', 'Dafalgan', 'Irfen'], 
                                                      range=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']))
        ).properties(width=600, height=400)
        
        st.altair_chart(bars, use_container_width=True)

 


         
   
        