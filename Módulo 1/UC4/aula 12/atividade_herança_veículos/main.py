from carro import Carro
from moto import Moto
from caminhao import Caminhao

# ---------------------------------------------------------

carro1 = Carro("Civic", "Honda", 2022, 4)
carro2 = Carro("Onix", "Chevrolet", 2023, 4)
carro3 = Carro("Corolla", "Toyota", 2021, 4)
carro4 = Carro("Mobi", "Fiat", 2024, 4)
carro5 = Carro("Mustang", "Ford", 2020, 2)

moto1 = Moto("CG 160", "Honda", 2023, 160)
moto2 = Moto("FZ25 Fazer", "Yamaha", 2022, 250)
moto3 = Moto("Ninja 400", "Kawasaki", 2021, 399)
moto4 = Moto("XRE 300", "Honda", 2020, 291)
moto5 = Moto("BMW R 1250 GS", "BMW", 2024, 1254)

caminhao1 = Caminhao("Constellation", "Volkswagen", 2021, 23.0)
caminhao2 = Caminhao("FH 540", "Volvo", 2023, 74.0)
caminhao3 = Caminhao("Scania R 450", "Scania", 2022, 50.0)
caminhao4 = Caminhao("Actros 2651", "Mercedes-Benz", 2024, 57.0)
caminhao5 = Caminhao("Delivery 11.180", "Volkswagen", 2020, 10.5)

# ---------------------------------------------------------

carro1.apresentar_veiculo()
carro1.mostrar_qtd_portas()

carro5.apresentar_veiculo()
carro5.mostrar_qtd_portas()

moto1.apresentar_veiculo()
moto1.mostrar_cilindradas()

moto4.apresentar_veiculo()
moto4.mostrar_cilindradas()

caminhao3.apresentar_veiculo()
caminhao3.mostrar_capacidade()

caminhao5.apresentar_veiculo()
caminhao5.mostrar_capacidade()