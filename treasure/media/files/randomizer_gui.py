import tkinter as tk
import tkinter.font as tkFont
import random
import threading
  
    
##Title window
window = tk.Tk()
window.configure(bg="gold")
window.title("Randomizer")

menu_frame = tk.Frame(window)
window.rowconfigure(0, minsize=50, weight=1)
window.rowconfigure(1, minsize=50, weight=1)
window.rowconfigure(2, minsize=50, weight=1)


    
def create_number_window():
    " new window"
    try:
        if number_window.state() == "normal": number_window.focus()
    except NameError as e:
        print(e)
        number_window = tk.Toplevel()
        number_window.geometry("500x310+500+200")
        nw = tk.Label(number_window, text="Time to randomize numbers",
                      font=title_font)
        nw.pack()

    def repeated_effect():
        if repeated_button["relief"] == tk.RAISED:
            repeated_button.config(relief=tk.SUNKEN)
        else:
            repeated_button.config(relief=tk.RAISED)

    def randomize_numbers():
        start = int(range_start.get())
        end = int(range_end.get())
        total = how_entry.get()
        generated_numbers = set()
        produce = True
        if repeated_button["relief"] == tk.SUNKEN:
            while produce:
                number = random.randint(start, end)
                print(number)
                if len(generated_numbers) == int(total):
                    produce = False
                else:
                    if number not in generated_numbers:
                        generated_numbers.add(number)
                        



        else:
            for _ in range(int(total)):
                number = random.randint(start, end+1)
                generated_numbers.add(number)


        numbers = ""
        count = 0
        for result in generated_numbers:
            numbers = numbers + str(result) + ", "
            count += 1
            if count%10 == 0:
                numbers += '\n'
        print(results_label.winfo_width)
        print(number_window.winfo_screenwidth)
        print(number_window.winfo_reqwidth())
        print(results_label.winfo_reqwidth())
        results_label["text"] = numbers[:-2]

   
        
    
                
    ##Range line
    range_frame = tk.Frame(number_window)
    range_label = tk.Label(range_frame, text="Range?")
    separator_label = tk.Label(range_frame, text="-")
    range_start = tk.Entry(range_frame, width=10)
    range_end = tk.Entry(range_frame, width=10)

    ##How many line
    how_frame = tk.Frame(number_window)
    how_label = tk.Label(how_frame, text="How many?(No more than 100, please)")
    how_entry = tk.Entry(how_frame, width=10)

    ##Create Button
    repeated_frame = tk.Frame(number_window)
    repeated_button = tk.Button(repeated_frame, text="Repeated?",
                                relief=tk.RAISED, command=repeated_effect)
    button_frame = tk.Frame(number_window)
    create_button = tk.Button(button_frame, text="RANDOMIZE!!!!",
                              activebackground="green yellow",
                              activeforeground="lime green",
                              command=randomize_numbers)

    ##Results
    results_frame = tk.Frame(number_window)
    results_label = tk.Label(results_frame, text="What numbers?")
    


    ##Pack range line
    range_frame.pack()
    range_label.pack(side=tk.LEFT)
    range_start.pack(side=tk.LEFT)
    separator_label.pack(side=tk.LEFT)
    range_end.pack(side=tk.LEFT)

    ##Pack how many line
    how_frame.pack()
    how_label.pack(side=tk.LEFT)
    how_entry.pack(side=tk.LEFT)

    ##Pack randomize button
    repeated_frame.pack()
    repeated_button.pack()
    button_frame.pack()
    create_button.pack(side=tk.LEFT)

    ##Pack results
    results_frame.pack()
    results_label.pack(side=tk.LEFT)
 

    



    
        
    
    

    
def create_things_window():
    " new window"
    try:
        if things.state() == "normal": things.focus()
    except NameError as e:
        print(e)
        things_window = tk.Toplevel()
        things_window.geometry("500x310+500+200")
        tw = tk.Label(things_window, text="Time to randomize things",
                    font=title_font)
        tw.pack()

    things = list()
        
    


    ##Things frames
    top_frame = tk.Frame(things_window, height=10)
    things_frame = tk.Frame(top_frame)
    things_entries = tk.Frame(top_frame)
    amount_frame = tk.Frame(things_window)
    tresults_frame = tk.Frame(things_window, height=10)
    randbutton_frame = tk.Frame(things_window)

    def create_new_entry():
        new_entry = tk.Entry(things_entries, width=30)
        things.append(new_entry)
        new_entry.pack(side=tk.TOP, pady = 5)
        


    def randomize_things():
        print(12521126)
        things.append(things_entry)
        total = int(amount_entry.get())
        generated_items = set()
        while len(generated_items) != total:
            number = random.randint(0, len(things)-1)
            randthing = str(things[number].get())
            if randthing not in generated_items:
                generated_items.add(randthing)

        answer = ""
        for result in generated_items:
            answer = answer + str(result) + ", "
        tresults_label["text"] = answer[:-2]
            
        
        

    
    ##Things Widgets
    things_label = tk.Label(things_frame, text="What things?")
    things_entry = tk.Entry(things_entries, width = 30)
    add_button = tk.Button(things_entries, text="+", width=3, height=1,
                           command=create_new_entry)
    amount_label = tk.Label(amount_frame, text="How many?")
    amount_entry = tk.Entry(amount_frame, width=30)
    
    tresults_label = tk.Label(tresults_frame, text="")
    
    create_button = tk.Button(randbutton_frame, text="RANDOMIZE!",
                              command=randomize_things)
    
    
    
    
    

    ##Things pack
    top_frame.pack()
    things_frame.pack(side=tk.LEFT)
    things_entries.pack(side=tk.LEFT)
    amount_frame.pack()
    tresults_frame.pack()
    randbutton_frame.pack()
    
    things_label.pack(side=tk.TOP, padx = 20)
    things_entry.pack(side=tk.TOP, pady = 5)
    add_button.pack(side=tk.BOTTOM)
    amount_label.pack(side=tk.LEFT, padx = 20)
    amount_entry.pack(side=tk.LEFT)
    create_button.pack(side=tk.LEFT)
    tresults_label.pack(side=tk.LEFT)


    ##MAIN WINDOW
    

title_font = tkFont.Font(family="Lucida Grande", size=18)


title = tk.Label(window, text="Welcome to Randomize Numbers!",
                 font=title_font, bg="gold")

number_button = tk.Button(window, text="Randomize Numbers", command=create_number_window,
                        height=5)
other_button = tk.Button(window, text="Randomize Others", command=create_things_window,
                         height=5)


##Grid of title window
title.grid(row=0, column=0, sticky="ew")
number_button.grid(row=1, column=0, sticky="ew")
other_button.grid(row=2, column=0, sticky="ew")




window.mainloop()

