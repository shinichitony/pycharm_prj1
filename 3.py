# price=8.5
# weight = 7.5
#
# money = weight * price
#
# money = money - 5
# print(money)


# name = "xiaoming"
# age = 11
# print("my namne is %s" % name)
# print(
# "my age is %3d\n my name is %s"
#
#     %
# (age, name)
# )

pay_day=True
salary=100

def pay_the_debit(salary_sub):
    remain = salary_sub - 20
    print(remain)

def main():
    if pay_day:
        pay_the_debit(salary)


main()

