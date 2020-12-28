import abc


class ModifiyFunc(object):
    def __init__(self, window):
        self.window = window
        self.query = self.get_query(window)
        self.modify()

    def modify(self):
        self.window.cursor.execute(self.query)
        self.window.connection.commit()
        self.window.display_result(f'SELECT * FROM {self.window.table_combo.get()}')

    @abc.abstractmethod
    def get_query(self, window):
        pass

