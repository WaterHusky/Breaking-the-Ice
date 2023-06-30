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
    
    "It's getting late."

    "Being stuck in a cabin for three days isn't something I envisioned for my trip here, but Tai Zhou's company has been amazing."

    "Tai Zhou peers out of the window."

    t "Looks like the weather is clearing up! With any luck, we'll be able to explore the outside tomorrow."

    k "Hopefully. I need to catch my flight back."

    t dismayed "Wait, when is it?"

    k "Tomorrow morning."

    t "Ah…"

    k "Is everything okay?"

    t "Well, I thought we'd have longer to hang out. I want to show you the beautiful spots around here."

    jump ending_evening


label ending_evening:
    if success_emotional:
        # They have a heart-to-heart talk about where their friendship is going to go
        call ending_evening_emotional
    elif success_intellectual:
        # They have a talk about life and the philosophy of goodbyes
        call ending_evening_intellectual
    elif success_physical:
        # Instead of chatting, Tai Zhou eases them into the bedroom scene
        call ending_evening_physical
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

    "The outside air blah blah TODO"

    # beautiful outside, air is fresh, everything feels brighter and vibrant
    # feels surreal. different from just when it's on the other side of the window pane
    # The only time he's been outside was when he was tired after his first night here
    # Konrad plays around for a bit.

    if success_emotional:
        # Tai Zhou doesn't follow Konrad to the airport
        call ending_leaving_follow
    else:
        # Tai Zhou follows Konrad to the airport
        call ending_leaving_nofollow

    jump ending_reflection


label ending_reflection:
    if success_physical and success_intellectual and success_emotional:
        # if physical+intellectual+emotional, promise to take the time to recover, and then come back to Tai Zhou when he's ready for a relationship
        call ending_reflection_best
    elif success_physical and success_emotional:
        # if physical+emotional, they chat after Konrad returns to his life, and Konrad looks forward to visiting again, imagining their bodies against each other
        call ending_reflection_physical_emotional
    elif  (success_intellectual and success_emotional) or (success_emotional):
        # if intellectual+emotional or emotional, they become good friends
        call ending_reflection_emotional
    elif (success_physical and success_intellectual) or (success_physical or success_intellectual):
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

    # They talk about philosophy about leaving or something

    return

label ending_evening_emotional:
    # Possibilities: emotional = true

    # They talk about where to go from here

    return

label ending_evening_physical:
    # Possibilities: emotional = false, intellectual = false, physical = true

    # Tai Zhou transitions into moving into the bedroom

    t smiling "Well, I know what we can do instead."

    "Tai Zhou takes a step towards me."

    k "What are you thinking of—"

    k "He places"

    return

label ending_evening_bad:
    # Possibilities: emotional = false, intellectual = false, physical = false

    # Awkward evening

    return


# ============================
# ===== Bedroom sections =====
# ============================

label ending_bedroom_physical:
    # Possibilities: physical = true

    # Story
    # if they had a convo before, transition to physical


    show bg black

    # Exposition before falling asleep

    show bg cabin_inside_day

    # Wake up and see Tai Zhou in bed

    return

label ending_bedroom_bad:
    # Possibilities: physical = false

    # Story
    # if they had a convo before, transition to going to bed

    show bg black

    # Exposition before falling asleep

    show bg cabin_inside_day

    # Wake up and see Tai Zhou greeting him in the living room

    return


# ============================
# ===== Leaving sections =====
# ============================

label ending_leaving_nofollow:
    # Condition: emotional = false

    # Tai Zhou doesn't accompany Konrad to the airport.
    # If physical = true, Tai Zhou says that they should meet again when he returns *winks
    # If intellectual = true and physical = false, Tai Zhou sees them as friends and promises to stay in touch

    return

label ending_leaving_follow:
    # Condition: emotional = true

    return

# ===============================
# ===== Reflection sections =====
# ===============================

label ending_reflection_best:
    # Condition: all 3 traits
    # They promise to take the time to recover, and then come back to Tai Zhou when he's ready for a relationship
    return


label ending_reflection_physical_emotional:
    # Condition: physical AND emotional
    # They chat after Konrad returns to his life, and Konrad looks forward to visiting again, imagining their bodies against each other
    
    return


label ending_reflection_emotional:
    # Condition: emotional (intellectual is optional)
    # They become good friends
    
    return


label ending_reflection_physical_intellectual:
    # Condition: physical, intellectual, or both
    # They chat for a while, but it trails off, and life goes on 
    
    return


label ending_reflection_bad:
    # Condition: all traits failed
    # Konrad moves on and eventually forgets about Tai Zhou
   
    return




