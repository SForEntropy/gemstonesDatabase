import sqlite3

def insert_gemstone():
    try:
       
        conn = sqlite3.connect('Gemstones.db')
        cursor = conn.cursor()

        
        name = input("Enter gemstone name: ")
        primary_color = input("Enter primary color: ")
        place_mined = input("Enter place mined: ")
        mohs = float(input("Enter Mohs hardness (use one decimal place e.g. 5.0): "))

        
        cursor.execute('''
            INSERT INTO stonesTable (name, primaryColour, placeMined, mohs)
            VALUES (?, ?, ?, ?)
        ''', (name, primary_color, place_mined, mohs))

        
        conn.commit()
        conn.close()

        print(f"{name} inserted into stonesTable.")
    except sqlite3.OperationalError as e:
        print(f"Failed because of operational error: {e}")
    except sqlite3.ProgrammingError as pe:
        print(f"Failed because of programming error: {pe}")
    except sqlite3.Error as er:
        print(f"Failed as error: {er}")

if __name__ == "__main__":
    insert_gemstone()  
