import queue


class PQEntry:

    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val


class DocumentPrint:
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val

    def __lt__(self, other):
        return self.val > other.val


def gettime(n_test):
    """
            3
        1 0
        5
        4 2
        1 2 3 4
        6 0
        1 1 9 1 1 1
    :param n_test:
    :param n:
    :param m:
    :param arr:
    :return:
    """
    for i in range(n_test):
        n, m = map(int, input().split(' '))
        queue_print = queue.Queue()
        max_heep_print = queue.PriorityQueue()
        list_print = list(map(int, input().split(' ')))
        for idx, val in enumerate(list_print):
            queue_print.put(DocumentPrint(idx, val))
            max_heep_print.put(DocumentPrint(idx, val))
        count_time = 0
        first_val = queue_print.get()
        a = first_val.val
        b = first_val.idx
        first_max = max_heep_print.get()
        c = first_max.idx
        d = first_max.val
        while True:
            if first_val.val == first_max.val:
                count_time += 1
                if first_val.idx == m:
                    print(count_time)
                    break
                first_val = queue_print.get()
                first_max = max_heep_print.get()

            else:
                queue_print.put(first_val)
                first_val = queue_print.get()


n_test = int(input())
gettime(n_test)
