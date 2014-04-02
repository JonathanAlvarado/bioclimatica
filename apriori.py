from itertools import chain, combinations
from collections import defaultdict
from optparse import OptionParser


def subsets(arr):
    return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])


def items_min_support(itemSet, trans_list, minSupport, freqSet):
    _itemSet = set()
    localSet = defaultdict(int)

    for item in itemSet:
        for transaction in trans_list:
            if item.issubset(transaction):
                freqSet[item] += 1
                localSet[item] += 1

    for item, count in localSet.items():
        support = float(count)/len(trans_list)

        if support >= minSupport:
            _itemSet.add(item)

    return _itemSet


def join_set(itemSet, length):
    return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


def get_item_set_trans_list(data_iterator):
    trans_list = list()
    itemSet = set()

    for record in data_iterator:
        transaction = frozenset(record)
        trans_list.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))
    return itemSet, trans_list


def apriori(data_iter, minSupport, minConfidence):
    itemSet, trans_list = get_item_set_trans_list(data_iter)

    freqSet = defaultdict(int)
    largeSet = dict()

    assocRules = dict()

    oneCSet = items_min_support(itemSet,
                                        trans_list,
                                        minSupport,
                                        freqSet)

    currentLSet = oneCSet
    k = 2
    while(currentLSet != set([])):
        largeSet[k-1] = currentLSet
        currentLSet = join_set(currentLSet, k)
        currentCSet = items_min_support(currentLSet,
                                                trans_list,
                                                minSupport,
                                                freqSet)
        currentLSet = currentCSet
        k = k + 1

    def getSupport(item):
        return float(freqSet[item])/len(trans_list)

    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), getSupport(item))
                           for item in value])

    toRetRules = []
    for key, value in largeSet.items()[1:]:
        for item in value:
            _subsets = map(frozenset, [x for x in subsets(item)])
            for element in _subsets:
                remain = item.difference(element)
                if len(remain) > 0:
                    confidence = getSupport(item)/getSupport(element)
                    if confidence >= minConfidence:
                        toRetRules.append(((tuple(element), tuple(remain)),
                                           confidence))
    return toRetItems, toRetRules


def get_results(items, rules):
    for item, support in items:
        print "item: %s , %.3f" % (str(item), support)

    print "\n------------------------ RULES:"

    for rule, confidence in rules:
        pre, post = rule
        print "Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence)


def open_file(fname):
    file_iter = open(fname, 'rU')
    for line in file_iter:
        line = line.strip().rstrip(',')
        record = frozenset(line.split(','))
        yield record


if __name__ == "__main__":

    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile',
                         dest='input',
                         help='filename containing csv',
                         default=None)
    optparser.add_option('-s', '--minSupport',
                         dest='minS',
                         help='minimum support value',
                         default=0.15,
                         type='float')
    optparser.add_option('-c', '--minConfidence',
                         dest='minC',
                         help='minimum confidence value',
                         default=0.6,
                         type='float')

    (options, args) = optparser.parse_args()

    inFile = None
    if options.input is None:
            inFile = sys.stdin
    elif options.input is not None:
            inFile = open_file(options.input)
    else:
        print 'No dataset filename specified, system with exit\n'
        sys.exit('System will exit')

    minSupport = options.minS
    minConfidence = options.minC

    items, rules = apriori(inFile, minSupport, minConfidence)

    get_results(items, rules)
