import datetime
import locale
import os
import csv

# Configurar el locale para formateo de moneda
try:
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, 'Spanish_Spain.1252')
    except locale.Error:
        pass

def format_currency(amount):
    """Formatea un valor como moneda"""
    try:
        return locale.currency(float(amount), grouping=True)
    except:
        return f"S/ {float(amount):.2f}"

def format_date(date):
    """Formatea una fecha en formato dd/mm/yyyy"""
    if isinstance(date, str):
        try:
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            return date
    return date.strftime("%d/%m/%Y")

def get_current_date():
    """Obtiene la fecha actual en formato yyyy-mm-dd"""
    return datetime.date.today().strftime("%Y-%m-%d")

def export_to_csv(data, filename, headers=None):
    """Exporta datos a un archivo CSV"""
    filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exports', filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if headers:
            writer.writerow(headers)
        writer.writerows(data)
    
    return filepath

def calculate_subtotal(price, quantity):
    """Calcula el subtotal de un producto"""
    return float(price) * int(quantity)