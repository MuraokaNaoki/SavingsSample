import math
import numpy as np
import matplotlib.pyplot as plt

year_object = int(input("１年の目標貯金額を入力してください:"))
month_object = float(year_object) / 12
month_object = math.ceil(month_object)
month_object = round(month_object, -3)
print("1ヶ月の目標貯金額は",month_object,"円です")

months = [1,2,3,4,5,6,7,8,9,10,11,12]
days = list(range(1,4,1))


def saving_money():
    for month in months:
        month_income = int(input("今月の収入を教えてください:"))
        useable_money_month = month_income - month_object
        print("今月使えるお金は",useable_money_month,"円です")
        useable_money_day = int(useable_money_month)/31
        useable_money_day = math.ceil(useable_money_day)
        useable_money_day = round(useable_money_day, -2)
        print("1日に使えるお金は",useable_money_day,"円です")

        monthly_report = []
        monthly_report_income = []

        for day in range(3):

            day = int(input("今日の支出を教えてください:"))
            day_income = int(input("今日の臨時収入を教えてください:"))
            income_expenditure = int(day_income - day)
            saving_amount = int(useable_money_day + income_expenditure)
            final_money_day = saving_amount +useable_money_day

            if saving_amount > 0:
                print("よくできました！明日は",useable_money_day,"円まで使えます！使いすぎには注意しましょう！")

            else:
                print("注意！1日の利用可能料金を超過しています！明日の支出は",final_money_day,"円までに留めましょう！")

            monthly_report.append(day)
            monthly_report_income.append(day_income)
            spend_amount = np.sum(monthly_report)
            income_amount = np.sum(monthly_report_income)
            saving_amount_month = month_income + income_amount - spend_amount

            print(month,"月の今日までの支出は",spend_amount,"円です\n")


        print(month,"月の支出額は",spend_amount,"円でした！")

        print(month,"月の貯金額は",saving_amount_month,"円でした！")
        saving_defference = month_object - saving_amount_month
        object_judge = spend_amount - useable_money_month
        next_month = int(month) + 1

        if saving_defference >= 0:
            print("目標の貯金額",month_object,"円まで",saving_defference,"円足りていません。来月はもっと節約できるように頑張りましょう。\n")

        else:
            saving_defference = np.abs(saving_defference)
            print("目標の貯金額",month_object,"円を",saving_defference,"円上回りました！目標達成です！引き続き節約頑張りましょう！\n")
