# # Background
# black
# cabin_outside_day
# cabin_inside_day

# # Characters
# k = Konrad (tired)
# t = Tai Zhou (neutral, concerned, smiling)

label cabinAfternoon:

    scene bg black

    show bg cabin_inside_day
    
    "The storm continued to rage outside, and I continued to lay in the bed that Tai Zhou had graciously provided. He mentioned he was busy with work, leaving me alone in the room."

    "The cabin lacked a TV, computer, or any form of recreational electronics for that matter so there wasn't much to do inside besides read a book or use my phone. And before I knew it, it was already mid afternoon."

    "Feeling rather lazy, I decided to go stretch my legs."

    "I walk back into the living room, seeing Tai Zhou standing with his feet apart on a thin, spongy mat. He wore a thin shirt that fit his muscular frame tightly, exposing his thick biceps."

    "I watched as he pointed his muzzle straight ahead and his arms moved in a slow, but controlled manner. I cough softly so as not to startle him."

    k neutral "What are you doing?"

    t neutral "Tai chi."

    k neutral "Well, I hope you don't mind if I watch." 
    
    "I took a seat on the nearby sofa. He ignores me and carries on with his routine."

    "Tai Zhou carries on his routine for a bit, before turning to me."
    
    t neutral "Would you like to try it?"

    "I hesitated, not sure if I could do it, but his warm smile encouraged me to give it a shot."

    k smiling "Sure, why not?"
    
    "I stepped up confidently. It looked pretty simple."

    "He made room for me on the mat, and I stood next to him. The mat felt soft under my feet as I copied his starting position, standing with my feet apart and looking straight ahead."

    t smiling "Take a deep breath and follow me."

    "He brought his hands together, before gradually lifting them upwards. I followed by swinging my arms sloppily, almost losing my balance. Turns out, it's not as easy as it looks."

    t neutral "Slowly. You want to do it properly, not complete the exercise."

    "I try again. My movements flow like a dead cow tumbling down a river."

    menu:
        "Could you show me how it's done?":
            $ Physical += 1
            t smiling "Here, let me help."
            
            "Tai Zhou steps over behind me and grips both of my wrists with his hands. While his strong grip was firm like a pair of cuffs, his fur was soft and I couldn't help but blush as I felt it brush against the length of my arms."

            t neutral "Now, move like this."

            "He brings my arms away from me with a controlled shift. His chest naturally leaned forward, and I could feel his body warmth press against my back."

            t concerned "Are you alright? You don't seem to be relaxed."

            "In all the distraction, I hadn't noticed that my heart started racing."

            menu:
                "I can't help it...":
                    $ Emotional += 1

                    k smiling "Sorry, it's just that... I'm not used to being this close to someone."
                    
                    "Come to think of it, I hadn't seen Johnny in three months."

                    t neutral "Well, would you like me to stop?"

                    k neutral "It's okay, let's continue."

                    t neutral "Now, like this."

                    "I stood helplessly as he effortlessly moved my arms."

                    t neutral "Now, you try."

                    "He let go, and I try to follow his movements without his help."

                    t smiling "Much better."

                    "Tai Zhou went through a few basic moves, guiding my arms and legs."
                    
                "It's nothing.":
                    k neutral "It's nothing.” I mutter."

                    t neutral "Okay, let's continue."

                    "Tai Zhou went through a few basic moves, guiding my arms and legs. It wasn't long before I got tired though."

                "Let's just stop here.":
                    "I say a few words about feeling unwell, but my speech came out as a low mumble."

        "This is embarrassing...":
            k sad "Maybe I'll just sit out for now..."

    "I move back towards my seat. Tai Zhou nods in understanding, and carries on with his routine. It's interesting to watch, if not repetitive."

    k neutral "Do you do this every day?"

    t neutral "Well, I try to. Do you want to guess why?"

    menu:
        "Because it helps you be mindful?":
            $ Intellectual += 1

            k neutral "Well from what I know, Tai chi is a style of martial arts meant to promote relaxation and mindfulness. Meditation in motion, as they say. Kind of like yoga."

            t smiling "Wow. You seem quite knowledgable."

        "Because it's healthy?":
            $ Emotional += 1

            k smiling "Exercise? I'm sure it helps you lose weight and keep fit. Not to mention the health benefits."

            t smiling "Maybe. I get more than enough exercise outside though. Plenty to do around up here in the mountains."

        "To develop your physique?":
            $ Physical += 1

            k smiling "Building a nice body? You look like you work out a lot. Your muscles are huge."

            t smiling "Tai Zhou blushes."

    t neutral "To be honest, it's just a habit. My parents made me do it when I was young and in my home country, along with other martial arts like Wu Shu and Karate. I've never really questioned it."

    k concerned "That's good though. I hate exercising, and now look at me.” I brushed a hand down my own abdomen, feeling a distinctly round bump."

    t smiling "You look fine. Maybe when the weather clears up we can go for a walk. The mountains are a great place to explore."

    k smiling "Sure, I don't mind."

    "I smile as I lay back on the sofa, watching the snow leopard finish up his routine."

    jump cabinNight
