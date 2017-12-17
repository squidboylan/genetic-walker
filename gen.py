#!/usr/bin/env python3
from random import *
import yaml
import os

def create_generation(gen_num, size, genomes_max=200, mutation=0.05, predecessor=None):
    if not predecessor:
        try:
            os.mkdir("gens")
        except FileExistsError as e:
            pass

        os.mkdir(os.path.join("gens", str(gen_num)), mode=0o700)
        for i in range(size):
            path = os.path.join("gens", str(gen_num), str(i))
            genomes = randint(1, genomes_max)
            tmp = []
            for k in range(genomes):
                f = []
                for j in range(4):
                    f.append(random())
                tmp.append(f)
            with open(path, 'w') as yaml_file:
                yaml.dump(tmp, yaml_file)

if __name__ == "__main__":
    create_generation(0, 100)
