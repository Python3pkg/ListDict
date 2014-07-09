#!/usr/bin/env python

class ListDict(object):
    
    def __init__(self, l=None):
        if l:
            self.__l = [(i,None) for i in l]
        else:
            self.__l = []
        self._d = {}
    
    def append(self, val, label=None):
        v = [val,label]
        print "appending", v
        if label:
            self._d[label] = len(self.__l)
        self.__l.append(v)
    
    def __str__(self):
        return str(list(v[0] for v in self.__l))
    
    def __len__(self):
        return len(self.__l)
    
    def __getitem__(self, ix):
        print "getting", ix
        if ix in self._d:
            return self.__l[self._d[ix]][0]
        else:
            return self.__l[ix][0]

    def __setitem__(self, ix, val):
        if ix in self._d:
            self.__l[self._d[ix]][0] = val
        else:
            self.__l[ix][0] = val
        

if __name__ == "__main__":
    ld = ListDict()
    ld.append(3, 'y')
    ld.append(4, 'z')
    ld.append(2)
    print ld["y"], "== 3"
    print ld["z"], "== 4"
    print ld, "== [3, 4, 2]"
    print len(ld), "== 3"
    ld["y"] = 5
    print ld["y"], "== 5"
    print ld[0], "== 5"
    ld[0] = 6
    print ld["y"], "== 6"
    print ld[0], "== 6"
    print ld[2], "== 2"
    ld[2] = 1
    print ld[2], "== 1"
    print ld
    print ld._d
    
    le = ListDict()
    print "new le =", le
    le.append(10)
    print le[0], "== 10"
    le.append(11, "z")
    print le["z"], "== 11"
    print le[1], "== 11"
    print "le =", le
    print le._d
    
    lf = ListDict([20,21,22])
    print "lf =", lf
    print lf._d