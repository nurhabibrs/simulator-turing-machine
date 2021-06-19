import time

from turing_machine import TuringMachine


def main():
    tm = TuringMachine(states={'q1', 'q2', 'q3', 'q4'},
                       symbols={'0', '+', 'B'},
                       blank_symbol='B',
                       input_symbols={'0'},
                       initial_state='q1',
                       accepting_states={'q4'},
                       transitions={
                           ('q0', '0'): ('q1', '0', 1),
                           ('q0', '+'): ('q4', 'B', 1),
                           ('q0', 'B'): ('q0', 'B', 1),
                           ('q1', '0'): ('q2', '0', 1),
                           ('q1', '+'): ('q1', '0', 1),
                           ('q1', 'B'): ('q2', 'B', 1),
                           ('q2', '0'): ('q2', '0', 1),
                           ('q2', '+'): ('q2', '0', 1),
                           ('q2', 'B'): ('q3', 'B', -1),
                           ('q3', '0'): ('q4', 'B', 1),
                        #    ('q3', '+'): (ERROR),
                           ('q3', 'B'): ('q3', 'B', 1),
                       })
    # tm.initialize({i: '1' for i in range(5)})
    # or a nicer way to input a string

    # untuk 4+2 = 6
    tm.initialize(dict(enumerate("0000+00")))


    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(.3)

    print(tm.accepted_input())


if __name__ == '__main__':
    main()