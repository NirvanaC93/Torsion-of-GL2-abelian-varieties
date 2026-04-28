This repo contains auxiliary code and files that complement the paper "Torsion points on GL_2-type abelian varieties" https://arxiv.org/abs/2602.21047 by Jessica Alessandrì & Nirvana Coppola.

There are two possible ways to perform the computations.

The first one only uses MAGMA, but is much slower, since it needs to build all the information for each modular form.

The second one accesses the the database LMFDB via the interface at the link https://github.com/roed314/lmfdb-lite (using python), which makes computations quit fast and allowed us to improve our conjectural results.

# First option - MAGMA only

The file "PossibleTorsionOrders.m" is a MAGMA files with the following functions:
 - TorsionValuation(K, l, x):
   the inputs are a number field K, a rational prime l and an element x of K;
   the function outputs the max over all primes lambda over l of l^(val*f),
   where val is the lambda-adic valuation of x and f is the inertia degree of lambda-
 - CorrectValuation(K, l):
   the inputs are a number field K and a rational prime l;
   the output is true if l is totally inert in L. This function is not used in the current implementation of the main function.
 - PossibleTorsionOrders(Nlbd, Nubd, deg):
   the inputs are three integers: Nlbd and Nubd are the extremal of the interval where the level N of the newforms varies; deg is the dimension of the abelian varieties considered;
   this function computes the list of the torsion order predicted by our Theorem 4.2/4.3 for abelian varieties associated to newforms of weight 2, level N and dimension deg.

The files "gGuptoN.txt" contain the output of the function PossibleTorsionOrders(2,N,G).

We also print the newforms found in the loop and whether their predicted torsion order matches the bound given by the gcd of the number of points on the abelian varieties.
The file "sortedlists.m" contains the code necessary to complete and sort the list of all possible torsion orders (adding the divisors of the orders that are already in the list).

# Second option (better) - LMFDB and MAGMA

How to use:

The file getforms.py is a python script that accesses the database LMFDB via the interface at the link https://github.com/roed314/lmfdb-lite
We thank Sam Frengley for suggesting to use that and for allowing us to adapt his code available at https://github.com/dlaird-ens/p-tors-sha/blob/main/data/code/extract_data.py
The user give as input:
- the dimension of the abelian varietes (i.e. the degree of the coefficient fields of the forms);
- lower and upper bounds of the interval where the level N of the newforms varies;
- the file name of the output (including the .m extension), e.g. "formsgi.m" (for i=2,3,4,5).
The output is a MAGMA file containing the following lists:
 - "labels" is the list of the labels of the newforms in LMFDB having coefficient fields of degree g=i over Q;
 - "levels" is the list of the levels of the newforms listed in "labels"
 - "fields" is the list of the coefficient fields of the newforms listed in "labels"
- "aps" is the list of the lists of the coefficients "ap" for the newforms listed in "labels"
(obviously, list[i] will give the data for the i-th newform).

It is very heavy, because it writes very long lists, so it makes sense to run it separately for each g, possibly splitting the N's in intervals.

Open MAGMA and run:
load "formsgi.m";
load "getforms.m";

This will print the label of each newform listed in the file "formsgi.m" followed by its predicted torsion order. It also clarifies when the predicted torsion order is equal to the one à la Katz.
At the end, it prints the lists of predicted torsion orders, of the ones that agree with Katz's bound, and of the primes dividing torsion orders.
