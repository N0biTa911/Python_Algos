#this program takes a string as an input and performs P&C on the input
a = input("Enter the string:")

s = []
kll = []
for i in a:
    s = s + [i]
    if i not in kll:
        kll = kll + [i]
for i in range(len(kll)):
    lp = 1
    for j in range(len(s)):
        if kll[i] == s[j]:
            s[j] = s[j] + "*"*lp
            lp += 1
#this is a statemet
reference = s

gr = []
for i in reference:
    gr = gr + [[i]]
gr = [gr]


def combina(reference, gr, kk, n):
    if kk < n:
        kgb = []
        for i in reference:
            k = []
            for j in gr[-1]:
                if j[-1] not in reference[reference.index(i):]:
                    k += [j + [i]]
        
            kgb = kgb + k
        gr = gr + [kgb]
        combina(reference, gr, kk+1, n)
    else:
        
        kgb = list()
        for sk in range(len(gr)):
            for i in gr[sk]:
                ss = ""
                for j in i:
                    ss = ss + j[0]
                if ss not in kgb:
                    kgb = kgb + [ss]
        print(kgb)
        
combina(reference, gr, 1, len(reference))
