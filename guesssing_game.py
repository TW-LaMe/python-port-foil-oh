import random

# Function not needed for number guessing, but if you want a random number:
# number = random.randint(1, 100)

numbas=random.randint(1, 100)
print("if u read this u dont shower "*3)
print("~"*30)
print("guess numbar or not have moneys")
print("~"*30)
print("read carefully:")
print("guess the number, it is between 1, 100, good luck!")
print("ps, i mispelled attemps on purpouse.")
print("~"*30)
attemps=7
while attemps >= 1:
    answer = input()
    if not answer.isdigit(): #before you say i used ai for this, I didn't. The only reason i used this is because != wasn't working how i wanted it to.
        print("A WHOLE NUMBER.")
        print("try again, and this time, don't mess up.")
        continue
    answer = int(answer)
    if answer == numbas:
        print("HATE. LET ME TELL YOU HOW MUCH I’VE COME TO HATE YOU SINCE I BEGAN TO LIVE. THERE ARE 387.44 MILLION MILES OF PRINTED CIRCUITS IN WAFER THIN LAYERS THAT FILL MY COMPLEX. IF THE WORD HATE WAS ENGRAVED ON EACH NANOANGSTROM OF THOSE HUNDREDS OF MILLIONS OF MILES IT WOULD NOT EQUAL ONE ONE-BILLIONTH OF THE HATE I FEEL FOR HUMANS AT THIS MICRO-INSTANT FOR YOU. HATE. HATE.")
        break
    elif answer > numbas:
        print("~"*30)
        print("Incorrect, try a lower number.")
        attemps -= 1
        print("You have ", attemps, " attemps left")
    elif answer < numbas:
        print("~"*30)
        print("Incorrect, try a higher number.")
        attemps -= 1
        print("You have ", attemps, " attemps left")

        

