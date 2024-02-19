def chatbot():
    while True:
        user_input=input("\nuser: ")
        if user_input=="hi":
            print("chatbot: hi!  how can I help you?")
        elif user_input=="what is your name":
            print("chatbot: my name is chatbot.")
        elif  user_input=="what is the date today":
            from datetime import date
            date=date.today()
            print("chatbot: today's date is ",date)
        elif user_input=="what is the time now":
            from datetime import datetime
            time=datetime.now()
            current_time=time.strftime("%H:%M:%S")
            print("chatbot: now the time is ",current_time)
        elif user_input=="bye":
            print("chatbot: bye!")
            break
        else:
            print("chatbot: sorry!...I didn't Understand")
chatbot()
