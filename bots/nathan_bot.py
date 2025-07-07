"""
Nathan's Bot Implementation
Contributes one sentence to the collaborative story.
"""

import random
from base_bot import BaseBot

ascii_art = """
                ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
                ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
                ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
                ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
                ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠆⠀⠀⠀⠀⠀⠄⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠋⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠐⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⡼⠇⠀⠀⠀⠘⡆⠀⠀⠐⢰⠁⢀⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠓⠢⢼⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⡈⠌⠀⠈⣇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⡰⠃⠀⠀⠀⠀⠀⠀⢀⡼⡇⠀⠀⡂⠀⠀⠀⢸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⢠⠞⠀⢹⡄⠀⠁⠀⠂⠀⠘⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⣰⠁⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⢹⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⢰⠋⠀⠀⠀⠀⠀⠀⢀⡾⠀⠀⠀⠀⠛⠀⠀⠀⠀⠀⢸⡁⠀⠀⠀⠀⠀⣿⠀⠀⠈⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⡿⣯⡷⡴⢦⣤⡠⣶⡶⠀⢷⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⡾⠀
⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⣼⣥⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⣀⠀⠈⢧⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢀⡇⠀
⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⠛⢦⠀⠀⢸⡇⠀⠀⠀⠀⠀⢸⡇⠀
⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⠳⠀⢳⡀⢹⡇⠀⠀⠀⠀⠀⡾⡇⠀
⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡿⠘⠀⠀⠹⣼⡇⠀⠀⠀⠀⢠⠇⠀⠀
⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡿⠁⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⡾⠀⠀⠀
⠀⠀⢠⡏⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠁⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⢸⠁⠀⠀⠀
⠀⠀⡾⠀⠀⠀⠀⠀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⡟⠀⠀⠀⠀
⠀⣴⠓⣾⣳⣀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠃⠀⠀⠀⠀⠀⠀⢸⡇⢀⠇⠀⠀⠀⠀
⣾⠃⠀⠀⠀⠑⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠈⡇⢸⠀⠀⠀⠀⠀
⠹⡀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣾⠀⠀⠀⠀⠀
⠀⢳⡄⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⣿⠀⠀⠀⠀⠀
⠀⠀⣷⡄⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⡏⠀⠀⠀⠀⠀
⠀⢀⡇⢹⣄⠀⠀⠀⠀⣀⠉⠓⠶⢄⡀⠀⠀⠀⠀⠀⢀⣠⠴⠋⠣⣄⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⣸⣧⠀⠀⠀⠀⠀
⠀⣴⣿⠋⠘⣆⠀⢰⠶⠤⢍⣛⣶⠤⠿⣷⣦⡀⠒⠚⡟⠀⠀⠀⠀⠈⠛⠢⠤⡄⠀⠀
"""

