class DFA:
    def __init__(self, states, t_function, accepting_states, starting_point):
        self.states = states
        self.t = t_function  # this is a dict
        self.accepted = accepting_states
        self.start = starting_point

    def print(self):
        print(
            f"DFA with states: {self.states}, accepting states: {self.accepted}, starting point: {self.start}"
        )

    def get_next_state(self, state_input):
        try:
            return self.t[state_input]
        except KeyError:
            return False

    def run(self, input):
        cur = self.start
        for i in range(len(input)):
            s = input[i]
            cur = self.get_next_state((cur, s))
            if cur is False:
                return False

        return True if cur in self.accepted else False

    def NFA(self):
        new_t = {cs: {inp} for cs, inp in self.t.items()}
        return NFA(self.states, new_t, self.accepted, {self.start})


class NFA:
    def __init__(
        self,
        symbols: set,
        states: set,
        t_function: dict,
        accepting_states: set,
        starting_points: set,
    ):
        """
        Creates an NFA

        Args:
            symbols: set of the alphabet
            states: set containing state labels
            t_function: A dict of the transitions. Keys are of the form (x, y) where x is current state label
                and y is input. Values are of the form {x, y, z}, where x,y,z are possible end states
            accepting_states: a set of accepting states
            starting_points: a set of starting points

        Returns an NFA object with method run()
        """
        self.states = states
        self.symbols = symbols
        self.t = t_function  # this is a dict
        self.accepted = accepting_states
        self.starts = starting_points

    def print(self):
        print(
            f"NFA with states: {self.states}, input: {self.input}, accepting states: {self.accepted}, starting point: {self.start}"
        )

    def get_next_state(self, state_input):
        try:
            return self.t[state_input]
        except KeyError:
            return set({})

    def run(self, input):
        cur = self.starts

        for i in input:
            new_cur = set({})
            for j in cur:
                new_cur = new_cur | self.get_next_state((j, i))
            cur = new_cur

        return (cur & self.accepted) != set({})

    def DFA(self):
        states_list = [self.starts]
        new_states = [self.starts]
        new_transition = dict()
        new_accepted = set()

        index = 0
        while index < len(states_list):
            cur_state = frozenset(states_list[index])
            for i in self.symbols:
                new_state = set()
                for j in cur_state:
                    new_state.update(self.get_next_state((j, i)))
                if new_state not in states_list:
                    states_list.append(new_state)
                    new_states.append(new_state)
                if bool(self.accepted & new_state):
                    new_accepted.add(frozenset(new_state))
                new_transition[(cur_state, i)] = frozenset(new_state)
            index += 1

        return DFA(new_states, new_transition, new_accepted, frozenset(self.starts))


# nfa = NFA(
#     {"0", "1"},
#     {0, 1, 2},
#     {
#         (0, "0"): {0},
#         (0, "1"): {0, 1},
#         (1, "0"): {2},
#         (1, "1"): {2},
#         (2, "0"): {0},
#         (2, "1"): {1},
#     },
#     {2},
#     {0},
# )

# print(nfa.run("10"))
# converted_nfa = nfa.DFA()
# print(converted_nfa.run("10"))
