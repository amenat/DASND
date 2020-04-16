from collections import defaultdict
from typing import List, Union

# A RouteTrieNode will be similar to our autocomplete TrieNode...
# with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = defaultdict(RouteTrieNode)
        self.handler = None

    # def insert(self):                # not implemented/ not equired
    #     # Insert the node as before
    #     pass


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the
        # root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = None
        self.not_found_handler = None

    def insert(self, addr: List[str], handler:str) -> None:
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        ptr = self.root

        for subaddr in addr:
            ptr = ptr.children[subaddr]

        ptr.is_page = True
        ptr.handler = handler

    def find(self, addr: List[str]) -> str:
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        ptr = self.root

        for subaddr in addr:
            if subaddr not in ptr.children:
                return self.not_found_handler
            ptr = ptr.children[subaddr]

        # if handler exists return it; else 404
        if ptr.handler:
            return ptr.handler
        else:
            return self.not_found_handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler: str, not_found_handler: str) -> None:
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.server = RouteTrie()
        self.server.root.handler = root_handler
        self.server.not_found_handler = not_found_handler

    def add_handler(self, path: str, handler: str) -> None:
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        addr = self.split_path(path)
        self.server.insert(addr, handler)

    def lookup(self, path: str) -> str:
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        addr = self.split_path(path)
        return self.server.find(addr)

    def split_path(self, path: str) -> List[str]:
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        addr = path[1:].split('/')

        # remove trailing slash
        if addr[-1] == '':
            addr.pop()

        return addr


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
