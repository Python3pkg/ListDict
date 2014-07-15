#!/usr/bin/env python

class ListDict(object):
    """
    This is a container class that acts like a list and a dictionary
    and a structure.
    
    So far, "append" is the only list method supported.
    
    The "append" method adds items to the list. If there's a second
    parameter, it is a label that can subsequently be used as an
    index, but that also is stored in the main dictionary. This means
    that an element could be read or written as, for example, ld[1],
    ld["somelabel"], and ld.somelabel.
    
    A ListDict can optionally be initialized with a starting list value.
    """
    
    """
    __l is a list of lists of [value,label]
    __d is a dictionary indexed by label containing the index into __l
        of this [value,label]

    If an item has a label, then the definitive value is in the
    structure, i.e. in self.__dict__. This is necessary so that
    ld.somelabel=value works.
    """
    
    def __init__(self, initial_list=None):
        if initial_list:
            # Initialize the list with the given values and no labels.
            self.__l = [[i,None] for i in initial_list]
        else:
            self.__l = []
        # Initialize the dictionary of labels:indexes.
        self.__d = {}
    
    def append(self, val, label=None):
        v = [val,label]
        if label:
            # If there's a label, save the index.
            self.__d[label] = len(self.__l)
            # And create a structure element.
            self.__dict__[label] = val
        self.__l.append(v)
    
    def __str__(self):
        # The __str__ is simply the str of the list part.
        return str(list(val for val,label in self.__l))
    
    def __len__(self):
        return len(self.__l)
    
    def __getitem__(self, ix):
        if isinstance(ix, slice):
            # A slice was requested. Return that slice of the list of values.
            return [val for val,label in self.__l][ix]
        elif ix in self.__d:
            # The index is a label; return the value from the structure.
            return self.__dict__[ix]
        elif self.__l[ix][1]:
            # The index must be an integer, and this item has a label;
            # return the value from the structure.
            return self.__dict__[self.__l[ix][1]]
        else:
            # The index must be an integer, and this item has no label;
            # return the value from the list.
            return self.__l[ix][0]

    def __setitem__(self, ix, val):
        if ix in self.__d:
            # The index is a label; set the value in the structure.
            self.__dict__[ix] = val
        elif self.__l[ix][1]:
            # The index must be an integer, and this item has a label;
            # set the value in the structure.
            self.__dict__[self.__l[ix][1]] = val
        else:
            # The index must be an integer, and this item has no label;
            # set the value in the list.
            self.__l[ix][0] = val
        

if __name__ == "__main__":
    # For these tests, __d cannot start with two underscores.
    # It should have two underscores for production.
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
    print ld.__d
    
    le = ListDict()
    print "new le =", le
    le.append(10)
    assert le[0] == 10
    le.append(11, "z")
    assert le["z"] == 11
    assert le[1] == 11
    assert le.z == 11
    print "le =", le
    print le.__d
    
    lf = ListDict([20,21,22])
    assert lf[0] == 20
    lf[0] = 23
    assert lf[0] == 23
    print "lf =", lf
    print lf.__d
