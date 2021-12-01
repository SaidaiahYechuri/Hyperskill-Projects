msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
ops = ['+', '*', '-', '/']

memory = []


def check_M(num):
    if num == "M" and len(memory) == 0:
        return 0
    elif num == "M" and len(memory) > 0:
        return memory[0]
    else:
        return num


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def calculator(num1, op, num2):
    result = 0
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    return result


def continue_calc():
    while True:
        print(msg_5)
        answer = input()
        if answer == "n":
            exit()
        elif answer == "y":
            main()
            break
        else:
            continue


def store_result(res):
    while True:
        print(msg_4)
        answer = input()
        if answer == "y":
            memory.append(res)
            continue_calc()
        elif answer == "n":
            continue_calc()
        else:
            continue


def is_one_digit(v):
    try:
        v = int(v)
        return -10 < v < 10
    except ValueError:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6

    if v3 == "*" and (float(v1) == 1 or float(v2) == 1):
        msg += msg_7

    if (float(v1) == 0 or float(v2) == 0) and (v3 != "/"):
        msg += msg_8

    if msg:
        msg = msg_9 + msg
        print(msg)


def main():
    while True:
        print(msg_0)
        user_input = input().split()

        x = check_M(user_input[0])
        op = user_input[1]
        y = check_M(user_input[2])
        check(x, y, op)

        if is_float(x) == False or is_float(y) == False:
            print(msg_1)
            continue

        elif op not in ops:
            print(msg_2)
            continue

        elif op == '/' and float(y) == 0:
            print(msg_3)
            continue
        else:
            result = calculator(float(x), op, float(y))
            print(float(result))
            store_result(float(result))
            break


if __name__ == "__main__":
    main()
