# rama_height=1.3
# raja_height=1.7
# if rama_height>raja_height:
#     print("rama is taller")
# else:
#     print("raja is taller")


# cpu_hours=int(input("enter a cpu hours: "))
# storage=int(input("enter storage in gb: "))
# data_taransfer=int(input("enter a data_transfer in gb: "))
# cpu_cost=cpu_hours*5
# storage_cost=storage*2
# data_taransfer=data_taransfer*1
# total_amount=cpu_cost+storage_cost+data_taransfer
# if cpu_hours >100:
#     print(total_amount+500)
# else:
#     print(total_amount)


uptime = float(input("enter a uptome:"))
bill=int(input("enter a bill: "))
if uptime>=99.9:
    refund=0
elif uptime>=98:
    refund=bill*0.10
else:
    refund=bill*0.25
print("refund amount:",refund)