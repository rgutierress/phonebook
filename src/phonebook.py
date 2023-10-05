class Phonebook:

    def __init__(self):
        self.entries = {
                'POLICIA': '190',
                'BOMBEIRO': '193'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name:
            return 'Nome inválido'
        if '@' in name:
            return 'Nome inválido'
        if '!' in name:
            return 'Nome inválido'
        if '$' in name:
            return 'Nome inválido'
        if '%' in name:
            return 'Nome inválido'

        if len(name.strip()) == 0:
            return "Nome inválido"

        if len(number) == 0:
            return 'Número inválido'

        ##verifica se a string é vazia ou nula
        if name not in self.entries:
            self.entries[name] = number
            return 'Número adicionado'
        else:
            return 'Nome já existe'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if '#' in name:
            return 'Nome inválido'
        if '@' in name:
            return 'Nome inválido'
        if '!' in name:
            return 'Nome inválido'
        if '$' in name:
            return 'Nome inválido'
        if '%' in name:
            return 'Nome inválido'
        if name in self.entries:
            return self.entries[name]
        else:
            return 'Nome inválido'

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return list(self.entries.keys())

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        ##Alterado para retornar a lista de valores
        return list(self.entries.values())

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'Phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append((name, number))
        return result

    def get_phonebook_sorted(self):
        """
        # Correção: Incluir a ordenação da lista, hoje não ocorre
        :return: return phonebook in sorted order
        """
        sorted_entries = sorted(self.entries.items(), key=lambda x: x[0])
        return sorted_entries

    def get_phonebook_reverse(self):
        """
        # Correção: Incluir a ordenação da lista reversa que não ocorre
        :return: return phonebook in reverse sorted order
        """
        sorted_entries = sorted(self.entries.items(), key=lambda x: x[0], reverse=True)
        return sorted_entries

    def delete(self, name):
        """
         # Correção: Incluir validação para nome não identificado

        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        if name is None:
            return 'Nome não pode ser None'
        elif not isinstance(name, str):
            return 'Nome deve ser string'
        elif name == '':
            return 'Nome não pode ser vazio'

        if name in self.entries:
            del self.entries[name]
            return 'Número deletado'
        else:
            return 'Nome não encontrado'