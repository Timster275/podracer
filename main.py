from podracer import ResourceOwner
from sorting_algorithms import bubble_sort, insertion_sort, heap_sort, radix_sort
def main():
    resource_owner = ResourceOwner(sample_size=40)
    resource_owner.animate(bubble_sort)
    resource_owner.logSummary()

    resource_owner = ResourceOwner(sample_size=40)
    resource_owner.animate(insertion_sort)
    resource_owner.logSummary()

    resource_owner = ResourceOwner(sample_size=40)
    resource_owner.animate(heap_sort)
    resource_owner.logSummary()
    
    resource_owner = ResourceOwner(sample_size=40)
    resource_owner.animate(radix_sort)
    resource_owner.logSummary()
if __name__ == "__main__":
    main()
