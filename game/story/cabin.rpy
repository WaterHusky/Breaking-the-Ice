# # Background
# black
# cabin_outside_night
# cabin_inside_night

# # Characters
# k = Konrad (tired)
# t = Tai Zhou (neutral, concerned, smiling)

label cabin:

    scene bg black

    "The trek feels like hours to my tired body, but we finally come to the cabin."

    show bg cabin_outside_night

    t neutral "We’re here!"

    "He opens the door and invites me in."

    show bg cabin_inside_night

    "The inside of the cabin is warm from the burning logs in the fireplace."

    "The leopard closes the door behind me. He sets down my belongings before taking off his winter coat and boots."

    show taizhou with dissolve

    t "Ah, much better."

    "I stand in the doorway. The leopard looks at me with a concerned look."

    t "Here, let me help you."

    "He takes off my coat and helps me out of my shoes. They’re wet from the snow, so he sets them aside to dry."

    hide taizhou with dissolve

    "He heads into another room. I hear the sound of wooden cupboards opening and closing."

    show taizhou with dissolve

    "He passes me a towel. It’s warm and fluffy."

    t "I got you a towel to dry yourself off. Then you can change into these."

    "He hands me a set of clothes."

    t "Might be a bit loose, given that these are meant for me. But it’ll work."

    "I have my own clothes, but it’s in my luggage. Opening it to get my clothes would take energy that I don’t have."

    t "And over there is the guest room."

    "He points to the room he was just in."

    t "I just gave it a quick wipe, so it might still be a bit dusty. Hopefully it’s enough for tonight."

    "I nod."

    k tired "{size=*0.4}Thank you…{/size}"

    t concerned "Hmm?"

    k "Thank you."

    t smiling "Ah, no problem."

    t "He pauses."

    t "Oh, before you head to bed, mind sharing your name?"

    k "Konrad."

    t neutral "Nice to meet you Konrad. I’m Tai Zhou."

    "Tai Zhou."

    "I nod in acknowledgement."

    hide taizhou with dissolve

    scene bg black

    "The rest of the night was a blur. My body ran on auto-pilot as I cleaned up and got changed."

    "I got in bed, snuggling up in the silky sheets and blanket. It’s warm and comforting."

    "Before I know it, I’m fast asleep."

    jump cabinMorning






    