import os
import sqlite3
import csv

if __name__ == "__main__":
    path = "C:\\Users\\swedwise\\Documents\\Formula 1 tables\\"
    files = ["circuits", "constructor_results", "constructor_standings", "driver_standings", "constructors",
             "drivers", "lap_times", "pit_stops", "qualifying", "races", "results", "seasons", "status"]

    con = sqlite3.connect("sqlite:///../../../formula1_database_tmp.db")
    cur = con.cursor()
    sql_file = open('generate_db.sql')
    sql_string = sql_file.read()
    cur.executescript(sql_string)
    for file in files:
        name = path + file + ".csv"
        print(name)
        with open(name, 'r', encoding='utf-8') as fin:
            reader = csv.reader(fin)
            cols = tuple(next(reader))
            fin.seek(0)
            # TODO: Add constraints to table!!
            # cur.execute(f"DROP TABLE {file};") # use your column names here  
            # cur.execute(f"CREATE TABLE {file} {(cols)};") # use your column names here  

            dr = csv.DictReader(fin)  # comma is default delimiter
            #to_db = [(i[col] for col in cols) for i in dr]
            to_db = []
            for row in dr:
                tmp = []
                for col in cols:
                    tmp.append(row[col])
                to_db.append(tmp)
            inj_prot = []
            for i in range(len(cols)):
                inj_prot.append('?')
            q = ', '.join(inj_prot)
            cur.executemany(f"INSERT INTO {file} {cols} VALUES ({q});", to_db)
    con.commit()
    con.close()
