#!/usr/bin/env python

class ListDict(object):
    
    def __init__(self, intial_list=None):
        if intial_list:
            self.__l = [[i,None] for i in intial_list]
        else:
            self.__l = []
        self._d = {}
    
    def append(self, val, label=None):
        v = [val,label]
        #print "appending", v
        if label:
            self._d[label] = len(self.__l)
            self.__dict__[label] = val
        self.__l.append(v)
    
    def __str__(self):
        return str(list(v[0] for v in self.__l))
    
    def __len__(self):
        return len(self.__l)
    
    def __getitem__(self, ix):
        #print "getting", ix
        if isinstance(ix, slice):
            return [val for val,label in self.__l][ix]
        elif ix in self._d:
            #return self.__l[self._d[ix]][0]
            return self.__dict__[ix]
        elif self.__l[ix][1]:
            return self.__dict__[self.__l[ix][1]]
        else:
            return self.__l[ix][0]

    def __setitem__(self, ix, val):
        if ix in self._d:
            #self.__l[self._d[ix]][0] = val
            self.__dict__[ix] = val
        elif self.__l[ix][1]:
            self.__dict__[self.__l[ix][1]] = val
        else:
            self.__l[ix][0] = val
        

if __name__ == "__main__":
    ld = ListDict()
    ld.append(3, 'y')
    ld.append(4, 'z')
    ld.append(2)
    assert ld[0] == 3
    assert ld.y == 3
    assert ld["y"] == 3
    assert ld[1] == 4
    assert ld.z == 4
    assert ld["z"] == 4
    assert ld[2] == 2
    assert str(ld) == "[3, 4, 2]"
    assert len(ld) == 3
    ld["y"] = 5
    assert ld["y"] == 5
    assert ld[0] == 5
    assert ld.y == 5
    ld[0] = 6
    assert ld["y"] == 6
    assert ld[0] == 6
    assert ld.y == 6
    ld.y = 7
    assert ld["y"] == 7
    assert ld[0] == 7
    assert ld.y == 7
    ld[2] = 1
    assert ld[2] == 1
    print ld
    print ld._d
    
    le = ListDict()
    print "new le =", le
    le.append(10)
    assert le[0] == 10
    le.append(11, "z")
    assert le["z"] == 11
    assert le[1] == 11
    assert le.z == 11
    print "le =", le
    print le._d
    
    lf = ListDict([20,21,22])
    assert lf[0] == 20
    lf[0] = 23
    assert lf[0] == 23
    print "lf =", lf
    print lf._d
