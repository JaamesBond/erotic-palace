import sqlite3
from flask import jsonify
from config import CONFIG


def dict_factory(cursor, row):
    fields = [ column[0] for column in cursor.description ]
    return {key: value for key, value in zip(fields, row)}


def get_db_connection():
    db_conn = sqlite3.connect(CONFIG["database"]["name"])
    db_conn.row_factory = dict_factory
    return db_conn


def read_all():
    ALL_GIRLS = "SELECT * FROM girls"

    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(ALL_GIRLS)
    result = cursor.fetchall()
    db_conn.close()

    return jsonify(result)


def create(girl):
    INSERT_GIRL = ("INSERT INTO girls (name, age, hair_colour, phone, boobs, ass, race, bmi, personality, services) "
                   "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(INSERT_GIRL, (girl["name"], girl["age"], girl["hair_colour"], girl["phone"], girl["boobs"], girl["ass"], girl["race"], girl["bmi"], girl["personality"], girl["services"]))
    db_conn.commit()
    new_girl_id = cursor.lastrowid
    cursor.close()

    return new_girl_id, 201


def read_girlById(id):
    ONE_GIRL = "SELECT * FROM girls WHERE id = ?"

    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(ONE_GIRL, (id,))
    result = cursor.fetchall()
    db_conn.close()

    if len(result) < 1:
        return "Not found", 404
    elif len(result) > 2:
        return "Too many girls!", 500

    return jsonify(result[0])


def read_girlByName(name):
    NAME_GIRL = "SELECT * FROM WHERE name = ?"

    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(NAME_GIRL, (name,))
    result = cursor.fetchall()

    return jsonify(result)


def update_girlById(id, girl):
    UPDATE_GIRL = """
    UPDATE girls
    SET age = ?,
    hair_colour = ?,
    phone = ?,
    boobs = ?,
    ass = ?,
    race = ?,
    bmi = ?,
    personality = ?,
    services = ?
    WHERE id = ?
    """

    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(UPDATE_GIRL, (girl['age'], girl['hair_colour'], girl['phone'], girl['boobs'], girl['ass'], girl['race'], girl['bmi'], girl['personality'], girl['services'], id))
    db_conn.commit()

    return read_girlById(id)


def delete_girlById(id):
    DELETE_GIRL = "DELETE FROM girls WHERE id = ?"

    db_conn = get_db_connection()
    cursor = db_conn.cursor()
    cursor.execute(DELETE_GIRL, (id,))
    db_conn.commit()

    return "Successfully deleted", 204
