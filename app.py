from datetime import datetime
from flask import Flask, render_template
import sqlite3
import math

app = Flask(__name__)

def calculeaza_media(note_dict):
    note_totale = []
    for lista in note_dict.values():
        for n in lista:
            note_totale.append(n['nota'])
    if note_totale:
        return round(sum(note_totale) / len(note_totale), 2)
    return None


@app.template_filter('format_date')
def format_date(value):
    luni = [
        '', 'ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie',
        'iulie', 'august', 'septembrie', 'octombrie', 'noiembrie', 'decembrie'
    ]
    try:
        date_obj = datetime.strptime(value, "%Y-%m-%d")
        return f"{date_obj.day} {luni[date_obj.month]} {date_obj.year}"
    except Exception:
        return value


@app.template_filter('round_to_integer')
def round_to_integer(value):
    """Rotunjește media la numărul întreg cel mai apropiat"""
    if value is None:
        return None
    
    # Rotunjire matematică standard
    # 9.50 → 10, 9.40 → 9, 9.60 → 10, etc.
    return round(value)


def get_note():
    conn = sqlite3.connect('catalog.db')
    c = conn.cursor()
    c.execute('''
        SELECT m.nume, n.nota, n.data
        FROM note n
        JOIN materii m ON n.materie_id = m.id
        WHERE n.elev_id = 1
        ORDER BY m.nume, n.data DESC
    ''')
    rows = c.fetchall()
    conn.close()
    
    data = {}
    for materie, nota, data_nota in rows:
        data.setdefault(materie, {'note': [], 'media': 0})
        data[materie]['note'].append({'nota': nota, 'data': data_nota})
    
    # Calculez media pentru fiecare materie
    medii_materii = []
    for materie in data:
        note = [n['nota'] for n in data[materie]['note']]
        if note:
            media = round(sum(note) / len(note), 2)
            data[materie]['media'] = media
            medii_materii.append(media)
    
    # Calculez media generală (media mediilor)
    media_generala = round(sum(medii_materii) / len(medii_materii), 2) if medii_materii else 0

    return data, media_generala




def get_absente():
    conn = sqlite3.connect('catalog.db')
    c = conn.cursor()
    c.execute('''
        SELECT m.nume, a.data, a.motivata
        FROM absente a
        JOIN materii m ON a.materie_id = m.id
        WHERE a.elev_id = 1
        ORDER BY a.data DESC
    ''')
    rows = c.fetchall()
    conn.close()
    absente_pe_materii = {}
    for materie, data, motivata in rows:
        absente_pe_materii.setdefault(materie, []).append({
            'data': data,
            'motivata': bool(motivata)
        })
    return absente_pe_materii

@app.route('/')
def note():
    note_pe_materii, media_generala = get_note()
    return render_template(
        'note.html',
        elev_nume="Țiplea Mariana-Alexandra",
        note=note_pe_materii,
        media_generala=media_generala
    )


@app.route('/absente')
def absente():
    absente_elev = get_absente()
    return render_template('absente.html', elev_nume="Țiplea Mariana-Alexandra", absente=absente_elev)

if __name__ == '__main__':
    app.run(debug=True)
