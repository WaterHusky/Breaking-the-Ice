# # Background
# black
# cabin_inside_day

# # Characters
# k = Konrad (neutral, smiling, angry)
# t = Tai Zhou (neutral, smiling, nodding)

label cabinMorning3:

    scene bg cabin_inside_day
    
    "It's another day in the cabin. The worst of the storm seems to have subsided, from what I could hear. Still, I couldn't see the outside, since the cabin was still snowed in. Hopefully everything would melt by tomorrow."
    
    "I yawned and stretched my arms, before grabbing a fresh set of clothes. After a quick change, I head back out into the living room."
    
    "I glance over at Tai Zhou, who seems to have just emerged from his room."

    k smiling "Good morning, Tai Zhou. Sleep well?"

    t smiling "Morning, Konrad. How about you?"

    k smiling "Same here. I slept surprisingly well despite the storm. I guess I'm starting to get used to the sound of the snowfall outside."

    t nodding "Indeed. It's oddly calming."

    "I went to wash up, feeling refreshed and ready for the day ahead. Tai Zhou had already gotten the fireplace going, and the cabin felt warm and cozy, providing a comforting refuge from the winter chill."

    k smiling "How about I help prepare breakfast this time?"

    t neutral "Oh? Do you cook often?"

    k neutral "Well, from time to time. Let me see what you have."

    "We make our way to the kitchen. I take a quick look in the pantry, taking stock of the various ingredients. There were many weird bottles of oils and various seasonings, most of them written in a language I don't even recognize."
    
    t neutral "What are you going to cook?"

    k neutral "Well... I'll make some pancakes, I think you have all the ingredients."

    "Thankfully, flour and oil was all I needed. And I was sure there was eggs and milk in the fridge."

    t smiling "That sounds nice. I like pancakes."

    k neutral "You've had them?"

    t neutral "Well, maybe not the kind you're talking about. We add things like green onion and it's salty."

    k neutral "Ah I see."

    "I fetched the ingredients and started pouring it in a bowl. Unfortunately, there wasn't a recipe available so I just stirred in water until the consistency looked right."

    t neutral "Do you cook often?"

    k neutral "Ah, sometimes..."

    "There was a catch in my throat as I spoke."

    t neutral "Hmm? Something wrong?"

    k neutral "Oh, it's nothing... It's just that cooking was one of the things Johnny and I used to share together."

    t neutral "Oh, your ex-boyfriend, correct?"

    "I nod."

    k neutral "We stayed together for a while during one of the summers when he came to visit my country. I'd plan the menu and buy groceries every week, and every day during lunch we'd head to the kitchen and cook together. I'd do the cooking and he'd do the cleaning up. It was a good time."

    t neutral "I see. You two were really close, then?"

    k neutral "Well, yeah. We started to drift apart some time shortly after he left though."

    "I turn the stove on, adding some oil to the pan and letting it heat up."

    t neutral "Whatever happened between you two, anyway?"

    k neutral "Oh..."

    "I tell Tai Zhou about what happened at the airport two days ago."

    t neutral "I see. Sorry to hear about that."

    "I pour the batter into the pan, which immediately starts to sizzle."

    k neutral "It's okay..."

    menu:
        "It was my fault":
            $ Emotional += 1
            k neutral "It was my fault, really. I let my insecurities and doubts get the best of me. I couldn't fully trust Johnny, even though he had given me no reason to doubt him."
            
            k neutral "I pushed him away, questioning his every move, and it eventually became too much for him to handle."

            t neutral "Oh, don't be so hard on yourself. Johnny sounds like an ass, he doesn't deserve you."

            k neutral "Yeah..."

        "It was his fault":
            k neutral "To be honest, it was his fault. Johnny started to become distant and secretive. He wouldn't open up to me about his struggles or share his thoughts."
            
            k neutral "It created a rift between us, and despite my efforts to communicate, he shut me out completely. It felt like I was fighting alone to save our relationship."

            k angry "Honestly, I'm done with people like him."

            t neutral "Well, relationships can be quite tricky, I agree."

        "It was mutual":
            $ Intellectual += 1
            k neutral "Looking back, I think it was both our faults. We both had our own issues and insecurities that we couldn't fully address or overcome together."
            
            k neutral "We lacked effective communication and understanding. It became a toxic cycle of miscommunication and blame, and in the end, we couldn't salvage what we once had."

            k neutral "Maybe it's for the best that we broke up. I hope he finds happiness with someone else."

            t neutral "That's very mature of you to say."

    "I stuck the spatula under the hardened batter, crossing my fingers. Unfortunately, it was a dull shade of blackened brown. Tai Zhou gives a hearty chuckle."
 
    k neutral "Relationships are like pancakes aren't they?"

    t smiling "That's a little cheesy don't you think?"

    k smiling "Just trying to lighten the mood."

    "The morning unfolds with warmth and the gentle aroma of pancakes lingering in the air. Thankfully, the next one turned out a lot better."
    
    "It wasn't long before I was scraping the bottom of the bowl. Tai Zhou helped clean up the dirty utensils as I lifted the last pancake off the pan onto the neat stack that sat atop a plate on the kitchen counter."

    k smiling "Well, bon appétit!"

    "We sat down at the cozy kitchen table, enjoying the delicious homemade pancakes. The sound of cutlery clinking against the plates filled the room."

    t neutral "These pancakes are amazing, Konrad. Thank you."

    k smiling "You're welcome, Tai Zhou. I'm glad you like them."

    "Secretly, I'm surprised my improvised recipe didn't turn out to be a disaster."

    k neutral "Have you ever been in a relationship before?"
    
    t neutral "Well I've had some here and there, but nothing serious."

    "I pause, setting my fork down and looking at Tai Zhou with genuine interest."

    k neutral "Really? May I ask why?"

    t neutral "Well, I've always been more focused on my work and my family, so romance took a back seat. Plus, living alone up here means I don't meet a lot of new people."

    menu:
        "Priorities, am I right?":
            $ Intellectual += 1
            k neutral "I see. It sounds like you've prioritized other aspects of your life."

            t neutral "Yes, exactly. I have goals and aspirations."

            k neutral "Absolutely. It's important to have that straight and focus on what matters most to you."

            t neutral "That's true. I've always believed in giving my best to my work and my family."

            k neutral "I can respect that. Love will always naturally come later."
        "Well, when it happens, it happens.":
            $ Emotional += 1

            k neutral "I see. Well I don't go out of my way to look for relationships either, but it can be a tricky thing, especially when it comes to relationships. Sometimes the universe has its own plans for us."

            t smiling "That's true. Like being here with you in this cabin during the snowstorm, it feels like a special moment."

            k smiling "I feel the same way, Tai Zhou. Sometimes unexpected circumstances bring people together in the most beautiful ways."
        
        "Are you looking for one right now?":
            $ Physical += 1
            k neutral "Are you open to the idea of being in a relationship now?"

            t neutral "Well, I've never actively looked for one. If the right person comes along, I'm willing to explore it."

            k smiling "Happy to hear that."

            "I gaze into his eyes with a knowing smile. He stares back and his cheeks turn a shade of red."

            t neutral "Do you mean..."

            k neutral "Oh, never mind..."

            "I look back down, burying my nose in my plate."

    "We continue to enjoy our breakfast, savoring each bite and sharing stories of our past adventures and missed connections."

    t smiling "Thanks for cooking, Konrad. I don't think I've had a meal like that in a long time."

    k smiling "You're welcome! I'm glad you loved it."

    jump cabinAfternoon3
