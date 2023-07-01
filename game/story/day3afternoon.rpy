# # Background
# black
# cabin_inside_day

# # Characters
# k = Konrad (neutral, smiling, angry)
# t = Tai Zhou (neutral, smiling)

label cabinAfternoon3:

    scene bg cabin_inside_day
    
    "I flipped another page of my book, settling myself comfily in the living room. All my holiday plans went out the window, but for some reason I didn’t seem to mind. I was starting to get used to being around here."

    "As I immersed myself in the pages of the book, the sound of soft snores reached my ears. I looked up and saw Tai Zhou sprawled across the couch, fast asleep. A content smile graced his features, and I couldn’t help but feel a surge of warmth."

    "It was a rare sight, seeing someone like him napping so comfortably."

    k smiling "He looks so cute when he’s sleeping…"

    "There was no response. Maybe he was deeply lost in his dreams."

    menu:
        "Join him":
            $ Physical += 1

            "I set my book aside and made my way to the couch. Carefully, so as not to disturb him, I eased myself onto the other end of the couch, just next to his legs. I could see his chest slowly rise and fall, in time with his gentle snores."

            "As my arm brushed against his leg however, he began to stir."
            
            t neutral "… Konrad?"

        "Keep your distance respectfully":
            $ Intellectual += 1
            
            "Deciding not to disturb him, I head back into my room to give him some privacy."

            "As I stepped towards my room though, he began to stir."
            
            t neutral "… Konrad?"

        "Call his name":
            k neutral "Tai Zhou?"

            t neutral "zzz … Huh?"

            k neutral "Sorry, I just noticed you there, you look so comfy."

            t neutral "… Oh."

            "He seems a little groggy and annoyed."

    k neutral "Ah, sorry! Did I wake you?"

    t neutral "It’s okay, I wasn’t really sleeping you know."

    k neutral "Well I can head to the bedroom if you’d like some quiet."

    t neutral "Oh no, it’s quite alright. In fact, would you like to join me? It’s a great afternoon for a nap."

    k neutral "Oh…"

    menu:
        "It’s okay, I’d rather read.":
            $ Intellectual += 1

            k neutral "It’s alright. I’m more than happy just to enjoy reading my book. I appreciate just having your company though."

            t smiling "Well, if you insist."

            "I carried on with my reading, while Tai Zhou stared into space. The room filled with a comfortable silence as we each indulged in our own relaxation."

        "Slide under the covers with him.":
            $ Physical += 1

            "I moved towards him and gently lifted up the covers, adjusting the blanket to cover both of us. The warmth from the fireplace enveloped us, creating a cozy cocoon."

            t neutral "That’s not really what I had in mind…"

            t smiling "But it’s alright. This feels comfortable."

            "I snuggled closer to Tai Zhou, our bodies nestled together under the covers. The sound of our synchronized breathing created a soothing rhythm, and the shared warmth brought a sense of intimacy and contentment."

        "Sit on the other end of the couch.":
            "I set my book down, but decided to stay on my end of the couch, giving Tai Zhou his personal space."
            
            "I grabbed one of the pillows and set myself down right next to him, and we both lay together, staring into the ceiling."

    t neutral "Konrad?"

    k neutral "Yeah?"

    t neutral "What do you think you want in a partner?"

    "I was slightly taken aback by that remark. I took some time to think about it."

    menu:
        "He should be physically and emotionally compatible, and share my goals and aspirations.":
            $ Intellectual += 2

            k smiling "I think it’s important for a partner to be someone I can connect with on both physical and emotional levels."
            
            k smiling "Someone who shares similar values, goals, and aspirations."
            
            k smiling "I believe in supporting each other’s growth and being able to have deep intellectual conversations."

            k smiling "That to me is a strong foundation for a relationship."
            
            t smiling "I agree, it’s important to have that connection on an intellectual level."
            
        "He should be my best friend and be there for me when I need him most.":
            $ Emotional += 2

            k smiling "For me, a partner should be my best friend."
            
            k smiling "Someone I can share my joys and sorrows with, who understands and accepts me for who I am."
            
            k smiling "Someone I can trust and rely on in any situation."

            k smiling "Having a strong friendship as the core of a romantic relationship can create a strong bond and lasting happiness."

            t smiling "I agree. Friendship is important in any partnership."

        "He should be rugged, strong, and take good care of me.":
            $ Physical += 2

            k smiling "Well, physical attraction is definitely important to me."
            
            k smiling "I admire strength and someone who can take care of themselves and others. I believe in nurturing and protecting each other in a relationship."

            k smiling "Also I guess it helps if they have big muscles… And look sexy…"

            "I look away to hide my blush, placing my paw to the back of my neck."

            t smiling "Well, I can’t I deny that."
            
        "He should have lots of money.":
            k smiling "Well, hopefully someone rich!"

            k angry "And someone who won’t ditch me at the airport for his stupid computer game with his stupid buddies."

            "Tai Zhou laughs."

    "I subconsciously let out a yawn."

    k smiling "Maybe I should take a break too. I’m feeling really tired today."

    t smiling "Go for it."

    "I lay down and closed my eyes. I could feel the gentle rise and fall of Tai Zhou’s breath, syncing with mine. The rhythmic sound and the comforting presence beside me lulled me into a peaceful slumber."

    "The cabin was filled with a tranquil silence, broken only by the crackling of the fireplace and our synchronized breathing. In this moment, time seemed to stand still, and the world outside was forgotten. All I could think about was taking a nap with Tai Zhou."
    
    "We found solace in each other’s company, even in the simplicity of sharing a nap."

    "The afternoon drifted by, the snow falling softly outside the windows, as we rested together, hearts intertwined in the quiet embrace of the cabin’s warmth and the blossoming connection between us."

    jump ending
