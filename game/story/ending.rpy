# # Background
# black
# cabin_inside_day
# cabin_inside_night
# snowscape
# airport

# # Characters
# k = Konrad (tired)
# t = Tai Zhou (neutral, concerned, smiling)

label ending:

    $ success_physical = False
    $ success_intellectual = False
    $ success_emotional = False
    # Starts on day 3 evening

    # Todo: Assign conditionals based on score

    #default Physical
    #default Intellectual
    #default Emotional
    
    if Physical > max(Intellectual, Emotional):
        $ success_physical = True
    elif Intellectual > max(Physical, Emotional):
        $ success_intellectual = True
    elif Emotional > max(Physical, Intellectual):
        $ success_emotional = True
    elif Physical == Intellectual:
        $ success_physical = True
        $ success_intellectual = True
    elif Physical == Emotional:
        $ success_physical = True
        $ success_emotional = True
    elif Intellectual == Emotional:
        $ success_intellectual = True
        $ success_emotional = True
    elif Physical == Intellectual == Emotional:
        $ success_physical = True
        $ success_intellectual = True
        $ success_emotional = True
    else:
        $ success_physical = False
        $ success_intellectual = False
        $ success_emotional = False

    scene bg cabin_inside_night
    
    "It’s getting late."

    "Being stuck in a cabin for three days isn’t something I envisioned for my trip here, but Tai Zhou’s company has been amazing."

    "Tai Zhou peers out of the window."

    t "Looks like the weather is clearing up! With any luck, we’ll be able to explore the outside tomorrow."

    k "Hopefully. I need to catch my flight back."

    t concerned "Wait, when is it?"

    k "Tomorrow morning."

    t "Ah…"

    k "Is everything okay?"

    t "Well, I thought we’d have longer to hang out. I want to show you the beautiful places around here."

    jump ending_evening


label ending_evening:
    if success_emotional:
        # They have a heart-to-heart talk about where their friendship is going to go
        call ending_evening_emotional
    elif success_intellectual:
        # They have a talk about life and the philosophy of goodbyes
        call ending_evening_intellectual
    elif success_physical:
        # Instead of chatting, Tai Zhou eases them straight into the bedroom scene
        call ending_evening_physical
        pass
    else:
        # They have an awkard evening together
        call ending_evening_bad
    
    jump ending_bedroom


label ending_bedroom:
    if success_physical:
        # They get physical in the bedroom
        call ending_bedroom_physical
    else:
        # They go to their own bedrooms and fall asleep
        call ending_bedroom_bad
    
    jump ending_leaving


label ending_leaving:
    # They leave the house

    show bg snowscape

    # beautiful outside, air is fresh, everything feels brighter and vibrant
    # feels surreal. different from just when it’s on the other side of the window pane
    # The only time he’s been outside was when he was tired after his first night here
    # Konrad plays around for a bit.

    "The vast expanse of untouched snow stretches as far as the eye can see, sparkling under the gentle rays of sunlight. The landscape is adorned with glistening icicles hanging from tree branches, and a sense of tranquility envelops the surroundings."

    "As I step outside, a wave of wonder washes over me. It’s been three days since I last stepped foot beyond the cabin’s walls, and the freedom feels exhilarating. The world outside is transformed into a winter paradise."

    k smiling "Wow, this is absolutely stunning! It feels almost surreal being outside now after the storm."

    "I can’t help but be captivated by the beauty around me. The sunlight creates a dazzling display as it reflects off the individual snowflakes, making the whole landscape shine. The air is so fresh and invigorating, and every breath fills me with a sense of renewed energy."

    t smiling "I’m glad you get to experience the beauty of nature firsthand."
    
    t "It’s one of the best parts about living up here."

    "I take a deep breath, savoring the crisp winter air. I feel a sense of liberation as I walk through the snow, leaving behind footprints that soon get filled with more snowflakes. It’s a reminder that I’m part of this vast, ever-changing world."

    "We take a leisurely stroll together, our breath visible in the cold air. As we walk, I can’t help but appreciate the stillness and tranquility that surrounds us. It’s a stark contrast to the busy city life I’m accustomed to."

    k "Thanks for accompanying me, Tai Zhou."

    t "It’s no problem."

    k "Moments like these remind us of the simple joys in life."

    "I smile back, feeling a deep sense of gratitude. Tai Zhou’s cabin has become more than just a shelter from the storm. It has become a place of connection, reflection, and unexpected beauty."

    "We continue walking, hand in hand, in awe of the picturesque scenery. The snow-covered trees seem to whisper secrets of serenity, and the gentle crunch of our footsteps harmonizes with the peacefulness of the winter landscape. In this moment, surrounded by nature’s grandeur, I realize that this unexpected journey has left an indelible mark on my heart."

    if success_emotional:
        # Tai Zhou doesn’t follow Konrad to the airport
        call ending_leaving_follow
    else:
        # Tai Zhou follows Konrad to the airport
        call ending_leaving_nofollow

    jump ending_reflection


