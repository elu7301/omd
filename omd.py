# Guido van Rossum <guido@python.org>

def step2_umbrella():
    print('Утка-маляр 🦆 решила взять зонтик ☂️, она пристроила его рядом с собой на барной стойке и наслаждалась '
          'своими напитками, не беспокоясь о возможном дожде.')


def step2_no_umbrella():
    print('Утка-маляр 🦆 не взяла зонт ☂️, она просто решила рискнуть и перебежала до бара под проливным дождем,'
          ' сияя яркими перьями под дождевыми каплями.')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
