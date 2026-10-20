def ft_recursive_count(i: int, n: int) -> None:
    if i == n:
        return print("Harvest time!")
    else:
        print("Day ", i)
        ft_recursive_count(i + 1, n)


def ft_count_harvest_recursive() -> None:
    h_days = int(input("Days until harvest: "))
    ft_recursive_count(1, h_days + 1)

# ft_count_harvest_recursive()
