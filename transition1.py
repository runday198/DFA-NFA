def transition_0n_1n(cur: set, input: str, stack: list, stack_start: str):
    new_state = set()

    for i in cur:
        if i == 0:
            new_state.add(1)
            if input == "0":
                new_state.add(0)
                top = stack.pop()
                if top == "A":
                    stack.append("A")
                    stack.append("A")
                elif top == stack_start:
                    stack.append(stack_start)
                    stack.append("A")
        elif i == 1:
            if input == "1":
                top = stack.pop()
                if top == "A":
                    new_state.add(1)
                else:
                    stack.append(top)
            elif input == "":
                top = stack.pop()
                if top == stack_start:
                    new_state.add(2)
                else:
                    stack.append(top)

    return new_state
