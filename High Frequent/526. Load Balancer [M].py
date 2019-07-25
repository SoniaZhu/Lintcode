import random
class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.idToIndex = dict()
        self.servers = []

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        if server_id not in self.idToIndex:
            self.idToIndex[server_id] = len(self.servers)
            self.servers.append(server_id)

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id in self.idToIndex:
            index = self.idToIndex.pop(server_id)
            self.servers[index] = self.servers[-1]
            self.idToIndex[self.servers[index]] = index
            self.servers.pop()

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        if self.servers:
            pick = random.randint(0,len(self.servers)-1)
            return self.servers[pick]
        return None

###########################
import random
class LoadBalancer:
    def __init__(self):
        self.servers = set()

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        self.servers.add(server_id)

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        self.servers.discard(server_id)

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        return random.sample(self.servers,1)[0] if self.servers else None
