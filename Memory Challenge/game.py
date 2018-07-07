# source code

import random, os, time, msvcrt, sys


# main code
def main():
    # main screen 1
    os.system('color 1f')
    print('\n'*12)
    print('Memory Challenge Game'.center(120))
    time.sleep(2)

    # main screen 2
    os.system('cls')
    os.system('color 3f')
    print('\n'*12)
    print('---< Remember The Sequence of Symbols in each Level >---'.center(120))
    time.sleep(4)
    os.system('cls')

    # main screen 3
    for i in range(8):
        status = _level_(i+1, i+3)
        if status == 'win': continue
        else: play_again()
    play_again()


# function to set a level
def _level_(num, _size_):
    os.system('color 1f')
    j = 0
    _list_ = random_sym(_size_)
    temp_list = [' ' for x in range(_size_)]
    status = 'win'
    
    # screen 1
    screen_top(num)
    display_sym(_list_)
    print('\n'*12)
    display_timer(0.04)
    
    # screen 2
    while True:
        screen_top(num)
        display_sym(temp_list)
        print('\n'*12)
        inp = msvcrt.getwch()
        if _list_[j] == inp :
            temp_list[j] = inp
        else:
            status = 'lose'
            break
        if j == len(_list_)-1: break
        j += 1

    # screen 3
    screen_top(num)
    display_sym(_list_)
    print('\n'*12)
    if status == 'win': time.sleep(1)
    else: time.sleep(3)
    display_result(status, num)
    print('\n'*12)
    print('_'*60)
    
    return status


# for forming a set of random symbols
def random_sym(_size_):
    symbol = ['+', '-', '*', '/', '.', '[', ']', '=']
    _list_ = []
    while True:
        sym = symbol[random.randint(0, 7)]
        if(len(_list_) == _size_): break
        elif sym not in _list_: _list_.append(sym)
    return _list_


# to display the set of random symbols
def display_sym(_list_):
    temp = (120 -(len(_list_)*3)) // 2
    print('\n'*9)
    print(' '*temp, end = '')
    for i in _list_:
        print(i, end = '  ')
    print()


# to display the timer
def display_timer(sec):
    for i in range(120):
        print('>', end = '')
        time.sleep(sec)
        sys.stdout.flush()
    time.sleep(1)


# function to display screen set
def screen_top(num):
    os.system('cls')
    print('_'*120)
    print()
    print(('Level '+ str(num)).center(120))
    print('_'*120)


# function to ask for play again
def play_again():
    os.system('cls')
    os.system('color 9f')
    print('\n'*12)
    print('Wanna Play Again: y|n'.center(120))
    inp = msvcrt.getwch()
    if inp.lower() == 'y': main()
    else: sys.exit()


# function to show result
def display_result(status, num):
    if status == 'win':
        os.system('cls')
        os.system('color 2f')
        print('\n'*12)
        print('You Won!! Level Up'.center(120))
        time.sleep(2)
    else:
        os.system('cls')
        os.system('color Cf')
        print('\n'*12)
        print(('You Lose!! Max Level Reached '+str(num)).center(120))
        time.sleep(4)
        play_again()



if __name__ == '__main__':
    main()
    
