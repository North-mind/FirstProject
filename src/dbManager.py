#!/usr/bin/env python
# coding: utf-8

import sqlite3


def createDB():
    global dbFileName
    print("Open or create databese file.")
    dbFileName = input("Input database file name: ")
    return sqlite3.connect("{}.db".format(dbFileName))


def activateDB(dbName):
    global activeDB
    activeDB = dbName.cursor()


def runDB():
    global db
    db = createDB()
    activateDB(db)
    

def createTableWithID(tableName):
    sqlCreateTableSyntax = """
    CREATE TABLE {}(id INTEGER);
    """.format(tableName)
    
    activeDB.execute(sqlCreateTableSyntax)


def createColumn(tableName, columnName, columnType):
    sqlCreateColumnSyntax = """
    ALTER TABLE {}
    ADD {} {}
    """.format(tableName, columnName, columnType)
    
    activeDB.execute(sqlCreateColumnSyntax)
    db.commit()


### create dbHeaders example ###
dbHeaders = {
    'date':'DATE', 
    'category':'VARCHAR(30)',
    'title':'VARCHAR(200)', 
    'text':'VARCHAR(8000)',
    'author':'VARCHAR(40)'
}

for header in dbHeaders:
    createColumn('books', header, dbHeaders[header])

### end example ###

def setPrimaryKey(tableName, columnName):
    sqlPrimatyKeySyntx = """
    ALTER TABLE {} 
    ADD PRIMARY KEY ({});
    """.format(tableName, columnName)
    activeDB.execute(sqlPrimatyKeySyntax)


def dropTable(tableName):
    sqlDropTableSyntax = """
    DROP TABLE {}
    """.format(tableName)
    
    activeDB.execute(sqlDropTableSyntax)


def selectData(selectedColumn, tableName):
    sqlSelectSyntax = """
    SELECT {} FROM {}""".format(selectedColumn, tableName)
    
    activeDB.execute(sqlSelectSyntax)
    selectedData = activeDB.fetchall()
    return selectedData


def insertInTable(tableName, values):
    sqlInsertIntoSyntax = """
    INSERT INTO {}
    VALUES (?, ?, ?, ?, ?) 
    """.format(tableName)
     
    activeDB.executemany(sqlInsertIntoSyntax, values)

### example of data set ###

values = [(3, '2019-08-13 13:00:00', "sport", "Lewy blysnal", "Lewandowski strzelił 2 bramki Enerdze Cottbus"), 
          (4, '2019-08-13 13:10:00', "sport", "Milik nie zagral", "Arkadusz Milik nie wzial udziału w meczu towarzystkim z powodu kontuzji kolana")]

insertInTable('news', values)

### end example ###


def inputSqlStatement():
    sqlStatement = input("Input SQL Statement: ")
    activeDB.execute(sqlStatement)
    sqlStatementResult = activeDB.fetchall()
    return sqlStatementResult


def dbSaveAndClose():
    db.commit()
    db.close()
    return "{} was saved and closed".format(dbFileName)



