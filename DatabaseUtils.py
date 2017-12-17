import sqlite3 as sql
from DatabaseConstants import DatabaseConstants
import DatabaseTestingUtils as dtu

dc = DatabaseConstants()
con = sql.connect(dc.databaseName)


# This function creates all necessary tables needed in the SQLite database.
def createTables():
    cur = con.cursor()
    cur.execute(dc.getAccountsTableCreateQuery())
    cur.execute(dc.getContactsTableCreateQuery())
    cur.execute(dc.getCreditCardsTableCreateQuery())
    cur.execute(dc.getPaymentsTableCreateQuery())
    cur.execute(dc.getInvoicesTableCreateQuery())
    con.commit()

# This function drops all non-system tables in the SQLite database. BE CAREFUL USING THIS FUNCTION!!!


def dropAllTables():
    cur = con.cursor()
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite%'")
    for row in cur.fetchall():
        query = "DROP TABLE IF EXISTS " + row[0]
        print(query)
        cur.execute(query)
        con.commit()

def selectAllFromTable(tableName):
    cur = con.cursor()
    cur.execute("SELECT * FROM " + tableName)
    return cur


def selectAllFromTableHTML(tableName):
    cur = selectAllFromTable(tableName)
    resultHTML = """<html lang="en"><head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="hi">
    <meta name="author" content="">
    <title>Flask Demo</title>
    <!-- Bootstrap Core CSS -->
    <link href="static/styles/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
    <table class="table table-striped">
    <thead>
    <tr>
    """
    columnNames = []
    for column in cur.description:
        resultHTML += "<th>" + column[0] + " </th> \n"
    resultHTML += "</tr></thead><tbody> \n"
    for row in cur:
        resultHTML += "<tr> \n"
        for column in row:
            resultHTML += "<td>" + str(column) + " </td> \n"
        resultHTML += "</tr> \n"
    resultHTML += "</tbody></table></div></body></html>"
    return resultHTML