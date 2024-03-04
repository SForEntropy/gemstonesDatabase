import sqlite3

def delete_gemstone():
    try:
        
        conn = sqlite3.connect('Gemstones.db')
        cursor = conn.cursor()

        
        gemstone_name = input("Enter the name of the gemstone to be deleted: ")
        cursor.execute(f"SELECT * FROM stonesTable WHERE name = ?", (gemstone_name,))

        
        row = cursor.fetchone()

        if row is None:
            print(f"Delete is not possible as no record with the name {gemstone_name} exists!")
        else:
            cursor.execute("DELETE FROM stonesTable WHERE name = ?", (gemstone_name,))
            conn.commit()
            print(f"The record {gemstone_name} deleted from the stonesTable.")

    except sqlite3.OperationalError as e:
        print(f"Failed because of operational error: {e}")
    except sqlite3.ProgrammingError as pe:
        print(f"Failed because of programming error: {pe}")
    except sqlite3.Error as er:
        print(f"Failed because of error: {er}")
    finally:
        conn.close()

if __name__ == "__main__":
    delete_gemstone()  