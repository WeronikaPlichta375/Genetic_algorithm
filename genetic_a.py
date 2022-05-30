from random import randint, random
class Individual():
    def __init__(self, all_size_of_products, all_costs, all_weights, space_limit, weight_limit, generation=0):
        self.all_size_of_products = all_size_of_products
        self.all_costs = all_costs
        self.all_weights = all_weights
        self.space_limit = space_limit
        self.weight_limit = weight_limit
        self.generation = generation
        self.total_score = 0
        self.used_space = 0
        self.used_weight = 0
        self.chromosome = []
        for i in range(len(self.all_size_of_products)):
            self.chromosome.append(randint(0, 1))
        # print(self.chromosome)

    def fitness(self):
        score = 0
        sum_spaces = 0
        sum_weight = 0
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == 1:
                score +=self.all_costs[i]
                sum_spaces += self.all_size_of_products[i]
                sum_weight += self.all_weights[i]
        if sum_spaces >self.space_limit or sum_weight >self.weight_limit:
            score = 1
        self.total_score = score
        self.used_space = sum_spaces
        self.used_weight = sum_weight

    #From one pair we have "one pair" of children -> we are creating next generation
    def crossover(self, second_individual):
        cutoff = randint(1, len(self.chromosome)-1)
        #print(cutoff)
        child1 = second_individual.chromosome[0:cutoff]+self.chromosome[cutoff::]
        child2 = self.chromosome[0:cutoff] + second_individual.chromosome[cutoff::]
        #print(child1, child2)
        children = [Individual(self.all_size_of_products, self.all_costs, self.all_weights, self.space_limit, self.weight_limit, self.generation+1),
                    Individual(self.all_size_of_products, self.all_costs, self.all_weights, self.space_limit, self.weight_limit, self.generation+1)]
        children[0].chromosome = child1
        children[1].chromosome = child2
        return children

    def mutation(self, p_rate):
        for i in range(len(self.chromosome)):
            if random() < p_rate:
                print("Mutation", self.chromosome[i])
                if self.chromosome[i] == 1:
                    self.chromosome[i]=0
                else:
                    self.chromosome=1
        return self

class GeneticAlgorithm():
    def __init__(self, size_population):
        self.population_size = size_population
        self.population = []
        self.generation = 0
        self.best_solution = None
        self.list_of_solutions = []

    def initalize_population(self, all_size_of_products, all_costs, all_weights, space_limit, weight_limit):
        for individual in range(self.population_size):
            self.population.append(Individual(all_size_of_products, all_costs, all_weights, space_limit, weight_limit))
        self.best_solution = self.population[0]

    def order_population(self):
        self.population = sorted(self.population, key=lambda population: population.total_score, reverse=True)       #Czy warto zaaplikować inny algorytm sortowania?

    def best(self, individual):
        if individual.total_score > self.best_solution.total_score:
            self.best_solution=individual

    def sum_evaluations(self):
        total_sum = 0
        for i in self.population:
            total_sum += i.total_score
            # total_sum +=sum(i.all_costs)

        return total_sum

    def select_parent(self, total_sum):
        parent = -1
        random_value = random() * total_sum
        sum = 0
        i = 0
        # print("\nSpinning the wheel:", random_value)
        while i <len(self.population) and sum<random_value:
            sum+=self.population[i].total_score
            parent+= 1
            i += 1
            # print("\n i", i, "sum", sum)
        return parent

    def visualize_generation(self):
        best = self.population[0]
        print('Generation: ', self.population[0].generation,
              'Total price/score: ', best.total_score, 'Space: ', best.used_space, 'Weight: ', best.used_weight,
              'Chromosome: ', best.chromosome)
    # def visualize_best_generation(self):
    #     print('****Best solution Generation: ', self.population[0].generation,
    #           'Total price: ', self.best_solution.total_score, 'Space: ', self.best_solution.used_space, 'Weight: ', self.best_solution.used_weight,
    #           'Chromosome: ', self.best_solution.chromosome)
    def solve(self, mutation_probability, crossover_probability, number_of_generations, spaces, prices, weight, limit_space, limit_weight):
        #Initalizing population
        self.initalize_population(spaces, prices,  weight, limit_space, limit_weight)
        #Evaluating population
        for individual in self.population:
            individual.fitness()
        self.order_population()
        #For graph
        self.best_solution = self.population[0]
        self.list_of_solutions.append(self.best_solution.total_score)
        self.visualize_generation()
        #Stopping criterium
        for generation in range(number_of_generations):
            sum_of_all_scores = self.sum_evaluations()
            # print("Tworzona nowa generacja")
            new_population = []
            crossed = 0
            for new_individuals in range(0, self.population_size):  # Jeżeli ustawimy na cały rozmiar, to wszystkie  ZAWSZE bedą miały crossover

                #while random() < crossover_probability and crossed < self.population_size:  # We won't have the same size popraw
                    # Selecting parents
                parent1 = self.select_parent(sum_of_all_scores)
                parent2 = self.select_parent(sum_of_all_scores)
                # if parent1 == parent2:
                #     break
                # Crossover
                # print('\nSelected parents', parent1, parent2, '\n', self.population[parent1].chromosome, '\n',
                #       self.population[parent2].chromosome)
                children = self.population[parent1].crossover(self.population[parent2])
                # crossed += 1
                # print('\nChildren \n', children[0].chromosome, '\n', children[1].chromosome)
                #Mutation
                new_population.append(children[0].mutation(mutation_probability))
                new_population.append(children[1].mutation(mutation_probability))
            #Drop the old population and replacing with the new one
            self.population = list(new_population)

            for individual in self.population:
                individual.fitness()

            self.visualize_generation()
            #Setting best solution
            best = self.population[0]
            self.list_of_solutions.append(best.total_score)
            #self.list_of_solutions.append(best)
            self.best(best)

        print('**** Best solution - Generation: ', self.best_solution.generation,
              'Total price: ', self.best_solution.total_score, 'Space: ', self.best_solution.used_space,
              'Chromosome: ', self.best_solution.chromosome)
        return self.best_solution.chromosome
