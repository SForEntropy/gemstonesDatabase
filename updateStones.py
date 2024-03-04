import sqlite3

def update_gemstone():
    try:
      
        conn = sqlite3.connect('Gemstones.db')
        cursor = conn.cursor()

        
        gemstone_name = input("Enter the name of the gemstone to be updated: ")
        cursor.execute(f"SELECT * FROM stonesTable WHERE name = ?", (gemstone_name,))

        
        row = cursor.fetchone()

       
        if row is None:
            print(f"No record with the name {gemstone_name} exists.")
        else:
            field_name = input("Enter the field (name, primaryColour, placeMined, mohs) to be updated: ").title()
            field_value = input(f"Enter the new value for {field_name}: ")

            
            cursor.execute(f"UPDATE stonesTable SET {field_name} = ? WHERE name = ?", (field_value, gemstone_name))
            conn.commit()
            print(f"Record with name {gemstone_name} Updated.")

    except sqlite3.OperationalError as e:
        print(f"Failed because of operational error: {e}")
    except sqlite3.ProgrammingError as pe:
        print(f"Failed because of programming error: {pe}")
    except sqlite3.Error as er:
        print(f"Failed because of error: {er}")
    finally:
        conn.close()

if __name__ == "__main__":
    update_gemstone()  