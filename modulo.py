import time

from turing_machine import TuringMachine

def modulo(inputAdd):
    tm = TuringMachine(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'},
                       symbols={'0', 'm', 'X', 'Y', 'B'},
                       blank_symbol='B',
                       input_symbols={'0'},
                       initial_state='q0',
                       accepting_states={'q9'},
                       transitions={
                           ('q0', '0'): ('q0', '0', 1),
                           ('q0', 'm'): ('q0', 'm', 1),                        
                           ('q0', 'B'): ('q1', 'B', -1),
                           ('q1', '0'): ('q2', 'Y', -1),
                           ('q1', 'm'): ('q5', 'm', -1),                       
                           ('q2', '0'): ('q2', '0', -1),
                           ('q2', 'm'): ('q3', 'm', 1),                        
                           ('q3', '0'): ('q4', 'X', 1),
                           ('q3', 'm'): ('q3', 'm', -1),
                           ('q3', 'X'): ('q3', 'X', -1),                       
                           ('q3', 'B'): ('q8', 'B', 1),
                           ('q4', '0'): ('q4', '0', 1),
                           ('q4', 'm'): ('q4', 'm', 1),
                           ('q4', 'X'): ('q4', 'X', 1),
                           ('q4', 'Y'): ('q1', 'Y', 1),                     
                           ('q5', '0'): ('q6', '0', 1),
                           ('q5', 'm'): ('q5', 'm', -1),
                           ('q5', 'X'): ('q5', 'm', -1),                   
                           ('q5', 'B'): ('q8', 'B', 1),
                           ('q6', 'm'): ('q6', 'm', 1),
                           ('q6', 'Y'): ('q6', '0', 1),
                           ('q6', 'B'): ('q7', 'B', -1),
                           ('q7', '0'): ('q7', '0', -1),
                           ('q7', 'm'): ('q7', 'm', -1),
                           ('q7', 'B'): ('q0', 'B', 1),
                           ('q8', '0'): ('q8', 'B', 1),
                           ('q8', 'm'): ('q8', 'B', 1),
                           ('q8', 'X'): ('q8', '0', 1),
                           ('q8', 'Y'): ('q8', 'B', 1),
                           ('q8', 'B'): ('q9', 'B', 0),
                       })

    # memasukkan nilai
    tm.initialize(dict(enumerate(inputAdd)))


    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(.3)

    print(tm.accepted_input())