from podracer import ResourceOwner
from generator import DataGenerator
from sorting_algorithms import bubble_sort, insertion_sort, heap_sort, radix_sort

def main():
    SAMPLE_SIZE = 150
    dg = DataGenerator(SAMPLE_SIZE)
    # resource_owner = ResourceOwner(sample_size=SAMPLE_SIZE, data=dg.rand())
    # resource_owner.animate(bubble_sort)
    # resource_owner.logSummary()

    # resource_owner = ResourceOwner(sample_size=SAMPLE_SIZE, data=dg.rand())
    # resource_owner.animate(insertion_sort)
    # resource_owner.logSummary()

    # resource_owner = ResourceOwner(sample_size=SAMPLE_SIZE, data=dg.rand())
    # resource_owner.animate(heap_sort)
    # resource_owner.logSummary()
    resource_owner = ResourceOwner(sample_size=SAMPLE_SIZE, data=dg.lin())
    resource_owner.animate(radix_sort)
    resource_owner.logSummary()
if __name__ == "__main__":
    main()
