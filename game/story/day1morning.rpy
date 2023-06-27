# # Background
# black
# cabin_outside_day
# cabin_inside_day

# # Characters
# k = Konrad (tired)
# t = Tai Zhou (neutral, concerned, smiling)

label cabin:

  scene bg black

  show bg cabin_inside_day
  
  "I slowly opened my eyes, the remnants of sleep clinging to my senses. The warmth of the cabin enveloped me, providing a stark contrast to the frigid air outside.""

  "Rubbing my eyes, I glanced around and noticed that the room was empty. Tai Zhou, the cabin's owner, was nowhere to be seen."

  "Curiosity tugged at me, urging me to explore the cabin further. I rose from the bed and padded across the creaking wooden floor."

  "I ventured into the small living area, my eyes drawn to the narrow window. A gasp escaped my lips as I peered outside, greeted by a blinding wall of snow. The storm had intensified overnight. I was trapped, confined within the safety of the cabin's walls."

  "Just as the realization settled in, the door burst open, bringing with it a gust of icy wind and swirling snowflakes. Tai Zhou stumbled inside, quickly slamming the door shut behind him. His breath came out in visible puffs as he shook off the snow clinging to his jacket."

  t smiling "Konrad, glad to see you awake, the storm's worse. Looks like we cannot go outside for a while."

  "I nodded, a mix of gratitude and concern filling my heart."

  k smiling "Thank you for keeping me safe, Tai Zhou. I didn't expect the storm to become this intense."

  "He smiled warmly, his eyes sparkling with a hint of mischief."

  "No problem. I've been through my fair share of storms out here. We'll be fine as long as we stick together."

  "A low growl suddenly emanates from my stomach and I blush."

  t neutral "Hungry? Don't worry. Clean up and get ready. I'll make breakfast."

  show bg cabin_inside_day with dissolve

  "As I settled down at the small table, the aroma of freshly brewed coffee wafted through the air, mingling with an unusual but pleasant scent. The cozy atmosphere of the cabin provided respite from the storm raging outside."

  "Tai Zhou returns, setting down a bowl of rice porridge. It was coloured a pleasant white, topped with a sprinkle of coriander, shredded ginger, and some unusual bits of what looked like black jelly. I scooped one up with a spoon and took a closer look."

  menu: 
    "What is this?":
      t neutral "Pí dàn. I'm not sure what it's called in english but it's quite common to eat with pork porridge."

    "Is this boba?":
      t neutral "No. It's called Pí dàn. I'm not sure what it's called in english but it's quite common to eat with pork porridge."

    "Is this grass jelly?":
      t neutral "No, but good guess. It's called Pí dàn. I'm not sure what it's called in english but it's quite common to eat with pork porridge."

    "Is this century egg?": 
      #! +Intellectual
      t smiling "Yes! You've heard of it?” He seems impressed."
      k neutral "Well, I've seen it in pictures... But I've never tried it."

  "Suspiciously, I brought it up towards my nose. A sharp odour stung my nostrils, smelling of fermented vinegar."

  menu:
    "I'll try anything once!":
      #! +Physical
      "I cautiously place the spoon into my mouth. As I bite down into the strange gelatin, immediately a strange sensation spreads across my tongue and I can't help but make a face."

      menu:
        "Urk, I can do this...":
          #! +Emotional
          "I bite down with my jaw and choke it down. It leaves a strange aftertaste, which I quickly wash away with a drink of coffee."
          "That tastes... interesting...."
          show t smiling
          "Tai Zhou laughs, clearly noticing my discomfort."

        "Spit it out!":
          "My hands flail around the table, before snatching a sheet of tissue from the nearby tissue box. I spat the revolting jelly out onto it, before wrapping it up in ball."
          show t concerned
          "Tai Zhou gives me a slightly crestfallen look."

      "You need to stir it in. It doesn't taste good on its own." Nevertheless, he offers me his glass of water.

    "I'm good, thanks...":
      t concerned "It's okay, you can just pass yours to me."
      
      "The snow leopard frowns, but deftly picks up the slivers of black jelly with his chopsticks and places them in his own bowl. It's a wonder how he can use them so well with his paws."

  "The two of us finish the rest of our breakfast. The hot porridge warms up my insides, and I feel the cold dissipating from my body."

  "Thanks, Tai Zhou. That was delicious."

  "He smiles, and leaves to clear the dishes."
