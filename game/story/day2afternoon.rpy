# # Background
# cabin_inside_day

# # Characters
# k = Konrad (neutral, smiling)
# t = Tai Zhou (neutral, smiling, impressed)

label cabinAfternoon2:

    scene bg cabin_inside_day
    
    "I lay back in my chair, sipping on a cup of hot cocoa while my laptop sat in front of me, whirring away noisily as it blew hot air into the cold atmosphere. Thankfully, there was still power up here in this cabin."
    
    k smiling "Ahh…"

    "Bedroom music production on a lazy saturday. This was the life I was more used to. I wish I had my full music production setup back at home, but this was nice too."
    
    "The cozy atmosphere of the cabin envelops me as I immerse myself, lost in a world of melodies and beats."

    k neutral "Hmm, maybe I should add a bit more reverb to this section."

    "Just as I’m fine-tuning the mix, I hear a knock on the door. Startled, I turn my attention towards it."

    k neutral "Who could it be?"

    "Well, who else? I make my way to the door and open it, revealing Tai Zhou standing there, curiosity in his eyes."

    k smiling "Tai Zhou! What’s up?"

    t neutral "I heard some strange noises coming from the room. May I come in?"

    k neutral "Of course, come on in. I’m just working on some music."

    "Tai Zhou enters the room and looks around, taking in the sight of my laptop."

    t neutral "What’s this?"

    k neutral "I’m just working on some music. It’s one of my favourite hobbies."

    t neutral "Oh. Looks fascinating."

    "The snow leopard looks over at the screen, A program was open with various knobs, bars and other strange controls. This must’ve seemed alien to him."

    k neutral "Have you used a computer before?"

    t neutral "No. I’ve seen other people use them sometimes when I’m in the city."

    k neutral "Really? I think I’d be bored to death without electronics."

    t neutral "Well, I never saw the need. I grew up without any gadgets while I was in my village. I prefer just doing things the old way."

    k smiling "I understand. Simple life, happy life, right?"

    t neutral "Yes!"

    "Nevertheless, he still seemed interested in what I was doing."

    t impressed "I had no idea you were into music. Is there something you’re working on right now?"

    k smiling "Actually, yes! I’m working on a new track. Would you like to listen?"

    t neutral "Well sure, why not."

    "I hand him my pair of earphones. He seemed a little confused at first, but it didn’t take him long to figure out."

    k smiling "I call this…"

    menu:
        "Captivated by You":
            $ add_emotional_score(1)

            "A sweet, romantic melody starts playing in Tai Zhou’s ears. The delicate harmonies and gentle rhythm evoke a sense of longing and tenderness."

            t neutral "This is nice. Reminds me of the songs we used to sing in our own country."

            k smiling "Aww, thanks! I wanted to create something that captures the essence of being deeply in love. Music has a way of expressing emotions that words alone sometimes cannot."

            t smiling "I see. Is that you singing?"

            k smiling "Well, yes! I recorded it at home."

            k neutral "I hope you like it…"

            t smiling "Your voice is really good."

            "I hide a blush."

        "Concerto of Celestial Colors":
            $ add_intellectual_score(1)

            "A complex orchestral arrangement starts playing in Tai Zhou’s ears. The grandeur of the orchestral sound, the interplay of different instruments, and the ever-changing dynamics create a vivid musical tapestry."

            k neutral "I wanted to experiment with a more elaborate orchestral piece. Each instrument plays a role in painting a vivid sonic landscape, where listeners can imagine themselves amidst a celestial symphony."

            t neutral "I see."
            
            t smiling "You’re very good at this."

            k neutral "Thanks! It took years of self-study and practice."

        "The Rebel’s Anthem":
            "A loud rock song starts playing in Tai Zhou’s ears. The raw energy, pounding drums, and powerful guitar riffs make my heart race. It’s a rebellious anthem that ignites a fire within."

            k smiling "This song is my way of expressing a rebellious spirit and letting loose. It’s cathartic, in a way. Sometimes, you just need a burst of energy and attitude."

            t neutral "…"

            "Tai Zhou looks a little shocked, but he tries to hide it."

            k neutral "Well it’s okay. My music isn’t really for everyone."

            t neutral "No no, it’s really good. I like it. I feel energized already."

    "The unfinished track abruptly cuts to a halt. I hit pause, and Tai Zhou gives me a nod of gratitude as he returns my earphones."

    k neutral "Do you play any instruments?"

    t neutral "Not really, I’ve never had the opportunity."

    k neutral "Aww, that’s a shame. Not even in school?"

    t neutral "Well… I never really went to school."

    k neutral "Really?"

    t neutral "I know, but growing up, my family faced financial difficulties, and we couldn’t afford education. I had to support my parents and siblings, so I started work helping the family business right out of primary school."

    menu:
        "But you have other skills!":
            $ add_intellectual_score(1)

            k neutral "Aww, I understand. Sometimes circumstances make it challenging to pursue certain paths."
        
            k smiling "But education comes in various forms. You have valuable skills and knowledge that can’t be taught in a classroom."

            t neutral "What do you mean?"

            k smiling "Well, you have practical skills like gardening, cooking, and building things. Those are talents that not everyone possesses."

            t smiling "I never really thought about it that way."

        "I’m sure they’ll be proud of you.":
            $ add_emotional_score(1)
            k neutral "It’s okay, I’m sure you did the right thing. Your family will be proud of you, won’t they?"

            t smiling "Thanks. And yeah, they are."

            k smiling "Well, you seem to be doing very well for yourself. I’m sure I’d probably struggle if I was in your position, living in a cabin in the mountains."

            t smiling "Perhaps."
        
        "Why not I teach you?":
            k neutral "Why not I teach you?"

            t neutral "Teach? Teach what?"
            
            k neutral "Er… I don’t know."

            "The idea seemed stupid now that I said it out loud. I certainly couldn’t cover fifteen years of schooling in an afternoon."

            t smiling "It’s okay. I think I’m doing quite well for myself."

            k smiling "Yeah!"

    "The two of us sit in the cabin, the warmth of the fire embracing us as we continue our conversation, discussing our past. I share a bit about my work, my hobbies and life in my home country, while Tai Zhou tells me about his life growing up and his struggles."

    k smiling "Thanks for sharing with me, Tai Zhou. I feel like I understand you a lot better now."

    t smiling "No problem. Same to you. Enjoy your time here, I need to go prepare dinner."

    "With that, Tai Zhou leaves the room, allowing me to carry on with my work."

    jump cabinNight2