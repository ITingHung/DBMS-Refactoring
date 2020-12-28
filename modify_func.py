class ModifiyFunc(object):
    def __init__(self, window):
        self.window = window
        self.query = self.get_query(window)
        self.modify()

    def get_query(self, window):
        pass

    def modify(self):
        self.window.cursor.execute(self.query)
        self.window.connection.commit()
        self.window.display_result(f'SELECT * FROM {self.window.table_combo.get()}')

