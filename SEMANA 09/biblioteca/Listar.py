# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:10:42 2022

@author: ANTONY
"""

import sqlite3

conexion=sqlite3.connect("bdbiblioteca.db")
cursor=conexion.cursor()
consulta = """ SELECT *
             FROM LIBRO
             WHERE
                  precio>=55
            ORDER BY titulo
           """
cursor= conexion.cursor()
cursor.execute(consulta)

libros = cursor.fetchall()
# Aca libros es una lista...... entonces

for libro in libros:
    print(libro)
conexion.close()