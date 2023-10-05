import unittest

from src.phonebook import Phonebook


class TestPhonebook(unittest.TestCase):

    # def setUp(self):
    #     self.phonebook = Phonebook()

    ## Testa a adição de uma entrada válida ##
    def test_add_valid_entry(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Número adicionado'

        ##Chamada
        result = phonebook.add('Stephane', '81987456123')

        ##Avaliação
        assert expect_result == result

    ## Testa a adição de uma entrada duplicada (mesmo nome) ##
    def test_add_duplicate_entry(self):
        ##Setup
        phonebook = Phonebook()
        phonebook_exist = 'Stephane'
        number = '81987456123'
        phonebook.add(phonebook_exist,number)

        ##Chamada
        result = phonebook.add('Stephane', '81987456123')

        ##Avaliação
        assert result == 'Nome já existe'

    ## Testa a adição de um nome com caracteres especiais (@/#/$/%/!) ##
    def test_add_name_with_special_characters(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Nome inválido'

        ##Chamada + Avaliação
        assert phonebook.add('Steph@ne', '81987456123')
        assert phonebook.add('Stephane#', '12345') == 'Nome inválido'
        assert phonebook.add('Stephane!', '12345') == 'Nome inválido'
        assert phonebook.add('Stephane$', '12345') == 'Nome inválido'
        assert phonebook.add('Stephane0%', '12345') == 'Nome inválido'

    ## Testa a adição de um nome vazio ##
    def test_add_empty_name(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Nome inválido'

        ##Chamada
        result = phonebook.add('', '123456')

        ##Avaliação
        assert expect_result == result

    ## Testa a adição de um número vazio ##
    def test_add_empty_number(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Número inválido'

        ##Chamada
        result = phonebook.add('Stephane', '')

        ##Avaliação
        assert expect_result == result

    ## Testa a adição de um nome com espaço ##
    def test_add_name_with_spaces(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Número adicionado'

        ##Chamada
        result = phonebook.add('Stephane Miranda', '81987456123')

        ##Avaliação
        assert expect_result == result

    ## Testa a busca por um nome que existe no livro de telefones ##
    def test_lookup_existing_name(self):
        ##Setup
        phonebook = Phonebook()

        ##Avaliação
        assert phonebook.lookup('POLICIA') == '190'
        assert phonebook.lookup('BOMBEIRO') == '193'


    ## Testa a busca por um nome que não existe no livro de telefones ##
    def test_lookup_non_existing_name(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Nome inválido'

        ##Avaliação
        assert expect_result == phonebook.lookup('Stephane')

    ## Testa a busca por um nome com caracteres especiais (#) ##
    def test_lookup_name_with_special_characters(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Nome inválido'

        ##Avaliação
        assert expect_result == phonebook.lookup('Steph@ne')

        ## Testa a busca por um nome com espaços ##
    def test_lookup_name_with_spaces(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Nome inválido'

        ##Avaliação
        assert expect_result == phonebook.lookup('Stephane Miranda')

        ## Testa a busca por um nome vazio ##
    def test_lookup_empty_name(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Nome inválido'

        ##Avaliação
        assert expect_result == phonebook.lookup('')

        ## Testa o retorno dos nomes com entradas existentes ##
    def test_get_names_with_entries(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = ['POLICIA', 'BOMBEIRO']

        ##Avaliação
        assert expect_result == phonebook.get_names()

    ## Testa o retorno de números em um livro de telefones com entradas existentes ##
    def test_get_numbers_with_entries(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = ['190', '193']

        ##Avaliação
        assert expect_result == phonebook.get_numbers()

    ## Testa a busca por um nome que corresponde exatamente a uma entrada no livro de telefones ##
    def test_search_exact_match(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = [('POLICIA', '190')]

        ##Chamada
        result = phonebook.search('POLICIA')

        ##Avaliação
        assert expect_result == result

    ## Testa a busca por um nome que corresponde parcialmente a uma entrada no livro de telefones ##
    def test_search_partial_match(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = [('POLICIA', '190')]

        ##Chamada
        result = phonebook.search('POL')

        ##Avaliação
        assert expect_result == result

    ## Testa a busca por um nome que não existe no livro de telefones ##
    def test_search_no_match(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = []

        ##Chamada
        result = phonebook.search('MARIA')

        ##Avaliação
        assert expect_result == result

    ##  Testa a busca por um nome com caracteres especiais (#) ##
    def test_search_with_special_characters(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = []

        ##Chamada
        result = phonebook.search('POLICI@')

        ##Avaliação
        assert expect_result == result

    def test_clear(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Phonebook limpado'

        ##Chamada
        result = phonebook.clear()

        ##Avaliação

        assert expect_result == result


    def test_get_phonebook_sorted(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = [('BOMBEIRO', '193'), ('POLICIA', '190')]

        ##Chamada
        result = phonebook.get_phonebook_sorted()

        ##Avaliação
        assert expect_result == result

    def test_get_phonebook_reverse(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = [('POLICIA', '190'), ('BOMBEIRO', '193')]

        ##Chamada
        result = phonebook.get_phonebook_reverse()

        ##Avaliação
        assert expect_result == result


    def test_delete(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Número deletado'

        ##Chamada
        result = phonebook.delete('POLICIA')

        ##Avaliação
        assert expect_result == result

    def test_delete_name_non_existent(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Nome não encontrado'

        result = phonebook.delete('Stephane')

        ##Avaliação
        assert expect_result == result


    def test_delete_name_none(self):

        ##Setup
        phonebook = Phonebook()
        expect_result = 'Nome não pode ser None'

        ##Chamada
        result = phonebook.delete(None)

        ##Avaliação
        assert expect_result == result

    def test_delete_name_non_existent(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Nome deve ser string'

        ##Chamada
        result = phonebook.delete(1234)

        ##Avaliação
        assert expect_result == result

    def test_delete_name_empty(self):
        ##Setup
        phonebook = Phonebook()
        expect_result = 'Nome não pode ser vazio'

        ##Chamada
        result = phonebook.delete('')

        ##Avaliação
        assert expect_result == result