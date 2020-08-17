import numpy as np


def main():
    names = ['Absol', 'Aron', 'Jynx', 'Natu', 'Orix']
    attacks = np.array([130, 70, 50, 50, 45])
    
    total_attacks_avg = attacks.mean()
    
    for pokemon, attack in zip(names, attacks):
        if attack > total_attacks_avg:
            print("{}'s attack: {} > average: {}".format(pokemon, attack, total_attacks_avg))


if __name__ == "__main__":
    main()
