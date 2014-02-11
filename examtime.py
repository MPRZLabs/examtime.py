#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  examtime.py
#  
#  Copyright 2014 Unknown <michcioperz@LunaticArchitect>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sqlite3, logging
from datetime import date

def init():
	global rlog, conn, c, supstack
    rlog = logging.getLogger("examtime")
    rlog.setLevel(logging.DEBUG)
    rlogch = logging.StreamHandler()
    rlogch.setLevel(logging.DEBUG)
    rlogfm =  logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rlogch.setFormatter(rlogfm)
    rlog.addHandler(rlogch)
    rlogfh = logging.FileHandler('examtime.log')
    rlogfh.setFormatter(rlogfm)
    rlog.addHandler(rlogfh)
    rlog.info("Initializing SQLite database connection")
    conn = sqlite3.connect('examtime.sqlite')
    c = conn.cursor()
    supstack = []

def install():
    global rlog, c
    rlog.info("Performing initial queries")
    c.execute("CREATE TABLE IF NOT EXISTS lessons (schoolhour integer, subject text, teacher text)")
    c.execute("CREATE TABLE IF NOT EXISTS dayevents (year integer, month integer, day integer, target text)")
    c.execute("CREATE TABLE IF NOT EXISTS subjects (id text PRIMARY KEY)")
    c.execute("CREATE TABLE IF NOT EXISTS teachers (id text PRIMARY KEY)")
    c.execute("CREATE TABLE IF NOT EXISTS supress (subject text, year integer, month integer, day integer)")

def main():
	init()
	install()
	deinit()
	return 0

if __name__ == '__main__':
	main()

