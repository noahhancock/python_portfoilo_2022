#Noah Hancock

# import modules
import random
import math
import datetime
# tuples of daily options and matching prices
options = ("Snorkeling","Scuba Diving","Fishing","Sunbathing","Shopping","Helicopter Ride","Sleeping")
prices  = (10.00, 150.00, 25.00, 0.00, 200.00, 450.00, 0.00)

# get and parse vacation starting and ending dates
user_strt_time=input("put the starting date in yyyy-mm-dd: ")
start_time=datetime.datetime.strptime(user_strt_time,"%Y-%m-%d")
user_end_time=input("put the ending date in yyyy-mm-dd: ")
end_time=datetime.datetime.strptime(user_end_time,"%Y-%m-%d")
##print(start_time)
##print(end_time)
# calculate and print the timedelta difference between dates
vaction_length=end_time - start_time
print(str.format("your vaction is {} days long",vaction_length.days))

# initialize empty costs list
costs=[]
for i in range(0,vaction_length.days):
    activity_index= random.randrange(0,len(options))
    activity= options[activity_index]
    cost= prices[activity_index]
    this_date= start_time + datetime.timedelta(days=i)
    this_date_string= datetime.datetime.strftime(this_date,"%Y-%m-%d")
    print(str.format("On {}, {} costs ${:.2f}",this_date_string,activity,cost))
    costs.append(cost)
  

# print most and least expensive days
print(str.format("the most expensive day cost ${}",max(costs)))
print(str.format("the least expensive day cost ${}",min(costs)))

# calculate and print total cost of the trip
total= sum(costs)
print(str.format(" Your total trip cost is ${}",total))

# calculate and print the average cost per day
average= total/vaction_length.days
print(str.format("your average cost per day is ${}",average))



