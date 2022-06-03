import node
from problem import Problem
from node import Node
import heapq

def expand(problem, node):
    nodeslist = []
    actions = problem.actions(node.state)  # returns the available actions in a certain state
    if actions is not None:
        for action in actions:
            res = problem.result(node.state, action)
            action_cost = node.path_cost + problem.action_cost(node.state, action, res)
            nodeslist.append(Node(res, node, action, action_cost))

    return nodeslist



def get_path_actions(node):
    if node is None:
        return []

    if node.parent_node is None:
        return []
    else:
        nodelist2 = get_path_actions(node.parent_node)
        nodelist2.append(node.action_from_parent)
        return nodelist2


def get_path_states(node):
    if node is None:
        return []

    if node.parent_node is None:
        nodelist1 = [node.state]
        return nodelist1
    else:
        nodelist2 = get_path_states(node.parent_node)
        nodelist2.append(node.state)
        return nodelist2


def best_first_search(problem, f):
    node = Node(problem.initial_state)
    frontier = PriorityQueue([node], f)
    reached = {node.state: node}
    while len(frontier) != 0:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        else:
            for child in expand(problem, node):
                s = child.state
                if s not in reached or child.path_cost < reached[s].path_cost:
                    reached[s] = child
                    frontier.add(child)




    return None



def best_first_search_treelike(problem, f):
    node = Node(problem.initial_state)
    frontier = PriorityQueue([node], f)
    while frontier:
        newNode = frontier.pop()
        if problem.is_goal(newNode.state):
            return newNode
        else:
            for child in expand(problem, newNode):
                s = child.state
                frontier.add(child)




    return None



def breadth_first_search(problem, treelike = False):
    if treelike:
       return best_first_search_treelike(problem, f=lambda node: node.depth)
    else:
        return best_first_search(problem, f=lambda node: node.depth)



def depth_first_search(problem, treelike = False):
    if treelike:
       return best_first_search_treelike(problem, f=lambda node: -1*node.depth)
    else:
        return best_first_search(problem, f=lambda node: -1*node.depth)



def uniform_cost_search(problem, treelike = False):
    if treelike:
       return best_first_search_treelike(problem, f=lambda node: node.path_cost)
    else:
        return best_first_search(problem, f=lambda node: node.path_cost)



def greedy_search(problem, h, treelike = False):
    if treelike:
        return best_first_search_treelike(problem, h)
    else:
        return best_first_search(problem, h)


def astar_search(problem, h, treelike = False):
    if treelike:
       return best_first_search_treelike(problem,  f=lambda node: node.path_cost+ h(node))
    else:
        return best_first_search(problem, f=lambda node: node.path_cost + h(node))



'''def is_empty(frontier):
    s = frontier.pop
    if s is None:
        return False
    else:
        frontier.add(s)
        return True'''




class PriorityQueue:
    def __init__(self, items=(), priority_function=(lambda x: x)):
        self.priority_function = priority_function
        self.pqueue = []
        # add the items to the PQ
        for item in items:
            self.add(item)


    def add(self, item):
        pair = (self.priority_function(item), item)
        heapq.heappush(self.pqueue, pair)


    def pop(self):
        return heapq.heappop(self.pqueue)[1]


    def __len__(self):
        return len(self.pqueue)