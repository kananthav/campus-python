def main():
    timeInSec = eval(input("Enter time: "))
    hour = int(timeInSec / 3600)
    minute = int((timeInSec / 60) % 60)
    second = timeInSec % 60

    print(timeInSec, "seconds =", hour, "hours", minute, "minutes", second, "seconds")

main()
