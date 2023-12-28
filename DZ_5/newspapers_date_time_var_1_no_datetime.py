# Задание 1
# Печатные газеты использовали свой формат дат для каждого выпуска.
# Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime:
# The Moscow Times - Wednesday, October 2, 2002
# The Guardian - Friday, 11.10.13
# Daily News - Thursday, 18 August 1977
# Пример работы программы
# Программа должна выводить на экран объекты типа datetime, соответствующие датам в условии задачи.


days_of_the_week: dict = {1: "Sunday",
                          2: "Monday",
                          3: "Tuesday",
                          4: "Wednesday",
                          5: "Thursday",
                          6: "Friday",
                          7: "Saturday"
                          }

months_of_the_year: dict = {"01": "January",
                            "02": "February",
                            "03": "March",
                            "04": "April",
                            "05": "May",
                            "06": "June",
                            "07": "July",
                            "08": "August",
                            "09": "September",
                            "10": "October",
                            "11": "November",
                            "12": "December"
                            }

day_month_year = [i for i in input("Input week's day (1-7, 1 - Sunday), month, date, year (example: 1 01 01 2023): ").split()]
print(day_month_year)

# TODO: checking entered parameters

newspaper_num: int = int(input("Input newspaper's number. 1 - The Moscow Times, 2 - The Guardian, 3 - Daily News: "))

print("\nFinal result: ", end="")
match newspaper_num:
    case 1:
        print(f"{days_of_the_week[newspaper_num]}, {months_of_the_year[day_month_year[1]]} {day_month_year[2]}, {day_month_year[3]}")
    case 2:
        print(f"{days_of_the_week[newspaper_num]}, {day_month_year[2]}.{day_month_year[1]}.{day_month_year[3][2:]}")
    case 3:
        print(f"{days_of_the_week[newspaper_num]}, {day_month_year[2]} {months_of_the_year[day_month_year[1]]} {day_month_year[3]}")
    case _:
        print("Unknown newspaper.")
