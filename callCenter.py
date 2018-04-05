''' 
Author: Daryll Osis
Date: April 5, 2018
Description: This is a program for a call center. Every time a call comes in you need a way to track that call. 
             One of your program's requirements is to store calls in a queue while callers wait to speak 
             with a call center employee. 
             
             This program lets the user add call, remove call, and display info about the call and the queue.
'''

class Call:
    def __init__(self, ID, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.ID = ID
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    
    def displayCall(self):
        print("ID:", self.ID)
        print("Caller name:", self.caller_name)
        print("Caller phone number:", self.caller_phone_number)
        print("Time of call:", self.time_of_call)
        print("Reason for call:", self.reason_for_call)


class CallCenter:
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    #method to add a call in the queue
    def addCall(self, call):
        self.calls.append(call)
        return self

    #method to remove the first call in the queue
    def removeCall(self):
        self.calls.pop(0)
        return self

    #method to display the information of the calls in the queue, just prints the name and the number
    def displayInfo(self):
        for x in self.calls:
            print (x.caller_name)
            print (x.caller_phone_number)
        print ("There are", len(self.calls), "call(s) in queue")
        return self
    

#adding calls
call1 = Call("1a", "Ninjaguy", "542-222-5152", "1:21pm", "just want to call")
call2 = Call("2a", "Daryll", "719-222-2222", "6:23pm", "emergency")
call3 = Call("5a", "Kobe", "102-232-6646", "9:23pm", "no reason")

callcenter = CallCenter()

#adding calls to the queue and displaying it
callcenter.addCall(call1)
callcenter.addCall(call2)
callcenter.addCall(call3)
callcenter.displayInfo()

#removing a call and then displaying it
callcenter.removeCall()
callcenter.displayInfo()