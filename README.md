# binomial_distribution
command line calculator for binomial distributions written in python

<code>python3 binomial_dist.py -h</code> for usage

sample output:
<pre>
>> python3 binomial_dist.py -h
usage: binomial_dist.py [-h] [-p PROB] [-n TRIALS] [-a LAMBT] [-m MINVAL] [-s SCALE]

options:
  -h, --help            show this help message and exit
  -p PROB, --prob PROB  success probability
  -n TRIALS, --trials TRIALS
                        number of trials
  -a LAMBT, --lambt LAMBT
                        lambda argument
  -m MINVAL, --minval MINVAL
                        minimum value for lambda
  -s SCALE, --scale SCALE
                        scale for distribution y values (min 100 recommended)

>> python3 binomial_dist.py -p 0.5 -n 14 -a "x <= 1" -m 1 -s 200
p=0.5, trials=14
P(x <= 1), x > 1 = 0.0008544921875

002: *
003: ****
004: ************
005: ************************
006: ************************************
007: *****************************************
008: ************************************
009: ************************
010: ************
011: ****
012: *
</pre>
