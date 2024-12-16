import matplotlib.pyplot as plt

#This program is coded by Sapna Patel, CS 111 @UIC in 10/26/2024
#Project 4 -  - Data Analysis : Investigating Bias in Rate.My.Professor Ratings
#This program analyzes professoral ratings for potential gender bias by categorizing reviews based on the inputted word.

#Milestone1: Load in and understand the data
file_name = input("Enter the filename:")
big_file = open(file_name) #open the file user wants
data = big_file.readlines() #reads all lines in the file picked

#initalize empty lists that will have data stored throughout the process
gender = []
comments = []
ratings = []

#Milestone2: Process and clean the data to extract gender, comments, and ratings
for each_line in data:
    columns = each_line.split(",") #split each line by commas
    gender.append(columns[24]) #append gender data from column 24
    comments.append(columns[22]) #append comment data from column 22
    ratings.append(columns[6]) #append rating data from column 6
big_file.close()

#Milestone3: Continue processing data and setup user input validation as well as word analysis
loop = True
while loop: 
    word = input('Enter a word or "exit": ')

    #if user enters "exit", exit the program
    if word == "exit":
        print("Goodbye.")
        loop = False

    #if user enters eligible word, analyze the data
    if word != "exit":
        #initialize all these counters (g = good, b = bad, m = medium)
        gwomen = 0
        bwomen = 0
        mwomen = 0
        gmen = 0
        bmen = 0
        mmen = 0
        total_women = 0
        total_men = 0
        made_comment = 0

        #will loop through each comment to check for that inputted word and increment count if neccesary
        for i in range(len(comments)):
            if word in comments[i]:
                made_comment = made_comment + 1

                #classify ratings based on professor's gender
                if gender[i] == "male":
                    if float(ratings[i]) < 2.5 and float(ratings[i]) > 0:
                        bmen = bmen + 1
                    elif float(ratings[i]) > 3.5 and float(ratings[i]) < 5:
                        gmen = gmen +1
                    elif float(ratings[i]) >= 2.5 and float(ratings[i]) <= 3.5: 
                        mmen = mmen + 1
                if gender[i] == "female":
                    if float(ratings[i]) < 2.5 and float(ratings[i]) > 0:
                        bwomen = bwomen + 1
                    elif float(ratings[i]) > 3.5 and float(ratings[i]) < 5:
                        gwomen = gwomen +1
                    elif float(ratings[i]) >= 2.5 and float(ratings[i]) <= 3.5: 
                        mwomen = mwomen + 1

        total_women = bwomen + gwomen + mwomen
        total_men = bmen + gmen + mmen

#Milestone 4: Print the results in a formatted table
        print("------------------------------------------------------------")
        print(f"Here are the ratings for the word {word}")
        print(f"There were {total_women + total_men} total review(s) containing the word {word}.\n")
        print("       |Total     |Good          |Medium       |Bad ")
        print(f"Male   |{total_men:<10}|{gmen:<14}|{mmen:<13}|{bmen:<10}")
        print(f"Female |{total_women:<10}|{gwomen:<14}|{mwomen:<13}|{bwomen:<10}")
        print("------------------------------------------------------------")

#Milestone5: Plot the results
        categories = ["good", "medium", "bad"] #list to display the three options in ratings
        male_plot = [gmen, mmen, bmen] #list to display the male rating counts 
        women_plot = [gwomen, mwomen, bwomen] #list to display the female rating counts
        print(male_plot)
        print(women_plot)

        #max will define plot scales
        max_male = max(male_plot)
        max_women = max(women_plot)
        total_max = max(max_male,max_women)

        plt.subplot(121)
        plt.bar(categories, male_plot, color='orange')
        plt.title(f'Male "{word}"')
        plt.ylim(0, 50 + total_max)

        plt.subplot(122)
        plt.bar(categories, women_plot, color='blue')
        plt.title(f'Female "{word}"')
        plt.ylim(0, 50 + total_max)

        plt.savefig("plot_" + word + ".png")