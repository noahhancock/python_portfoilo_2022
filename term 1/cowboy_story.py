from time import sleep

print("""
     __________     ________   _____    ___ ____________               ___________   ___________   __        __
     | |_____  \   /  ____  \  |    \   | | |  _________|              |  |_____  \  |  |______ \  \ \      / /
     | |     |  | |  /    \  | |     \  | | |  |                       |  |     \  | |  |______| |  \ \    / /
     | |____/  /  | |      | | |  |\  \ | | |  |________               |  |      | | |  |     __/    \ \__/ /
     | |____  |   | |      | | |  | \  \| | |   ________|              |  |      | | |  |__  \        \    /
     | |    \  \  | |      | | |  |  \    | |  |                       |  |      | | |  |  \  \        |  |
     | |_____|  | |  \____/  | |  |   \   | |  |________               |  |_____/  | |  |   \  \       |  |
     |_|_______/   \________/  |__|    \__| |___________|              |__|_______/  |__|    \__\      |__|


                        __________  ___      ___ ____           __________  ____    ____
                       /   _______| | |      | | |  |          /   _______| |  |    |  |
                       |  /         | |      | | |  |          |  |         |  |    |  |
                       | |          | |      | | |  |          |  |         |  |____|  |
                       | |     __   | |      | | |  |          |  |         |  ______  |
                       | |     \ \  | |      | | |  |          |  |         |  |    |  |
                       |  \_____| | |  \____/  | |  |________  |  |_______  |  |    |  |
                       \__________/ \__________/ |___________| \__________| |__|    |__|
""")
userName = input("Enter your name: ")
#story setup
def intro():
    sleep(0.5)
    print("""
    Your cousin has written to you saying
that he is in dire need of help. He hasn’t
specified what he needs help with, but you
oblige. He lives in a town in the middle of
the desert. You decided to bring 20 dollars
and a pistol. You need a way to get there,
but you need to decide whether to go by horse
or by train.
""")
    sleep(0.3)
    input("\nPress the enter key to continue.\n")
    sleep(0.5)
    print("1: [Go by horse]")
    sleep(0.5)
    print("2: [Go by train]\n")
    sleep(0.2)
    while True:      
        choice1 = input("Enter your choice (1 or 2): ")
        if choice1 == "1":
            sleep(0.5)
            print("\nYou decided to go by horse.\n")
            horse()
            break
        elif choice1 == "2":
            sleep(0.5)
            print("\nYou decided to go by train.\n")
            train()
            break
        else:
            sleep(0.5)
            print("\nThat was not a valid choice.\n")
def train():
    print("""
	The train running to Bone Dry Gulch wasn’t exactly known for being safe.
It was mainly used for carrying freight, but occasionally carried passengers.
Today was a busier day than usual, with the train carrying upwards of 30 passengers.
You knew this route was infamous for being robbed, but you felt safer since
there were more passengers, therefore more people to fend off the bandits.
You went to grab tickets at the nearest opportunity. 
As you boarded the train, dread still hung in the air despite your previous reasoning.
You could still go by horse if you really wanted to.""")
    sleep(0.3)
    input("\nPress the enter key to continue.\n")
    sleep(0.5)
    print("1: [Continue on train]")
    sleep(0.5)
    print("2: [Abandon and go by horse]\n")
    sleep(0.2)
    while True:      
        choice1 = input("Enter your choice (1 or 2): ")
        if choice1 == "1":
            sleep(0.5)
            print("\nYou continue by train\n")
            board()
            break
        elif choice1 == "2":
            sleep(0.5)
            print("\nYou Leave the train and go by horse\n")
            abandon()
            break
        else:
            sleep(0.5)
            print("\nThat was not a valid choice.\n")
def abandon():
    print("""Your hunch caused you to abandon the train and instead go by horse alone. You saddle up
and ride West, towards Bone Dry Gulch.

As you ride, you notice some small shadowy shapes in the distance. If your hunch was
correct, these would have to be bandits attempting to rob the very train you were about to
board earlier. As you get closer, you see their guns shining in the sun. Your suspicions
were correct.""")
    sleep(0.5)
    decline_abandon()
#train storyline
def board():
    print("""
           ___  ,--------,
         ///|\\\:________|
         \-----/|  .--. |
          \   / |  |  | |
       --,_._,__|  '--' |
      |  | |:|          |
      c  | |:|   .--.   |
      |  | |:|  /    \  |
     //| .-.   :  ()  :_|
    ///|-(O=====\==' /--'
----------*------*--*----------
""")
    print("""Despite your fears, you push on and board the train. It seems like you’ll be 
  quite comfortable here. The seats are plush, each having a small pillow in case you fell asleep.
You take your seat, and begin to drift off.
SLAM!
You suddenly awake to an extremely loud sound. You look around in fear and panic, 
unknowing of its source. As you look around, it becomes clear that the sound came from
the opposite train car. You, suspecting an attack at any moment, rest your hand on your pistol,
hoping that it was just an accident and not something worse. As you listen, 
booming footsteps come from the other train car. You barely have any time to prepare, 
but you come up with several ideas to avoid being robbed in case those footsteps were from thieving bandits.""")
    sleep(0.3)
    input("\nPress the enter key to continue.\n")
    sleep(0.5)
    print("\n1: [Pretend to be asleep]")
    sleep(0.5)
    print("2: [Pull out gun]")
    sleep(0.2)
    while True:
        conchoice = input("\nEnter your choice (1 or 2): ")
        if conchoice == "1":
            sleep(0.5)
            print("\nYou decided to pretend to be asleep.\n")
            asleep()
            break
        elif conchoice == "2":
            sleep(0.5)
            print("\nYou decided to pull out your gun.\n")
            gun()
            break
        else:
            sleep(0.5)
            print("\nThat was not a valid choice.\n")
