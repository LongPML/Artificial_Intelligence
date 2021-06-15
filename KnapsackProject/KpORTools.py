from ortools.algorithms import pywrapknapsack_solver
import pandas as pd
import numpy as np

def KpORTools(idx, jdx):
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    values, weights, capacities = ReadData(idx, jdx)

    solver.Init(values, weights, capacities)
    solver.set_time_limit(300)
    solver.Solve()

    packed_items = []

    for _ in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)

    return [packed_items]

def ReadData(idx, jdx):
    files = ['00Uncorrelated', '01WeaklyCorrelated', '02StronglyCorrelated', '03InverseStronglyCorrelated', '04AlmostStronglyCorrelated',
            '05SubsetSum', '06UncorrelatedWithSimilarWeights', '07SpannerUncorrelated', '08SpannerWeaklyCorrelated', '09SpannerStronglyCorrelated',
            '10MultipleStronglyCorrelated', '11ProfitCeiling', '12Circle']
    random = ['n00050/R01000/s000.kp', 'n00200/R01000/s049.kp', 'n01000/R01000/s099.kp', 'n05000/R10000/s049.kp', 'n10000/R10000/s099.kp']

    values = list()
    weights = list()

    file = open('/kplib/{}/{}'.format(files[idx], random[jdx]), 'r')
    file.readline()
    n = int(file.readline())
    capacities = int(file.readline())
    file.readline()

    for i in range(n):
        Vi, Wi = file.readline().strip().split()
        values.append(int(Vi))
        weights.append(int(Wi))

    return values, [weights], [capacities]

for idx in range(13):
    print('\n', idx)
    for jdx in range(5):
        print(jdx, end= ' ')
        pd.DataFrame(KpORTools(idx, jdx)).to_csv('KpORTools.csv', mode='a', header= None)