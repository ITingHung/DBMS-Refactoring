from modify_func import ModifiyFunc


class InsertFunc(ModifiyFunc):
    def get_query(self, window):
        insert_value = []
        for i in range(len(self.entry)):
            insert_value.append(self.entry[i].get())

        return f'INSERT INTO {window.table_combo.get()} VALUES{tuple(insert_value)}'
