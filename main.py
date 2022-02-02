import decimal

from file_reader import get_action_list_POO
from brute_force import brute_force_POO
from optimized import optimized, optimized_POO
from decimal import *

import time
import argparse

# data = "data/dataset0_Python+P7.csv"
data = "data/dataset1_Python+P7.csv"
W = 500


def print_results(actions_bought, profits, total_cost, solving_time):
    profits = "{:.2f}".format(profits)
    print(F"Actions boughts : {actions_bought}\n"
          F"Total profits : {profits}€\n"
          F"Total cost : {total_cost}€\n"
          F"Solving time : {solving_time}\n")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Script solving the best "
                                                 "shares to buy for a specific"
                                                 " wallet")
    parser.add_argument("filename", type=str, help="Path to the CSV file")
    parser.add_argument("--wallet", type=int,
                        help="Choose the wallet size in euro", default=500)
    parser.add_argument("--algorithm_type", type=str,
                        choices=["brute", "optimized"],
                        help="Solving method"
                             "Default = Brute-force",
                        default="brute")
    args = parser.parse_args()
    data_path = args.filename
    wallet = args.wallet

    #       get data from CSV
    actions = get_action_list_POO(data_path)

    start = time.time()
    #       selecting the algorithm
    if args.algorithm_type == "brute":
        actions_bought, profits, total_cost = brute_force_POO(actions, wallet)
    elif args.algorithm_type == "optimized":
        actions_bought, profits, total_cost = optimized(actions, wallet)
    stop = time.time()
    solving_time = stop - start

    print_results(actions_bought, profits, total_cost, solving_time)
