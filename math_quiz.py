import random
import time
operators=["+","-","*"]
min_operand=2
max_operand=99
total_prb=10
def generate_prb():
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    operator=random.choice(operators)
    exp=str(left)+" "+operator+" "+str(right)
    ans=eval(exp)
    return exp,ans

wrong=0
input("press enter to start")
print("------------------------")
start_time=time.time()
for i in range(total_prb):
    exp,ans=generate_prb()
    while True:
        guess=input("problem"+str(i+1)+":"+exp+"=")
        if guess==str(ans):
            break
        wrong+=1
end_time=time.time()
total_time=round(end_time-start_time,2)
print("-------------------------")
print("Nice work!,you finished in",total_time,"seconds")
