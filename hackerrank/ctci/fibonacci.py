def fibonacci(num):
    if num<2:
        return num
    if num not in memory.keys():
        memory[num]=fibonacci(num-1)+fibonacci(num-2)
    return memory[num]

num = int(raw_input())
print fibonacci(num)
        
