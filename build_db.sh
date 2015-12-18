#!/bin/bash

DB=autolama.db

sqlite3 $DB < create_lama.sql
