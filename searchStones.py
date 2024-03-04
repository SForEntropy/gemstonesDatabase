import sqlite3

def search_gemstone():
    try:
        
        conn = sqlite3.connect('Gemstones.db')
        cursor = conn.cursor()

        
        field = input("Search by name, primaryColour, placeMined, or mohs: ")

        if field in ["name", "primaryColour", "placeMined", "mohs"]:
           
            str_input = input(f"Enter the value for the field {field}: ")

            
            cursor.execute(f"SELECT * FROM stonesTable WHERE {field} LIKE ?", ('%' + str_input + '%',))

            rows = cursor.fetchall()  

            if not rows:
                print(f"No record(s) with field {field} matching {str_input}")
            else:
               
                for records in rows:
                    print(records)
        else:
           
            print(f"Search field {field} invalid!!!!")

    except sqlite3.OperationalError as e:
        print(f"Failed because of operational error: {e}")
    except sqlite3.ProgrammingError as pe:
        print(f"Failed because of programming error: {pe}")
    except sqlite3.Error as er:
        print(f"Failed because of error: {er}")
    finally:
        conn.close()

if __name__ == "__main__":
    search_gemstone()