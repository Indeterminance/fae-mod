default persistent._flatter_db = dict()

init -1 python in fae_flatter:

    import random
    import store

    COMPLIMENT_DEFS = dict()

    CUTE = 0
    ADORABLE = 1
    FUNNY = 2
    BEST_GIRL = 3

    prior_compliment = None

    def load_all_flatters():

        return store.Chat.chat_filt(
            COMPLIMENT_DEFS.values(),
            affection=store.Affection._getAffectionStatus(),
            unlocked=True
        )

label compliment_init:

    python:

        compliment_menu_items = [
            (_compliment.prompt, _compliment.label)
            for _compliment in fae_flatter.load_all_flatters()
        ]
        compliment_menu_items.sort()
    
    call screen neat_menu_scroll(compliment_menu_items, ("Nevermind.", None))

    if _return:
        $ ats(_return)
        jump cnc
    
    return


init 5 python:

    chatReg(
        Chat(
            persistent._flatter_db,
            prompt="I think you're best girl!",
            label="compliment_best_girl",
            unlocked=True,
            affection_range=(fae_affection.HAPPY, fae_affection.LOVE)
        ),
        chat_group=CHAT_GROUP_FLATTER
    )

label compliment_best_girl:
    if persistent.fae_compliment_best_girl:
        $ Affection.calculatedAffectionGain(3, bypass=False)
    else:
        $ Affection.calculatedAffectionGain(3, bypass=True)
    s abagcea "I'm the best girl? Aww, you're so sweet, [player]!" 
    s abagdka "I'm really happy you think so! It means a lot to me, ehehehe~" 
    s bbfclfc "After all, I always thought that I might be the least likable given the fact most would choose one of my friends over me, but..."
    pause 2.0
    if Affection.isAffectionate(higher=True):
        s abfbcqa "I'm glad you care so much about me! I love you, [player]~" 
    else:
        s abfbcqa "I'm glad you care so much about me!"
    $ persistent.fae_compliment_best_girl = True
    return 


init 5 python:

    chatReg(
        Chat(
            persistent._flatter_db,
            prompt="I think you're beautiful.",
            label="compliment_beautiful",
            unlocked=True
            #affection_range=(fae_affection.HAPPY, fae_affection.LOVE)
        ),
        chat_group=CHAT_GROUP_FLATTER
    )

label compliment_beautiful:
    if persistent.fae_compliment_beautiful:
        $ Affection.calculatedAffectionGain(3, bypass=False)
    else:
        $ Affection.calculatedAffectionGain(3, bypass=True)
    s abhfmkb "You think so, [player]? Aww, I don't know what to say, ehehehe~"
    s bbhfmebj "Especially since I'm pretty messy sometimes, ahahaha..."
    s abfccea "But that means so much to me coming from you, [player]!"
    if Affection.isAffectionate(higher=True):
        s abfcdqa "Remember that you're the most beautiful person in the world to me too!"
    $ persistent.fae_compliment_beautiful = True
    return 

init 5 python:

    chatReg(
        Chat(
            persistent._flatter_db,
            prompt="I think you're pretty.",
            label="compliment_pretty",
            unlocked=True,
            affection_range=(fae_affection.HAPPY, fae_affection.LOVE)
        ),
        chat_group=CHAT_GROUP_FLATTER
    )

label compliment_pretty:
    if persistent.fae_compliment_pretty:
        $ Affection.calculatedAffectionGain(3, bypass=False)
    else:
        $ Affection.calculatedAffectionGain(3, bypass=True)
    s abaacka "Aww [player], your words always flatter me~"
    s abaacoa "It makes me so happy knowing you think so!" 
    s abfcjoa "And I always think you're pretty too!" 
    $ persistent.fae_compliment_pretty = True
    return 

init 5 python:

    chatReg(
        Chat(
            persistent._flatter_db,
            prompt="I love your hair!",
            label="compliment_love_hair",
            unlocked=True
            #affection_range=(fae_affection.HAPPY, fae_affection.LOVE)
        ),
        chat_group=CHAT_GROUP_FLATTER
    )

