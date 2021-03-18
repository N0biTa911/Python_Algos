s = {1, 2, 4, 5, 6, 7, 10}

initial = list(s)
gr = []
for i in initial:
    gr = gr + [[i]]
gr = [gr]

def summ(x):
    s = 0
    for i in x:
        s = s + i
    return(s)
def sum_equal(gr,initial,gg):
    if gg < len(initial) + 1:
        ll = []
        for i in initial:
            k = []
            for j in gr[-1]:
                if i not in j:
                    k = k + [j + [i]]
            ll = ll + k
        kgb = gr + [ll]
        gg = gg + 1
        sum_equal(kgb,initial, gg)
    else:
        kkk = []
        for i in gr:
            for j in i:
                if set(j) not in kkk:
                    kkk = kkk + [set(j)]
        lp = []
        for i in kkk:
            for j in kkk:
                for k in kkk:
                    if (i!=j and j!= k and i!= k) and (summ(i) == summ(j) == summ(k)) and (i.isdisjoint(j) and j.isdisjoint(k) and k.isdisjoint(i)):
                        lp = lp + [[i,j,k]]
        print(lp)
                    
        
sum_equal(gr, initial , 1)
        
    
    
