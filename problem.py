


class Problem:

    def __init__(self, initial_state, goal_state = None):
        self.initial_state = initial_state
        self.goal_state = goal_state


    def actions(self, state):
        raise NotImplementedError


    def result(self, state, action):
        raise NotImplementedError


    def is_goal(self, state):
        if(state == self.goal_state):
            return True
        else:
            return False


    def action_cost(self, state1, action, state2):
        return 1


    def h(self, node):
        return 0


class RouteProblem(Problem):
    def __init__(self, initial_state, goal_state = None, map_graph = None, map_coords = None):
        super().__init__(initial_state, goal_state)
        self.map_graph = map_graph
        self.map_coords = map_coords
        self.neighbors = map_graph.keys()


    def actions(self, state):
        allstates = self.map_graph
        reached = []
        for reach in allstates:
            if reach[0] == state:
                reached.append(reach[1])

        return reached



    def result(self, state, action):
        resState = state
        for tuple in self.map_graph:
            if state == tuple[0] and action == tuple[1]:
                resState = action
                return resState


        return resState


    def action_cost(self, state1, action, state2):
        value = 0
        for tuple in self.map_graph:
            if state1 == tuple[0] and action == tuple[1]:
                value = self.map_graph[tuple]
                return value


        return value


    def h(self, node):
        tuple = self.map_coords[self.goal_state]
        goalX = tuple[0]
        goalY = tuple[1]
        if self.is_goal(node.state):
            return 0
        else:
            tuple = self.map_coords[node.state]
            x = tuple[0]
            y = tuple[1]

            distance = ((goalX - x)**2 + (goalY - y)**2)**0.5
            return distance



class GridProblem(Problem):
    def __init__(self, initial_state, N, M, wall_coords = None, food_coords = None):
        self.N = N
        self.M = M
        self.wall_coords = wall_coords
        self.food_coords = food_coords
        self.food_eaten = tuple([False] * len(food_coords))
        self.initial_state = (initial_state, self.food_eaten)


    def actions(self, state):
        actions = []
        coords = state[0] #get the tuple of coords of the tuple of coords+food_eaten
        x = coords[0]
        y = coords[1]

        if (x, y+1) not in self.wall_coords and y+1 <= self.N:
            actions.append('up')

        if (x, y-1) not in self.wall_coords and y-1 >= 1:
            actions.append('down')

        if (x+1, y) not in self.wall_coords and x+1 <= self.M:
            actions.append('right')

        if (x-1, y) not in self.wall_coords and x-1 >= 1:
            actions.append('left')
        return actions
        """probUP = False
        probDW = False
        probLF = False
        probRH = False

        for wall in self.wall_coords:
            if (x + 1) == wall[0] or (x + 1) > self.M: #if a move right is illegal
                probRH = True
            if (x - 1) == wall[0] or (x - 1) < 1: #if a move left is illegal
                probLF = True

            if (y + 1) == wall[1] or (y + 1) > self.N: #if a move up is illegal
                probUP = True

            if (y - 1) == wall[1] or (y - 1) < 1: #if a move down is illegal
                probDW = True



        if probUP is False:
            actions.append('up')

        if probDW is False:
            actions.append('down')

        if probRH is False:
            actions.append('right')

        if probLF is False:
            actions.append('left')"""


    def result(self, state, action):
        actionList = self.actions(state)
        food_eaten = state[1]
        state = state[0]
        if action in actionList:
            if action is 'up':
                state = (state[0], state[1]+1)
            if action is 'down':
                state = (state[0], state[1]-1)
            if action is 'right':
                state = (state[0]+1, state[1])
            if action is 'left':
                state = (state[0]-1, state[1])
            if state in food_eaten:
                index = self.food_coords.index(state)
                temp = list(food_eaten)
                temp[index] = True
                self.food_eaten = tuple(temp)


            state = (state, self.food_eaten)
            return state
        else:
            return state



    def action_cost(self, state1, action, state2):
        return 1



    def is_goal(self, state):
        for value in state[1]:
            if value is False:
                return False


        return True



    def h(self, node):
        if self.is_goal(node.state):
            return 0
        else:
            coords = node.state[0]
            x = coords[0]
            y = coords[1]
            i = 0
            distance = 1000000000000000000 ###could use a list and find min later
            for food in node.state[1]:
                if food is False:
                    coords = self.food_coords[i]
                    xcoords = coords[0]
                    ycoords = coords[1]
                    i = i+1
                    newDistance = abs(x - xcoords) + abs(y - ycoords)
                    if newDistance < distance:
                        distance = newDistance


            return distance
