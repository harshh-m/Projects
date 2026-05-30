import time

print("=== Stopwatch ===")

input("Press Enter to START the stopwatch...")

start_time = time.time()

input("Press Enter to STOP the stopwatch...")

end_time = time.time()

elapsed_time = end_time - start_time

print(f"\nElapsed Time: {round(elapsed_time, 2)} seconds")
