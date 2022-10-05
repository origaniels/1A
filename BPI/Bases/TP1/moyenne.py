N1=17,9
N2=15,6
N3=4,1
def moy():
    p1=N1[0]*N1[1]
    p3=N3[0]*N3[1]
    p2=N2[0]*N2[1]
    s=p1+p2+p3
    tot=N1[1]+N3[1]+N2[1]
    return s/tot

print(moy())