label compliment_love_hair:
    if persistent.fae_compliment_love_hair:
        $ Affection.calculatedAffectionGain(3, bypass=False)
    else:
        $ Affection.calculatedAffectionGain(3, bypass=True)
    s ebaacqa "Ehehehe, even when it's a little messy? You're such a sweetheart, [player]~"
    s ebfcdoa "I hope you like my signature bow, too!"
    s abgcaoa "I think it fits my hairstyle, {w=0.5}{nw}"
    extend abfcaaa "don't you agree?"
    s abaaaka "Anyway, thanks for the compliment! It really means a lot to me." 
    $ persistent.fae_compliment_love_hair = True
    return 

init 5 python:

    chatReg(
        Chat(
            persistent._flatter_db,
            prompt="I love your eyes.",
            label="compliment_love_eyes",
            unlocked=True
            #affection_range=(fae_affection.HAPPY, fae_affection.LOVE)
        ),
        chat_group=CHAT_GROUP_FLATTER
    )

label compliment_love_eyes:
    if persistent.fae_compliment_love_eyes:
        $ Affection.calculatedAffectionGain(3, bypass=False)
    else:
        $ Affection.calculatedAffectionGain(3, bypass=True)
    s abhfkoa "Aww, I'm glad you think so, [player]!" 
    s abegikb "How about we have a staring contest then? Teehee~" 
    s abegmobj "Only kidding, of course! Unless that's something you're really interested in..."
    s abhfmabj "Ehehehe! Anyway..."
    s abbbkoa "I think blue suits me really well! It represents happiness and sensitivity, and I always try my best to connect with others in a positive way."
    s abbbcqa "And I think they make me unique and give me something to be confident about!"
    $ persistent.fae_compliment_love_eyes = True
    return 

init 5 python:

    chatReg(
        Chat(
            persistent._flatter_db,
            prompt="You're so kind...",
            label="compliment_kind",
            unlocked=True,
            affection_range=(fae_affection.HAPPY, fae_affection.LOVE)
        ),
        chat_group=CHAT_GROUP_FLATTER
    )

label compliment_kind:
    if persistent.fae_compliment_kind:
        $ Affection.calculatedAffectionGain(3, bypass=False)
    else:
        $ Affection.calculatedAffectionGain(3, bypass=True)
    s abhfcoa "Aww, you're so nice, [player]!"
    s abhfaka "I'm happy you think so! I always try to be welcoming and pleasant to others around me."
    s abbbcqa "And I think you're really kind too, {w=0.5}{nw}"
    extend abgccoa "you always make my days brighter with your company!"
    s abhfcka "I just want you to know that I really appreciate that."
    if Affection.isLove(higher=True):
        s "I love you so much, [player]~"
    $ persistent.fae_compliment_kind = True
    return 

init 5 python:

    chatReg(
        Chat(
            persistent._flatter_db,
            prompt="I look up to you.",
            label="compliment_look_up_to_you",
            unlocked=True,
            affection_range=(fae_affection.HAPPY, fae_affection.LOVE)
        ),
        chat_group=CHAT_GROUP_FLATTER
    )

label compliment_look_up_to_you:
    if persistent.fae_look_up_to_you:
        $ Affection.calculatedAffectionGain(3, bypass=False)
    else:
        $ Affection.calculatedAffectionGain(3, bypass=True)
    s abfbksa "You do? You look up to me? That's so kind of you, [player]!" 
    s bbfbmoaj "Honestly, I didn't expect to hear that from you. I always thought there were other people who are actually worth looking up to."
    s bbfblhaj "And I never really considered myself to be... that kind of person, I guess."
    s abfcaka "But the fact that I can be that someone for you makes it really special!" 
    s abaaloa "You're someone I look up to as well, {w=0.5}{nw}"
    extend bbaaiaa "you inspire and motivate me every single day."
    s abaacka "Thank you so much, [player]. It really means a lot to me." 
    $ persistent.fae_look_up_to_you = True
    return  

