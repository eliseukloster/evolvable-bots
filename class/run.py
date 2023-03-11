import search
import numpy as np
import supress
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--weights', type=int, default=[0], nargs=1, help='Selects the weights<i>.csv file to load. Default is 0.')
parser.add_argument('-n', '--no-neurons', action='store_true')

if __name__ == '__main__':
    args = parser.parse_args()
    with supress.stdout_redirected(to='file.txt'):
        if args.no_neurons:
            s = search.Solution(0)
            s.evaluate(['--gui'])
            s.join()
        else:
            weights = np.loadtxt(f'weights{args.weights[0]}.csv', delimiter=',')
            weights[-1]
            s = search.Solution(0, weights[-1])
            s.evaluate(['--gui'])
            s.join()
            print(f'weights{args.weights[0]}.csv — fitness: {s.fitness}')