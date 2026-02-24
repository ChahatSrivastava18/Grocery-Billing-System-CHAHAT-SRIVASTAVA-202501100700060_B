p1=float(input("Enter 1st price"))
p2=float(input("Enter 2nd price"))
p3=float(input("Enter 3rd price"))
p4=float(input("Enter 4th price"))
p5=float(input("Enter 5th price"))
q1=int(input("Enter 1st quan"))
q2=int(input("Enter 2nd quan"))
q3=int(input("Enter 3rd quan"))
q4=int(input("Enter 4th quan"))
q5=int(input("Enter 5th quan"))
cost=(p1*q1)+(p2*q2)+(p3*q3)+(p4*q4)+(p5*q5)
print("total:",cost)
if cost>100:
    discount=0.1*cost
    final_cost = cost-discount
    print("discount:",discount)
else:
    final_cost=cost
print("final cost:",final_cost)