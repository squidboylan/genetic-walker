#!/usr/bin/env python3

from random import *
import yaml
import os
import sys
from multiprocessing import Pool

def create_individual(gen_num, ind_num, genomes, mutation, parent1=None, parent2=None):
    if parent1 == None and parent2 == None:
        path = os.path.join("gens", str(gen_num), str(ind_num))
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

    elif parent1 != None and parent2 == None:
        path = os.path.join("gens", str(gen_num), str(ind_num))
        tmp = parent1[:]
        for k in range(len(tmp)):
            for j in range(4):
                num = random()
                sign = randint(0,1)
                if sign == 1:
                    num = num * -1

                if random() < .05:
                    tmp[k][j] = num
        with open(path, 'w') as yaml_file:
            yaml.dump(tmp, yaml_file)

    else:
        path = os.path.join("gens", str(gen_num), str(ind_num))
        genomes = min(len(parent1), len(parent2))
        split = randint(1, min(len(parent1), len(parent2)))
        tmp = []
        tmp += parent1[:split]
        tmp += parent2[split:]
        for k in range(len(tmp)):
            for j in range(4):
                num = random()
                sign = randint(0,1)
                if sign == 1:
                    num = num * -1

                if random() < .05:
                    tmp[k][j] = num
        with open(path, 'w') as yaml_file:
            yaml.dump(tmp, yaml_file)

def create_generation(gen_num, size, workers=2, genomes=120, mutation=0.05, predecessor=None):
    if predecessor == None:
        try:
            os.mkdir("gens")
        except FileExistsError as e:
            pass

        os.mkdir(os.path.join("gens", str(gen_num)), mode=0o700)
        args_list = []
        for i in range(size):
            args_list.append((gen_num, i, genomes, mutation))

        with Pool(workers) as p:
            p.starmap(create_individual, args_list)

    else:
        try:
            os.mkdir("gens")
        except FileExistsError as e:
            pass

        os.mkdir(os.path.join("gens", str(gen_num)), mode=0o700)
        next_gen = {}
        for i in range(size):
            path = os.path.join("gens", str(predecessor), str(i))
            results_path = path + "-result"

            with open(path, 'r') as actions_file:
                actions = yaml.load(actions_file)

            with open(results_path, 'r') as results_file:
                results = yaml.load(results_file)

            next_gen[str(i)] = {"actions": actions, "reward": results['reward']}

        simple_dict = {}
        for i in next_gen.keys():
            simple_dict[i] = next_gen[i]['reward']

        i = 0
        to_generate = []
        used_ids_rev = []
        for w in sorted(simple_dict, key=simple_dict.get):
            #print(w, simple_dict[w])
            if i < size/2:
                to_generate.append(w)
                next_gen.pop(w, None)
                i = i + 1
            else:
                used_ids_rev.append(w)

        parent_keys = used_ids_rev[::-1]
        #print(parent_keys)

        args_list = []
        to_generate_num = len(to_generate)
        for i in parent_keys:
            parent1 = next_gen[i]['actions']
            args_list.append((gen_num, i, genomes, mutation, parent1))

        for i in range(int(to_generate_num/2)):
            i = i * 2
            parent1 = next_gen[parent_keys.pop(0)]['actions']
            parent2 = next_gen[parent_keys.pop(0)]['actions']
            args_list.append((gen_num, to_generate.pop(0), genomes, mutation, parent1, parent2))
            args_list.append((gen_num, to_generate.pop(0), genomes, mutation, parent2, parent1))

        with Pool(workers) as p:
            p.starmap(create_individual, args_list)

if __name__ == "__main__":
    try:
        workers = int(sys.argv[1])
    except:
        workers = 2

    gen_size = 400

    #create_generation(0, gen_size, workers=workers)
    create_generation(1, gen_size, predecessor=0)
