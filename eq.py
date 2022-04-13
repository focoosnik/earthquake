import requests
import sqlite3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import time
from functools import wraps
from tkinter import *
import uipyqt5


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
    mainform.statusBar().showMessage("Found EQ " + str(len(data['features'])))
    for i in range(0,len(data['features'])):
        place = data['features'][i]['properties']['place']
        mag = data['features'][i]['properties']['mag']
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
    #result_form.
    #result_box.delete(0,result_box.size())

    result_form = Tk()
    result_form.geometry('500x500')
    result_form.title(mainform.statusBar().currentMessage ())
    scrollbar = Scrollbar(result_form)
    scrollbar.pack(side=RIGHT, fill=Y)
    result_box = Listbox(result_form, yscrollcommand=scrollbar.set, height=30)

    result_box.pack(fill=BOTH, expand=1, padx=5, pady=5)
    scrollbar.config(command=result_box.yview)

    cursor.execute(select_query)
    for i in cursor.fetchall():
        result_box.insert(END, i)
    conn.commit()
    conn.close()
    result_form.mainloop()

def btn_clicked():
    params_dict['starttime'] = f'{mainform.dStarttime.date().year()}-' \
                               f'{mainform.dStarttime.date().month()}-'\
                               f'{mainform.dStarttime.date().day()}'
    params_dict['endtime'] = f'{mainform.dEndtime.date().year()}-' \
                               f'{mainform.dEndtime.date().month()}-'\
                               f'{mainform.dEndtime.date().day()}'
    mainform.statusBar().showMessage(params_dict['starttime'])
    params_dict['latitude'] = mainform.leLat.text().replace(',', '.')
    params_dict['longitude'] = mainform.leLong.text().replace(',', '.')
    params_dict['maxradiuskm'] = mainform.leMaxrad.text()
    params_dict['minmagnitude'] = str(mainform.cldMinMag.value()/10)
    save_eq('eq', request_eq(params_dict))
    if mainform.cbShowres.isChecked():
        print_eq_from_db('eq')


if __name__ == '__main__':
    app_main = QApplication(sys.argv)
    mainform = uipyqt5.MainForm()
    mainform.show()
    mainform.btnGet.clicked.connect(btn_clicked)
    sys.exit(app_main.exec_())
close_app = None





