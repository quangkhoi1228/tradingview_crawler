import threading, time

def _sum(n):
    time.sleep(0.2)
    print(f"square: {n*n}")

while 1:

    t = input("Enter the number of times the function should be executed:\n").strip()
    try:
        max_threads = int(t)
        for n in range(0, max_threads):
            threading.Thread(target=_sum, args=[n]).start()
    except:
        pass
        print("Please type only digits (0-9)")
        continue

    print(f"Started {max_threads} threads.")

    # wait threads to finish
    while threading.active_count() > 1:
        time.sleep(0.5)

    t = input("Create another batch (y/n)?\n").lower().strip() #
    if t != "y":
        print("Exiting.")
        break