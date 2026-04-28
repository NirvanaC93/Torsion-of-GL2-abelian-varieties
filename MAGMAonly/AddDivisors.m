//A useful function to state the correct conjectures taking into account the divisors of the numbers in the lists computed in PossibleTorsionOrders.m. The first one adds the divisors of the numbers in the list, and the second one sorts the list and removes duplicates.

function AddDivisors(L)
    for l in L do
        for d in Divisors(l) do
            if d notin L then
                L := Append(L, d);
            end if;
        end for;
    end for;
    return L;
end function;

