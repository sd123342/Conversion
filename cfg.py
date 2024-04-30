class PDA:
    def __init__(self, states, input_alphabet, stack_alphabet, transitions, start_state, start_stack_symbol):
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transitions = transitions  # Dict with key as (state, input, stack_top) and value as (new_state, new_stack)
        self.start_state = start_state
        self.start_stack_symbol = start_stack_symbol

class CFG:
    def __init__(self):
        self.productions = {}  # Dict with key as non-terminal and value as list of replacements

    def add_production(self, non_terminal, replacement):
        if non_terminal in self.productions:
            self.productions[non_terminal].append(replacement)
        else:
            self.productions[non_terminal] = [replacement]

    def display(self):
        for non_terminal, replacements in self.productions.items():
            replacements_str = " | ".join(replacements)
            print(f"{non_terminal} -> {replacements_str}")

def cfg_to_pda(cfg):
    states = set()
    input_alphabet = set()
    stack_alphabet = set()
    transitions = {}
    start_state = 'q0'
    start_stack_symbol = 'Z'

    # Create PDA states
    for non_terminal in cfg.productions:
        states.add(non_terminal)
        for production in cfg.productions[non_terminal]:
            for symbol in production:
                if symbol.isupper():
                    states.add(symbol)

    # Create input alphabet and stack alphabet
    for non_terminal in cfg.productions:
        for production in cfg.productions[non_terminal]:
            for symbol in production:
                if symbol.islower():
                    input_alphabet.add(symbol)
                elif symbol.isupper():
                    stack_alphabet.add(symbol)

    # Create transitions based on CFG rules
    for non_terminal in cfg.productions:
        for production in cfg.productions[non_terminal]:
            if len(production) == 1:
                # Handle epsilon productions
                transitions[(non_terminal, '', production)] = (non_terminal, '')
            elif len(production) == 2:
                transitions[(non_terminal, production[0], production[1])] = (non_terminal, '')
            elif len(production) == 3:
                transitions[(non_terminal, production[0], production[1])] = (production[2], production[1])

    pda = PDA(states, input_alphabet, stack_alphabet, transitions, start_state, start_stack_symbol)
    return pda

# Example usage
cfg = CFG()
cfg.add_production('S', 'aSb')
cfg.add_production('S', 'epsilon')

pda = cfg_to_pda(cfg)
print("States:", pda.states)
print("Input Alphabet:", pda.input_alphabet)
print("Stack Alphabet:", pda.stack_alphabet)
print("Transitions:", pda.transitions)
print("Start State:", pda.start_state)
print("Start Stack Symbol:", pda.start_stack_symbol)
