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
                           ('q3', 'B'): ('q3', 'B', 1)
                       })

    # memasukkan nilai
    tm.initialize(dict(enumerate(inputAdd)))


    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(.2)

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
                           ('q5', 'B'): ('q6', 'B', 1)
                       })

    # memasukkan nilai
    tm.initialize(dict(enumerate(inputSubs)))


    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(.2)

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
        time.sleep(.2)

    print(tm.accepted_input())

def division(inputDiv):
    tm = TuringMachine(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'},
                       symbols={'0', '/', '#', 'x', 'B'},
                       blank_symbol='B',
                       input_symbols={'0'},
                       initial_state='q0',
                       accepting_states={'q8'},
                       transitions={
                            ('q0', '0'): ('q1', 'B', 1),
                            ('q0', '/'): ('q4', '/', 1),
                            ('q1', '0'): ('q1', '0', 1),
                            ('q1', '/'): ('q2', '/', 1),
                            ('q2', '0'): ('q3', 'x', -1),
                            ('q2', '#'): ('q6', 'B', -1),
                            ('q2', 'x'): ('q2', 'x', 1),
                            ('q3', '0'): ('q3', '0', -1),
                            ('q3', '/'): ('q3', '/', -1),
                            ('q3', 'x'): ('q3', 'x', -1),
                            ('q3', 'B'): ('q0', '0', 1),
                            ('q4', '0'): ('q4', '0', 1),
                            ('q4', '#'): ('q4', '#', 1),
                            ('q4', 'x'): ('q4', 'x', 1),
                            ('q4', 'B'): ('q5', '0', -1),
                            ('q5', '0'): ('q5', '0', -1),
                            ('q5', '/'): ('q5', '/', -1),
                            ('q5', '#'): ('q5', '#', -1),
                            ('q5', 'x'): ('q5', 'x', -1),
                            ('q5', 'B'): ('q0', 'B', 1),
                            ('q6', '0'): ('q6', 'B', -1),
                            ('q6', '/'): ('q6', 'B', -1),
                            ('q6', 'x'): ('q6', 'B', -1),
                            ('q6', 'B'): ('q7', 'B', 1),
                            ('q7', '0'): ('q8', '0', -1),
                            ('q7', 'B'): ('q7', 'B', 1)
                       })

    # memasukkan nilai
    tm.initialize(dict(enumerate(inputDiv)))


    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(.2)

    print(tm.accepted_input())

def factorial(inputFac):
    tm = TuringMachine(states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
                                'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
                                'q21', 'q22', 'q23', 'q24', 'q25'},
                       symbols={'0', '1', 'x', 'B'},
                       blank_symbol='B',
                       input_symbols={'0'},
                       initial_state='q0',
                       accepting_states={'q22'},
                       transitions={
                            ('q0', '0'): ('q0', '0', 1),
                            ('q0', 'B'): ('q1', '1', 0),
                            ('q1', '0'): ('q1', '0', -1),
                            ('q1', '1'): ('q1', '1', -1),
                            ('q1', 'B'): ('q2', 'B', 1),
                            ('q2', '0'): ('q3', 'x', 1),
                            ('q2', '1'): ('q5', '1', 1),
                            ('q3', '0'): ('q3', '0', 1),
                            ('q3', '1'): ('q3', '1', 1),
                            ('q3', 'B'): ('q4', '0', 0),
                            ('q4', '0'): ('q4', '0', -1),
                            ('q4', '1'): ('q4', '1', -1),
                            ('q4', 'x'): ('q2', 'x', 1),
                            ('q5', '0'): ('q5', '0', 1),
                            ('q5', 'B'): ('q6', '1', -1),
                            ('q6', '0'): ('q6', '0', -1),
                            ('q6', '1'): ('q6', '1', -1),
                            ('q6', 'x'): ('q6', '0', -1),
                            ('q6', 'B'): ('q7', 'B', 1),
                            ('q7', '0'): ('q8', 'B', 1),
                            ('q8', '0'): ('q9', 'x', 1),
                            ('q8', '1'): ('q15', '1', -1),
                            ('q9', '0'): ('q9', '0', 1),
                            ('q9', '1'): ('q10', '1', 1),
                            ('q10', '0'): ('q11', 'x', 1),
                            ('q10', '1'): ('q13', '1', -1),
                            ('q11', '0'): ('q11', '0', 1),
                            ('q11', '1'): ('q11', '1', 1),
                            ('q11', 'B'): ('q12', '0', 0),
                            ('q12', '0'): ('q12', '0', -1),
                            ('q12', '1'): ('q12', '1', -1),
                            ('q12', 'x'): ('q10', 'x', 1),
                            ('q13', '1'): ('q14', '1', -1),
                            ('q13', 'x'): ('q13', '0', -1),
                            ('q14', '0'): ('q14', '0', -1),
                            ('q14', '1'): ('q14', '0', -1),
                            ('q14', 'x'): ('q8', 'x', 1),
                            ('q15', '0'): ('q15', '0', -1),
                            ('q15', '1'): ('q15', '1', -1),
                            ('q15', 'x'): ('q15', 'x', -1),
                            ('q15', 'B'): ('q16', 'B', 1),
                            ('q16', '1'): ('q17', 'B', 1),
                            ('q16', 'x'): ('q18', 'B', 1),
                            ('q17', '0'): ('q17', '0', 1),
                            ('q17', '1'): ('q17', 'B', 1),
                            ('q17', 'B'): ('q22', 'B', 0),
                            ('q18', '0'): ('q23', 'B', 1),
                            ('q18', '1'): ('q23', 'B', 1),
                            ('q18', 'x'): ('q20', 'x', 1),
                            ('q19', '0'): ('q15', 'x', -1),
                            ('q19', '1'): ('q15', 'x', -1),
                            ('q19', 'x'): ('q19', 'x', -1),
                            ('q20', '0'): ('q20', '0', 1),
                            ('q20', '1'): ('q21', '1', 1),
                            ('q20', 'x'): ('q20', 'x', 1),
                            ('q21', '0'): ('q21', '0', 1),
                            ('q21', '1'): ('q19', '1', -1),
                            ('q21', 'x'): ('q21', 'x', 1),
                            ('q23', '0'): ('q23', 'B', 1),
                            ('q23', '1'): ('q22', 'B', 0),
                            ('q23', 'x'): ('q24', 'x', 1),
                            ('q24', '0'): ('q24', '0', 1),
                            ('q24', '1'): ('q24', '1', 1),
                            ('q24', 'x'): ('q24', 'x', 1),
                            ('q24', 'B'): ('q25', '1', -1),
                            ('q25', '0'): ('q25', '0', -1),
                            ('q25', '1'): ('q25', '1', -1),
                            ('q25', 'x'): ('q25', '0', 1),
                            ('q25', 'B'): ('q8', 'B', 1)
                       })

    # memasukkan nilai
    tm.initialize(dict(enumerate(inputFac)))


    while not tm.halted:
        tm.print()
        tm.step()
        time.sleep(.2)

    print(tm.accepted_input())

