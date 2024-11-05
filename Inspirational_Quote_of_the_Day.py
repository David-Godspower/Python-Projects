print ("A Program for Inspirational Quotes\n")
import random
# Declaring the quote of the day 
quote_of_the_day = ["The best way to predict the future is to invent it. - Alan Kay",
          "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
          "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
          "Keep  the faith. Allow Christ full reign in your life. — Lailah Gifty Akita",
         "  It’s only the ego that wants to surrender the ego; the real meaning of surrender does not involve anything external. It means to surrender to your true nature. — Enza Vita",
         "Happiness  is a sacred bliss. — Lailah Gifty Akita",
         "Most  often people seek in life occasions for persisting in their opinions rather than for educating themselves.— André Gide",
          "Wise  words are like seeds. The more you scatter them, the more they will grow into infinite gardens of knowledge. — Suzy Kassem",
            "You  get peace of mind not by thinking about it or imagining it, but by quietening and relaxing the restless mind — Remez Sasson",
            "If  you don't like what someone has to say, argue with them. — Noam Chomsky",
 ]
 # Randomly select 
selected_quote_of_the_day = random.choice(quote_of_the_day )
# Display the output 
print("Quote of the day:\n" + selected_quote_of_the_day     )
#Declaring the categories 
# Technology 
technology = ["Technology is a gift of God. After the gift of life, it is perhaps the greatest of God's gifts. It is the mother of civilizations, of arts and of sciences. — Freeman Dyson",

"The best way to predict the future is to invent it. — Alan Kay",

 "Technology is unlocking the innate compassion we have for our fellow human beings. — Bill Gates",

"The most important thing about technology is how it changes people. — Jaron Lanier" ,

"Technology, through automation and artificial intelligence, is definitely one of the most disruptive sources. — Alain Dehaze" ,

"With the new day comes new strength and new thoughts. — Eleanor Roosevelt " ,

"We are changing the world with technology. — Bill Gates" ,

"Technology is a tool for solving human problems. — Phil Libin" ,

"There's a way to do it better—find it. — Thomas Edison" ,

 "Innovation is the unrelenting drive to break the status quo and develop anew where few have dared to go. — Steven Jeffes" ,
]
# Arts
arts = ["Every artist was first an amateur.  — Ralph Waldo Emerson",

"Art is the only way to run away without leaving home. — Twyla Tharp" ,

"You can’t use up creativity. The more you use, the more you have. — Maya Angelou" ,

"Creativity is intelligence having fun. — Albert Einstein" ,

"Art is the most intense mode of individualism that the world has known. — Oscar Wilde" ,

"Art washes away from the soul the dust of everyday life. — Pablo Picasso",

"Life beats down and crushes the soul, and art reminds you that you have one. — Stella Adler" ,

"Art is the lie that enables us to realize the truth.  — Pablo Picasso",

"Great things are not done by impulse, but by a series of small things brought together. — Vincent Van Gogh" ,

"The purpose of art is not a rarified, intellectual distillate—it is life, intensified, brilliant life. — Alain Arias-Misson",
]
# Self Improvement 
self_improvement = ["Do not wait to strike till the iron is hot; but make it hot by striking. — William Butler Yeats",

 "The only limit to our realization of tomorrow is our doubts of today. — Franklin D. Roosevelt",
 
 "Life isn’t about finding yourself. Life is about creating yourself. — George Bernard Shaw",
 
 "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. — Albert Schweitzer",

"Growth is the great separator between those who succeed and those who do not.— John C. Maxwell",

"The only way to do great work is to love what you do.— Steve Jobs",

 "What you do today can improve all your tomorrows. — Ralph Marston",
 
"Personal growth is not a matter of learning new information but unlearning old limits. — Alan Cohen",

"Small daily improvements over time lead to stunning results. — Robin Sharma",

 "The journey of a thousand miles begins with one step.— Lao Tzu",
]
# Randomly select one from each category 
selected_technology = random.choice(technology)
selected_arts = random.choice(arts)
selected_self_improvement = random.choice(self_improvement)
# loop to allow user to select their interest 
while True:
# Accept user input 
    userinput = input("""\nChoose  your area of interest
1) Technology
2) Arts
3)Self Improvement
4)Exit
\t""" )
# conditions to determine user input on

    if userinput == '1':
        print("You chose 'Technology'\t ")
        userinput = input("Press 'Enter' to see the quote    \n")
        # Display quote based on Technology 
        print(selected_technology)
    elif userinput == '2':
        print("You chose 'Arts' \t")
        userinput = input("Press 'Enter' to see the quote    \n")
        # Display quote based on arts
        print(selected_arts)
    elif userinput == '3':
        print("You chose 'Self Improvement' \t")
        userinput = input("Press 'Enter' to see the quote    \n")
        # Display quote based on self Improvement 
        print(selected_self_improvement)
    elif userinput == '4':
      print("Thanks")
      break # Exit the loop
      #  condition to check if user didn't follow the instruction 
    else:
        print("Follow the instruction above. ")
    