s = ({'MINID', 'HY', 1980, 'HTML'},
     {'MINID', 'HY', 1980, 'CUDA'},
     {'MINID', 'HY', 1980, 'XML'},
     {'MINID', 'HY', 1973, 'HTML'},
     {'MINID', 'HY', 1973, 'CUDA'},
     {'MINID', 'HY', 1973, 'XML'},
     {'MINID', 'HY', 1986, 'HTML'},
     {'MINID', 'HY', 1986, 'CUDA'},
     {'MINID', 'HY', 1986, 'XML'},
     {'MINID', 'XS', 'HTML', 1980},
     {'MINID', 'XS', 'HTML', 1973},
     {'MINID', 'XS', 'HTML', 1986},
     {'MINID', 'XS', 'CUDA'},
     {'MINID', 'XS', 'XML'},
     {'XC'})


def main(r):
    s1 = set(r)
    return [i for i in range(len(s))
            if not (len(s[i] - s1))][0]


print(main(['XML', 'MINID', 1998, 1980, 'XS']))
print(main(['XML', 'XC', 1971, 1973, 'HY']))
