def bubble_sort(resource_owner):
        for i in range(resource_owner.len):
            for j in range(resource_owner.len - 1):
                if resource_owner.get(j) > resource_owner.get(j + 1):
                    _old = resource_owner.get(j)
                    resource_owner.set(j, resource_owner.get(j + 1))
                    resource_owner.set(j + 1, _old)
                    yield resource_owner.get_snapshot()

def insertion_sort(resource_owner):
        for i in range(1, resource_owner.len):
            j = i
            while j > 0 and resource_owner.get(j - 1) > resource_owner.get(j):
                _old = resource_owner.get(j - 1)
                resource_owner.set(j - 1, resource_owner.get(j))
                resource_owner.set(j, _old)
                j -= 1
                yield resource_owner.get_snapshot()
def heap_sort(resource_owner):
        def heapify(resource_owner, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and resource_owner.get(l) > resource_owner.get(largest):
                largest = l
            if r < n and resource_owner.get(r) > resource_owner.get(largest):
                largest = r
            if largest != i:
                _old = resource_owner.get(i)
                resource_owner.set(i, resource_owner.get(largest))
                resource_owner.set(largest, _old)
                yield resource_owner.get_snapshot()
                yield from heapify(resource_owner, n, largest)
        n = resource_owner.len
        for i in range(n, -1, -1):
            yield from heapify(resource_owner, n, i)
        for i in range(n - 1, 0, -1):
            _old = resource_owner.get(i)
            resource_owner.set(i, resource_owner.get(0))
            resource_owner.set(0, _old)
            yield resource_owner.get_snapshot()
            yield from heapify(resource_owner, i, 0)

def radix_sort(resource_owner):
        def counting_sort(resource_owner, exp):
            n = resource_owner.len
            output = [0] * n
            count = [0] * 10
            for i in range(0, n):
                index = int(resource_owner.get(i) / exp)
                count[int((index) % 10)] += 1
            for i in range(1, 10):
                count[i] += count[i - 1]
            i = n - 1
            while i >= 0:
                index = int(resource_owner.get(i) / exp)
                output[count[int((index) % 10)] - 1] = resource_owner.get(i)
                count[int((index) % 10)] -= 1
                i -= 1
            for i in range(0, n):
                resource_owner.set(i, output[i])
                yield resource_owner.get_snapshot()
        m = max(resource_owner.get_snapshot())
        exp = 1
        rmn = 0
        while int(m / exp) > 0:
            for element in counting_sort(resource_owner, exp):
                if rmn > 25:
                    yield element
                    rmn = 0
                rmn += 1
            # yield from counting_sort(resource_owner, exp)
            exp *= 10
        yield resource_owner.get_snapshot()