init 5 python:

    chatReg(
        Chat(
            persistent._flatter_db,
            prompt="I like seeing you happy.",
            label="compliment_like_seeing_happy",
            unlocked=True,
            affection_range=(fae_affection.HAPPY, fae_affection.LOVE)
        ),
        chat_group=CHAT_GROUP_FLATTER
    )

label compliment_like_seeing_happy:
    if persistent.fae_like_seeing_happy:
        $ Affection.calculatedAffectionGain(3, bypass=False)
    else:
        $ Affection.calculatedAffectionGain(3, bypass=True)
    s abhfcka "Aww! That's so cute of you to say, [player]! Thank you so much!" 
    s ebbckea "I am {i}happy{/i} to make you {i}happy{/i} when you see me {i}happy{/i}, ehehehe~"
    s ebbbcka "I like seeing you happy as well! It makes all the time we spend together worth it."
    $ persitent.fae_like_seeing_happy = True
    return

init 5 python:

    chatReg(
        Chat(
            persistent._flatter_db,
            prompt="Thanks for being here for me.",
            label="compliment_thank_for_being_here",
            unlocked=True,
            affection_range=(fae_affection.HAPPY, fae_affection.LOVE)
        ),
        chat_group=CHAT_GROUP_FLATTER
    )

label compliment_thank_for_being_here:
    if persistent.fae_compliment_thank_for_being_here:
        $ Affection.calculatedAffectionGain(3, bypass=False)
    else:
        $ Affection.calculatedAffectionGain(3, bypass=True)
    s ebbbcka "Of course, [player]! I'll always be here for you when you need me!" 
    s abhfaoa "And thank you for being here for me too, it means a lot to me."
    s abbcmoaj "You know, you've done so much to help me and you've always been by my side, {w=0.5}{nw}"
    extend bbbciaa "despite everything that happened..."
    s abaacaa "And I really can't thank you enough for that."
    if Affection.isLove(higher=True):
        s "I love you so much, [player]." 
    $ persistent.fae_compliment_thank_for_being_here = True
    return  

init 5 python:

    chatReg(
        Chat(
            persistent._flatter_db,
            prompt="I like your writing.",
            label="compliment_like_your_writing",
            unlocked=True,
            affection_range=(fae_affection.HAPPY, fae_affection.LOVE)
        ),
        chat_group=CHAT_GROUP_FLATTER
    )

label compliment_like_your_writing:
    if persistent.fae_compliment_like_your_writing:
        $ Affection.calculatedAffectionGain(3, bypass=False)
    else:
        $ Affection.calculatedAffectionGain(3, bypass=True)
    s abaanea "Aww, that means a lot to me, [player]! Thank you so much!"
    s abaamoaj "You know, since there isn't much else for me to do in here, I try to put a lot of effort into my poetry..."
    s abbbmhaj "Sometimes it's hard for me to think of what to write, {w=0.5}{nw}"
    extend bbbbaaaj "or I get a bit too insecure about my abilities..."
    s abbbcka "But if you really look forward to seeing my creations, I think it's worth it!"
    s abbbksa "Do you write, [player]? I'd love to see your work someday if you do!"
    s abhfcka "I'm sure you can write some amazing things too, ehehehe~"
    $ persistent.fae_compliment_like_your_writing = True
    return

init 5 python:

    chatReg(
        Chat(
            persistent._flatter_db,
            prompt="You're a ball of sunshine!",
            label="compliment_ball_of_sunshine",
            unlocked=True,
            affection_range=(fae_affection.HAPPY, fae_affection.LOVE)
        ),
        chat_group=CHAT_GROUP_FLATTER
    )

label compliment_ball_of_sunshine:
    if persistent.fae_compliment_ball_of_sunshine:
        $ Affection.calculatedAffectionGain(3, bypass=False)
    else:
        $ Affection.calculatedAffectionGain(3, bypass=True)
    s abgccea "[player]! That was so cute!"
    s abbcnka "Thank you! I hope I can continue making you happy, and brightening up your days, {w=0.5}{nw}"
    extend abgccaa "just like you do for me!"
    s abaacqa "Ehehehe~"
    $ persistent.fae_compliment_ball_of_sunshine = True
    return
