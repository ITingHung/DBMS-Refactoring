class ModifiyFunc(object):
    def __init__(self, window):
        query = self.get_query(window)

        window.cursor.execute(query)
        window.connection.commit()
        window.display_result(f'SELECT * FROM {window.table_combo.get()}')

    def get_query(self, window):
        pass
