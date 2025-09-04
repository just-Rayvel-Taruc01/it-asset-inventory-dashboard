
# Database utility functions using SQLite
import sqlite3

DB_PATH = '../../db/asset_inventory.db'

def get_conn():
    return sqlite3.connect(DB_PATH)

# DEVICE CRUD
def insert_device(device_row):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO devices (asset_tag, device_type, model, os, location, department, owner, purchase_date, status, decommission_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tuple(device_row))
    conn.commit()
    conn.close()

def get_devices():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM devices")
    rows = cur.fetchall()
    conn.close()
    return rows

def update_device(device_id, update_dict):
    conn = get_conn()
    cur = conn.cursor()
    set_clause = ', '.join([f"{k}=?" for k in update_dict.keys()])
    values = list(update_dict.values()) + [device_id]
    cur.execute(f"UPDATE devices SET {set_clause} WHERE id=?", values)
    conn.commit()
    conn.close()

def delete_device(device_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM devices WHERE id=?", (device_id,))
    conn.commit()
    conn.close()

# SOFTWARE CRUD
def insert_software(software_row):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO software (name, version, vendor)
        VALUES (?, ?, ?)
    """, tuple(software_row))
    conn.commit()
    conn.close()

def get_software():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM software")
    rows = cur.fetchall()
    conn.close()
    return rows

def update_software(software_id, update_dict):
    conn = get_conn()
    cur = conn.cursor()
    set_clause = ', '.join([f"{k}=?" for k in update_dict.keys()])
    values = list(update_dict.values()) + [software_id]
    cur.execute(f"UPDATE software SET {set_clause} WHERE id=?", values)
    conn.commit()
    conn.close()

def delete_software(software_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM software WHERE id=?", (software_id,))
    conn.commit()
    conn.close()

# LICENSE CRUD
def insert_license(license_row):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO licenses (software_id, license_key, expiration_date, renewal_status, assigned_user)
        VALUES (?, ?, ?, ?, ?)
    """, tuple(license_row))
    conn.commit()
    conn.close()

def get_licenses():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM licenses")
    rows = cur.fetchall()
    conn.close()
    return rows

def update_license(license_id, update_dict):
    conn = get_conn()
    cur = conn.cursor()
    set_clause = ', '.join([f"{k}=?" for k in update_dict.keys()])
    values = list(update_dict.values()) + [license_id]
    cur.execute(f"UPDATE licenses SET {set_clause} WHERE id=?", values)
    conn.commit()
    conn.close()

def delete_license(license_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM licenses WHERE id=?", (license_id,))
    conn.commit()
    conn.close()
