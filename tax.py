def calc_tax(salary, free, rule):
    salary -= free
    tax = 0
    for r in rule:
        if salary > r[0]:
            tax = salary * r[1] - r[2]
            break
    return tax