def main():
    start = True
    while start:
        print()
        print('Program Simulator Turing Machine')
        print('Pilih Menu:\n' +
            '1. Penjumlahan\n' + 
            '2. Pengurangan\n' + 
            '3. Perkalian\n' + 
            '4. Pembagian\n' +
            '5. Faktorial\n' +
            '6. Modulo\n' +
            '7. Exit Program')
        number = input('Masukkan pilihan: ')
        number = int(number)
        if number == 1:
            print('Selamat datang di turing machine pertambahan\n' +
                'Silakan input jumlah bilangan bulat dengan 0\n' +
                'Contoh: 3+4 --> 000+0000')
            inputAdd = input("Masukkan input: ")
            addition(inputAdd)
        elif number == 2: 
            print('Selamat datang di turing machine pengurangan\n' +
                'Silakan input jumlah bilangan bulat dengan 0\n' + 
                'Contoh: 4-3 --> 0000-000')
            inputSubs = input("Masukkan input: ")
            subtraction(inputSubs)
        elif number == 3: 
            print('Selamat datang di turing machine perkalian\n' +
                'Silakan input jumlah bilangan bulat dengan 0\n' + 
                'Pada akhir diberi tanda pagar (#)\n' +
                'Contoh: 2*2 --> 00*00#')
            inputMult = input("Masukkan input: ")
            multiplication(inputMult)
        elif number == 4: 
            print('Selamat datang di turing machine pembagian\n' +
                'Silakan input jumlah bilangan bulat dengan angka 0\n' + 
                'Pada akhir diberi tanda pagar (#) dan penyebut ditulis sebelum tanda slahs (/)\n' +
                'Contoh: 4/2 --> 00/0000#')
            inputDiv = input("Masukkan input: ")
            division(inputDiv)
        elif number == 5: 
            print('Selamat datang di turing machine faktorial\n' +
                'Silakan input jumlah bilangan bulat dengan angka 0\n' +
                'Contoh: 3! --> 000')
            inputFac = input("Masukkan input: ")
            factorial(inputFac)
        elif number == 6: 
            print('Selamat datang di turing machine modulo\n' +
                'Silakan input jumlah bilangan bulat dengan angka 0\n' +
                'Contoh: 3! --> 000')
            inputMod = input("Masukkan input: ")
            modulo(inputMod)
        elif number == 7:
            print('Program telah berakhir.')
            start = False
        else: 
            print('Input yang Anda masukkan salah.')
        
if __name__ == '__main__':
    main()