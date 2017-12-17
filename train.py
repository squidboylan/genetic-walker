#!/usr/bin/env python3

import os
import sys
from runner import test_creature
from multiprocessing import Pool

if __name__ == '__main__':
    with Pool(16) as p:
        path_list = []
        for i in range(100):
            path_list.append(os.path.join("gens", "0", str(i)))

        p.map(test_creature, path_list)

