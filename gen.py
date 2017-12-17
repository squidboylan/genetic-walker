#!/usr/bin/env python3
from random import *
import yaml
import os

def create_generation(gen_num, size, genomes_max=200, mutation=0.05, predecessor=None):
    if predecessor == None:
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
                    num = random()
                    sign = randint(0,1)
                    if sign == 1:
                        num = num * -1

                    f.append(num)
                tmp.append(f)
            with open(path, 'w') as yaml_file:
                yaml.dump(tmp, yaml_file)

    else:
        prev_gen = {}
        for i in range(size):
            path = os.path.join("gens", str(predecessor), str(i))
            results_path = path + "-result"

            with open(path, 'r') as actions_file:
                actions = yaml.load(actions_file)

            with open(results_path, 'r') as results_file:
                results = yaml.load(results_file)

            prev_gen[str(i)] = {"actions": actions, "reward": results['reward']}

        simple_dict = {}
        for i in prev_gen.keys():
            simple_dict[i] = prev_gen[i]['reward']

        for w in sorted(simple_dict, key=simple_dict.get):
              print(w, simple_dict[w])


if __name__ == "__main__":
    #create_generation(0, 100)
    create_generation(1, 100, predecessor=0)
