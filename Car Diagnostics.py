import obd
import sqlite3

choice = int(input("What do wish to do? (1) Scan Automatic Code or (2) Enter Code Manually - "))

if choice == 1:
    connection = obd.OBD()
    obd2_code = connection.query(obd.commands.GET_DTC)
else:
    obd2_code = input("Enter OBD2 code: ")

conn = sqlite3.connect('obd2_codes.db')
c = conn.cursor()

c.execute("SELECT Fix FROM obd2_codes WHERE Code=?", (obd2_code,))
fixes = c.fetchall()

if fixes:
    print("Possible fixes for OBD2 code", obd2_code, ":")
    for fix in fixes:
        print(fix[0])
else:
    print("No fixes found for OBD2 code", obd2_code)

conn.close()