from kivy.lang import Builder
from kivymd.app import MDApp
import mysql.connector
from kivy.uix.screenmanager import ScreenManager, Screen # Dodawanie wielu okien

class FirstWindow(Screen):
    pass

class SecondCheckWindow(Screen):
    pass

class SecondMenuWindow(Screen):
    pass

class KatnatarciaWindow(Screen):
    pass

class KsztaltWindow(Screen):
    pass

class RodzajWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('main.kv')

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Define DB Stuff
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password123",
            database = "second_db",
            )


        # Create A Cursor
        c = mydb.cursor()

        # Create an actual database
        c.execute("CREATE DATABASE IF NOT EXISTS second_db")

        # Check to see if database was created
        c.execute("SHOW DATABASES")
        for db in c:
            print(db)

        # Drop table
        #c.execute("DROP TABLE plytki")

        # Create A Table
        c.execute("""CREATE TABLE if not exists kształt_plytki(
            oznaczenie      VARCHAR(2),
            opis            VARCHAR(250))
        """)

        c.execute("""CREATE TABLE if not exists katnatarcia_plytki(
                    oznaczenie      VARCHAR(2),
                    opis            VARCHAR(250))
                """)

        c.execute("""CREATE TABLE if not exists rodzaj_plytki(
                            oznaczenie      VARCHAR(2),
                            opis            VARCHAR(250))
                        """)

        c.execute("""CREATE TABLE if not exists tolerancja_plytki(
                                    oznaczenie      VARCHAR(2),
                                    ic              VARCHAR(250),
                                    grubosc         VARCHAR(10))
                                """)

        # Check to see if table created
        c.execute("SELECT * from kształt_plytki")

        print(c.description)

        # Commit changes
        # mydb.commit()

        # Close connection
        # mydb.close()

        return kv

    def submit(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password123",
            database = "second_db",
            )

        # Create A Cursor
        c = mydb.cursor()

        # Add A Record
        sql_command = "INSERT INTO kształt_plytki (oznaczenie, opis) VALUES (%s, %s)"
        value = (self.root.ids.ksztalt.ids.word_input.text,self.root.ids.ksztalt.ids.word_input2.text, )

        # Exceute SQL Command
        c.execute(sql_command, value)


        # Add a message
        self.root.ids.ksztalt.ids.word_label_dodaj.text = f'{self.root.ids.ksztalt.ids.word_input.text} Added'

        # Clear the input box
        self.root.ids.ksztalt.ids.word_input.text = ''
        self.root.ids.ksztalt.ids.word_input2.text = ''


        # Commit changes
        mydb.commit()

        # Close connection
        mydb.close()

    def submit_kat_natarcia(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password123",
            database = "second_db",
            )

        # Create A Cursor
        c = mydb.cursor()

        # Add A Record
        sql_command = "INSERT INTO katnatarcia_plytki (oznaczenie, opis) VALUES (%s, %s)"
        value = (self.root.ids.katnatarcia.ids.word_input.text,self.root.ids.katnatarcia.ids.word_input2.text, )

        # Exceute SQL Command
        c.execute(sql_command, value)


        # Add a message
        self.root.ids.katnatarcia.ids.word_label_dodaj_katnatarcia.text = f'{self.root.ids.katnatarcia.ids.word_input.text} Added'

        # Clear the input box
        self.root.ids.katnatarcia.ids.word_input.text = ''
        self.root.ids.katnatarcia.ids.word_input2.text = ''


        # Commit changes
        mydb.commit()

        # Close connection
        mydb.close()

    def submit_rodzaj(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password123",
            database = "second_db",
            )

        # Create A Cursor
        c = mydb.cursor()

        # Add A Record
        sql_command = "INSERT INTO rodzaj_plytki (oznaczenie, opis) VALUES (%s, %s)"
        value = (self.root.ids.rodzaj.ids.word_input.text,self.root.ids.rodzaj.ids.word_input2.text, )

        # Exceute SQL Command
        c.execute(sql_command, value)


        # Add a message
        self.root.ids.rodzaj.ids.word_label_dodaj_rodzaj.text = f'{self.root.ids.rodzaj.ids.word_input.text} Added'

        # Clear the input box
        self.root.ids.rodzaj.ids.word_input.text = ''
        self.root.ids.rodzaj.ids.word_input2.text = ''


        # Commit changes
        mydb.commit()

        # Close connection
        mydb.close()

    def submit_tolerancja(self):
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password123",
            database = "second_db",
            )

        # Create A Cursor
        c = mydb.cursor()

        # Add A Record
        sql_command = "INSERT INTO tolerancja_plytki (oznaczenie, ic, grubosc) VALUES (%s, %s, %s)"
        value = (self.root.ids.tolerancja.ids.word_input.text,self.root.ids.tolerancja.ids.word_input2.text,self.root.ids.tolerancja.ids.word_input4.text, )

        # Exceute SQL Command
        c.execute(sql_command, value)


        # Add a message
        self.root.ids.tolerancja.ids.word_label_dodaj_rodzaj.text = f'{self.root.ids.tolerancja.ids.word_input.text} Added'

        # Clear the input box
        self.root.ids.tolerancja.ids.word_input.text = ''
        self.root.ids.tolerancja.ids.word_input2.text = ''
        self.root.ids.tolerancja.ids.word_input4.text = ''


        # Commit changes
        mydb.commit()

        # Close connection
        mydb.close()
    def show_records(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password123",
            database="second_db",
        )

        # Create A Cursor
        c = mydb.cursor()

        # Grab records from database
        c.execute("SELECT * FROM kształt_plytki")
        records = c.fetchall()

        word = ''
        # Loop for records
        for record in records:
            word = f'{word}\n{record}'
            self.root.ids.ksztalt.ids.word_label_dodaj.text = f'{word}'

        # Commit changes
        mydb.commit()

        # Close connection
        mydb.close()

    def show_records_natarcia(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password123",
            database="second_db",
        )

        # Create A Cursor
        c = mydb.cursor()

        # Grab records from database
        c.execute("SELECT * FROM katnatarcia_plytki")
        records = c.fetchall()

        word = ''
        # Loop for records
        for record in records:
            word = f'{word}\n{record}'
            self.root.ids.katnatarcia.ids.word_label_dodaj_katnatarcia.text = f'{word}'

        # Commit changes
        mydb.commit()

        # Close connection
        mydb.close()

    def show_records_rodzaj(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password123",
            database="second_db",
        )

        # Create A Cursor
        c = mydb.cursor()

        # Grab records from database
        c.execute("SELECT * FROM rodzaj_plytki")
        records = c.fetchall()

        word = ''
        # Loop for records
        for record in records:
            word = f'{word}\n{record}'
            self.root.ids.rodzaj.ids.word_label_dodaj_rodzaj.text = f'{word}'

        # Commit changes
        mydb.commit()

        # Close connection
        mydb.close()

    def show_records_tolerancja(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password123",
            database="second_db",
        )

        # Create A Cursor
        c = mydb.cursor()

        # Grab records from database
        c.execute("SELECT * FROM rodzaj_plytki")
        records = c.fetchall()

        word = ''
        # Loop for records
        for record in records:
            word = f'{word}\n{record}'
            self.root.ids.rodzaj.ids.word_label_dodaj_rodzaj.text = f'{word}'

        # Commit changes
        mydb.commit()

        # Close connection
        mydb.close()

    def check(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password123",
            database="second_db",
        )

        # Create A Cursor
        c = mydb.cursor()

        # Działa indeksowanie jak po tablicy/stringu
        value = self.root.ids.second_check.ids.word_input3.text
        # Grab records from database
        sql_query = """SELECT opis FROM kształt_plytki WHERE oznaczenie = %s"""
        try:
            c.execute(sql_query, (value,))
            record = c.fetchone()
            # nie chcąc otrzymać w odpowiedzi ('cos') tylko cos to trzeba dać indeks [0]
            self.root.ids.second_check.ids.word_label.text = f'Jest to {record[0]}'
        except TypeError:
            self.root.ids.second_check.ids.word_label.text = f'Nie znaleziono podanego kodu płytki w bazie danych, sprawdź poprawność ' \
                                            f'wpisanych danych i spróbuj jeszcze raz'

        # Commit changes
        mydb.commit()

        # Close connection
        mydb.close()

MainApp().run()