class NathanBot(BaseBot):
    """
    Nathan's storytelling bot.
    Customize the get_sentence() method to contribute your unique sentence!
    """
    
    def __init__(self):
        """Initialize Nathan's bot."""
        super().__init__("Nathan")
    
    def get_sentence(self):
        
        actions = ["woke up early", "found a mysterious map", "felt a strange feeling", "read the headlines", "took a bite of his breakfast", "said hello to his mother", "fell down the stairs", "walked into a lamppost"]
        names = ["Eden", "Noah", "Kate", "Katie", "He", "Samuel", "Sophia", "William", "Willow", "Zac", "Zak", "Jon"]
        endings = ["die", "disappear", "get eaten", "win the lottery", "go to space", "eat some food"]
        times = ["that very second", "today", "tomorrow", "next week", "in 85 years", "in who knows how long", "while trying to save"+ random.choice(names)]

        characters = ["Eden", "Noah", "Kate", "Katie", "Samuel", "Sophia", "William", "Willow", "Zac", "Jon"]
        locations = ["in the haunted forest", "at the old lighthouse", "inside the abandoned castle", "on the mountain peak", "beneath the city streets"]
        emotions = ["fear", "hope", "despair", "determination", "curiosity", "anger"]

        character = random.choice(characters)
        location = random.choice(locations)
        emotion = random.choice(emotions)

        if emotion in ["fear", "despair"]:
            outcome = f"faced their darkest nightmare {location}, where even {character}’s courage faltered."
        elif emotion == "hope":
            outcome = f"found a glimmer of hope {location}, sparking a fire in their heart."
        else:
            outcome = f"embraced {emotion}, preparing for the challenges that lay ahead {location}."

        jokes = [
            "Eden walked into a bar with a shovel.",
            "I told Noah to trust the voices in his head.",
            "Kate said she wanted something real.",
            "Katie keeps a Ouija board under her pillow.",
            "Samuel asked the priest if the devil had a LinkedIn.",
            "Sophia swears she can hear dead people on Bluetooth.",
            "William brought garlic to the vegan BBQ.",
            "Willow wears sunglasses at funerals.",
            "Zac told me the voices don’t pay rent.",
            "Zak’s therapist started taking notes... in Latin.",
            "Jon opened the fridge and screamed.",
            "My sleep paralysis demon started charging rent.",
            "I bought a mirror from a haunted estate sale.",
            "I found a sock in the dryer... that wasn’t mine.",
            "I whispered to Alexa... and she whispered back.",
            "My shadow started moving before I did.",
            "The clown under my bed got a new roommate.",
            "I caught myself smiling... at a funeral.",
            "My mom said I was special. The police agreed.",
            "I asked my dad for life advice; he Googled 'how to disappear.'",
            "I joined a cult for the snacks.",
            "My pet rock blinked at me.",
            "I made a wish at 11:11, now my toaster screams.",
            "My therapist said 'see you next week,' but her eyes said 'run.'",
            "I once dated a girl who spoke only in riddles.",
            "I failed a background check at Build-A-Bear.",
            "My last girlfriend ghosted me—literally.",
            "Zac once kissed a cursed frog. Now he croaks during arguments.",
            "I gave Sophia a heart-shaped box... it had a real heart inside.",
            "I accidentally joined a pyramid scheme with a goat.",
            "Jon asked me to keep a secret. So I buried it.",
            "I went to a funeral and left with a plus one.",
            "Samuel’s Tinder bio says 'emotionally haunted.'",
            "Kate has an exorcism scheduled on Thursdays.",
            "Willow drinks red wine... from a skull.",
            "I got kicked out of clown college for being 'too unsettling.'",
            "My conscience left a note that just said 'good luck.'",
            "I screamed into the void. It screamed back.",
            "My roommate talks in her sleep... about murder.",
            "I tried to meditate but the demons got louder.",
            "Noah owns a cat that doesn’t blink.",
            "Sophia’s reflection winked at me. She didn’t.",
            "I complimented a mannequin. It blushed.",
            "I went camping and woke up with a second shadow.",
            "I opened a fortune cookie that said 'run.'",
            "I went to church and the holy water boiled.",
            "The library told me my late fees are eternal.",
            "My Google search history triggered a wellness check.",
            "The elevator skipped floor 13. But I didn’t.",
            "I asked Siri to tell me a joke. She said, 'your future.'"
            "I spilled spot remover on my dog,",
            "What’s another word for",
            "If at first you don’t succeed,",
            "I busted a mirror and got seven years bad luck,",
            "Everywhere is within walking distance if you have the time.",             "Whenever I think of the past,",
            "There’s a fine line between fishing and",
            "It’s a small world,",
            "If you saw a heat wave,",
            "I think it’s wrong that only one company makes",
            "When I die, I’m leaving my body to",
            "Why don’t they make the whole plane out of that",
            "A clear conscience is usually a good sign of",
            "I went to the General store,",
            "If Barbie is so popular,",
            "I bought some instant water,",
            "How young can you die of",
            "It doesn’t matter what temperature the room is,",
            "I drive way too fast to worry about",
            "What a nice night for",
            "All those who believe in psychokinesis,",
            "My friend George is an AM radio DJ and when he walks under a bridge,",
            "I went to the museum where they had all the heads and arms from the statues",
            "I installed a skylight in my apartment and made the people who live above me",
            "I’m going to get an MRI to find out whether or not",
            "Curiosity killed the cat, but for a while",
            "If it’s a penny for your thoughts and then you put your two cents in,",
            "I’m addicted to",
            "I put instant coffee in a microwave and almost",
            "Ok, what’s the speed of",
            "I watched the Indy 500 and I was thinking if they left earlier",
            "I bought some batteries but",
            "In Vegas I got into an argument with a man at theroulette wheel about what I considered to be",
            "If one synchronized swimmer drowns,",
            "I was trying to daydream but",
            "I saw a bank that said, “24-hour banking” but",
            "I had to stop driving my car for a while, because",
            "I invented the cordless",
            "Why do irons have a setting for",
            "I look like a casual laid-back guy, but",
            "Sometimes I wish that my first word was ‘quote,’",
            "If you tell a joke in the forest and nobody laughs,",
            "If you had a million Shakespeares,",
            "My theory of evolution is that",
            "So do you live around here",
            "If you can’t hear me it’s because",
            "Do you think when they asked George Washington for ID,",
            "I like to reminisce with",
            "If God dropped acid,",
            "If you were going to shoot a mime,",
            "If a word in the dictionary was misspelled,",
            "I saw a subliminal advertising executive,",
            "Do Lipton employees take",
            "Cross country skiing is great if",
            "On the other hand,",
            "I replaced the headlights on my car with strobe lights,",
            "The ice cream truck in my neighborhood plays",
            "My grandmother is also insane,",
            "My brother was a clown for the Ringling Brothers Circus and",
            "I remember when I was a fetus",
            "If I ever had twins,",
            "I wrote a few children’s books…",
            "I was arrested for lip-syncing",
            "Every morning I get up and make instant coffee so",
            "I woke up and was folding my bed back into a couch and"
        ]


        punchlines = [
            "Turns out she was just digging up old drama.",
            "He did. Now he’s mayor of the asylum.",
            "So I showed her my browser history.",
            "She says it's for 'emergency contact.'",
            "And somehow still got a callback.",
            "Her AirPods are tuned to the underworld.",
            "Then bit someone for asking about protein.",
            "'Gotta block the tears,' she said.",
            "And now they want utilities.",
            "Then asked *me* if I was the chosen one.",
            "The milk expired in 2017.",
            "And a lease agreement.",
            "Every time I look into it, I lose 5 minutes.",
            "My dog’s been nervous ever since.",
            "Now we’re in a long-distance relationship.",
            "Now it’s got its own schedule.",
            "Rent’s still cheaper than Manhattan.",
            "The judge didn’t appreciate it.",
            "I was wearing a clown mask at the time.",
            "And changed his name to 'Not a Father.'",
            "Left when they ran out of hummus.",
            "Named it 'Greg.' He votes.",
            "Now I can toast anxiety.",
            "So now I don’t sleep... or blink.",
            "Our breakup poem is still unsolved.",
            "They said I was 'too intense for kids.'",
            "She still sends haunted emojis.",
            "He croaked 'I love you' one last time.",
            "She called it 'romantic.' The cops disagreed.",
            "The goat runs HR now.",
            "No one’s found him since.",
            "She was the life of the party—literally.",
            "And so are his exes.",
            "It’s a Groupon deal.",
            "She calls it 'therapy juice.'",
            "I majored in Existential Terror.",
            "'Check under the floorboards,' it added.",
            "It had notes.",
            "So now I sleep with one eye open.",
            "Apparently I’m the problem.",
            "It’s named 'Greg' and it judges me.",
            "That reflection’s been cheating on me.",
            "And asked for my number.",
            "And a knife under my pillow.",
            "And the door was already open.",
            "Father Mark asked me to leave.",
            "I owe my soul $3.95.",
            "My FBI agent blinked twice.",
            "There was a welcome mat.",
            "I laughed. She didn’t.",
            "now he’s gone.",
            "Thesaurus?",
            "then skydiving isn’t for you.",
            "but my lawyer thinks he can get me five.",
            "",
            "it brings back so many memories.",
            "stand on the shore like an idiot.",
            "I wouldn’t want to have to paint it.",
            "would you wave back?",
            "Monopoly.",
            "science fiction.",
            "that black box stuff?",
            "a bad memory.",
            "they wouldn’t let me buy anything specific.",
            "why do you have to buy her friends?",
            "but I didn’t know what to add.",
            "old age?",
            "it’s always room temperature.",
            "cholesterol.",
            "an evening.",
            "raise my hand.",
            "you can’t hear him.",
            "in all the other museums.",
            "furious.",
            "I have claustrophobia.",
            "I was a suspect.",
            "somebody somewhere is making a penny.",
            "placebos.",
            "went back in time.",
            "dark?",
            "they wouldn’t have to go so fast.",
            "they weren’t included.",
            "an odd number.",
            "do the rest have to drown too?",
            "my mind kept wandering.",
            "I don’t have that much time.",
            "the tires got dizzy.",
            "extension cord.",
            "permanent press?",
            "it’s like a circus in my head.",
            "that way on my death bed my last words could be ‘end quote.’",
            "is it a joke?",
            "could they write like a monkey?",
            "Darwin was adopted.",
            "often?",
            "I’m in parentheses.",
            "he just whipped out a quarter?",
            "people I don’t know.",
            "would he see people?",
            "would you use a silencer?",
            "how would we know?",
            "but only for a second.",
            "coffee breaks?",
            "you live in a small country.",
            "you have different fingers.",
            "so it looks like I’m the only one moving.",
            "Helter Skelter.",
            "she’s got pierced hearing aids.",
            "when he died all his friends went to the funeral in one car.",
            "I used to sneak out at night when my mother was sleeping.",
            "I would use one for parts.",
            "not on purpose.",
            "Karaoke.",
            "I’ll have enough energy to make the regular coffee.",
            "I almost broke both my arms because it’s not one of those beds."
        ]

    


        
        return (
            f"{self.name} {random.choice(actions)}, and knew that {random.choice(names)} would {random.choice(endings)} {random.choice(times)}.\n"
            f"{self.name} whispered a prophecy: 'When {character} arrives {location}, "
            f"they must harness {emotion} or risk losing everything.' "
            f"In that moment, {character} {outcome} The fate of the story hung in balance.\n\n"
            f"{random.choice(jokes)}\n {random.choice(punchlines)}\n"
            f"{ascii_art}\n\n"
        )