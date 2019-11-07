# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler
        
    def insert(self, part):
        # Insert the node as before
        if not self.children.get(part):
            self.children[part] = RouteTrieNode()
            
            
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.handler = handler
        
    def insert(self, parts, handler): # parts is a list
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        
        for part in parts:
            node.insert(part)

            node = node.children[part]

        node.handler = handler

    def find(self, parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        
        for part in parts:
            if not node.children.get(part):
                return None
            node = node.children[part]
        
        return node.handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.RouteTrie = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the path parts
        # as a list to the RouteTrie
        parts = self.split_path(path)
        
        self.RouteTrie.insert(parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        parts = self.split_path(path)
        handler = self.RouteTrie.find(parts)
        
        if handler is None:
            return self.not_found_handler
        else:
            return handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path == '/' or path == '':
            return []
        
        return path.strip('/').split('/')
        
        

# create the router and add a route
router = Router("root handler", "not found handler") 
print('\nAdd a route \"/home/about\" with a handler \"about handler\"')
router.add_handler("/home/about", "about handler")  # add a route
        
# test case 1
print('\nTest case 1: lookup of "/". Answer is root handler.')
print(router.lookup('/'))

# test case 2
print('\nTest case 2: lookup of "/home/". Answer is not found handler.')
print(router.lookup('/home/'))

# test case 3
print('\nTest case 3: lookup of "/home/about". Answer is about handler.')
print(router.lookup('/home/about'))

# test case 4
print('\n\nTest case 4: lookup of "/home/about/". Answer is about handler.')
print(router.lookup('/home/about/'))

# test case 5
print('\nTest case 5: lookup of "/home/about/me". Answer is not found handler.')
print(router.lookup('/home/about/me'))

# test case 6
print('\nTest case 6: lookup of "123456". Answer is not found handler.')
print(router.lookup('123456'))

# test case 7
print('\nTest case 7: lookup of "". Answer is root handler.')
print(router.lookup(''))

# test case 8
print('\nTest case 8: lookup of "/////". Answer is not found handler.')
print(router.lookup('/////'))
