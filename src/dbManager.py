    
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
    CREATE TABLE {}(NewsId INTEGER NOT NULL, PRIMARY KEY (NewsId));
    """.format(tableName)
    
    activeDB.execute(sqlCreateTableSyntax)


def createColumn(tableName, columnName, columnType):
    sqlCreateColumnSyntax = """
    ALTER TABLE {}
    ADD {} {}
    """.format(tableName, columnName, columnType)
    activeDB.execute(sqlCreateColumnSyntax)
    db.commit()


def setPrimaryKey(tableName, columnName):
    sqlPrimaryKeySyntax = """
    ALTER TABLE {} 
    ADD PRIMARY KEY ({});
    """.format(tableName, columnName)
    activeDB.execute(sqlPrimaryKeySyntax)


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
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) 
    """.format(tableName)
    activeDB.executemany(sqlInsertIntoSyntax, values)


def inputSqlStatement():
    sqlStatement = input("Input SQL Statement: ")
    activeDB.execute(sqlStatement)
    sqlStatementResult = activeDB.fetchall()
    return sqlStatementResult


def dbSaveAndClose():
    db.commit()
    db.close()
    return "{} was saved and closed".format(dbFileName)



