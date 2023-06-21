# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Unknown = Character("???", color = "#ffffff")
define Stranger1 = Character("Stranger 1", color = "#ffffff")
define Stranger2 = Character("Stranger 2", color = "#ffffff")
define Driver = Character("Driver", color = "#ffffff")
define FemaleReceptionist = Character("Female Receptionist", color = "#ffffff")
define MaleWaiter = Character("Male Waiter", color = "#ffffff")
define FemaleFriend = Character("Female Friend", color = "#ffffff")
define MaleFriend = Character("Male Friend", color = "#ffffff")
define Attacker1 = Character("Attacker 1", color = "#ffffff")
define Attacker2 = Character("Attacker 2", color = "#ffffff")
define Attacker3 = Character("Attacker 3", color = "#ffffff")
define Konrad = Character("Konrad", color = "#08f1f9")
define Johnny = Character("Johnny", color = "#5e0101")
define Tai = Character("Tai Zhou", color = "#93E9BE")


init:
    $ Physical = 0;
    $ Mental = 0;
    $ Emotional = 0;
    $ Knock = False;
    $ NKnock = False;

# The game starts here.

label start:
    #Day1
    "Day 1"
    # Background 
    Unknown "A week’s getaway vacation… finally."
    "A young St. Bernard is on an airplane with a bunch of sleeping passengers. 
    The window cover beside him is open, and he sees a winter wonderland with so many people enjoying themselves."
    "From above, he sees people skiing down from a mountain, starting snowball fights, ice skating on the frozen lake, and more.
    There is even live music that can be heard from a distance a bit as the plane is slowly approaching landing."
    "The plane lands,  and he grabs all his belongings before exiting the plane with the crowd."
    "Now exiting the airport, people who were on the flight are being picked up by friends, family, and significant others."
    "As for himself, he picks up his phone and calls a man named Johnny. 
    The phone rings a bit until the call is picked up."
    Unknown "Hey love! I wanna let you know that I just arrived at the airport! Are you gonna come pick me up?"
    Johnny " {i} In a tired voice {/i} Oh Konrad? Hey babe, what’s up?"
    Konrad "Weren’t you going to pick me up? I told you what day and time I was going to arrive in Kingcardine, Montelasco for the entire week."
    Johnny "You did?..."
    Johnny "You did. I’ll be there in an hour or two."
    Konrad "Wait, what?!"
    "{i} His excited expression shifted to a shocked look. {/i}"
    Konrad "An hour or two? Darling, I have to check into a hotel room in an hour, and the Silver Summit Hotel is thirty minutes from here—"
    "The phone hangs up. Konrad puts away his phone before muttering to himself in disappointment."
    Konrad "He’s always acting like this for the past three months after we’d met in person after two years of a long-distance relationship… Whatever, I’ll just hail a taxi."
    "Coincidentally, a taxi driver is nearby and shows up at the airport just in time."
    # Background 
    "Probably because Kingcardine, Montelasco is a popular winter vacation to come to during the winter season, 
    especially with its main attraction being a beautifully big mountain."
    "Konrad hails a taxi with his arm raised as he yells “Taxi”. He catches the attention of the taxi driver as the driver parks for Konrad to put his luggages in and enter the car."
    Driver "Where to my good sir?"
    Konrad "To the Silver Summit Hotel, please."
    "Surprisingly, the taxi driver took twenty minutes to arrive at the entrance of the Silver Summit Hotel."
    "Konrad enters the building with his belongings."
    # Background 
    "He arrives at the hotel. The hotel looks so cozy and fancy at the same time."
    "Silver Summit Hotel has several leather chairs that look so comfy that you could fall asleep on them and has carpets designed with unique patterns as if it was imported from another country."
    "He even smells food being cooked that feels so sweet and aromatic from a large kitchen."
    "It makes Konrad eager to stay in the motel longer than his vacation as it is."
    "He heads to the front desk and proceeds to check in."
    Konrad "Hello, I would like to check into a room, please."
    FemaleReceptionist "Sure thing! May I have your full name, please?"
    Konrad "Full name is Konrad Ajit. K-O-N-R-A-D A-J-I-T."
    "The receptionist types the name into the system to search for the information. 
    However, the receptionist looks back with an expression of pained news."
    FemaleReceptionist "I’m sorry to inform you sir, but your check-in was yesterday."
    "Konrad’s expression suddenly shifts from a slightly happy to a shocked expression."
    Konrad "Wait, what?!  I remember booking my appointment for today though!"
    FemaleReceptionist "Again, I’m sorry sir. The system notified me that your booking was yesterday and failed to check-in."
    "Konrad takes a deep breath in to calm down before thinking it over and asking."
    Konrad "Okay okay… do you have a room available?"
    FemaleReceptionist "Let me check—"
    "The woman continues typing to see if there were any rooms available at the request of Konrad."
    FemaleReceptionist "—sorry sir, there are no rooms available as every room is booked out, unfortunately."
    "Konrad becomes disappointed after hearing the news."
    Konrad "Thank you for your time…"
    "Konrad left the hotel before pulling out his phone and calling Johnny. 
    /* Background */
    He waits for the call to be picked up. It is answered."
    Konrad "Oh! Johnny, love, I just wanna let you know that I—"
    Johnny " Hey {i}yawns{/i}… what’s up?"
    Konrad "I want to let you know that I am at Silver Summit Hotel, and I don’t have a room. 
    Could I stay at your place for a bit for the vacation?"
    Johnny "Uh yeah yeah, sure babe. {i}Deeply sighs{/i} Want me to pick you up or sum’in?"
    Konrad "Well, yeah. I need to save money doing some stuff on vacation."
    Johnny "{i}Sighs{/i} Okay. Just give me a moment. Hope you don’t mind my boys comin’ with me though."
    Konrad "Ehhh… can it just be us alone? I did come to Kingcardine not just to have a vacation by myself after all. 
    Won’t it be fun to spend time to—"
    "The phone hangs up interruptively once more and making Konrad only to be saddened by today. 
    He finds a nearby bench to sit on before pulling out his phone to surf through."
    "He waits for what feels like minutes and sometimes a few hours just waiting at the bench near Silver Summit Hotel for his boyfriend."
    "Konrad continues scrolling through his phone seeing pictures of couples and attractive men on social media."
    "Konrad sighs before overhearing a conversation between, what seems like, two best friends, or more."
    Stranger1 "We have to be careful when going out at night."
    Stranger2 "Huh? How come? The nighttime is always so quiet to enjoy though."
    Stranger1 "Haven’t you heard the news that has been going on? With how popular tourists are, 
    there have been so many cases of mugging and stealing at weapon point, even kidnapping if they know you are rich! They’re ruthless!"
    Stranger2 "Nah, you’re kidding. Montelasco is like a peaceful place, especially since we’re friendly in Kingcardine."
    Stranger1 "For real, I’m not even kidding! It’s been all over the news for the past days now, especially every winter season on the news near everyday, 
    and especially at the summit where it is most popular for attackers to strike at night where no one can hear you scream!"
    Konrad "{i}Thinking to himself{/i} Wait, that could actually happen…?"
    "Konrad was thinking about it, even might be overthinking himself about that situation. 
    Eventually, he shakes his head and goes back to surfing through his phone to ease his mind."
    "The day becomes early evening, and Konrad is seen napping on the bench."
    Unknown "Yo Konrad!"
    "The mysterious voice called out paired with noises of waves of laughter. 
    Slowly, Konrad wakes up from his nap."
    "His vision was blurry at first before seeing things clearly. 
    It is Johnny and his group of friends laughing in the backseat and passenger."
    Johnny "Hey Konrad."
    Konrad "{i}Yawns{/i} You took awhile…"
    "He checks his phone only to realize what time it is as he had been waiting for what seems to be five to seven hours. 
    Konrad is frustrated that his whole day was just waiting for Johnny."
    Johnny "Yeah, and?"
    "Konrad takes the deepest sigh and not saying anything else."
    Konrad "Ugh… never mind…"
    "He places his belongings in the trunk of Johnny’s car before heading to one of the sides of the car. 
    He sees somebody in the passenger seat already."
    Johnny "Take the backseat."
    "Konrad groans before taking the backseat."
    # Background 
    "When Konrad enters the car, he could smell the car reeking of alcohol and scented vapors, even seeing vapors inside the car still lingering along with empty bottles on the floor; 
    it almost made him retch."
    "As for Johnny’s group, in the backseat, it is majorly awkward since there were two people, a guy and a girl, kissing each other as if they have been doing it for a while. 
    The guy in the passenger seat was reeking of weed and was zoned out."
    "However, Johnny, just looks nonchalant as he starts driving."
    "Besides the noise of kissing, the silence is awkward between Johnny and Konrad. 
    It is so overbearing that Konrad tried to start the conversation."
    Konrad " So… what took you a bit, Johnny?"
    Johnny "Huh? Oh… I was asleep."
    "For him to hear that answer, Konrad’s hands slowly forms a pair of fists with a slightly tight grip."
    Konrad "Oh yeah?"
    Johnny "Yeah, had a major party and stuff and was tired and shi’."
    Konrad "Yeah, yeah… I bet."
    Johnny "Bro, you good?"
    Konrad "Yeah yeah. I’m so fine."
    "Konrad’s voice radiates in annoyance. 
    He keeps looking through the window so as to not show his face to him."
    "The day went from sunset to complete shade of night, and eventually, they arrived. 
    Everybody comes out of the car, and Konrad is standing in front of the apartment complex."
    "Johnny’s friends went to their respective apartment rooms. 
    Konrad follows Johnny to his apartment room and enters inside."
    "Johnny’s apartment is a little bit messy and slightly reeks of vapors and strong alcohol. Empty cups were lying around the counter, table, and floor."
    "Furniture was haphazardly placed around the area as if this place were roughed up, and the room feels so empty yet overwhelming."
    "Konrad feels like this place is poisonous the moment he steps inside, even thinking of sleeping outside like a homeless man."
    Johnny "Let me prep an air bed for ya."
    "Konrad’s expression changes from anger to shock."
    Konrad "Wait, don’t you wanna sleep together, since we are in a relationship after all?"
    Johnny "I guess? Just didn’t clean my room is all."
    Konrad "I can help clean it for you. As I said, I didn’t come to Kingcardine JUST for vacation."
    Konrad "Come on, let me-"
    Johnny "Can you just chill and let me do things?! God, you are so annoying!"
    "Konrad falls into silence when Johnny yelled at him like that."
    Johnny "You are sleeping on an airbed, and I am sleeping in my bed."
    Konrad "Fine…"
    "He places his luggages and bags on the couch before asking."
    Konrad "Where’s your bathroom?"
    "Johnny points to the bathroom that is nearby his bedroom while he is getting the airbed ready."
    "Konrad gets some of his clothes from his luggage and heads to the bathroom to take a shower. 
    He turns on the faucet and proceeds to take a shower with shampoo and body wash. 
    He could not help but feel hurt by Johnny and how he has been acting for the past three months until now."
    "Konrad finishes taking a shower and heads out feeling clean. 
    When he exits the bathroom, he sees Johnny not in the living room with the airbed and assumes he is in his bedroom."
    "It is annoying Konrad to see trash and the smell lingering in the living room. 
    He takes action and starts cleaning with what he could find in the kitchen such as a trash bag and an air freshener."
    "When he finishes, he heads to his airbed to sleep for the night with a pained heart. 
    He could not help but cry himself to sleep silently."
    
    
