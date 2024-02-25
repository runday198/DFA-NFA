from transition1 import transition_0n_1n


class PDA:
    z = "z"

    def __init__(self, symbols, states, t_function, accepting_states, starting_points):
        self.symbols = symbols
        self.states = states
        self.t = t_function
        self.accepted = accepting_states
        self.starts = starting_points

        self.stack = [self.z]

    def run(self, input):
        cur = self.starts

        for sym in input:
            if sym not in self.symbols:
                return False

            cur = self.t(cur, sym, self.stack, self.z)

        while True:
            new_cur = self.t(cur, "", self.stack, self.z)
            if bool(new_cur & self.accepted):
                cur = new_cur
            if cur == new_cur:
                break
            cur = new_cur

        return bool(cur & self.accepted) and len(self.stack) == 0

# TODO: This function does not work. It needs the length of the input sequence or some other solution
def transition_ab_palindrome(cur: set, input: str, stack: list, stack_start: str):
    new_state = set()

    for i in cur:
        if i == 0:
            new_state.add(0)
            new_state.add(1)
            if input == "a":
                stack.append("a")
            elif input == "b":
                stack.append("b")
        elif i == 1:
            new_state.add(1)
            if input == "a":
                top = stack.pop()
                if top != "a":
                    stack.append(top)
            elif input == "b":
                top = stack.pop()
                if top != "b":
                    stack.append(top)
            elif input == "":
                top = stack.pop()
                if top == stack_start:
                    new_state.add(2)
                else:
                    stack.append(top)

    return new_state


# pda1 = PDA({"0", "1"}, {0, 1, 2}, transition_0n_1n, {2}, {0})

# print(pda1.run("0011"))

pda2 = PDA({"a", "b"}, {0, 1, 2}, transition_ab_palindrome, {2}, {0})

print(pda2.run(""))
