print(12%4)
print(-12%4)

current_time =10 # 10:00
hr_later = 8 
time_on_clock = (current_time + hr_later) % 12
print("time on colck after 8 hr's is", time_on_clock)

current_time = 12
hr_later = 9
time_on_clock = (current_time + hr_later)%12
print("time on colck after 9 hr's is",time_on_clock)

number = 5
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    
    
