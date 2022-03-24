def say_the_number(num):
    number = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }

    digit = 1000
    hundred = digit * 1000
    thousand = hundred * 1000
    million = thousand * 1000

    assert(0 <= num)

    if (num < 20):
        return number[num]

    if num < 100:
        if num % 10 == 0: return number[num]
        else: return number[num // 10 * 10] + '-' + number[num % 10]

    if (num < digit):
        if num % 100 == 0: return number[num // 100] + ' hundred'
        else: return number[num // 100] + ' hundred and ' + say_the_number(num % 100)

    if (num < hundred):
        if num % digit == 0: return say_the_number(num // digit) + ' thousand'
        else: return say_the_number(num // digit) + ' thousand, ' + say_the_number(num % digit)

    if (num < thousand):
        if (num % hundred) == 0: return say_the_number(num // hundred) + ' million'
        else: return say_the_number(num // hundred) + ' million, ' + say_the_number(num % hundred)

    if (num < million):
        if (num % thousand) == 0: return say_the_number(num //thousand) + ' billion'
        else: return say_the_number(num // thousand) + ' billion, ' + say_the_number(num % thousand)

    if (num % million == million): return say_the_number(num // million) + ' trillion'
    else: return say_the_number(num // million) + ' trillion, ' + say_the_number(num % million)

    raise AssertionError('num is too large: %s' % str(num))