label ending_reflection:
    if success_physical and success_intellectual and success_emotional:
        # if physical+intellectual+emotional, promise to take the time to recover, and then come back to Tai Zhou when he’s ready for a relationship
        call ending_reflection_best
    elif success_physical and success_emotional:
        # if physical+emotional, they chat after Konrad returns to his life, and Konrad looks forward to visiting again, imagining their bodies against each other
        call ending_reflection_physical_emotional
    elif  (success_intellectual and success_emotional) or (success_emotional):
        # if intellectual+emotional or emotional, they become good friends
        call ending_reflection_emotional
    elif (success_physical and success_intellectual) or success_physical or success_intellectual:
        # if physical+intellectual or physical or intellectual, they chat for a while, but it trails off, and life goes on  
        call ending_reflection_physical_intellectual
    else:
        # if none, Konrad moves on and eventually forgets about Tai Zhou
        call ending_reflection_bad

    return


# ============================
# ===== Evening sections =====
# ============================

label ending_evening_intellectual:
    # Possibilities: emotional = false, intellectual = true

    "As we lay side by side, the silence between us feels comfortable and serene. The soft glow of moonlight seeps through the curtains, casting a gentle glow upon our faces."

    k neutral "Tai Zhou, have you ever thought about the philosophy of goodbyes?"

    t neutral "Hmm, goodbyes? What do you mean?"

    k "Well, in life, we often have to say goodbye to people, places, and moments that have shaped us. But is goodbye truly an end, or is it just the beginning of something new?"

    k "Goodbyes can be bittersweet, as they mark the end of a chapter while opening the door to new possibilities."

    t "That’s an interesting way to see it."
    
    k "Exactly. It’s like closing one book and starting another. We carry the memories and lessons with us, allowing them to shape our journey."

    k "In a way, goodbyes remind us of the transient nature of life. They teach us to appreciate the present moment and cherish the connections we form along the way."

    k "And as we find ourselves here, in this cabin, having shared this unique experience, I can’t help but think that this is not just a goodbye but a beginning of something meaningful."
        
    k "Our paths may diverge after this, but the impact we’ve had on each other’s lives will remain. Goodbyes don’t have to be permanent; they can be the starting point of a lifelong connection."

    t smiling "You’re right, Konrad. I don’t think I’ll ever forget you."

    "In that moment, a profound sense of understanding and acceptance fills the room. We may part ways physically, but our intellectual bond and shared experiences will continue to shape us."

    k smiling "Thank you, Tai Zhou. The days we’ve spent together really broadened my perspective."

    t "And thank you, Konrad. You’ve helped me better understand the world. "
    
    return

label ending_evening_emotional:
    # Possibilities: emotional = true

    # They talk about where to go from here in terms of their friendship/relationship
    
    "As we lay next to each other, the quiet ambiance of the room creates an atmosphere of intimacy and vulnerability. The flickering candlelight casts dancing shadows on the walls, adding to the depth of the moment."

    k neutral "You know, Tai Zhou, spending all this time together has been incredibly special to me. It’s like we’ve formed a connection that goes beyond friendship."

    k smiling "It’s amazing how we’ve opened up to each other, sharing our thoughts, fears, and dreams. Our bond has grown stronger through this experience."

    t smiling "I feel the same way, Konrad."

    k "I’ve been thinking a lot about where our friendship might lead. I’ve enjoyed every moment we’ve spent together, and I can’t help but wonder if there’s potential for something more."

    t "I couldn’t agree more."

    k "Love knows no boundaries, and it can blossom in the most unexpected places. If we’re both willing to navigate the uncertainties, I’m open to seeing where this journey takes us."

    "In that moment, our eyes meet, and a mixture of hope and excitement fills the room. We know that embarking on this path together may not be easy, but the potential for something beautiful outweighs the risks."

    k "Thank you, Tai Zhou. Your willingness to explore this with me means the world."

    t "Thank you for being the person who understands me like no one else. Let’s see where this road leads us, hand in hand."

    return

