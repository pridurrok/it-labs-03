# Минимальная программа для лабораторной по Git.
def main():
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Исходный список:", data)
    print("Сумма элементов:", sum(data))
    print("Максимальный элемент:", max(data))


def helper():
    return "helper from feature branch"


def second_helper():
    return "second helper added on feature branch"


if __name__ == "__main__":
    main()
