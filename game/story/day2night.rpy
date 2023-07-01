# # Background
# black
# cabin_inside_night

# # Characters
# k = Konrad (neutral, smiling, relaxed)
# t = Tai Zhou (neutral, smiling)

label cabinNight2:

    scene bg cabin_inside_night
    
    "Before I knew it, night had come around again. The sky was dark, but given the current state of weather it could’ve been any time between 3pm and 12am."

    "I sat alone, huddled in bed under a stack of blankets with my nose buried in a book. The temperature had dropped significantly compared to the previous days, now that the cabin was completely snowed in."
    
    k neutral "Brr…"

    "I feared that we might be in trouble, but Tai Zhou reassured me that he’d been through worse storms."

    k neutral "Whoops. Nature’s calling."

    "I reluctantly got out of bed, wincing as my feet touched against the freezing floor. I quickly made my way to the restroom, tiptoeing as I went."

    "The bathroom was on the other side of the cabin. I pushed the half-opened door, headed in and started doing my business."

    k neutral "Ahh…"

    "Suddenly, I heard a splash nearby."

    t neutral "Konrad? Is that you?"

    "Hearing his familiar voice shocked me, and I almost lose control. I quickly finish up and rush to wash my hands."

    k neutral "I’m sorry! I didn’t know you were in here!"

    t neutral "It’s okay. I guess I should’ve locked the door."

    "I turn around towards him, and my jaw dropped slightly. The snow leopard was soaking in a large tub of steaming hot water, wearing nothing but a towel around his waist."

    t neutral "Care to join me? There’s enough room for both of us."

    "My cheeks turn a shade of red as I looked over his muscular, half naked body. The water looked really inviting though, and I was freezing my fur off."

    menu: 
        "Okay!":
            k neutral "Uh… sure, why not?"

        "I’m not so sure…":
            k neutral "Uhh… it’s okay, I think I’ll come back later."

            t smiling "Are you sure? I won’t ask again…"

            menu:
                "Well, if you insist…":
                    k neutral "Well okay. I could use a relaxing soak."
    
                "I’d rather not.":
                    k neutral "Thanks, but it’s okay."

                    t neutral "Alright."

                    "Tai Zhou seemed a little disappointed as I exited the bathroom and headed back to my room."

                    jump scene_end

    $ Physical += 1

    "I quickly strip down and join Tai Zhou in the warm, inviting waters of the hot tub. The tension from the awkward bathroom encounter dissipates as we settle into the relaxing embrace of the hot water."

    k relaxed "This feels amazing. I didn’t expect to this cabin to have a hot tub."

    t smiling "You like it? I built it myself. It’s good for the cold isn’t it?"

    "The steam rises around us, creating a cozy atmosphere as we soak in the soothing warmth. We felt comfortable simply being in each other’s company, but I decided to make a move."

    menu:
        "Let’s talk.":
            $ Intellectual += 1

            k neutral "Tai Zhou, you’ve mentioned your family before, but I don’t know much about them. What were they like?"

            t neutral "Ah, my family… They were hardworking and resilient. They wanted to provide a better life for me and my siblings."

            k neutral "It sounds like they instilled important values in you. What were some of the fondest memories you have with them?"

            t smiling "There are many, but one that stands out is when we would gather around the dinner table. Despite our humble circumstances, my parents always made sure we had a warm meal to share. It was a time for laughter, storytelling, and being together as a family."

            k smiling "That sounds wonderful. Family bonds are truly special."

            t neutral "Yes, they are. I miss them dearly, but I know they would want me to keep moving forward and making the most of life."

            k smiling "And you’re doing just that, Tai Zhou. I’m honored to have met someone as remarkable as you."

            t smiling "Thank you, Konrad. Your kind words mean a lot to me."

        "Let’s skip the chatter ;)":
            $ Physical += 1

            "I found my body slowly inching towards where he sat. Before I knew it, my shoulders were brushing up against his."

            t neutral "Konrad?"

            "I lifted my hand out of the water, leaning towards him and placing it around his neck, feeling his muscular build."

            "The snow leopard blushes. He seems a little taken aback, but he lets it happen."

            menu:
                "That’s probably enough…":
                    k neutral "Sorry… forgive me. I hope that didn’t weird you out."

                    t neutral "It’s okay."

                "Keep going.":
                    $ Physical += 1

                    "I turned towards him, and began softly brushing the tip of my snout against his neck."

                    "He lets out a soft purr, and leaned to the side."

                    k neutral "I don’t think I’ve mentioned but I think you’re very attractive."

                    "Tai Zhou says nothing, but I could see a grin form on the side of his lips."

                    show bg black with dissolve
            
        "Let’s just enjoy the moment.":
            $ Emotional += 1
            "The air fills with a comfortable silence as we continue to enjoy the serene ambience. The warm water envelops us, washing away any lingering worries or stress."

            k neutral "You know, Tai Zhou, spending time with you has made this snowstorm more bearable. I’m grateful for your company."

            t neutral "Likewise, Konrad. It’s been a pleasure getting to know you."

    "The sound of the crackling fire, combined with the bubbling water, creates a symphony of tranquility. As the snow continues to fall outside, we remain in the hot tub, sharing stories, laughter, and enjoying each other’s company."

    "It’s a moment of genuine connection and warmth amidst the wintry embrace of the log cabin."

    label scene_end:

    jump cabinMorning3
