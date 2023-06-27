# # Background
# black
# cabin_outside_day
# cabin_inside_day

# # Characters
# k = Konrad (tired)
# t = Tai Zhou (neutral, concerned, smiling)

label cabin:

  scene bg black

  show bg cabin_inside_night
  
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
      #! +Emotional
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
      #! +Intellectual
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

