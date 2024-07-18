import time, readline, os, pathlib, csv
from datetime import date

def timer(subject):
    start_time = time.time()
    print("press enter to end timer")
    input(f"timer running for '{subject}'...")
    end_time = time.time()
    total_time = int(end_time - start_time)
    return total_time
    
def export(subject, total_time_in_seconds):
    with open("today.txt", "a") as file:
        file.write(f"{subject},{total_time_in_seconds}\n")
        file.close()
    print("session succesfully recorded")
    
def endday():
    pathlib.Path('./journal').mkdir(parents=True, exist_ok=True) 
    pathlib.Path('./csv').mkdir(parents=True, exist_ok=True) 

    data = {}
    with open("today.txt", "r") as file:
        for line in file:
            # Split the line into key and value
            key, value = line.split(',')
            # Convert the value to an integer
            value = int(value)
            # If the key is already in the dictionary, add the value to the existing value
            if key in data:
                data[key] += value
            # Otherwise, add the key and value to the dictionary
            else:
                data[key] = value
        file.close()
    # Delete contents of file
    open("today.txt", "w").close()
    
    writeToJournal(data)
    writeToCSV(data)
    
def writeToCSV(data):
    with open(f"./csv/{date.today()}.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        for key, value in data.items():
            writer.writerow([key,value])
        
 
def writeToJournal(data):
    with open(f"./journal/{date.today()}.md", "w") as file:
        file.write(f"# {date.today()}\n\n")
        file.write(f"## Stats\n")
        for key in data:
            minutes = (data[key] % 3600) // 60
            hours = data[key] // 3600
            file.write(f"> {key}: {hours}h {minutes}m\n")
        file.write("------------------------------- \n")
        
        print("What did you do today? (type '!q' on a new line to finish):")
        lines = []
        while True:
            line = input()
            if line == '!q':
                break
            lines.append(line)

        # Join the lines into a single string
        text = '\n'.join(lines)
        file.write(text)
        print("day succesfully ended!")
        

def menu():
    commands = ["help", "start", "endday", "done"]
    print("""┌────────────────────────────────────────────────────────────────────────────┐
│                                                                            │
│                                                                            │
│   _______ __                  _______              __                      │
│  |_     _|__|.--------.-----.|   |   |.-----.----.|__|.-----.-----.-----.  │
│    |   | |  ||        |  -__||       ||  _  |   _||  ||-- __|  _  |     |  │
│    |___| |__||__|__|__|_____||___|___||_____|__|  |__||_____|_____|__|__|  │
│                                                                            │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘""")
    print(f"Type '{commands[0]}' for a list of commands")
    while (True):
        user_input = input("> ")
        
        if (user_input == commands[0] or user_input == commands[0][0]):
            print("------------------------------------------------")
            print("All commands can be shortened to just the starting character. Ex: h == help \n")
            print(f"{commands[1]} - starts the timer. takes an additional string input, subject. ex: start programming \n ")
            print(f"{commands[2]} - ends the current day. a CLI will be shown to write down what you've accomplished. all time data done so far will then be exported as a .csv file which you can find in the project's directory. \n")
            print(f"{commands[3]} - exits the program. data will still be saved. \n")
            print("------------------------------------------------")
        elif (commands[1] == user_input.split(" ")[0] or commands[1][0] == user_input.split(" ")[0]):
            try:
                subject = ' '.join(user_input.split(" ")[1:]).rstrip()
                if (subject == "" or subject == " "):
                    raise SyntaxError              
            except SyntaxError:
                print("provide a subject. ex: start programming")
            finally:
                total_time = timer(subject)  
                # less than 60 seconds
                if (total_time < 60):
                    minutes = 0
                    seconds = total_time
                else:
                    minutes = total_time // 60
                    seconds = total_time - minutes*60 
                
                export(subject, total_time)

                print("------------------------------------------------")
                print(f"you've spent {minutes} mins and {seconds} seconds working on '{subject}'")
                print("------------------------------------------------")
                
        elif (user_input == commands[2] or user_input == commands[2][0]):
            confirmation = input("Are you sure you want to end the day? (Only do this at the end of the day) Y/N: ").lower()
            if (confirmation == 'y'):
                endday()
        elif (user_input == commands[3] or user_input == commands[3][0]):
            break
        else:
            print("invalid command")

os.system('cls' if os.name == 'nt' else 'clear')
menu()