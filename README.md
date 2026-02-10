This repo contains auxiliary code and files that complement our paper "Torsion points on $\GL_2$-type abelian varieties".
The file "PossibleTorsionOrders.m" is a MAGMA files with the following functions:
 - TorsionValuation(K, l, x)
   the inputs are a number field K, a rational prime l and an element x of K;
   the function outputs the max over all primes lambda over l of l^(val*f),
   where val is the lambda-adic valuation of x and f is the inertia degree of lambda-
 - CorrectValuation(K, l)
   the inputs are a number field K and a rational prime l;
   the output is true if l is totally inert in L. This function is not used in the current implementation of the main function.
 - PossibleTorsionOrders(Nlbd, Nubd, deg)
   the inputs are three integers: Nlbd and Nubd are the extremal of the interval where the level N of the newforms varies; deg is the dimension of the abelian varieties considered;
   this function computes the list of the torsion order predicted by our Theorem 4.2/4.3 for abelian varieties associated to newforms of weight 2, level N and dimension deg.
The files "g2upto300", "g3upto300", "g4upto300", "g5upto300" contain the output of the function PossibleTorsionOrders(2,300,g) for g=2,3,4,5 respectively.
We also print the newforms found in the loop and whether their predicted torsion order matches the bound given by the gcd of the number of points on the abelian varieties.
With an upper bound on N large enough, the two lists are the same.
