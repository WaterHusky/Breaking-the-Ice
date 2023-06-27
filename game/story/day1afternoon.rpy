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
  
  "The storm continued to rage outside, and I continued to lay in the bed that Tai Zhou had graciously provided. He mentioned he was busy with work, leaving me alone in the room."

  "The cabin lacked a TV, computer, or any form of recreational electronics for that matter so there wasn't much to do inside besides read a book or use my phone. And before I knew it, it was already mid afternoon."

  "Feeling rather lazy, I decided to go stretch my legs."

  "I walk back into the living room, seeing Tai Zhou standing with his feet apart on a thin, spongy mat. He wore a thin shirt that fit his muscular frame tightly, exposing his thick biceps."

  "I watched as he pointed his muzzle straight ahead and his arms moved in a slow, but controlled manner. I cough softly so as not to startle him."

  "“What are you doing?”"

  t neutral "Tai chi. It helps me relax."

  "“Well that seems like something I need right about now.” I said, taking a seat on the nearby sofa. He ignores me and carries on with his routine."

  "Tai Zhou carries on his routine for a bit, before turning to me."
  
  t neutral "Would you like to try it?"

  "I hesitated, not sure if I could do it, but his warm smile encouraged me to give it a shot."

  "“Sure, why not?” I replied, trying to sound confident. It looked pretty simple."

  "He made room for me on the mat, and I stood next to him. The mat felt soft under my feet as I copied his starting position, standing with my feet apart and looking straight ahead."

  t smiling "Take a deep breath and follow me."

  "He brought his hands together, before gradually lifting them upwards. I followed by swinging my arms sloppily, almost losing my balance. Turns out, it's not as easy as it looks."

  t neutral "Slowly. You want to relax, not complete the exercise."

  "I try again. My movements flow like a dead cow tumbling down a river."

  menu:
    "Could you show me how it's done?":
      #! +Physical
      t smiling "Here, let me help."
      
      "Tai Zhou steps over behind me and grips both of my wrists with his hands. While his strong grip was firm like a pair of cuffs, his fur was soft and I couldn't help but blush as I felt it brush against the length of my arms."

      t neutral "Now, move like this."

      "He brings my arms away from me with a controlled shift. His chest naturally leaned forward, and I could feel his body warmth press against my back."

      t concerned "Are you alright? You don't seem to be relaxed."

      "In all the distraction, I hadn't noticed that my heart started racing."

      menu:
        "I can't help it...":
          #! +Emotional

          "“Sorry, it's just that... I'm not used to being this close to someone.” I hadn't seen Johnny in three months, and even before that we hardly ever met in person."

          t neutral "Well, would you like me to stop?"

          "“It's okay, let's continue.”"

          t neutral "Now, like this."

          I stood helplessly as he effortlessly moved my arms.

          t neutral "Now, you try."

          "He let go, and I try to follow his movements without his help."

          t smiling "Much better."

          "Tai Zhou went through a few basic moves, guiding my arms and legs."
          
        "It's nothing.":
          "“It's nothing.” I mutter."

          t neutral "Okay, let's continue."

          "Tai Zhou went through a few basic moves, guiding my arms and legs. Eventually I got tired though, and went back to my seat. Tai Zhou nods in understanding, and carries on with his routine."

        "Let's just stop here.":
          "I say a few words about feeling unwell, but my speech came out as a low mumble."

          "I move back towards my seat. Tai Zhou nods in understanding, and carries on with his routine."

    "This is embarrassing...":
      "“Maybe I'll just sit out for now...”"

      "I move back towards my seat. Tai Zhou nods in understanding, and carries on with his routine."