def asleep():
    print("""You promptly close your eyes and slump over, pretending you’re asleep. Following
another large door slam, this time much closer, groups of footsteps pour into your train
car, one yelling, 

“We’re gonna need all your money, or else! Pocket watches, cash, cool hats-- Anything
worth anything is goin’ in this bag!”

Bandits.
You recognize the voice as someone you knew. An old friend who you haven't seen in
years. Someone familiar who you’ve completely forgotten existed.

The footsteps start coming closer to you. You panic, but keep up your ruse. The bandit
stops right next to your seat. 

“Peek-a-boo.”

BAM!""")
    sleep(0.3)
    input("\nPress the enter key to continue.\n")
    sleep(0.5)
    print("END")
def gun():
    print("""You pull out your pistol in anticipation of a robbery. Following another large door slam,
this time much closer, a group of mean-looking men pour into your train car, one yelling, 

“We’re gonna need all your money, or else! Pocket watches, cash, cool hats-- Anything
worth anything is goin’ in this bag!”

Bandits.
You recognize the voice as someone you knew. An old friend who you haven't seen in
years. Someone familiar who you’ve completely forgotten existed.

Your moment of hesitation is quickly over, however, as the bandits begin violently
attacking anyone in the train car who wouldn’t comply. You subtly begin to aim towards
one of the criminals. In one quick shot, the man is down, and everyone in the train car
looks at you in shock. In that move, the entire train car becomes a gunfight. Bullets
ricochet off of every corner, every metal table leg, every person. Windows are broken,
people are down, and you’re crouching in the corner fending off anyone who comes your
way. After the dust clears, the coach becomes silent again. You scan the car, and find that
the entire posse has fled.

You blink in surprise. You had just fended off an entire group of bandits.""")
#horse storyline
def horse():
    sleep(0.5)
    print("""
          ,,
         /(-\
    ,---' /`-'
   /( )__))
_ /_//___\\___

    ``    ``""")
    print("""
	You choose to go by horse because it is safer
in the long run. While going on the trail to your cousin
you meet some old friends of yours.
“Hey old friend of mine. I heard your cousin needs some
help down at the town.”
“Yeah he does. Why do you ask?”
“ Oh we are heading the same way. Going to have some fun
with the train going by there. Want to come with us?
""")
    sleep(0.3)
    input("\nPress the enter key to continue.\n")
    sleep(0.5)
    print("1: ""Yeah, I'll go with you.""\n")
    sleep(0.5)
    print("2: ""No, I'd rather go alone.""\n")
    sleep(0.2)
    while True:
        choice2 = input("Enter your choice (1 or 2): ")
        if choice2 == "1":
            result1 = 1
            sleep(0.5)
            print("\nYou decided to head with your old friends.\n")
            bandit()
            break
        elif choice2 == "2":
            sleep(0.5)
            print("\nYou decided to keep on going alone.\n")
            decline()
            break
        else:
            sleep(0.5)
            print("\nThat was not a valid choice.\n")
#alone story
def decline():
    print("""“Yeah, I’m not up for that sort of thing.”
“Suit yourself.”

You saddle up and leave your pals in the dust. As you ride, you start to doubt your
decision. You start getting thirsty, but you are almost completely out of water. You get off
to sit and rest in the sand by your horse for a long while.

As you’re resting, you notice your pals far off in the distance making good time. You start
to wonder if it’s worth it to go after them to prevent their mischievous deeds.
You mount your horse and continue your long ride.""")
    sleep(0.5)
    decline_abandon()
def decline_abandon():
    print("""You want to confront the bandits, and perhaps bring them to justice, but you know such
an action would be quite risky. You could also just steer clear and hope they don’t see you,
but that’s also risky.""")
    sleep(0.3)
    input("\nPress the enter key to continue.")
    sleep(0.5)
    print("\n1: [Confront bandits]")
    sleep(0.5)
    print("2: [Steer clear]\n")
    sleep(0.2)
    while True:
        selfchoice = input("Enter your choice (1 or 2): ")
        if selfchoice == "1":
            sleep(0.5)
            print("\nYou decided to confront the bandits.\n")
            confront()
            break
        elif selfchoice == "2":
            sleep(0.5)
            print("\nYou decided to steer clear of the bandits.\n")
            clear()
            break
        else:
            print("That was not a valid choice.")
