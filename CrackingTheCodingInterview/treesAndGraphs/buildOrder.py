class Project:
    '''
    Project class for a graph.
    '''
    def __init__(self, name, marked=False):
        self.name = name
        self.marked = marked
        self.dependencies = list()

    def __str__(self):
        return str(self.name)

def buildOrder(projects):
    '''
    Basically a topological sort.
    '''
    flag = True
    while flag:
        flag = False
        for proj in projects:
            if proj.marked is False:
                flag = True
                dep_flag = False
                if len(proj.dependencies) == 0:
                    proj.marked = True
                for dep in proj.dependencies:
                    if dep.marked is False:
                        dep_flag = True
                        break
                    proj.marked = True
                if not dep_flag:
                    print(proj.name, end=' ')

if __name__ == '__main__':
    proj_list = [chr(i) for i in range(97, 97+6)]
    graph = []
    for p in proj_list:
        graph.append(Project(p))
    
    # -> Test suite 1
    # graph[3].dependencies.append(graph[0])
    # graph[1].dependencies.append(graph[5])
    # graph[3].dependencies.append(graph[1])
    # graph[0].dependencies.append(graph[5])
    # graph[2].dependencies.append(graph[3])

    # -> Test suite 2
    graph[0].dependencies.extend((graph[1], graph[2]))
    graph[1].dependencies.extend((graph[3], graph[4]))
    graph[2].dependencies.append(graph[4])
    graph[3].dependencies.append(graph[5])
    graph[5].dependencies.append(graph[4])

    for p in graph:
        print(p.name, [dep.name for dep in p.dependencies])
    print("######## Output ############")
    buildOrder(graph)