label ending_evening_physical:
    # Possibilities: emotional = false, intellectual = false, physical = true

    # Nothing happens here :3

    return

label ending_evening_bad:
    # Possibilities: emotional = false, intellectual = false, physical = false

    # Awkward evening

    "As we lay next to each other, an uncomfortable tension fills the room. The silence feels heavy, and the energy between us is strained."

    k neutral "So… I guess since the storm has ended, I can leave tomorrow."
    
    t neutral "I see."

    k "Thanks for everything. You’ve been very kind."
    
    t "You’re welcome."

    k "I’m sorry if I’ve done or said anything to make you uncomfortable."

    t "No, it’s not your fault, Konrad. I’ve been feeling the same way. Maybe spending so much time together has made things a little awkward."

    k "Yeah, perhaps…"
        
    return


# ============================
# ===== Bedroom sections =====
# ============================

label ending_bedroom_physical:
    # Possibilities: physical = true

    if success_emotional or success_intellectual:
        # They had an emotional/intellectual conversation before this

        t smiling "Ah. Anyway, it’s getting late."

        k smiling "Yeah, we should head to—"

        k surprised "Wha—"

        "He strokes my chin with his index finger. It’s warm, sending tingly feelings down my spine."

        t seductive "I was thinking of something else."

        "His hand moves down and he holds his palm against my chest."

        "My heart is fluttering, and I’m sure Tai Zhou feels it too."

        t neutral "Let’s head to my bedroom."

        "We get up and follow him to his room."

    else:
        # The evening begins with this

        t seductive "Well, I know what we can do instead."

        "Tai Zhou takes a step towards me."

        k neutral "What are you thinking of—"

        k surprised "Wha—"

        "He strokes my chin with his index finger. It’s warm, sending tingly feelings down my spine."

        t "Shh."

        "His hand moves down and he holds his palm against my chest."

        "My heart is fluttering, and I’m sure Tai Zhou feels it too."

        t neutral "Let’s head to my bedroom."

        "I follow him to his room."

    "It feels like I’m floating on air as I walk, as if my feet aren’t touching the ground."

    "This is actually happening, right? I’m not imagining it."

    "Yet the 10 steps to the bedroom feels like 10 steps too long. I want it {i}now{/i}."

    "As I enter the room, he steps to the side. I turn to face him and—"
    
    "He pushes me backwards onto the bed."

    k surprised "Hey!"

    t seductive "Relax~"
    
    "His fingers caress my lips with gentle but deliberate strokes."

    "His eyes gaze deeply into mine, and it feels like we’re communicating in a language beyond words."

    "He leans in and presses his lips against mine."

    "The kiss catches me off guard at first, but soon, our lips are moving in harmony."

    "Then he pulls back."

    "I look at him in anticipation."

    "He catches my expression and smiles. Then he swoops in for another kiss."

    "This time, I’m ready. Our lips touch and his tongue plunges into my mouth."

    "I gasp. Tingly sensations of euphoria surge through my body and a light-headedness washes over me."

    "Our tongues press against each other, dancing about in an unscripted choreography."

    "His hands are all over my back, massaging my muscles."

    "I grope his back too, squeezing and groping his upper back. His broad shoulders. His lats."

    "I’m out of breath when our kiss ends."

    k blush "Whoa—"

    "His hands are already on my shirt buttons, undoing them swiftly."

    "He opens the shirt, pulls it over my shoulders and down my back. I let my arms slip through the sleeves."

    "This time when he leans in, he nuzzles his check against the sensitive part of my neck."

    "I let out a soft gasp."

    "My hands unclasp his coat and pulls it off him, revealing his muscular chest."

    "His sculpted pecs press against mine and I can feel his warmth."

    k blush "Oh!"

    "He’s sporting a hard-on in his pants, but so am I."

    "I can’t control myself."

    "I thrust my hips forward, pushing my crotch against his. He grinds back."

    "Our moans fill the room."

    t "You’re so cute when you’re like that."

    k "L—like what?"

    t "So keen and horny. Eager for me to have my way with you."

    k seductive "Then what are you waiting for?"

    "He doesn’t hesistate. He undoes his pants and tosses them onto the floor."

    "His manhood is fully erect in front of me."

    "My pants is next to go as he enthusiastically takes them off and shoves them to the side."

    t "Turn over."

    "I flip over and hug his pillow against my chest."

    "He lifts my rear up and presses the tip of his manhood against my pucker."

    ""


    '''
        - fingers stroke lips
        - goes in for the kiss. a short one.
        - K is breathless, but T goes in for another one, longer this time.
        - they grope each other
        - T gets up and unbuttons K’s shirt and takes it off.
        - As T nuzzles against K’s neck, K takes off T’s shirt
        - They hug, grind crotches, grope
        - They pull off their pants
        - Start having sex (gently)
        - T hugs K from behind with each hump, holding close
        - Orgasm
        - Falls to bed, tired

    '''

    # Story
    # todo

    scene bg black

    "I sink into his embrace. His maleness is still inside me as I clench against his flesh."

    "This feels good. This feels right."

    "His warmth is my blanket in the midst of the waning blizzard."

    "I fall asleep."

    scene bg cabin_inside_day

    # Wake up and see Tai Zhou in bed
    "When I wake up, I’m face to face with a sleeping Tai Zhou."

    "I watch his peaceful expression, feeling a warmth in my heart."

    "Eventually, he wakes up."

    t smiling "Hey, you’re awake. Been up for long?"

    k smiling "Just a bit."

    t neutral "You could’ve woken me up, you know."

    k neutral "And ruin the magic? Nah."

    "We enjoy each other’s company in comfortable silence."

    "Tai Zhou finally breaks the silence."

    t "I think the worst of the storm is over."

    "Sure enough, the relentless pelting of snow on the window has been replaced by the gentle falling of snowflakes."

    t "Let’s get changed and check outside."

    "We hastily grab our clothes that had been hastily tossed on the floor last night."

    "When Tai Zhou opens the door…"

    return


