from typing import List
from TimeLimit import time_limit
from TimeLimit import TimeoutException
import numpy as np
from Settings import MAX_TIME_IN_SEC
# pip install func_timeout

POPULATION_SIZE = 100
PARENT_QUANTITY = 20
GENERATIONS = 150


def genetic_solve(n, value, weight, capacity):
    weight = np.array(weight)
    value = np.array(value)

    population = initialize_population(weight, capacity)
    best_solution = np.zeros(n)
    best_result = 0
    try:
        with time_limit(MAX_TIME_IN_SEC):
            for i in range(GENERATIONS):
                fitness_score = evaluate_fitness(population, value, weight, capacity)
                best_in_pop_id = max(range(len(population)), key=lambda x: fitness_score[x])
                best_in_pop = population[best_in_pop_id]
                result = np.sum(value * best_in_pop)
                # print(f"iteration {i} = {result}" if sum(fitness_score) != 0 else f"iteration {i} = {0}")
                if result > best_result and fitness_score[best_in_pop_id] != 0:
                    best_result = result
                    best_solution = best_in_pop
                population = generate_children(population, fitness_score)
                population = mutate_population(population)
            # można zwrócić też best solution jak chcemy wiedzieć co braliśmy
            return best_result
    except TimeoutException as e:
        print("timeout!")
        return best_result


def _fitness(values: np.ndarray, weights: np.ndarray, capacity: int, chromosome: np.ndarray):
    total_weight = np.sum(weights * chromosome)
    if total_weight > capacity:
        return 0
    return np.sum(values * chromosome)


def _generate_chromosome(weights: np.ndarray, capacity: int):
    while True:
        prob = 0.5 * capacity / np.sum(weights)
        rand = np.random.uniform(0, 1, len(weights))
        chromosome = np.array([1 if rand[i] < prob else 0 for i in range(len(weights))])
        if sum(chromosome * weights) <= capacity:
            return chromosome


def initialize_population(weights: np.ndarray, capacity: int):
    population = [_generate_chromosome(weights, capacity) for _ in range(POPULATION_SIZE)]
    return population


def evaluate_fitness(population: List, values: np.ndarray, weights: np.ndarray, capacity: int):
    fitness_score = [_fitness(values, weights, capacity, chromosome) for chromosome in population]
    return fitness_score


def _roulette_selection(population: List, fitness_score: List):
    total_fitness = sum(fitness_score)
    if not total_fitness:
        return population[0:PARENT_QUANTITY]
    relative_fitness = [f / total_fitness for f in fitness_score]
    for i in range(1, len(relative_fitness)):
        relative_fitness[i] += relative_fitness[i - 1]
    rand = np.random.uniform(0, 1, PARENT_QUANTITY)
    rand.sort()
    i, j = 0, 0
    parents = []
    while i < len(rand):
        if rand[i] <= relative_fitness[j]:
            parents.append(population[j])
            i += 1
            continue
        j += 1
    return parents


def _crossover(a: List, b: List):
    np.random.randint(0, 2, len(a))
    chromosom = [a[i] if i == 0 else b[i] for i in range(len(a))]
    return chromosom


def generate_children(population: List, fitness_score: List):
    parents = _roulette_selection(population, fitness_score)
    to_cross = np.random.randint(0, len(parents), (POPULATION_SIZE, 2))
    children = [_crossover(population[a], population[b]) for (a, b) in to_cross]
    return children


def _mutation(chromosom: List):
    prob = 1 / len(chromosom)
    rand = np.random.uniform(0, 1, len(chromosom))
    mutated = [0 if prob >= rand[i] and chromosom[i] else 1 if prob >= rand[i] and not chromosom[i] else chromosom[i]
               for i in range(len(chromosom))]
    return mutated


def mutate_population(population: List):
    pop_mutated = [_mutation(chromosom) for chromosom in population]
    return pop_mutated


if __name__ == '__main__':
    weights = [70,
               73,
               77,
               80,
               82,
               87,
               90,
               94,
               98,
               106,
               110,
               113,
               115,
               118,
               120]
    values = [135,
              139,
              149,
              150,
              156,
              163,
              173,
              184,
              192,
              201,
              210,
              214,
              221,
              229,
              240]
    res = genetic_solve(len(values), values, weights, 750)
    print("final value = ", res)
    # optimal = 1458
