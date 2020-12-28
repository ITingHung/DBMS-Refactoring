from modify_func import ModifiyFunc


class DeleteFunc(ModifiyFunc):
    def get_query(self, window):
        delete_value = {}
        condition = ''
        for i in range(len(window.table_columns)):
            delete_value[window.table_columns[i][0]] = window.entry[i].get()
            if delete_value[window.table_columns[i][0]] != '' and condition == '':
                condition = condition + \
                    str(f'{window.table_columns[i][0]}="{window.entry[i].get()}"')
            elif delete_value[window.table_columns[i][0]] != '':
                condition = condition + ' AND ' + \
                    str(f'{window.table_columns[i][0]}="{window.entry[i].get()}"')

        return f'DELETE FROM {window.table_combo.get()} WHERE {condition}'
