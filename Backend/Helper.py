import Database

def test():
    con = Database.create_connection('example.db')
    status = Database.create_account(con, 'la', 1234, 'asdsdgds')
    print(status)
    print(Database.get_account(con, 'la'))