label ending_bedroom_bad:
    # Possibilities: physical = false

    "I make my way to my own bedroom."

    show bg bedroom_night

    "I settle under the covers, thoughts swirling in my mind. It’s hard to shake off the memories of our time together in the cabin. As I close my eyes, I hope that sleep will bring some solace."

    show bg black

    "Dreams intertwine with fragments of reality as I drift into a restless sleep. Thoughts of the cabin, the conversations, and the fleeting moments of connection with Tai Zhou play on a loop in my mind."

    "Images of laughter, shared meals, and quiet conversations fill my subconscious. I find myself reliving the moments we spent together, each one etching itself deeper into my heart. The warmth of Tai Zhou’s presence lingers, even in my dreams."

    "As the night unfolds, my mind navigates the uncharted territory of what could have been. I wonder if I missed an opportunity, if I let fear and uncertainty guide my actions. A slight regret washes over me, but I let it pass."

    "Before I knew it, I was fast asleep."

    show bg cabin_inside_day

    "Morning comes. I slowly open my eyes, greeted by the sight of Tai Zhou, standing in the living room with a gentle smile."

    t smiling "Good morning, Konrad. Sleep well?"

    k neutral "Morning, Tai Zhou. It was a bit restless, to be honest. Dreams and memories kept intertwining."

    t neutral "I can relate."

    "As I stretch and get out of bed, a mix of emotions washes over me. Although our connection may not have evolved as I had hoped, I am grateful for the moments we shared."

    t "I think the worst of the storm is over."

    "Sure enough, the relentless pelting of snow on the window has been replaced by the gentle falling of snowflakes."

    t "Let’s get changed and check outside."

    "We hastily grab our clothes that had been hastily tossed on the floor last night."

    "When Tai Zhou opens the door…"

    return


