import requests
import sqlite3
from time import time
from functools import wraps
from tkinter import *

main_form = Tk()
main_form.geometry('500x500')
main_form.title('Found EQs')
params_dict = {'format':'geojson',
               'starttime':'2019-01-01',
               'endtime':'2019-05-01',
               'latitude':'51.51',
               'longitude':'-0.12',
               'maxradiuskm':'2000',
               'minmagnitude':'2'
}

def speed_test(function):
    @wraps(function)
    def wrap(*args, **kwargs):
        s_time = time
        result = function(*args, **kwargs)
        e_time = time
        return result
    return wrap


def request_eq(params):
    results_eq = []
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"
    response = requests.get(url, headers={'Accept': 'application/json'}, params=params)
    data = response.json()
    print("Found EQ " + str(len(data['features'])))
    for i in range(0,len(data['features'])):
        place = data['features'][i]['properties']['place']
        mag = data['features'][i]['properties']['mag']
        # print(f'{i}. Place {place} with {mag}')
        results_eq.append((i, place, mag))
    return results_eq


def save_eq(table_name, result_data):
    conn = sqlite3.connect("results_eq.db")
    cursor = conn.cursor()
    create_query = f"CREATE TABLE {table_name} (id INT, place TEXT, mag FLOAT);"
    into_query = f"INSERT INTO {table_name} VALUES (?, ?, ?);"
    try:
        cursor.execute(create_query)
    except sqlite3.OperationalError:
        cursor.execute(f"DROP TABLE {table_name }")
        cursor.execute(create_query)
    cursor.executemany(into_query, result_data)
    conn.commit()
    conn.close()


def print_eq_from_db(table_name):
    conn = sqlite3.connect("results_eq.db")
    cursor = conn.cursor()
    select_query = f"SELECT * FROM {table_name};"
    result_box = Listbox(main_form)
    result_box.pack(fill=X)
    cursor.execute(select_query)
    for i in cursor.fetchall():
        result_box.insert(END, i)
    print(cursor.fetchall())
    conn.commit()
    conn.close()


close_app = None
while close_app !='0':
    # params_dict['starttime'] = str(input("Enter the start time yyyy-mm-dd(example: 2019-01-01)= "))
    # params_dict['endtime'] = str(input("Enter the start time yyyy-mm-dd(example: 2019-05-01)= "))
    # params_dict['latitude'] = str(input("Enter the latitude (example: 51.51)= "))
    # params_dict['longitude'] = str(input("Enter the longitude (example: -0.12)= "))
    # params_dict['maxradiuskm'] = str(input("Enter the max radius in km (example: 2000)= "))
    # params_dict['minmagnitude'] = str(input("Enter the min magnitude (example: 2)= "))
    filename = input ('Enter tablename for results: ')
    save_eq(filename, request_eq(params_dict))
    print_eq_from_db(filename)
    main_form.mainloop()
    close_app = str(input('Enter "0" for close APP or any key for continue  '))




