#!/usr/bin/env python3

import os
import sys
from runner import test_creature
from gen import create_generation
from multiprocessing import Pool

if __name__ == '__main__':
    try:
        workers = int(sys.argv[1])
    except:
        workers = 2

    curr_gen = 100
    gen_size = 400
    while curr_gen < 1000:
        print("Creating generation: " + str(curr_gen))
        if curr_gen == 0:
            create_generation(curr_gen, gen_size, workers=workers)
        else:
            create_generation(curr_gen, gen_size, workers=workers, predecessor=curr_gen-1)

        print("Testing generation: " + str(curr_gen))
        with Pool(workers) as p:
            path_list = []
            for i in range(gen_size):
                path_list.append(os.path.join("gens", str(curr_gen), str(i)))

            p.map(test_creature, path_list)

        curr_gen = curr_gen + 1

