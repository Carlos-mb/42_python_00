def ft_count_harvest_recursive(total: int = None, cont: int = None) -> None:
    if cont is None:
        ft_count_harvest_recursive(int(input("Days until harvest: ")), 1)
        return
    else:
        print(f"Day {cont}")
        if total != cont:
            ft_count_harvest_recursive(total, cont + 1)
        else:
            print("Harvest time!")