def confront():
    print("""   You start riding towards the bandits at top speed, dust flowing behind your horse. The
train is in sight, with the thieves trailing behind. You quickly draw your pistol, and begin
firing at them, each shot ringing in your ears.

“What ‘n tarnation!?”

The bandits scattered from their formation, clearly panicked. Soon, however, the bandits
begin firing back. With the train between you and them, you begin to shoot between the
cars at the bandits on the other side. You shoot three more shots, two of which hit their
target, causing two of the three bandits to crash violently off of their horses onto the
ground. With only one ruffian left, you turn to fire your last shot into his noggin.

But it was too late.

The last bandit had fired a shot straight through your back, causing you to crumple onto
the rough desert terrain, dead.""")
    sleep(0.3)
    input("\nPress enter to continue.\n")
    sleep(0.5)
    print("END")
def clear():
    print("""   You completely ignore the bandits, as their actions, no matter how cruel, wouldn’t affect
you if you didn’t interfere. As you let the train travel over the horizon, you sigh. You
probably just avoided something terrible.


As you finally arrive in Bone Dry Gulch, tired as can be, your cousin greets you with a
friendly smile. 

“Hey partner! Glad you got here safely.”

You sit in silence, relieved, and finally done with your escapades.""")
    sleep(0.3)
    input("\nPress enter to continue.\n")
    sleep(0.5)
    print("END")
#bandit storyline
def bandit():
    sleep(0.5)
    print("""
    /\/\
    |  |
\\__|__|__//
   | - -|
   | _\ |
   \____/""")
    print("""
“Yeah, sounds fun. I’ll go with you.”
“Great. Now let’s go rob this train.”

You and the group of bandits ride on for a couple hours.
While the bandits are resting, Richard tells you what the plan is.

“After the train leaves we will chase at a safe distance for a
little while. Then we have the 3 groups split up. The first group,
led by yours truly, will gather donations from the passengers as
our second group, led by Joe, attacks the conductor and stop the train.
The third group, headed by Jesse will make sure no one will come
and mess this up.”

You agree to the plan and ask what group you will be in.
“Well, which group do you want to go with?”

    """)
    sleep(0.3)
    input("\nPress the enter key to continue.\n")
    sleep(0.5)
    print("1: [Go with Richard]")
    sleep(0.5)
    print("2: [Go with Joe]")
    sleep(0.5)
    print("3: [Go with Jesse]")
    sleep(0.2)
    while True:
        choice3 = input("\nEnter your choice (1, 2, or 3): ")
        if choice3 == "1":
            sleep(0.5)
            print("\nYou decided to go with Richard.\n")
            richard()
            break
        elif choice3 == "2":
            sleep(0.5)
            print("\nYou decided to go with Joe.\n")
            joe()
            break
        elif choice3 == "3":
            sleep(0.5)
            print("\nYou decided to go with Jesse.\n")
            jesse()
            break
        else:
            sleep(0.5)
            print("\nThat was not a valid choice.\n")
def richard():
	sleep(0.5)
	print("""
    /\/\
    | R|
\\__|__|__//
   | - -|
   | _\ |
   \____/""")
	print("I'll go with you, Rich.")
	print("Good choice.")
	print("""
	The bandits break up camp. You go off with group 1 to ride close to
the train without being seen. When you get the signal from group 2 that
they are ready to ride, you get closer to the train. As you get closer,
you hear screams from the passengers as they spot you. The train is
starting to slow and you let out a whoop of joy as it stops. Richard steps
off his horse and you closely follow. Richard goes in first and gives his
speech on robbing and cooperating. Everyong is scared and no one causes trouble.
You run off with the bandits and a lot of money.""")
def joe():
	sleep(0.5)
	print("""
    /\/\
    | J|
\\__|__|__//
   | - -|
   | _\ |
   \____/""")
	print("I'll go with you, Joe.")
	print("Okay, have fun stopping a train.")
	print("""
	You and the rest of Joe's group breaks off before camp is broken down to be by
the front of the train. When you get the signal to move into action and jump on the
train, the conductors try to fight back. However, they are overwhelmed by the sheer
numbers of you group. After you slow the train down you wait and watch as Richard robs
the train passengers. When the bandits regroup, they split up the money and let you
continue on your way to your cousin.""")
def jesse():
	sleep(0.5)
	print("""
    /\/\
    |Je|
\\__|__|__//
   | - -|
   | _\ |
   \____/""")
	print("Jesse looks like he needs more people. I'll go with him.")
	print("Whatever you say.")
	print("""
	Your group does most of the breaking up of camp because of the fact that your group
is the last one to leave. You get the signal from Richard's group and spread out around
the back and sides watching for cops. Sadly for you, no cops came to give the robbery
any trouble. After what felt like forever, you leave the train with the bandits, hoping
to get a bigger share of the money then you fear you will get. You get a decent share, 
but not as big as others because you didn't do much.""")

intro()