label Day2:
    #Day2
    "Day 2"
    "Everything is pitch black."
    "Konrad is traveling down a simple dirt road by himself and a flashlight."
    Konrad "Hello?"
    "He calls out, but there was no one to respond."
    "The path begins to warp nonstop as Konrad keeps walking and walking. It is then he realizes that he is walking in circles."
    "The more he walks, his feet start to pick up the pace faster and faster to the point of running."
    "He is panicking, freaking out, and shaky as he keeps running and running until there is a figure ahead…"
    Konrad "Help!"
    "He cries and continues to run with a flashlight, he stops himself only to see what seems to be himself, but mangled, injured, and… crying."
    "Konrad could not help but feel petrified at the sight of what he is seeing."
    "The mirrored self mutters something under his breath."
    Unknown "{i}Mutters mutters mutters… {/i}"
    "Konrad hesitantly say."
    Konrad "H-hello?"
    "Then…"
    Unknown "{b}AAAAAAAAAAAAAAAAAAAH!!!!!{/b}"
    with vpunch
    Konrad "{b}AAAAAAHH!!!{/b}"
    "Immediately, Konrad wakes up from his sleep. He is slightly hyperventilating, sweating, and shaking from the nightmare. 
    Instantly, he pats himself down just to see if he is still there before taking a deep breath in relief."
    "Konrad looks around to see only to see by himself in the apartment and a bright-white sunny morning with snow outside the window."
    "He looks around once more and checks to see if Johnny’s car is still there to confirm, and Johnny is there, but Konrad by himself at home, the sound is empty and isolated."
    Konrad "Great morning so far…"
    "He gets up from the airbed and proceeded his day with a nice hot shower before finding something to eat for breakfast and then trying to enjoy his first day of vacation."
    "After he had showered, he looks through Johnny’s fridge for food to cook… There was nothing but beer and… cheese?"
    Konrad "I’m not eating that…"
    "He closes the fridge."
    Konrad "Aye… Johnny, you seriously changed from the last time we met in person… {i}Sighs{/i}"
    "Konrad decides to go to search on his phone for a nearby place to eat out within walking distance, and he found one!"
    Konrad "So… the place is called ‘Silky Beans’, and it is a restaurant-cafe that serves any time of day, and it is just a seven-minute walk from here! Perfect!"
    "Immediately, Konrad gets dressed in the same outfit he wore yesterday: hoodie, sweater, baggy pants, and a pair of shoes. Before he looks at Johnny’s door as he is thinking…"
    menu:
        "Knock on Johnny’s Door":
            $ Knock == True
            "Konrad thinks about it before sighing a bit. He thinks to himself."
            Konrad "Well, he IS still my boyfriend, so I’ll let him know where I’m at for the most part."
            "He walks up to Johnny’s door and knocks before speaking."
            Konrad "Love, I’ll be out eating at Silk Beans. You’re welcome to join me and stuff. If not, I’ll see you soon."
            "There is no response from Johnny. He must be still sleeping probably."
            "Konrad heads out of the apartment and starts walking to Silky Beans."
            "He heads inside and surprisingly, there is not too many people in the morning. 
            He is in front of the podium and is seated and given the breakfast menu by the waiter."
            MaleWaiter "Good morning, may I get you started to drink something today, sir?"
            Konrad "Hmmmm… I would like to have a nice cup of hot cocoa."
            MaleWaiter "I got it, and do you need a moment to figure out what would you like to order sir?"
            Konrad "Yes, please."
            "The waiter nods before heading to the kitchen to place the order."
            "Konrad goes through the menu as he is debating on which to choose as all of them sound delicious."
            "As he continues to order, the waiter comes to the table with a mug of creamy hot chocolate with whipped cream and dark chocolate shavings on top."
            Konrad "Oh wow!"
            "Konrad’s eyes sparkle with delight to see something look so delicious and pretty at the same time."
            MaleWaiter "Are you ready to order sir?"
            menu:
                "He looks through the menu before ordering…"
                "One Pan Breakfast":
                        Konrad "I’ll order the One Pan Breakfast, please!"
                "Egg Benedicts with Cherry Tomatoes":
                        Konrad "I’ll order Egg Benedicts, please!"
                "Old-fashioned Pancakes":
                        Konrad "I’ll order the Old-fashioned Pancakes, please!"
                "Blueberry French Toast":
                        Konrad "I’ll order the Blueberry French Toast, please!"
                "Belgian Waffles":
                        Konrad "I’ll order the Belgian Waffles, please!"
                "Lumberjack’s Breakfast":
                        Konrad "I’ll order the Lumberjack’s Breakfast, please!"
            MaleWaiter "Coming right up for you sir!"
            "Konrad pulls out his phone as he takes a sip of his hot chocolate. 
            He goes through his photo galleries and starts scrolling."
            "There were photos of families and friends, even instances of him and his boyfriend in a photo, but not a lot."
            Konrad "I wonder what changed you…"
            "Eventually, Konrad’s food arrives at the table. 
            He thanks the waiter before digging into his food, and the moment he bites into his dish, he reminisces about the good time as he eats."
            "The streets of Kingcardine look peaceful with several people roaming around. It just makes him think…"
            Konrad "Man, I would love to live here when I’m done with college, or even find a job here afterwards. 
            Just this place looks so peaceful here than where I live."
            "Several minutes have passed and Konrad finishes his meal quite well as he pays the bill. 
            In the meantime, he continues to have his second mug of hot chocolate while resting his body well."
            "It is a bit sad for him as he reminisces about the good time spent, but he does not know why the feeling feels so nostalgic."
            "Afterwards, he gets up and exits out of Silky Beans."
        "Do not knock on Johnny’s Door":
            $ NKnock == True
            "He thinks to himself before shrugging his shoulders."
            Konrad "I’m still upset at him after what happened last night… I’ll leave him to sort out whatever he’s going. 
            We will talk it out when he and I are calm."
            "Konrad heads out of the apartment and starts walking to Silky Beans."
            "He heads inside and surprisingly, there were not too many people in the morning. 
            He is in front of the podium and is seated and given the breakfast menu by the waiter."
            MaleWaiter "Good morning, may I get you started to drink something today, sir?"
            Konrad "Hmmmm… I would like to have a nice cup of hot cocoa."
            MaleWaiter "I got it, and do you need a moment to figure out what would you like to order sir?"
            Konrad "Yes, please."
            "The waiter nods before heading to the kitchen to place the order."
            "Konrad goes through the menu as he is debating on which to choose as all of them sound delicious."
            "As he continues to order, the waiter comes to the table with a mug of creamy hot chocolate with whipped cream and dark chocolate shavings on top."
            Konrad "Oh wow!"
            "Konrad’s eyes sparkle with delight to see something look so delicious and pretty at the same time."
            MaleWaiter "Are you ready to order sir?"
            "He looks through the menu before ordering…"
            menu:
                "He looks through the menu before ordering…"
                "One Pan Breakfast":
                        Konrad "I’ll order the One Pan Breakfast, please!"
                "Egg Benedicts with Cherry Tomatoes":
                        Konrad "I’ll order Egg Benedicts, please!"
                "Old-fashioned Pancakes":
                        Konrad "I’ll order the Old-fashioned Pancakes, please!"
                "Blueberry French Toast":
                        Konrad "I’ll order the Blueberry French Toast, please!"
                "Belgian Waffles":
                        Konrad "I’ll order the Belgian Waffles, please!"
                "Lumberjack’s Breakfast":
                        Konrad "I’ll order the Lumberjack’s Breakfast, please!"
            MaleWaiter "Coming right up for you sir!"
            "Konrad nods to the waiter before looking out at the window to see plenty of snow covering the streets of Kingcardine."
            "When he is looking outside, he notices a few people walking on the other side of the street. 
            It is a rather peaceful sight for him to see while sipping on hot chocolate."
            "Eventually, Konrad’s food arrives at the table. He thanks the waiter before digging into his food, and the moment he bites into his dish, 
            he starts gorging the food down as it reminded him of a good feeling of home."
            "Several minutes have passed and Konrad finishes his meal quite well as he pays the bill. In the meantime, he continues to have his second mug of hot chocolate while resting his body well."
            "His moment feels peaceful and relaxing. However, he looks out the window and sees a familiar face, and his expression shifts downward."
            "He slightly squints his eyes and sees it is— Johnny, on the other side of the streets."
            "However, what makes it more shocking is that he sees him coddling another yet unfamiliar person with little playful gestures like kisses on the cheeks turning into what seems to be passionate kisses, 
            hands holding, and showing that carefree romance."
            "Konrad is gripping his mug so tightly. He could feel his heart sinking and aching at the sight of his boyfriend with another man."
            "It is a bit sad for him as he reminisces about the good time spent, but he does not know why the feeling feels so nostalgic."
            "He leaves his mug and heads out of the restaurant furiously."
    "After Konrad left Silky Beans, he receives a call. He pulls out his phone and it is from Johnny."
    "He debates in picking up his phone. After a few rings, he takes a deep breath, sighs, and picks it up."
    Konrad "H-hi Johnny."
    Johnny "Yo Konrad wanna hang together today to somewhere, and maybe in the evening, we can go to the ski resort and rent out a lodge together?"
    Konrad "Yeah, sure… Will it just be us this time?"
    Johnny "Nah, I’m still bringing my besties and bros. They’re kinda like brothers and sisters for life, y’know?"
    Konrad "Why can’t it just be us alone together?"
    Johnny "I don’t know, just feels better to be with people familiar, y’know?"
    Konrad "But you didn’t do that last time when we met in person together for the first time, and lately, you just been—"
    Johnny "Look, you killin’ the vibe here, can we just talk about it later?"
    Konrad "I just want to ask what got you acting so differently from the first time we met."
    Johnny "Can you not be annoying for two seconds and like if you wanna come or not?"
    "Konrad’s heart sunk a little deeper into an aching pain. 
    He silences for a moment before responding to the question with restrained anger."
    Konrad "Yeah, fine."
    Johnny "Cool. We’ll meet up in my room, so you can grab your stuff and we can stay at the lodge."
    Konrad "Fine, and could we please talk—"
    "Before Konrad has the chance to say anything more, the phone hangs up once more in a blink of an eye."
    "Konrad puts his phone away and heads back to the apartment once more with his head facing downward and staring at his own shoes."
    "He eventually arrives at the apartment as there was Johnny and his gang."
    Johnny "Welcome back Konrad."
    "Konrad did not say anything as he packs up his belongings in the process while Johnny’s friends keep conversing with one another."
    Johnny "Okay then…?"
    "Eventually, Konrad finishes packing up for the morning."
    Konrad "Finished packing up Johnny."
    Johnny "Great. Let’s get going. We’ll book a lodge at the ski resort, Morning Snow, and from there, we can have some fun!"
    "Johnny’s friends expresses their excitement with him before leaving his apartment room, and eventually Konrad is the last one to exit."
    "They all put their belongings inside of the trunk before hopping into Johnny’s car. 
    However, it is still the same seating from last time where Konrad is seated once more in the backseat.The same friends sit in the passenger seat as well."
    "Konrad looks at Johnny and his nonchalant face and him talking to his passenger friend as if everything is normal, but it just makes him think about what has been going on yesterday and now today."
    "It is mid-afternoon and they arrive at the lodge together as a group. It takes a few minutes to check in and pay for a total of two rooms."
    Johnny "Okay, for the two lovebirds, they get their own room to do whatever they want {i}coughs{/i} wrestling {i}coughs{/i}!"
    FemaleFriend "Oh my god, shut up!~"
    "One of Johnny’s male friends grabs the room cards before playfully grabbing his girlfriend and swinging over his shoulder before running to their room with laughter and squeals."
    Johnny "Lastly, I have three cards for all three of us for the same room, so we’ll be sleeping together."
    MaleFriend "Cool."
    "Konrad stays silent as he follows Johnny and his friend to the room."
    "The lodging room looks fancy with the two beds feeling so comfy like clouds, complimentary treats and drinks lying on the counter, 
    a bathroom fitting for a king, a cozy couch, and a wonderful view from the high height for a room."
    "Konrad sets his belongings against the wall as he sits gently on top of the couch and rests his body."
    Johnny " Alright, and in a few hours or earlier, we’ll be spending time skiing—"
    "However, his plan is interrupted when he could hear his friends' next door being loud and rough."
    Johnny "Okay, seems like just three of us—"
    "Johnny then was interrupted when he hears a snore from his friend sleeping on the bed immediately. He grumbles a bit as he looks at Konrad."
    Konrad "Hmmmmm…"
    Johnny "Seems like you and I will be skiing together."
    Konrad " I guess…"
    "The room suddenly becomes awkward and unbearably uncomfortable."
    "Silence emerges in the room like a poisonous gas as it just slowly angers the two for no reason."
    Johnny "Let’s get ready before going…"
    "Johnny dresses up in their winter clothes for skiing before leaving the room and heading to the nearby ski resort."
    "Johnny pays the entrance fee and rental equipment for both himself and Konrad, put it on, and slowly glides to the lift. 
    As Johnny is about to take the lift by himself, Konrad joins with him on the same lift. The moment that Konrad joined, Johnny groans as if it is agonizing."
    Konrad "Okay, what is your problem?! You been acting like you hate being around me!"
    Johnny " Yeah, and?!"
    Konrad "You starting to act so differently after the first time we’d met! You were romantic and expressive with me the first time, but now, this is different. What hell is wrong with you?!"
    Johnny "What the hell’s wrong with me?! Nah nah nah, I’m hella fine as fuck! What the hell is wrong with you?! I’m tryna to vibe and shit, but you keep ruining shit for me with your needy and paranoid ass!"
    if Knock == True:
        Konrad "How the hell am I paranoid?! I been asking questions nonstop, but no, you just kept calling me ‘annoying’ and get pissed off for me asking what’s wrong!"
        Konrad "Not to mention you’ve been acting so weird with putting me in the backseat and making me sleep on an airbed when we are boyfriends!?"
        Konrad "We been through two years of long distance and met for the first time in the last three months through phone and now this?! {b}THE HELL?!{/b}"
        "Konrad slowly becomes livid."
    if NKnock == True:
        Konrad "Oh?! You’re calling me paranoid?! I have every damn rights to be paranoid especially when I saw you kissing and holding your ‘little boyfriend’ out on the streets when I was getting breakfast at Silky Beans!"
        Konrad "Is being with me that annoying and angering, huh?!"
        Konrad "What gives you the goddamn rights for you to cheat on me when we spent two years long-distance and meeting each other for the first time three months ago…"
        "Konrad begins to tear up."
        Konrad "What made you change that badly?!"
    Johnny "{b}YOU STOPPED MAKING ME FEEL GOOD WHEN I FIRST SAW YOU! WHEN I SAW YOU, IT WAS A LIE ALL THIS TIME!{/b}"
    "The scream echoes through the cold air and the soon-dimming sky, even silencing Konrad."
    Johnny "{b} I CHANGED BECAUSE YOU DON’T HAVE WHAT IT TAKES TO EXCITE ME AGAIN!{/b}"
    Johnny "{b}I CHANGED BECAUSE I DESERVE WAY BETTER THAN YOU!{/b}"
    Johnny "{b}I CHANGED BECAUSE I DON’T LOVE YOU ANYMORE!{/b}"
    Johnny "{b}YOU DONT MAKE ME HAPPY ANYMORE LIKE MY FRIENDS AND NEW BOYFRIEND DOES!{/b}"
    "The sun has set and becomes early nighttime. The resort lightings shines against the falling snow. However, the amount of snow starts to fall more and more."
    "When the lift reaches to the summit, Konrad and Johnny gets off the lift."
    Johnny "Follow me, we got here too late… we’ll just ski down the mountain—"
    Konrad "No."
    Johnny "Konrad, stop being a dumbass for once and listen to me!"
    Konrad "{b}NO! YOU LISTEN HERE! YOU BROKEN MY TRUST YOU—{/b}"
    "Two gunfires is then sounded as it blends in with the harsh winds, especially that no one from below could hear it. 
    It draws the attention Konrad and Johnny’s attention to what seems to be three attackers with guns inside the shadows."
    Attacker1 "Put your hands up where I can see them!"
    "Konrad follows the order. He slowly looks back only to see that Johnny is not there with him anymore."
    "His visions becomes blurry, body becomes petrified, breathing becomes shaky, and everything of his body feels like several needles are sticking his body with this situation."
    Konrad " L-l-look… I-I d-don’t h-have any money, I—"
    Attacker2 "Shut up! We’ll be the judge of that! Search him."
    "The third attacker searches Konrad by patting all over his body for items or belongings."
    Attacker3 "Nothing on him boss!"
    "Konrad begins thinking to himself."
    Konrad "MaybeI’llgetscotchofffreebecauseIdonthaveanythingonme"
    Konrad "ThenthenIcouldbefreegobackhomeorsomething"
    Konrad "PleasepleasepleaseifIcanbefree—"
    Attacker2 "Kill him. His body will be buried by the blizzard. 
    He’ll probably rat on us if he is free, and I ain’t wastin’ my time on a nobody."
    Konrad "Wait—{b}NO, YOU CAN’T{/b}—"
    "Konrad’s face is slammed deep into the snow before the muzzle of the gun presses against the back of his head."
    "Everything feels so slow. He could hear his heart pounding loudly paired the violent winds shredding the night sky."
    "It seems like it is the end of Konrad."
    "Then…"
    "{i}Thump. Thump. Thump.{/i}"
    "{i}Thump... Thump... Thump...{/i}"
    "..."
    "{i}BANG!!!{/i}"
    with vpunch
    "..."
    Attacker1 "{b}SHOOT HIM! ACK!{/b}"
    "Gunfire sounds off repetitiously to the point of making clicking noises along with several snow-sounding steps."
    Attacker3 "{b}WAIT NO, PLEASE NO-{/b}"
    "Then thudding noises becomes present."
    "Konrad is scared, breathing heavy, his heart aching in pain from the adrenaline. 
    Few minutes have passed as he slowly lifts his head from snow to still see himself alive despite his vision being blurry."
    "He tries to calm himself. He slowly turns around only to see all three attackers knocked out. No blood and only bruises. 
    Then he sees one large mysterious figure standing gracefully as his clothes swayed with the winds."
    "After seeing the mysterious figure, presumably who saved him. Konrad’s body is overwhelmed by today’s event that he passed out and everything became pitch black."
    return
