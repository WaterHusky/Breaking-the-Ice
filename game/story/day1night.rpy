# # Background
# black
# cabin_inside_night

# # Characters
# k = Konrad (neutral, smiling)
# t = Tai Zhou (neutral, smiling, agreeing, sad, nodding)

label cabinNight:

    scene bg cabin_inside_night
    
    "My ears soon became accustomed to the howling winds outside. This blizzard was relentless. With what scant mobile reception reached the edge of the mountain, I struggled to look up weather information, but at this point it seemed obvious that I would have to stay in here for another night at the very least."

    k neutral "Sorry, I really hope I'm not overstaying my welcome."

    t neutral "It's okay. I don't mind."
    
    k smiling "Thanks, Tai Zhou. Anyway, it's your turn."

    t neutral "Oh."

    "His hand fumbles as he picks up the pair of dice and lazily rolls them."
        
    k neutral "Do you get a lot of visitors up here?"

    t neutral "Not really. You're the first one I've had in years."
        
    k neutral "Years?"

    t neutral "Yes, I usually keep to myself and hardly meet people."

    menu:
        "Doesn't it get lonely?":
            $ Emotional += 1
            k neutral "Doesn't it get lonely up here?"
            t neutral "Well, sometimes. But I make do. The people in the city don't really trust me, especially since I moved in from Asia. You were very lucky that I was in town last night."
            k neutral "Aww... I'm sorry to hear that."
            t neutral "It's not that bad. I get to do what I want up here and no one bothers me."
            k neutral "Still, I'm sure you'd like someone to talk to every now and then."
            t smiling "Maybe. I've never really felt the need."
            k smiling "Well for what it's worth I'm glad I have someone to accompany me during this snow storm. I'd probably be lost otherwise."
            t smiling "It's no problem."
            "Tai Zhou smiles."
            k smiling "I'm glad I met you, Tai Zhou. You've made this situation much more bearable."
            "I gently touches Tai Zhou's hand as he hand me the dice."
            t smiling "I'm glad too, Konrad."

        "A life of solitude, I get it.":
            $ Intellectual += 1
            k neutral "I can respect that. Sometimes a simple life is all you need, right?"
            t smiling "Yes. "
            k neutral "I understand. Life has its ups and downs. Sometimes we need to take a step back and focus on ourselves."
            k neutral "You're right. Maybe this snowstorm is a blessing in disguise. It's given me a chance to reflect and spend time with someone like you."
            t neutral "Someone like me?"
            k smiling "Yeah, someone kind and genuine. It's refreshing."
            t smiling "Thank you... I feel the same way."

        "No surprises there.":
            k angry "Makes sense, people suck. After my last relationship with Johnny I can see why people want to live alone."
            "Tai Zhou shrugs awkwardly."

    "I throw the dice and move my own piece. I could tell that he seemed bored."

    k neutral "So... What do you do in your free time, actually? Is there a lot to do up here?" 

    t neutral "Snowstorm like this, I need to make sure cabin stays warm, cook food for myself and fix up the house if anything gets damaged."

    k neutral "That sounds like hard work, but also fulfilling. Do you enjoy it?"

    t neutral "Yes, I do. Keeps me busy, gives purpose."

    k smiling "That's impressive, Tai Zhou. I've always wanted to learn more practical skills like that. Living in the city, we don't get much of those skills."

    t neutral "City life is different. Busy, many people. Here, it's quiet and peaceful."

    k neutral "I can see the appeal. Being here, surrounded by nature and away from it all, it's refreshing."

    t smiling "Yes, it's beautiful. Snow, mountains, trees. It calms my mind."

    k neutral "I can understand that. It's like a temporary escape from the chaos of everyday life."

    t agreeing "Exactly, Konrad. It's like sanctuary."

    k neutral "Tai Zhou, I've been meaning to ask... What made you decide to move here? It must have been a big change."

    t neutral "Ah... family moved here first, when I was very young. Also, opportunity. Father got a job here."

    k neutral "Well, at least it's nice that you have family nearby."

    t sad "Not really. Parents passed. I'm the only one left here."

    k neutral "Aww..."

    menu:
        "Hug him":
            $ Physical += 1

            "Before I knew it, I had leaned forward and hugged him in an embrace. Tai Zhou seems startled, but lets it happen."

            t smiling "Thanks, but it was a while ago. I've gotten over it."

            k neutral "Okay..."

            "I backed off, blushing slightly and flush with embarrassment."

        "Sympathize with him":
            $ Emotional += 1

            k neutral "I'm really sorry to hear about your parents, Tai Zhou. Losing loved ones can be incredibly difficult."

            t sad "Yes, it's been tough... Thank you for your sympathy."

            k neutral "I understand, Tai Zhou. If you ever want to share or talk about anything, I'm here to listen."

            t nodding "I appreciate that, Konrad. It means a lot to me."

        "Keep your distance":
            k neutral "I'm sorry for prying, Tai Zhou. I didn't mean to make you uncomfortable."

            t neutral "It's alright, Konrad. Some things are just hard to talk about."

    k neutral "So, shall we continue our game? I'm ready to win."

    t neutral "Don't be so confident!"

    show bg black

    show bg cabin_inside_night

    "As the board game came to an end, we tidied up the pieces and put them back in the box. The fire crackled, casting a warm glow across the cabin."

    k neutral "Well, Tai Zhou, it's getting late. I should probably get some rest. Thank you for the game and the company."

    t tired "You're welcome, Konrad. It was fun. Sleep well."

    k smiling "You too, Tai Zhou. Goodnight. Thanks again for letting me stay here."

    "I retreated to the bedroom area of the cabin, feeling a sense of contentment and gratitude."

    jump cabinMorning2
