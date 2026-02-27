load "AddDivisors.m";

L2 := [ 19, 20, 21, 10, 7, 13, 11, 12, 5, 4, 3, 16, 6, 28, 8, 2, 1, 14, 18, 9, 44, 22, 56, 15, 24 ];
L3 := [ 10, 13, 5, 7, 8, 16, 32, 20, 1, 4, 31, 11, 3, 17, 6, 2, 80, 14, 12, 92, 28, 9, 44, 58, 22, 23 ];
L4 := [ 146, 155, 71, 1, 4, 55, 72, 61, 34, 13, 31, 37, 21, 52, 28, 20, 16, 7, 23, 11,
48, 5, 8, 12, 3, 64, 9, 32, 76, 2, 36, 17, 74, 22, 18, 6, 80, 26, 49, 19, 40, 43, 176, 82, 56, 24 ];
L5 := [ 29, 13, 11, 16, 1, 8, 6, 38, 68, 5, 7, 4, 46, 35, 21, 25, 2, 19, 3, 36, 23, 10 ];

sortedL2 := Sort(AddDivisors(L2));
sortedL3 := Sort(AddDivisors(L3));
sortedL4 := Sort(AddDivisors(L4));
sortedL5 := Sort(AddDivisors(L5));

SetOutputFile("sortedlists.txt");

print "Sorted list of predicted torsion orders for dimension 2:", sortedL2;
print "Sorted list of predicted torsion orders for dimension 3:", sortedL3;
print "Sorted list of predicted torsion orders for dimension 4:", sortedL4;
print "Sorted list of predicted torsion orders for dimension 5:", sortedL5;

UnsetOutputFile();
