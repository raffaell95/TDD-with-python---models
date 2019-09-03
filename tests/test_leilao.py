from unittest import TestCase
from src.leilao.dominio import Usuario, Leilao, Lance
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):


    def setUp(self):
        
        self.luana = Usuario('Luana', 500)
        self.lance_da_luana = Lance(self.luana, 150.0)

        self.leilao = Leilao('Celular')


    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):

        rafael = Usuario('Rafael', 500)
        lance_do_rafael = Lance(rafael, 100.0)

        self.leilao.propoe(lance_do_rafael)
        self.leilao.propoe(self.lance_da_luana)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):


        with self.assertRaises(LanceInvalido):

            rafael = Usuario('Rafael', 500)
            lance_do_rafael = Lance(rafael, 100.0)

            self.leilao.propoe(self.lance_da_luana)
            self.leilao.propoe(lance_do_rafael)


    def test_deve_retornar_o_mesmo_valor_para_omenor_lance_quando_leilao_tiver_um_lance(self):

        self.leilao.propoe(self.lance_da_luana)

        self.assertEqual(150, self.leilao.menor_lance)
        self.assertEqual(150, self.leilao.maior_lance)

    
    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):

        rafael = Usuario('Rafael', 500)
        lance_do_rafael = Lance(rafael, 100.0)
        
        vini = Usuario('Vini', 500)
        lance_do_vini = Lance(vini, 200)

        self.leilao.propoe(lance_do_rafael)
        self.leilao.propoe(self.lance_da_luana)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


# se o leilão  não tiver lances, deve permitir propor um lance.

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_da_luana)

        quantidade_lance_recebida = len(self.leilao.lances)

        self.assertEqual(1, quantidade_lance_recebida)

    
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        pedro = Usuario('Pedro', 500)
        lance_do_pedro = Lance(pedro, 200)

        self.leilao.propoe(self.lance_da_luana)
        self.leilao.propoe(lance_do_pedro)

        quantidade_de_lance_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lance_recebido)

    
    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_da_luana200 = Lance(self.luana, 200)
       
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_da_luana)
            self.leilao.propoe(lance_da_luana200)
    