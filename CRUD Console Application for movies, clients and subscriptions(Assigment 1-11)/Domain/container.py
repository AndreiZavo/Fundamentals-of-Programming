

class MyContainer(object):

    def __init__(self):
        self._mylist = []
        self._index = -1

    def __iter__(self):
        "iterator for the class"
        return iter(self._mylist)

    def __next__(self):
        "getter for the next item from the list"
        if self._index > len(self._mylist) - 1:
            raise StopIteration
        else:
            self._index += 1
        return self._mylist[self._index]

    def __len__(self):
        "for the length"
        return len(self._mylist)

    def __setitem__(self, index, val):
        "the setter for an item"
        self._mylist[index] = val

    def __getitem__(self, index):
        "we get here the item"
        return self._mylist[index]

    def append(self, object):
        self._mylist.append(object)

    def remove(self, object):
        self._mylist.remove(object)

    def __delitem__(self, index):
        "here is the delete function"
        del self._mylist[index]

    def pop(self, id):
        self._mylist.pop(id - 1)

    def clear(self):
        self._mylist.clear()


class Methods():

    def gnomeSort(self, givenList, comparisonFunction):
        '''comparison function is considered such as:
           cmp(a,b) == True <=> a>=b
        '''
        index = 0
        while index < len(givenList):
            if index == 0 or comparisonFunction(givenList[index], givenList[index - 1]):
                index += 1
            else:
                auxilliaryVariable = givenList[index]
                givenList[index] = givenList[index - 1]
                givenList[index - 1] = auxilliaryVariable
                index -= 1
        return givenList

    def filter(self, givenList, filterCriteria):
        temporaryList = []
        for object in givenList:
            if filterCriteria(object) == True:
                temporaryList.append(object)
        return temporaryList
