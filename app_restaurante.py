from restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'gourmet')
restaurante_praca.receber_avaliacao('Gabriel', 10)

restaurante_praca.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()