# erik@interviewqs.com

### Question 1 - Fradulent retail accounts
# store_account table, columns are: store_id, date, status, revenue
# Here's some more information about the table:
# The granularity of the table is store_id and day
# Assume “close” and “fraud” are permanent labels
# Active = daily revenue > 0
# Accounts get labeled by Shopify as fraudulent and they no longer can sell product
# Every day of the table has every store_id that has ever been used by Shopify
# write code using Python (Pandas library) to show what percent of active stores were fraudulent by day.
# Some clarifications:
# We want one value for each day in the month.
# A store can be fraudulent and active on same day. E.g. they could generate revenue until 10AM, then be flagged as fradulent from 10AM onward.
### Answer
Active_stores =  store_account[store_account.revenue>0]
Active_stores['Fraud_Identifier'] = np.where(Active_stores.status=="fraud",1,0)
Active_stores_Fraud = pd.DataFrame(Active_stores.groupby('date').agg({'Fraud_Identifier':['sum','count']})).reset_index()
Active_stores_Fraud['Fraud_Percent'] = Active_stores_Fraud.sum/Active_stores_Fraud.count

### Question 2 - Calculating a moving average using Python. sliding window average.
# You are given a list of numbers J and a single number p. Write a function to return the minimum and maximum averages of the sequences of p numbers in J
### Answer
import numpy as np
J = [4, 4, 4, 9, 10, 11, 12]
p = 3
J = np.sort(J,axis=None)
n = len(J)
min_max_array = []
for i in [0,n-p]:
  min_max = np.mean(J[i:][0:p])
  min_max_array.append(min_max)
min_max_array


### Question 4 - Active users on a messaging application
# The table contains send/receive message data for the application's users, and has the following schema:
# time_stamp(#timestamp, epoch seconds)	
# sender_id(# id of the message sender)	
# receiver_id(# id of the message receiver)
# What fraction of active users communicated with at least 15 unique people on March 1, 2018?
### Answer
# Caller A might call Caller B multiple times. If caller D calls A but not otherwise even then it is considered that A has communicated with B
Message['time_stamp_Date'] = Message.time_stamp.dt.date #convert datetime to date var
sender_to_receiver = Message.rename(columns={"sender_id":"Communication1","receiver_id":"Communication2"})
receiver_to_sender = Message.rename(columns={"receiver_id":"Communication1","sender_id":"Communication2"})
# This is we are counting both ways. If actual in Message are A-B,D-A.
# Communication will produce A-B, D-A, B-A(left to right of A-B is generated), A-D(left to right of D-A is generated)
Communication = pd.concat([sender_to_receiver,receiver_to_sender],axis=1).drop_duplicates()
calculate count distinct per user and extract who has more than 15 unique users

### Question 5 - Employee survey results
# If a question per employee has multiple actions at different timestamps i.e a person will first view, then answer or view and skip
# And a skipped quesion might again appear (does a unanswered question reappear from random sample?)
# Response rate = Number of people who answered / Number of people who got the question
select TOP 1 A.questionID, 
from (select questionID, count(DISTINCT employee_id) as CountEmp
from survey_logging
group by questionID) as A LEFT JOIN
(select questionID, isnull(count(DISTINCT employee_id),0) as CountEmpAnswered
from survey_logging 
group by questionID
HAVING action='answer') as B
ON A.questionID=B.questionID
order by (CountEmpAnswered/CountEmp)

### Question 8 - Checking whether elements in array can be made equal through multiplication
# Given an array arr[], write a function to feed in the array elements check whether they can all be made equal by only multiplying the numbers by 2 or 7. (you can multiply by these #s as many times as you like)
# If all elements can be made equal, return False, otherwise return True.
# Example:arr[ ] = [128, 4, 2]
# 128, 4*2*2*2*2*2 = 128, 2*2*2*2*2*2*2 = 128
# -- True
# arr[ ] = [65, 4, 2]
# -- False
### Answer
Find prime factoriztion of that number and check if the values are only 2 or 7 
https://paulrohan.medium.com/prime-factorization-of-a-number-in-python-and-why-we-check-upto-the-square-root-of-the-number-111de56541f

### Question 9 - Time for a response on a messaging application
# self join such that A.receiver_id=B.sender_id AND B.receiver_id=A.sender_id AND A.timestamp<=B.timestamp
# Extract B.timestamp-A.timestamp to check if it is less than 5 mins

### Question 10 - Calculating student attendance using SQL
select grade_level, sum(PresentStatus)/count(PresentStatus) as OverallAttendanceRate
from (select date, grade_level, (case when attendance_status IN ('present', 'tardy') then 1 else 0 end) as PresentStatus
from student_attendance_log as A LEFT JOIN student_demographic as B ON A.student_id=B.student_id
group by date, grade_level
HAVING date='2018-03-12') as P

### Question 12 - Finding the value closest to 0
# You are given a list of Q 1D points, return the value in Q that is the closest to value j.
# Q = [1, -1, -5, 2, 4, -2, 1] ; j = 3
# We would return two values in this case: 2, 4
import numpy as np
Q = np.sort(Q,axis=None)
Diff_array = []
for i in range(0,len(Q)):
  Diff_array.append(np.absolute(Q[i]-j))
  min_Diff_array = np.min(Diff_array)
  Nearest_to_j = [Q[j] for j in range(0,len(Diff_array)) if Diff_array[j]==min_Diff_array]

### Question 13 - Cleaning and analyzing employee data










