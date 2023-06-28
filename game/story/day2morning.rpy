# # Background
# black
# cabin_outside_day
# cabin_inside_day

# # Characters
# k = Konrad (tired)
# t = Tai Zhou (neutral, concerned, smiling)

label cabinMorning2:

  scene bg black

  show bg cabin_inside_day
  
  "I wake up the next day, feeling refreshed from a restful sleep. The morning light filters through the cabin windows, casting a gentle glow on the surroundings. Stretching my limbs, I sit up in bed and reach for my phone on the bedside table."

  k neutral "Still no internet..."

  "I turned towards the window. Unsurprisingly, nothing but snow, filling up to almost the edge of the window."

  k neutral "I hope I don't get trapped here."

  "For some reason, that thought wasn't as bad as it sounds."

  "I was about to set my phone back down on the bedside table, when I noticed a message sent in the middle of the night."

  k neutral "Hmm?"

  "I opened it, and my mood soured."

  "Johnny: r u safe? heard there was a storm"

  k angry "..."

  "Without a second thought, I deleted it."

  show bg black

  show bg cabin_inside_day

  "After taking a moment to gather my thoughts, I stepped out of the bedroom."

  "{i}*Whack* *thud*{/i}"

  k neutral "Hmm?"

  "{i}*Whack* *thud*{/i}"

  "A rhythmic banging was sounding from the far end of the cabin. Curious, I head over to investigate."

  "Opening a door, I step into what looked like a workshop, a rustic and well-organized space filled with tools, lumber, and the smell of sawdust. The air here was significantly cooler, as only a sturdy roller door separated the indoors from the outside. I could tell this used to be a garage."

  t neutral "Huff..."

  "I spied the snow leopard standing in the center of the room, a large empty space cleared around him. Smaller chunks of wood lay scattered on the ground in various sizes." 
  
  t neutral "Huhhh..."

  "Tai Zhou lifts his hands over his head, and I could see now that he was wearing safety goggles and holding a sturdy axe. He gives it a mighty swing, striking a cylinder of wood, which splits into two even wedges and sends wood chips flying."

  k smiling "Morning, Tai Zhou."

  t smiling "Morning."

  k neutral "You're up pretty early."

  t neutral "Really? It's pretty late. "
  
  k neutral "Oh? How long have you been up?"

  t neutral "Well, I went outside to the woodpile, lugged it back here, then sawed it into logs, then the chopping... Maybe a few hours?"

  "Woah. I was lucky if I got anything productive done before 3 p.m."

  k neutral "Wow... you do this every day?"

  t neutral "No, but I realized we ran out of firewood. I didn't expect the storm to last this long."

  k neutral "Ah yeah, I see."

  "The snow leopard stands up fully, panting heavily and out of breath. He looked like he needed a break."

  k neutral "Need some help?"

  t neutral "Have you done this before?"

  k smiling "No... But I'll do my best!"

  t neutral "Better not to then. Maybe if we're outside but it's too dangerous indoors. Normally I wouldn't do this inside but it's an emergency now."

  k sad "Aww... Well, I can still..."

  menu:
    "Gather the wood?":
      k smiling "How about I gather the wood and bringing it inside?"

      t smiling "Thank you, Konrad. I appreciate your help."

      "I gathered up a bunch of wood lying on the floor and head out."
      
      "When I was walking to the fireplace, suddenly I heard a yell."

      t angry "Ow!"

      "I dropped the pile on the floor and rushed back into the garage."
    "Get you something to drink?":
      $ Emotional += 1

      "Since I can't help with chopping wood, I turn my attention to Tai Zhou's well-being."

      k smiling "How about I get you something to drink? You must be exhausted."

      t smiling "That's very kind of you, Konrad."

      "I nodded and head out."

      "When I was walking to the kitchen, suddenly I heard a yell."

      t angry "Ow!"

      "I dropped the pile on the floor and rushed back into the garage."
    "Offer moral support?":
      $ Emotional += 1

      "Even though I can't physically assist with the chopping, I can still offer my moral support."

      k smiling "Well, I'll be here cheering you on."

      "Tai Zhou can't help but laugh."

      t smiling "Sure, if you like."

      "Time seems to slip away as we talk, exchanging stories, laughter, and occasional playful competition."
      
      "The woodpile gradually grows, ensuring we'll have enough fuel to keep the cabin warm during this prolonged snowstorm."

      "Suddenly, I heard a yell."

      t angry "Ow!"

    "Get you a towel?":
      $ Physical += 1

      "As I notice Tai Zhou working up a sweat, I want to make sure he's comfortable."

      k smiling "Would you like a towel to wipe off the sweat? It might help you feel more refreshed."

      t smiling "Yes, a towel would be great."

      "Luckily, Tai Zhou had left one lying in on the table. I picked it up and walked over, before slowly wiping his back. I could feel his body heat radiating through the cloth, and the towel was quickly stained with his sweat."
      
      t smiling "Thanks, but you know you could've just passed it to me."

      k smiling "It's fine, this is probably easier."

      "Nevertheless, I handed it over after a few more brushes. Tai Zhou wipes the sweat off his forehead, before carrying on."

      "The woodpile gradually grows, ensuring we'll have enough fuel to keep the cabin warm during this prolonged snowstorm."

      "Suddenly, I heard a yell."

      t angry "Ow!"

  k neutral "What happened?"

  t neutral "Splinter... Don't worry, I'm fine."

  menu:
    "First aid!":
      $ Physical += 1

      k neutral "Let me see..."

      "I bent down. A short gash ran along the side of his thigh. The cut looked quite shallow and relatively harmless, but it was bleeding slightly."

      k neutral "I'll get my first aid kit. We should tend to the wound."

      t neutral "No need, I get hurt like this all the time"

      k neutral "It might get infected! It's okay, this will only take a bit."

      "I swiftly move to retrieve the first aid kit from the bedroom before he could say anything else."

      "Upon returning I grab a clean cloth and a mild antiseptic solution."

      k neutral "Let's clean the wound to prevent any infection."

      t neutral "Alright... I trust you."

      k smiling "Don't worry, medical care is in my blood."

      "I patch it up relatively quickly with a band-aid. Tai Zhou humoured me, but he seemed genuinely grateful when it was over."

      t smiling "Thanks Konrad. It does feel slightly better."

      k smiling "You're welcome."

    "Maybe it's time for a break?":
      $ Emotional += 1

      k smiling "You've been working hard, Tai Zhou. It might be a good idea to take a break and give yourself a chance to recover."

      t smiling "You're right, Konrad. I should take a moment to rest."

      "Tai Zhou sets down the axe for a moment, giving us a chance to talk. He tells me about a few humorous accidents he had in the past."
      
      "He laughs. I wonder how he actually survived."
    
    "Eh, he knows what he's doing":
      k neutral "Alright, Tai Zhou. But please be careful."

      t neutral "Thanks."

  t neutral "Well, I think we have more than enough firewood by now, what say we head back?"

  "I was more than happy to. The garage was freezing, though he probably didn't feel the same way."
    
  k neutral "Yeah, let's."

  jump cabinAfternoon2
  

