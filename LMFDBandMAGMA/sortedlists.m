load "AddDivisors.m";

L2 := [ 19, 20, 21, 13, 11, 5, 7, 12, 3, 10, 16, 28, 8, 4, 6, 1, 14, 18, 2, 9, 44, 22, 56, 15, 24, 17, 23, 31, 37 ];
L3 := [ 10, 13, 5, 7, 8, 16, 32, 20, 1, 4, 31, 11, 3, 17, 6, 2, 80, 14, 12, 92, 28, 9, 44, 58, 22, 23, 40, 37, 38, 19, 36, 
160, 49, 24, 18, 83, 15 ];
L4 := [ 146, 155, 71, 52, 68, 28, 55, 72, 61, 34, 31, 13, 37, 21, 36, 20, 19, 7, 16, 
23, 11, 48, 8, 9, 12, 1, 4, 5, 3, 64, 32, 76, 17, 2, 74, 22, 18, 6, 80, 26, 49, 
57, 40, 24, 43, 176, 56, 25, 82, 44, 136, 29, 14, 10, 63, 35, 15, 152, 88, 27 ];
L5 := [ 29, 13, 11, 16, 1, 8, 6, 38, 68, 5, 7, 4, 46, 35, 21, 25, 2, 19, 3, 23, 10, 24, 36, 52, 44, 12, 106, 28, 92, 9, 110, 
41, 18, 22, 20, 32, 17, 43, 192, 72, 48, 64, 56, 14, 63, 288, 50, 27, 320, 31, 40 ];

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