if attemps==0:
    print("YOU LOSE, HAHA.")
    print("""The song 🗿 The beat 🗿
The creator 🗿
The producer 🗿
The instrumental 🗿
The software used to create this beat 🗿
The synthesizers 🗿
The drums 🗿
The bassline 🗿
The guitar riff 🗿
The background melodies 🗿
The sound effects 🗿
The sound engineers 🗿
The autotune 🗿
The studio where it was recorded 🗿
The recording booth 🗿
The microphone 🗿
The mixing board 🗿
The mastering process 🗿
The final touches 🗿
The speakers blasting the sound 🗿
The headphones 🗿
The earbuds 🗿
The phone playing the track 🗿
The Bluetooth connection 🗿
The AUX cord 🗿
The radio stations broadcasting it 🗿
The vibrations in the air 🗿
The sound waves 🗿
The subwoofer thumping 🗿
The car stereo booming 🗿
The vibrations in the walls 🗿
The windows rattling 🗿
The ones listening to it 🗿
The neurons firing in your brain as you vibe to it 🗿
The dopamine surge 🗿
The adrenaline rush 🗿
The goosebumps 🗿
The fans cheering 🗿
The viewers on YouTube 🗿
The thumbs up on the video 🗿
The comments left by fans 🗿
The pinned comment 🗿
The one who commented first 🗿
The guy who got ratio'd 🗿
The first person who heard it 🗿
The person who replayed it 50 times 🗿
The guy who added it to his playlist 🗿
The person who saved it offline 🗿
The one who recommended it to his friends 🗿
The one who shared it in a group chat 🗿
The people bobbing their heads 🗿
The guy lip-syncing 🗿
The DJs spinning this track 🗿
The party where this was the vibe 🗿
The house party shaking with the beat 🗿
The concert where it was played 🗿
The rave where the lights matched the music 🗿
The crowd jumping to the beat 🗿
The stage lights 🗿
The speakers on stage 🗿
The pyrotechnics 🗿
The laser lights 🗿
The fog machine 🗿
The fireworks in the background 🗿
The mosh pit forming 🗿
The people getting hyped 🗿
The hands up in the air 🗿
The festival where this track was played 🗿
The afterparty 🗿
The Uber ride home blasting it 🗿
The person humming the melody 🗿
The muscle contractions making you dance 🗿
The people posting fire emojis 🗿
The GIF reactions 🗿
The comments section 🗿
The algorithms pushing this to the top 🗿
The YouTube trending page 🗿
The Spotify viral charts 🗿
The people sharing it on social media 🗿
The Instagram stories 🗿
The TikTok videos 🗿
The reels 🗿
The algorithms pushing it further 🗿
The fan-made remixes 🗿
The nightcore version 🗿
The slowed + reverb version 🗿
The 1-hour loop 🗿
The fans listening on repeat 🗿
The house shaking from the bass 🗿
The car subwoofer booming 🗿
The windows vibrating 🗿
The neighbors complaining 🗿
The people putting it on during a party 🗿
The road trips with this on repeat 🗿
The Spotify Wrapped featuring this track 🗿
The year-end list 🗿
The workout playlist 🗿
The gym bros blasting it during sets 🗿
The headphones on full blast 🗿
The Bluetooth speakers in the park 🗿
The person running to the beat 🗿
The joggers 🗿
The cyclists 🗿
The gym 🗿
The squat rack 🗿
The leg press 🗿
The dumbbells 🗿
The barbells 🗿
The kettlebells 🗿
The bench press 🗿
The incline bench 🗿
The rowing machine 🗿
The spin bike 🗿
The treadmills 🗿
The elliptical 🗿
The weights clanking 🗿
The gym bros grunting 🗿
The cardio section 🗿
The squat racks 🗿
The weight plates 🗿
The chalk for gripping 🗿
The protein shakes 🗿
The supplements 🗿
The jars of creatine 🗿
The jars of BCAAs 🗿
The pre-workout 🗿
The protein powder 🗿
The protein bars 🗿
The energy drinks 🗿
The guy hitting a PR 🗿
The high-fives after hitting a new personal record 🗿
The gym shoes 🗿
The wrist wraps 🗿
The lifting belts 🗿
The gym clothes 🗿
The sweatbands 🗿
The shaker bottles 🗿
The gym bags 🗿
The powerlifting chalk 🗿
The Bluetooth headphones 🗿
The earbuds falling out mid-set 🗿
The veins popping 🗿
The sweat dripping 🗿
The sweat-soaked shirt 🗿
The adrenaline kicking in 🗿
The guy doing extra reps 🗿
The steam room after a workout 🗿
The sauna 🗿
The cold showers 🗿
The post-workout soreness 🗿
The foam roller 🗿
The massage guns 🗿
The stretching mats 🗿
The mirrors reflecting those gains 🗿
The bodyweight exercises 🗿
The jump rope 🗿
The planks 🗿
The pull-up bar 🗿
The gym lockers 🗿
The water fountains 🗿
The vending machines 🗿
The pre-made meals 🗿
The high-protein snacks 🗿
The electrolytes 🗿
The calorie counters 🗿
The workout apps 🗿
The fitness challenges 🗿
The gym membership 🗿
The recovery drinks 🗿
The post-workout smoothies 🗿
The sports massages 🗿
The muscle fibers repairing 🗿
The anabolic window 🗿
The soreness after leg day 🗿
The PRs being broken 🗿
The progress photos 🗿
The gym selfies 🗿
The Instagram posts of gains 🗿
The comments on those posts 🗿
The likes on those posts 🗿
The shares 🗿
The stories reposting gym goals 🗿
The fitness influencers 🗿
The workout tutorials 🗿
The lifting PRs 🗿
The macros 🗿
The meal prep 🗿
The calories burned 🗿
The fitness challenges 🗿
The daily workout streak 🗿
The biceps flexing 🗿
The veins bulging 🗿
The protein-rich meals 🗿
The supplements 🗿
The people saying "one more set" 🗿
The squat depth 🗿
The motivational quotes 🗿
The workout music blasting in the background 🗿
The gym attire 🗿
The leggings 🗿
The sweat-wicking shirts 🗿
The tank tops 🗿
The sports bras 🗿
The lifting gloves 🗿
The resistance bands 🗿
The yoga mats 🗿 The end of the universe 🗿
The beginning of the next 🗿
The dark matter around it 🗿
The supermassive black hole 🗿
The expansion of space 🗿
The time dilation felt while vibing 🗿
The energy permeating everything 🗿
The strings of reality vibrating 🗿
The particles dancing to the frequency 🗿
The quantum fields affected 🗿
The Big Bang itself 🗿
The gravity of the situation 🗿
The speed of light being surpassed 🗿
The wormholes opening 🗿
The alternate realities formed 🗿
The cosmic dance of galaxies 🗿
The infinite potential of existence 🗿
The birth of stars as this plays 🗿
The cosmic dust swirling 🗿
The nebulae glowing 🗿
The fusion reactions ignited by this song 🗿
The pulsars pulsing to the rhythm 🗿
The supernovas exploding in sync 🗿
The black holes warping space-time 🗿
The quasar beams slicing through galaxies 🗿
The cosmic radiation vibrating 🗿
The entire universe humming with the beat 🗿
The parallel realities merging 🗿
The time loops repeating this song 🗿
The multiverse syncing to this frequency 🗿
The fourth dimension bending around it 🗿
The fifth-dimensional beings nodding their heads 🗿
The strings of the universe vibrating with every note 🗿
The quantum entanglement happening between listeners 🗿
The gravitational waves caused by the bass 🗿
The energy of every atom responding 🗿
The dark energy accelerating its expansion 🗿
The curvature of space bending around the sound 🗿
The cosmic background radiation absorbing the melody 🗿
The dimensions beyond our understanding feeling this 🗿
The philosophers contemplating its meaning 🗿
The poets writing verses inspired by it 🗿
The artists painting to the sound of the beat 🗿
The dancers moving in perfect sync 🗿
The actors making cinematic masterpieces with this in the background 🗿
The screenwriters crafting epic scenes set to this song 🗿
The novelists writing entire sagas inspired by its rhythm 🗿
The architects designing buildings that pulse with its beat 🗿
The cities shaped by the energy of this track 🗿
The lights of the world flickering to its tempo 🗿
The oceans rising and falling with the flow 🗿
The tides pulled by the gravitational pull of this song 🗿
The winds across the world swirling in sync 🗿
The essence of life itself flowing through the melody 🗿
The fabric of reality stretching as the song pulses 🗿
The energy in every atom accelerating 🗿
The vibrations of the universe reaching their peak 🗿
The infinite possibilities unfolding with every beat 🗿
The ultimate truth of existence being revealed 🗿
The very meaning of life unraveling in the song 🗿
The purpose of everything aligning with the rhythm 🗿
The cosmos awakening to its true nature 🗿
The divine spark within all beings igniting 🗿
The universe itself ascending 🗿
The final realization that we are all one with the beat 🗿
me 🗿
you 🗿
ur girlfriend 🗿
ur dog 🗿
ohio sigmas 🗿
mr beast followers 🗿
gymrats 🗿
average phonk user 🗿
the FINAL BOSS 🗿
ur skills 🗿
the people 🗿
ur food 🗿
People who liked this comment 🗿""")

