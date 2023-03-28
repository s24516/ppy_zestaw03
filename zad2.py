# 2. Napisz program, który wyświetli plan wycieczki – wybierając losowo
# z listy 10 największych
# miast w Polsce miasta do odwiedzenia. Miast ma być 10, nie mogą się powtarzać.
import random

lista = {"Warszawa, Krakow, Wroclaw, Lodz, Poznan, Gdansk, Szczecin, Bydgoszcz, Lublin, Bialystok"}
random.shuffle(lista)
print(lista)