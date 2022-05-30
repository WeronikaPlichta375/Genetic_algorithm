import pymysql
from product import Product
from genetic_a import Individual, GeneticAlgorithm
import plotly.express as px
from gui import show_graph
from data import simple_data

SPACE_LIMIT = 4000000  # cm^3 4000 l
WEIGHT_LIMIT = 200  # 200 kg
P_RATE_MUTATION = 0  # Mutation isn't working
P_RATE_CROSSOVER = 0.7
POPULATION_SIZE = 20
NR_OF_GENERATIONS = 100

if __name__ == '__main__':
    product_list = []
    # Connection with database (optional)
    # connection = pymysql.connect(host='localhost', user='root', passwd='###############', db='products')
    # cursor = connection.cursor()
    # cursor.execute('select product_name, weight, height, width, depth, price, amount from products')
    # # Collecting data from database
    # # Pack all the products
    # # for product in cursor:
    # #     i = 0
    # #     while i < product[6]:
    # #         product_list.append(Product(product[0], product[1], product[2], product[3], product[4], product[5]))
    # #         i += 1
    # # Pack one kind of products
    # for product in cursor:
    #     product_list.append(Product(product[0], product[1], product[2], product[3], product[4], product[5]))
    #
    # cursor.close()
    # connection.close()

    product_list = simple_data()

    names_of_products = []
    prices_of_products = []
    weight_of_products = []
    size_of_products = []

    for product in product_list:
        names_of_products.append(product.name)
        prices_of_products.append(product.price)
        weight_of_products.append(product.weight)
        size_of_products.append(product.space)

    example_ga = GeneticAlgorithm(POPULATION_SIZE)
    result = example_ga.solve(P_RATE_MUTATION, P_RATE_CROSSOVER, 100,
                              size_of_products, prices_of_products, weight_of_products, SPACE_LIMIT, WEIGHT_LIMIT)
    print(result)

    for i in range(len(product_list)):
        if result[i] == 1:
            print('Name: ', product_list[i].name, ' - Price: ', product_list[i].price, '- Weight',
                  product_list[i].weight)

    print(example_ga.list_of_solutions)
    figure = px.line(x=range(0, 101), y=example_ga.list_of_solutions, title='Genetic algorithm')
    figure.show()

    show_graph(example_ga.list_of_solutions)
