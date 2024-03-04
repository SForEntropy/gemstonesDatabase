import sqlite3

def read_gemstones():
    try:
       
        conn = sqlite3.connect('Gemstones.db')
        cursor = conn.cursor()

        
        cursor.execute("SELECT * FROM stonesTable")
        all_gemstones = cursor.fetchall()

        if all_gemstones:
            
            print("Name   |                Primary Color   |            Place Mined   |            Mohs Hardness")
            print("*" * 70)

            for gemstone in all_gemstones:
                print(f"{gemstone[0]:20} | {gemstone[1]:20} | {gemstone[2]:20} | {gemstone[3]:15}")
        else:
            print("No gemstone found in the stonesTable")

    except sqlite3.OperationalError as e:
        print(f"Failed because of operational error: {e}")
    except sqlite3.ProgrammingError as pe:
        print(f"Failed because of programming error: {pe}")
    except sqlite3.Error as er:
        print(f"Failed as error: {er}")

if __name__ == "__main__":
    read_gemstones()  