# ============================
# ===== Leaving sections =====
# ============================

label ending_leaving_nofollow:
    # Condition: emotional = false

    # Tai Zhou doesn’t accompany Konrad to the airport.
    # If physical = true, Tai Zhou says that they should meet again when he returns *winks
    # If intellectual = true and physical = false, Tai Zhou sees them as friends and promises to stay in touch

    "As the time comes for me to leave, I can’t help but feel a mix of emotions. Tai Zhou and I have shared unforgettable moments in this secluded cabin, and saying goodbye is bittersweet."

    t smiling "Konrad, it’s been fun spending these days together. Sorry I won’t be able to accompany you to the airport."

    k smiling "Thank you, Tai Zhou. This experience has been truly remarkable. I’ll cherish the memories we’ve created I do hope our paths cross again in the future.."

    "We exchange a warm hug, knowing that our lives will continue on separate paths. If physical attraction played a role, Tai Zhou leans closer and whispers in my ear with a playful smile."

    if success_physical:
        t "When you return, let’s make more memories together. Until then, safe travels."

        "Tai Zhou gives me a wink, before leaning forward to embrace me with a hug."

    elif success_intellectual:
        t "Although we won’t be physically together, I consider you a dear friend. Let’s stay in touch and share our adventures."

        t neutral "Take care, Konrad. Remember to keep in touch."

        "Tai Zhou bows his head politely."

    "With those parting words, we bid farewell. I turn to leave, thinking about the time we had together in the cabin, knowing that the impact of this unexpected encounter will stay with me."

    return

label ending_leaving_follow:
    # Condition: emotional = true

    "As the time comes for me to leave, Tai Zhou insists on accompanying me to the airport. It’s a gesture that fills me with warmth and gratitude. We walk side by side, our footsteps in sync, as we embark on this final journey together."

    t smiling "Konrad, this may be the end of our time together in the cabin, but it’s not the end of our friendship."
    
    t smiling "I want to see you off properly and let you know how much this experience has meant to me."

    k neutral "Tai Zhou, I can’t express enough how much this journey has impacted me. The moments we’ve shared, the conversations we’ve had— they’ve touched me deeply."

    "As we reach the airport, we find a quiet spot away from the bustling crowds. With a backdrop of departure gates and distant announcements, we stand facing each other, our eyes locked in a tender gaze."

    t "Konrad, you’ve brought so much light into my life during these days. I find myself feeling things I hadn’t felt in years."

    k smiling "Tai Zhou, I feel the same way. You’ve shown me a side of myself I hadn’t fully explored, and I’m grateful for the growth and vulnerability we’ve shared."

    "We embrace, our hug filled with a mixture of joy, sadness, and the promise of what’s to come."

    t "You may be leaving, but I know that our love is strong. Let’s make plans to meet again, to create more beautiful memories together."

    k "I couldn’t agree more. Our time in the cabin has been transformative, and I want to continue this journey with you. Let’s stay connected and explore what lies ahead."

    "With heartfelt promises and a shared understanding, we release our embrace. As I walk towards my departure gate, I carry with me the love and warmth we’ve cultivated in the cabin, knowing that our story is far from over."

    return

# ===============================
# ===== Reflection sections =====
# ===============================

label ending_reflection_best:
    # Condition: all 3 traits
    # They promise to take the time to recover, and then come back to Tai Zhou when he’s ready for a relationship

    # todo

    return


label ending_reflection_physical_emotional:
    # Condition: physical AND emotional
    # They chat after Konrad returns to his life, and Konrad looks forward to visiting again, imagining their bodies against each other
    
    # todo

    return


label ending_reflection_emotional:
    # Condition: emotional (intellectual is optional)
    # They become good friends
    
    # todo

    return


label ending_reflection_physical_intellectual:
    # Condition: physical, intellectual, or both
    # They chat for a while, but it trails off, and life goes on 
    
    # todo

    return


label ending_reflection_bad:
    # Condition: all traits failed
    # Konrad moves on and eventually forgets about Tai Zhou
   
    # todo

    return




