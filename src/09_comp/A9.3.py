import matplotlib
matplotlib.use("TkAgg")   # oder "QtAgg", je nach installiertem Backend
import matplotlib.pyplot as plt

def revenue_chart(days, revenues):
    fig, ax = plt.subplots()
    ax.bar(days, revenues)
    ax.set_xlabel("Wochentag")
    ax.set_ylabel("Umsatz in Euro")
    ax.set_title("Tagesumsatz")
    plt.show()

days = ["Mo", "Di", "Mi"]
rev = [120, 98, 143]

revenue_chart(days, rev)