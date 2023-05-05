from math        import factorial
from dataclasses import dataclass
from typing      import Callable
import argparse

@dataclass
class Condition:
    condition_lambda: Callable[[int], bool]
    minimum_value: float = 0
    maximum_value: float = 0

def lambt(arg_string):
    lambda_fn = lambda x: eval(arg_string)
    return (lambda_fn, arg_string)

def n_choose_k(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

def bin_pdf(x, n, p):
    return n_choose_k(n, x) * p**x * (1 - p)**(n - x)

def bin_cdf(x, n, p):
    index = x.minimum_value
    accum = 0
    while (x.condition_lambda(index) and index < x.maximum_value):
        accum += bin_pdf(index, n, p)
        index += 1
    
    return accum

def main():
    argparser = argparse.ArgumentParser()

    argparser.add_argument("-p", "--prob"  , type=float, help="success probability")
    argparser.add_argument("-n", "--trials", type=int  , help="number of trials")
    argparser.add_argument("-a", "--lambt" , type=lambt, help="lambda argument")
    argparser.add_argument("-m", "--minval", type=int  , help="minimum value for lambda")
    argparser.add_argument("-s", "--scale" , type=float, help="scale for distribution y values (min 100 recommended)")

    args = argparser.parse_args()

    if (args.scale == None):
        args.scale = 100

    success_probability = args.prob
    total_trials        = args.trials

    binary_cumulative_density_function = bin_cdf(Condition(args.lambt[0], 1, total_trials), 
                                                 total_trials, success_probability)

    print(f"p={args.prob}, "
          f"trials={args.trials}\n"
          f"P({args.lambt[1]}), x > {args.minval} "
          f"= {binary_cumulative_density_function}\n")

    for i in range(int((args.trials))):
        x = args.minval + i
        y = bin_pdf(x, total_trials, success_probability) * args.scale
        if (round(y) > 0):
            print(f"{x:0>3}: {'*' * int(y)}")
main()
