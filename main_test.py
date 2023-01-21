import main
import io
import sys
import re


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '10\n45\n50\n35\n25'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    regex_string = r'[\w,\W]*10'
    regex_string = r'[\w,\W]*45'
    regex_string = r'[\w,\W]*50'
    regex_string = r'[\w,\W]*35'
    regex_string = r'[\w,\W]*25'
    regex_string += r'[\w,\W]*'
    print(regex_string)
    res = re.search(regex_string, lines[0])
    assert res != None
    print(res.group())
    regex_string = r'[\w,\W]*50'
    regex_string = r'[\w,\W]*10'
    regex_string += r'[\w,\W]*'
    print(regex_string)
    res = re.search(regex_string, lines[1])
    assert res != None
    print(res.group())


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    datastr = '-10\n33\n55\n20\n-5'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    regex_string = r'[\w,\W]*-10'
    regex_string += r'[\w,\W]*33'
    regex_string += r'[\w,\W]*55'
    regex_string += r'[\w,\W]*20'
    regex_string += r'[\w,\W]*-5'
    regex_string += r'[\w,\W]*'
    print(regex_string)
    res = re.search(regex_string, lines[0])
    assert res != None
    print(res.group())
    regex_string = r'[\w,\W]*55'
    regex_string += r'[\w,\W]*-10'
    regex_string += r'[\w,\W]*'
    print(regex_string)
    res = re.search(regex_string, lines[1])
    assert res != None
    print(res.group())
