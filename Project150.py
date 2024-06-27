import tkinter as tk
import random

root = tk.Tk()
root.geometry("400x400")
root.title("Country and Capital Lists")


country_entry = tk.Entry(root, width=30)
country_entry.place(x=100, y=20)

city_entry = tk.Entry(root, width=30)
city_entry.place(x=100, y=50)

# Labels
country_label = tk.Label(root, text="Country List:", anchor="w", justify="left")
country_label.place(x=100, y=140)

city_label = tk.Label(root, text="Capital List:", anchor="w", justify="left")
city_label.place(x=100, y=170)

random_country_label = tk.Label(root, text="Random Country:", anchor="w", justify="left")
random_country_label.place(x=100, y=250)

random_city_label = tk.Label(root, text="Random Capital:", anchor="w", justify="left")
random_city_label.place(x=100, y=280)

# Lists to store country and capital names
country_list = []
city_list = []

def append_names():
    country_name = country_entry.get()
    city_name = city_entry.get()
    
    country_list.append(country_name)
    city_list.append(city_name)
    
    
    country_label.config(text="\n".join(country_list))
    city_label.config(text="\n".join(city_list))


def generate_random():
    if country_list:
        random_country = random.choice(country_list)
        random_city = city_list[country_list.index(random_country)]
        
        random_country_label.config(text=random_country)
        random_city_label.config(text=random_city)
        
append_button = tk.Button(root, text="Display Country And City Name", command=append_names)
append_button.place(x=100, y=100)
        
generate_button = tk.Button(root, text="Display Country And City Name Randomly", command=generate_random)
generate_button.place(x=70, y=210)

root.mainloop()


