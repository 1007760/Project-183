from tkinter import *
import requests
import json
root = Tk()
root.title("Project 183")
root.geometry("500x500")
root.configure(bg = "teal")

city_name_label = Label(root, text = "Captial city name", font = ("Bahnschrift Light", 15, "bold"), bg = "teal")
city_name_label.place(relx = 0.5, rely = 0.1, anchor = CENTER)
city_entry = Entry(root)
city_entry.place(relx = 0.5, rely = 0.2, anchor = CENTER)
country_name = Label(root, text = "Country : ", font = ("Helvetica", 15))
region_name = Label(root, text = "Region : ", font = ("Helvetica", 15))
region_name.place(relx = 0.5, rely = 0.4, anchor = CENTER)
country_name.place(relx = 0.5, rely = 0.3, anchor = CENTER)
language_name = Label(root, text = "Language : ", font = ("Helvetica", 15))
language_name.place(relx = 0.5, rely = 0.5, anchor = CENTER)
population_amount = Label(root, text = "Population : ", font = ("Helvetica", 15))
population_amount.place(relx = 0.5, rely = 0.6, anchor = CENTER)
area_size = Label(root, text = "Area : ", font = ("Helvetica", 15))
area_size.place(relx = 0.5, rely = 0.7, anchor = CENTER)

def city_details() :
    api_request = requests.get("https://restcountries.com/v2/capital/" + city_entry.get())
    api_output_json = json.loads(api_request.content)
    country = api_output_json[0]['name']
    reg = api_output_json[0]['region']
    lang = api_output_json[0]['languages']
    popn = api_output_json[0]['population']
    country_area = api_output[0]['area']
    country_name['text'] = "Country : " + country
    region_name['text'] = "Region : " + reg
    language_name['text'] = "Language : " + lang
    population_amount['text'] = "Population : " + popn
    area_size['text'] = "Area : " + country_area

btn = Button(root, text = "City details : ", relief = FLAT, command = city_details(), bg = teal)
btn.place(relx = 0.5, rely = 0.8, anchor = CENTER)
root.mainloop()