Problem 1: LRU Cache

I've simulated LRU using an ordered dictionary. Every time and entry is read/written it's sent to one extreme end; overtime stale entries move towards other extreme end; hence when capacity is full we can pop item from that end.

Runtime analysis:

Average case runtime of lookup in dict is O(1) same goes for adding item to dict().
OrderedDict moves items in constant time too. Hence all operations performed here are constant time.

Space complexity is O(n) where n is capacity of LRU.