import sqlite3

conn = sqlite3.connect('catalog.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS materii (
    id INTEGER PRIMARY KEY,
    nume TEXT UNIQUE
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS note (
    id INTEGER PRIMARY KEY,
    elev_id INTEGER,
    materie_id INTEGER,
    nota INTEGER,
    data TEXT,
    FOREIGN KEY (materie_id) REFERENCES materii(id)
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS absente (
    id INTEGER PRIMARY KEY,
    elev_id INTEGER,
    materie_id INTEGER,
    data TEXT,
    motivata INTEGER DEFAULT 0,
    FOREIGN KEY (materie_id) REFERENCES materii(id)
)
''')

c.execute("DELETE FROM note")
c.execute("DELETE FROM absente")
c.execute("DELETE FROM materii")

materii_demo = [
    ('Arte Vizuale și Abilități Practice',),
    ('Biologie',),
    ('Educație Antreprenorială',),
    ('Educație Muzicală',),
    ('Fizică',),
    ('Geografie',),
    ('Istoria Marii Britanii Și A Sua',),
    ('Informatică',),
    ('Istorie',),
    ('Psihologie',),
    ('Limba Engleză',),
    ('Limba Franceză',),
    ('Limba Română',),
    ('Matematică',),
    ('Purtare',),
    ('Religie',),
    ('Tehnologia Informației Și A Comunicațiilor',),
    ('Chimie',),
    ('Educație Fizică',)
]
c.executemany("INSERT INTO materii (nume) VALUES (?)", materii_demo)

def get_materie_id(nume):
    c.execute("SELECT id FROM materii WHERE nume = ?", (nume,))
    return c.fetchone()[0]

note_demo_raw = [
    (1, 'Arte Vizuale și Abilități Practice', 10, 1, '2025-03-18'),
    (1, 'Arte Vizuale și Abilități Practice', 10, 1, '2025-03-18'),
    (1, 'Arte Vizuale și Abilități Practice', 10, 1, '2024-12-17'),
    (1, 'Biologie', 6, 1, '2025-01-15'),
    (1, 'Biologie', 8, 1, '2024-02-5'),
    (1, 'Biologie', 9, 1, '2024-11-13'),
    (1, 'Biologie', 10, 1, '2024-09-26'),
    (1, 'Educație Antreprenorială', 10, 1, '2025-01-15'),
    (1, 'Educație Antreprenorială', 10, 1, '2025-02-14'),
    (1, 'Educație Fizică', 10, 1, '2025-02-03'),
    (1, 'Educație Fizică', 10, 1, '2024-12-09'),
    (1, 'Educație Fizică', 10, 1, '2024-10-17'),
    (1, 'Educație Muzicală', 10, 1, '2025-01-21'),
    (1, 'Educație Muzicală', 10, 1, '2024-12-10'),
    (1, 'Fizică', 10, 1, '2025-02-04'),
    (1, 'Fizică', 10, 1, '2024-11-29'),
    (1, 'Fizică', 9, 1, '2025-09-20'),
    (1, 'Geografie', 10, 1, '2025-03-31'),
    (1, 'Geografie', 9, 1, '2024-11-25'),
    (1, 'Istoria Marii Britanii Și A Sua',  10, 1, '2025-02-20'),
    (1, 'Istoria Marii Britanii Și A Sua',  10, 1, '2024-12-12'),
    (1, 'Istoria Marii Britanii Și A Sua',  10, 1, '2024-10-17'),
    (1, 'Informatică', 9, 1, '2024-11-14'),
    (1, 'Istorie',10,1,'2025-01-10'),
    (1, 'Istorie',10,1,'2024-11-15'),
    (1, 'Psihologie',10, 1,'2025-02-04'),
    (1, 'Psihologie',10, 1,'2024-12-10'),
    (1, 'Limba Engleză', 10,1,'2025-04-07'),
    (1, 'Limba Engleză', 10,1,'2025-04-04'),
    (1, 'Limba Engleză', 10,1,'2025-03-05'),
    (1, 'Limba Engleză', 10,1,'2024-12-02'),
    (1, 'Limba Engleză', 10,1,'2024-11-25'),
    (1, 'Limba Engleză', 7,1,'2024-10-11'),
    (1, 'Limba Engleză', 8,1,'2024-10-07'),
    (1, 'Limba Franceză', 8,1,'2025-02-20'),
    (1, 'Limba Franceză', 9,1,'2024-12-12'),
    (1, 'Limba Franceză', 10,1,'2024-10-17'),
    (1, 'Limba Română', 10,1,'2025-03-03'),
    (1, 'Limba Română', 10,1,'2025-01-27'),
    (1, 'Limba Română', 7,1,'2024-12-02'),
    (1, 'Limba Română', 8,1,'2024-10-15'),
    (1, 'Matematică',8,1,'2025-12-17'),
    (1, 'Matematică',7,1,'2025-11-19'),
    (1, 'Matematică',9,1,'2025-10-15'),
    (1, 'Purtare',10,1,'2025-02-21'),
    (1, 'Purtare',10,1,'2024-12-19'),
    (1, 'Purtare',10,1,'2025-10-25'),
    (1, 'Religie',10,1,'2025-04-04'),
    (1, 'Religie',10,1,'2025-03-23'),
    (1, 'Religie',10,1,'2025-12-13'),
    (1, 'Religie',10,1,'2025-11-10'),
    (1, 'Tehnologia Informației Și A Comunicațiilor',10,1,'2025-02-20'),
    (1, 'Tehnologia Informației Și A Comunicațiilor',10,1,'2024-12-12'),
    (1, 'Tehnologia Informației Și A Comunicațiilor',10,1,'2024-10-17'),
    (1, 'Chimie', 10, 1, '2025-02-20'),
    (1, 'Chimie', 8, 1, '2025-02-17'),
    (1, 'Chimie', 8, 1, '2024-10-14'),
#nou
    (1, 'Chimie', 7, 1, '2025-05-19'),
    (1, 'Biologie', 8, 1, '2025-04-10'),
    (1, 'Geografie', 10, 1, '2025-05-12'),
    (1, 'Limba Franceză', 7,1,'2025-04-10'),
    (1, 'Matematică', 7,1,'2025-01-28'),
    (1, 'Psihologie', 10,1, '2025-04-09')
]

note_demo = []
for elev_id, materie, nota, count, data in note_demo_raw:
    materie_id = get_materie_id(materie)
    for i in range(count):
        note_demo.append((elev_id, materie_id, nota, data))

c.executemany("INSERT INTO note (elev_id, materie_id, nota, data) VALUES (?, ?, ?, ?)", note_demo)
# 1 e bun
absente_demo_raw = [
    (1, 'Biologie', '2025-05-05', 0),
    (1, 'Biologie', '2025-04-03', 1),
    (1, 'Biologie', '2025-04-02', 1),
    (1, 'Biologie', '2025-03-27', 1),
    (1, 'Biologie', '2025-03-12', 1),
    (1, 'Biologie', '2025-01-23', 1),
    (1, 'Biologie', '2025-01-22', 1),
    (1, 'Biologie', '2025-01-16', 1),
    (1, 'Biologie', '2025-01-09', 0),
    (1, 'Biologie', '2024-12-04', 0),
    (1, 'Biologie', '2024-11-21', 1),
    (1, 'Biologie', '2024-11-20', 1),
    (1, 'Biologie', '2024-10-03', 1),
    (1, 'Biologie', '2024-10-02', 1),
    (1, 'Chimie', '2025-04-03', 1),
    (1, 'Chimie', '2025-03-27', 1),
    (1, 'Chimie', '2025-02-13', 1),
    (1, 'Chimie', '2025-02-10', 1),
    (1, 'Chimie', '2024-11-21', 1),
    (1, 'Educație Fizică', '2025-04-28', 0),
    (1, 'Educație Fizică', '2025-03-31', 0),
    (1, 'Educație Fizică', '2025-03-10', 1),
    (1, 'Educație Fizică', '2025-02-13', 1),
    (1, 'Educație Fizică', '2025-01-20', 1),
    (1, 'Educație Fizică', '2024-11-21', 1),
    (1, 'Educație Fizică', '2024-10-03', 1),
    (1, 'Educație Fizică', '2024-09-30', 1),
    (1, 'Arte Vizuale și Abilități Practice', '2025-03-10', 1),
    (1, 'Educație Antreprenorială', '2025-03-12', 1),
    (1, 'Educație Antreprenorială', '2025-02-12', 1),
    (1, 'Educație Antreprenorială', '2025-01-22', 1),
    (1, 'Educație Muzicală', '2025-03-11', 1),
    (1, 'Fizică', '2025-04-04', 1),
    (1, 'Fizică', '2025-04-02', 1),
    (1, 'Fizică', '2025-04-01', 1),
    (1, 'Fizică', '2025-03-11', 1),
    (1, 'Fizică', '2025-02-14', 1),
    (1, 'Fizică', '2025-02-12', 1),
    (1, 'Fizică', '2024-10-04', 1),
    (1, 'Fizică', '2024-10-02', 1),
    (1, 'Fizică', '2024-10-01', 1),
    (1, 'Geografie', '2025-03-10', 1),
    (1, 'Geografie', '2025-01-20', 1),
    (1, 'Geografie', '2024-09-30', 1),
    (1, 'Istoria Marii Britanii Și A Sua', '2025-03-27', 1),
    (1, 'Istoria Marii Britanii Și A Sua', '2025-02-12', 1),
    (1, 'Istoria Marii Britanii Și A Sua', '2025-01-23', 1),
    (1, 'Istoria Marii Britanii Și A Sua', '2024-11-21', 1),
    (1, 'Istoria Marii Britanii Și A Sua', '2024-10-03', 1),
    (1, 'Informatică', '2025-05-05', 0),
    (1, 'Informatică', '2025-04-03', 1),
    (1, 'Informatică', '2025-04-02', 1),
    (1, 'Informatică', '2025-03-10', 1),
    (1, 'Istorie', '2024-11-21', 1),
    (1, 'Limba Engleză', '2025-04-28', 0),
    (1, 'Limba Engleză', '2025-04-28', 0),
    (1, 'Limba Engleză', '2025-04-02', 1),
    (1, 'Limba Engleză', '2025-03-31', 0),
    (1, 'Limba Engleză', '2025-03-31', 0),
    (1, 'Limba Engleză', '2025-03-10', 1),
    (1, 'Limba Engleză', '2025-02-12', 1),
    (1, 'Limba Engleză', '2025-01-22', 1),
    (1, 'Limba Engleză', '2025-01-20', 1),
    (1, 'Limba Engleză', '2025-01-17', 1),
    (1, 'Limba Engleză', '2024-11-22', 1),
    (1, 'Limba Engleză', '2024-11-20', 1),
    (1, 'Limba Engleză', '2024-10-04', 1),
    (1, 'Limba Engleză', '2024-09-30', 1),
    (1, 'Limba Engleză', '2024-10-02', 1),
    (1, 'Limba Franceză', '2025-04-03', 1),
    (1, 'Limba Franceză', '2025-04-01', 1),
    (1, 'Limba Franceză', '2025-03-27', 1),
    (1, 'Limba Franceză', '2025-01-21', 1),
    (1, 'Limba Franceză', '2025-01-16', 1),
    (1, 'Limba Franceză', '2024-11-21', 1),
    (1, 'Limba Franceză', '2024-11-19', 1),
    (1, 'Limba Franceză', '2024-10-03', 1),
    (1, 'Limba Franceză', '2024-10-01', 1),
    (1, 'Limba Română', '2025-04-28', 0),
    (1, 'Limba Română', '2025-04-04', 1),
    (1, 'Limba Română', '2025-04-01', 1),
    (1, 'Limba Română', '2025-03-31', 0),
    (1, 'Limba Română', '2025-03-11', 1),
    (1, 'Limba Română', '2025-03-10', 1),
    (1, 'Limba Română', '2025-02-14', 1),
    (1, 'Limba Română', '2025-01-21', 1),
    (1, 'Limba Română', '2025-01-20', 1),
    (1, 'Limba Română', '2025-01-17', 1),
    (1, 'Limba Română', '2024-11-19', 1),
    (1, 'Limba Română', '2024-10-04', 1),
    (1, 'Limba Română', '2024-10-01', 1),
    (1, 'Limba Română', '2024-9-30', 1),
    (1, 'Matematică', '2025-05-06', 0),
    (1, 'Matematică', '2025-04-03', 1),
    (1, 'Matematică', '2025-04-02', 1),
    (1, 'Matematică', '2025-04-01', 1),
    (1, 'Matematică', '2025-03-27', 1),
    (1, 'Matematică', '2025-03-11', 1),
    (1, 'Matematică', '2025-02-13', 1),
    (1, 'Matematică', '2025-02-10', 1),
    (1, 'Matematică', '2025-01-22', 1),
    (1, 'Matematică', '2025-01-20', 1),
    (1, 'Matematică', '2025-01-16', 1),
    (1, 'Religie', '2025-02-14', 1),
    (1, 'Religie', '2024-11-22', 1),
    (1, 'Religie', '2024-10-04', 1),
    (1, 'Tehnologia Informației Și A Comunicațiilor', '2025-01-21', 1),
    (1, 'Psihologie', '2025-03-11', 1),
# Nou
    (1, 'Matematică', '2025-05-12', 1),
    (1, 'Matematică', '2025-05-13', 1),
    (1, 'Matematică', '2025-05-14', 1),
    (1, 'Matematică', '2025-05-15', 1),
    # Biologie
    (1, 'Biologie', '2025-05-14', 1),
    (1, 'Biologie', '2025-05-15', 1),
    # Informatică
    (1, 'Informatică', '2025-05-15', 1),
    # Educație Fizică
    (1, 'Educație Fizică', '2025-05-12', 1),
    (1, 'Educație Fizică', '2025-05-15', 1),
    # Limba Engleză
    (1, 'Limba Engleză', '2025-05-09', 1),
    (1, 'Limba Engleză', '2025-05-12', 1),
    (1, 'Limba Engleză', '2025-05-12', 1),
    (1, 'Limba Engleză', '2025-05-14', 1),
    (1, 'Limba Engleză', '2025-05-14', 1),
    (1, 'Limba Engleză', '2025-05-16', 1),
    # Limba Română
    (1, 'Limba Română', '2025-05-09', 1),
    (1, 'Limba Română', '2025-05-12', 1),
    (1, 'Limba Română', '2025-05-13', 1),
    (1, 'Limba Română', '2025-05-16', 1),
    # Fizică
    (1, 'Fizică', '2025-05-09', 1),
    (1, 'Fizică', '2025-05-13', 1),
    (1, 'Fizică', '2025-05-14', 1),
    (1, 'Fizică', '2025-05-16', 1),
    # Chimie
    (1, 'Chimie', '2025-05-12', 1),
    (1, 'Chimie', '2025-05-15', 1),
    # Limba Franceză
    (1, 'Limba Franceză', '2025-05-13', 1),
    (1, 'Limba Franceză', '2025-05-15', 1),
    # Istoria Marii Britanii Și A Sua
    (1, 'Istoria Marii Britanii Și A Sua', '2025-05-15', 1),
    # Religie
    (1, 'Religie', '2025-05-09', 1),
    (1, 'Religie', '2025-05-16', 1),
    # Istorie
    (1, 'Istorie', '2025-05-16', 1),
]


absente_demo = [
    (elev_id, get_materie_id(materie), data, motivata)
    for elev_id, materie, data, motivata in absente_demo_raw
]

c.executemany("INSERT INTO absente (elev_id, materie_id, data, motivata) VALUES (?, ?, ?, ?)", absente_demo)

conn.commit()
conn.close()
