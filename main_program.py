import time

from turing_machine import TuringMachine

def addition(inputAdd):
    tm = TuringMachine(states={'q0', 'q1', 'q2', 'q3', 'q4'},
                       symbols={'0', '+', 'B'},
                       blank_symbol='B',
                       input_symbols={'0'},
                       initial_state='q0',
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
                           ('q3', 'B'): ('q3', 'B', 1),
                       })

    # memasukkan nilai
    tm.initialize(dict(enumerate(inputAdd)))


    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(.3)

    print(tm.accepted_input())

def subtraction(inputSubs):
    tm = TuringMachine(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
                       symbols={'0', '-', 'B'},
                       blank_symbol='B',
                       input_symbols={'0'},
                       initial_state='q0',
                       accepting_states={'q4', 'q6'},
                       transitions={
                           ('q0', '0'): ('q1', 'B', 1),
                           ('q0', '-'): ('q5', 'B', 1),
                           ('q1', '0'): ('q1', '0', 1),
                           ('q1', '-'): ('q1', '-', 1),
                           ('q1', 'B'): ('q2', 'B', -1),
                           ('q2', '0'): ('q3', 'B', -1),
                           ('q2', '-'): ('q4', '0', -1),
                           ('q3', '0'): ('q3', '0', -1),
                           ('q3', '-'): ('q3', '-', -1),
                           ('q3', 'B'): ('q0', 'B', 1),
                           ('q5', '0'): ('q5', '0', 1),
                           ('q5', 'B'): ('q6', 'B', 1),
                       })

    # memasukkan nilai
    tm.initialize(dict(enumerate(inputSubs)))


    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(.3)

    print(tm.accepted_input())

def multiplication(inputMult):
    tm = TuringMachine(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'},
                       symbols={'0', '*', 'x', '#', 'B'},
                       blank_symbol='B',
                       input_symbols={'0'},
                       initial_state='q0',
                       accepting_states={'q7'},
                       transitions={
                            ('q0', '0'): ('q1', 'B', 1),
                            ('q0', '*'): ('q0', 'B', -1),
                            ('q0', 'B'): ('q6', 'B', 1),
                            ('q1', '0'): ('q1', '0', 1),
                            ('q1', '*'): ('q2', '*', 1),
                            ('q2', '0'): ('q3', 'x', 1),
                            ('q2', '#'): ('q5', '#', -1),
                            ('q3', '0'): ('q3', '0', 1),
                            ('q3', '#'): ('q3', '#', 1),
                            ('q3', 'B'): ('q4', '0', -1),
                            ('q4', '0'): ('q4', '0', -1),
                            ('q4', 'x'): ('q2', 'x', 1),
                            ('q4', '#'): ('q4', '#', -1),
                            ('q5', '0'): ('q5', '0', -1),
                            ('q5', '*'): ('q5', '*', -1),
                            ('q5', 'x'): ('q5', '0', -1),
                            ('q5', 'B'): ('q0', 'B', 1),
                            ('q6', '0'): ('q6', 'B', 1),
                            ('q6', '#'): ('q7', 'B', 0),
                            ('q6', 'B'): ('q6', 'B', 1)
                       })

    # memasukkan nilai
    tm.initialize(dict(enumerate(inputMult)))


    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(.3)

    print(tm.accepted_input())

def main():
    print('Program Simulator Turing Machine')
    print('Pilih Menu:\n' +
        '1. Penjumlahan\n' + 
        '2. Pengurangan')
    number = input('Masukkan pilihan: ')
    number = int(number)
    if number == 1:
        print('Selamat datang di turing machine pilihan\nSilakan input jumlah bilangan bulat dengan angka 0\n'+
            'Contoh: 3+4 --> 000+0000')
        inputAdd = input("Masukkan input: ")
        addition(inputAdd)
    elif number == 2: 
        print('Selamat datang di turing machine pilihan\nSilakan input jumlah bilangan bulat dengan angka 0\n'+
            'Contoh: 4-3 --> 0000-000')
        inputSubs = input("Masukkan input: ")
        subtraction(inputSubs)
    elif number == 3: 
        print('Selamat datang di turing machine pilihan\nSilakan input jumlah bilangan bulat dengan angka 0\n'+
            'Contoh: 4*3 --> 0000*000')
        inputMult = input("Masukkan input: ")
        multiplication(inputMult)
        
if __name__ == '__main__':
    main()