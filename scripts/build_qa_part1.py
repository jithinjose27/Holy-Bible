# Genesis Q&A Part 1: Chapters 1 to 10
import json

def get_chapters_1_to_10():
    data = {}

    # Chapter 1
    data[1] = [
        {
            "id": "gen-1-q1", "questionNumber": 1,
            "question": "What did God create in the beginning according to Genesis 1:1?",
            "options": ["The heavens and the earth", "The sun and the stars", "The Garden of Eden", "The sea creatures and birds"],
            "correctAnswerIndex": 0, "correctAnswer": "The heavens and the earth",
            "reference": "Genesis 1:1",
            "explanation": "Genesis 1:1 declares: 'In the beginning God created the heavens and the earth.'"
        },
        {
            "id": "gen-1-q2", "questionNumber": 2,
            "question": "What did God command to appear on the first day of creation?",
            "options": ["Dry land", "Light", "The sky/expanse", "Vegetation"],
            "correctAnswerIndex": 1, "correctAnswer": "Light",
            "reference": "Genesis 1:3",
            "explanation": "God said, 'Let there be light,' and there was light, separating light from darkness on Day One."
        },
        {
            "id": "gen-1-q3", "questionNumber": 3,
            "question": "On the second day, what was created to separate the waters above from the waters below?",
            "options": ["A mountain barrier", "An expanse (sky/firmament)", "The ocean floor", "Clouds of vapor"],
            "correctAnswerIndex": 1, "correctAnswer": "An expanse (sky/firmament)",
            "reference": "Genesis 1:6–8",
            "explanation": "God made the expanse on Day Two to separate the waters under the expanse from the waters above it, calling it 'sky'."
        },
        {
            "id": "gen-1-q4", "questionNumber": 4,
            "question": "What two things appeared when the waters under the heavens gathered together on Day Three?",
            "options": ["Sun and moon", "Dry land (earth) and gathered seas", "Fish and whales", "Reptiles and cattle"],
            "correctAnswerIndex": 1, "correctAnswer": "Dry land (earth) and gathered seas",
            "reference": "Genesis 1:9–10",
            "explanation": "The waters gathered into one place and dry ground appeared; God called the dry ground 'land' and the gathered waters 'seas'."
        },
        {
            "id": "gen-1-q5", "questionNumber": 5,
            "question": "What kind of vegetation did the earth produce on the third day?",
            "options": ["Only moss and lichen", "Plants bearing seed and fruit trees bearing fruit according to their kinds", "Thorny briars and thistles", "Floating seaweed only"],
            "correctAnswerIndex": 1, "correctAnswer": "Plants bearing seed and fruit trees bearing fruit according to their kinds",
            "reference": "Genesis 1:11–12",
            "explanation": "The earth produced vegetation: seed-bearing plants and trees bearing fruit with seed in it according to their kinds."
        },
        {
            "id": "gen-1-q6", "questionNumber": 6,
            "question": "What purpose was given for the lights placed in the expanse of the sky on the fourth day?",
            "options": ["To separate day from night and serve as signs for seasons, days, and years", "To illuminate only the angels", "To test the faith of mankind", "To consume the water of the deep"],
            "correctAnswerIndex": 0, "correctAnswer": "To separate day from night and serve as signs for seasons, days, and years",
            "reference": "Genesis 1:14–18",
            "explanation": "God set lights in the expanse to separate day from night, govern the day and night, and serve as signs to mark seasons, days, and years."
        },
        {
            "id": "gen-1-q7", "questionNumber": 7,
            "question": "Which living creatures were created on the fifth day?",
            "options": ["Cattle and beasts of the field", "Creatures that swarm in the waters and winged birds of the air", "Creeping insects and reptiles", "Human beings"],
            "correctAnswerIndex": 1, "correctAnswer": "Creatures that swarm in the waters and winged birds of the air",
            "reference": "Genesis 1:20–22",
            "explanation": "On Day Five, God created great sea creatures and every living thing that teems in the waters, as well as winged birds."
        },
        {
            "id": "gen-1-q8", "questionNumber": 8,
            "question": "Before creating humanity on Day Six, what category of creatures did God make?",
            "options": ["Fish and sea monsters", "Livestock, creeping things, and beasts of the earth according to their kinds", "Celestial beings", "Coral reefs"],
            "correctAnswerIndex": 1, "correctAnswer": "Livestock, creeping things, and beasts of the earth according to their kinds",
            "reference": "Genesis 1:24–25",
            "explanation": "God commanded the earth to produce living creatures according to their kinds: livestock, creatures that move along the ground, and wild animals."
        },
        {
            "id": "gen-1-q9", "questionNumber": 9,
            "question": "According to Genesis 1:26–27, in whose image and likeness was humanity created?",
            "options": ["In the image of the angels", "In the image and likeness of God", "In the image of the stars", "In the likeness of the beasts"],
            "correctAnswerIndex": 1, "correctAnswer": "In the image and likeness of God",
            "reference": "Genesis 1:26–27",
            "explanation": "God said, 'Let us make mankind in our image, in our likeness.' Male and female He created them in the image of God."
        },
        {
            "id": "gen-1-q10", "questionNumber": 10,
            "question": "How did God describe everything He had made at the conclusion of Day Six?",
            "options": ["It was imperfect", "It was partially good", "It was very good", "It was incomplete"],
            "correctAnswerIndex": 2, "correctAnswer": "It was very good",
            "reference": "Genesis 1:31",
            "explanation": "Genesis 1:31 states: 'God saw all that he had made, and it was very good. And there was evening, and there was morning—the sixth day.'"
        }
    ]

    # Chapter 2
    data[2] = [
        {
            "id": "gen-2-q1", "questionNumber": 1,
            "question": "What did God do on the seventh day after finishing creation?",
            "options": ["He planted another world", "He rested from all His work, blessed the seventh day, and made it holy", "He created more animals", "He sent rain over the earth"],
            "correctAnswerIndex": 1, "correctAnswer": "He rested from all His work, blessed the seventh day, and made it holy",
            "reference": "Genesis 2:2–3",
            "explanation": "By the seventh day God completed His work, rested from all His labor, blessed the seventh day, and sanctified it."
        },
        {
            "id": "gen-2-q2", "questionNumber": 2,
            "question": "How was the ground watered before rain had fallen upon the earth?",
            "options": ["By underground pipes", "A mist (or spring) came up from the earth and watered the whole surface", "By melting glaciers", "By ocean tsunamis"],
            "correctAnswerIndex": 1, "correctAnswer": "A mist (or spring) came up from the earth and watered the whole surface",
            "reference": "Genesis 2:5–6",
            "explanation": "The Lord God had not yet caused it to rain, but a mist or stream came up from the earth and watered the whole face of the ground."
        },
        {
            "id": "gen-2-q3", "questionNumber": 3,
            "question": "From what did the Lord God form the first man, and how did he become a living soul?",
            "options": ["From gold and silver, energized by lightning", "From the dust of the ground, and breathed into his nostrils the breath of life", "From sea foam, infused by celestial light", "From the bark of the Tree of Life"],
            "correctAnswerIndex": 1, "correctAnswer": "From the dust of the ground, and breathed into his nostrils the breath of life",
            "reference": "Genesis 2:7",
            "explanation": "The Lord God formed man of the dust of the ground and breathed into his nostrils the breath of life, and man became a living soul."
        },
        {
            "id": "gen-2-q4", "questionNumber": 4,
            "question": "Where did the Lord God plant the garden for man, and in which direction?",
            "options": ["In the desert to the west", "Eastward, in Eden", "On Mount Ararat to the north", "In the land of Ur"],
            "correctAnswerIndex": 1, "correctAnswer": "Eastward, in Eden",
            "reference": "Genesis 2:8",
            "explanation": "Genesis 2:8 states that the Lord God planted a garden eastward in Eden, placing the man He had formed there."
        },
        {
            "id": "gen-2-q5", "questionNumber": 5,
            "question": "Which two special trees are specifically named as growing in the midst of the Garden of Eden?",
            "options": ["The Cedar of Lebanon and the Olive Tree", "The Tree of Life and the Tree of the Knowledge of Good and Evil", "The Fig Tree and the Oak Tree", "The Almond Tree and the Palm Tree"],
            "correctAnswerIndex": 1, "correctAnswer": "The Tree of Life and the Tree of the Knowledge of Good and Evil",
            "reference": "Genesis 2:9",
            "explanation": "In the middle of the garden were the Tree of Life and the Tree of the Knowledge of Good and Evil."
        },
        {
            "id": "gen-2-q6", "questionNumber": 6,
            "question": "How many headwaters did the river flowing out of Eden divide into, and what were their names?",
            "options": ["Two: Nile and Jordan", "Three: Red Sea, Dead Sea, Mediterranean", "Four: Pishon, Gihon, Tigris (Hiddekel), and Euphrates", "Seven rivers"],
            "correctAnswerIndex": 2, "correctAnswer": "Four: Pishon, Gihon, Tigris (Hiddekel), and Euphrates",
            "reference": "Genesis 2:10–14",
            "explanation": "A river flowed from Eden to water the garden, dividing from there into four heads: Pishon, Gihon, Tigris, and Euphrates."
        },
        {
            "id": "gen-2-q7", "questionNumber": 7,
            "question": "What primary duty did God give Adam when placing him into the Garden of Eden?",
            "options": ["To build a fortress city", "To cultivate (dress) and keep (guard) the garden", "To build a boat for trade", "To hunt the animals for leather"],
            "correctAnswerIndex": 1, "correctAnswer": "To cultivate (dress) and keep (guard) the garden",
            "reference": "Genesis 2:15",
            "explanation": "The Lord God took the man and placed him in the Garden of Eden to tend and keep it."
        },
        {
            "id": "gen-2-q8", "questionNumber": 8,
            "question": "What command and consequence did God give to Adam regarding the Tree of the Knowledge of Good and Evil?",
            "options": ["He could eat it on the Sabbath", "He must not eat of it; for in the day he eats of it he would surely die", "He could eat the leaves but not the fruit", "He must burn its branches"],
            "correctAnswerIndex": 1, "correctAnswer": "He must not eat of it; for in the day he eats of it he would surely die",
            "reference": "Genesis 2:16–17",
            "explanation": "God commanded: 'You must not eat from the tree of the knowledge of good and evil, for when you eat from it you will certainly die.'"
        },
        {
            "id": "gen-2-q9", "questionNumber": 9,
            "question": "What observation did the Lord God make before bringing the animals to Adam to be named?",
            "options": ["'The garden needs more flowers'", "'It is not good that the man should be alone; I will make him an help meet for him'", "'The animals need masters'", "'Man is too wise'"],
            "correctAnswerIndex": 1, "correctAnswer": "'It is not good that the man should be alone; I will make him an help meet for him'",
            "reference": "Genesis 2:18",
            "explanation": "The Lord God said, 'It is not good for the man to be alone. I will make a helper suitable for him.'"
        },
        {
            "id": "gen-2-q10", "questionNumber": 10,
            "question": "How was the first woman created, and what was Adam's joyful response?",
            "options": ["From clay by the riverbank; Adam called her sister", "From one of Adam's ribs during a deep sleep; Adam declared: 'This is now bone of my bones, and flesh of my flesh'", "From a sunbeam; Adam called her daughter", "She descended from heaven on a chariot"],
            "correctAnswerIndex": 1, "correctAnswer": "From one of Adam's ribs during a deep sleep; Adam declared: 'This is now bone of my bones, and flesh of my flesh'",
            "reference": "Genesis 2:21–23",
            "explanation": "God caused a deep sleep to fall on Adam, took one of his ribs, and made it into a woman. Adam exclaimed: 'This is now bone of my bones and flesh of my flesh; she shall be called Woman!'"
        }
    ]

    # Chapter 3
    data[3] = [
        {
            "id": "gen-3-q1", "questionNumber": 1,
            "question": "How did the serpent initiate conversation with the woman in Genesis 3:1?",
            "options": ["By asking: 'Did God really say, You must not eat from any tree in the garden?'", "By offering her gold and jewels", "By claiming to be an angel of light", "By threatening her with harm"],
            "correctAnswerIndex": 0, "correctAnswer": "By asking: 'Did God really say, You must not eat from any tree in the garden?'",
            "reference": "Genesis 3:1",
            "explanation": "The serpent was more crafty than any wild animal and asked the woman: 'Did God really say, You must not eat from any tree in the garden?'"
        },
        {
            "id": "gen-3-q2", "questionNumber": 2,
            "question": "What lie did the serpent tell the woman regarding eating the forbidden fruit?",
            "options": ["'You will become invisible'", "'You will certainly not die... your eyes will be opened, and you will be like God, knowing good and evil'", "'God does not care what you eat'", "'The fruit will make you live forever instantly'"],
            "correctAnswerIndex": 1, "correctAnswer": "'You will certainly not die... your eyes will be opened, and you will be like God, knowing good and evil'",
            "reference": "Genesis 3:4–5",
            "explanation": "The serpent directly contradicted God's warning, saying: 'You will certainly not die. For God knows that when you eat from it your eyes will be opened, and you will be like God, knowing good and evil.'"
        },
        {
            "id": "gen-3-q3", "questionNumber": 3,
            "question": "What three things did the woman perceive about the tree before eating its fruit in Genesis 3:6?",
            "options": ["Good for food, pleasing to the eye, and desirable for gaining wisdom", "Bitter to taste, heavy to carry, and strange to smell", "Cold to touch, dark in color, and noisy in the wind", "Covered in thorns, poisonous to touch, and rotten"],
            "correctAnswerIndex": 0, "correctAnswer": "Good for food, pleasing to the eye, and desirable for gaining wisdom",
            "reference": "Genesis 3:6",
            "explanation": "She saw that the fruit of the tree was good for food and pleasing to the eye, and also desirable for gaining wisdom, so she took some and ate it, and gave some to her husband."
        },
        {
            "id": "gen-3-q4", "questionNumber": 4,
            "question": "What immediate realization came to the man and woman after eating the fruit, and how did they react?",
            "options": ["They realized they could fly and leapt into the air", "They realized they were naked, sewed fig leaves together, and made coverings for themselves", "They felt proud and celebrated", "They built an altar of thanksgiving"],
            "correctAnswerIndex": 1, "correctAnswer": "They realized they were naked, sewed fig leaves together, and made coverings for themselves",
            "reference": "Genesis 3:7",
            "explanation": "The eyes of both were opened and they realized they were naked; so they sewed fig leaves together and made coverings for themselves."
        },
        {
            "id": "gen-3-q5", "questionNumber": 5,
            "question": "What did Adam and his wife do when they heard the sound of the Lord God walking in the garden in the cool of the day?",
            "options": ["They ran to welcome Him with singing", "They hid from the Lord God among the trees of the garden", "They climbed to the top of the mountain", "They sailed down the river"],
            "correctAnswerIndex": 1, "correctAnswer": "They hid from the Lord God among the trees of the garden",
            "reference": "Genesis 3:8",
            "explanation": "They heard the sound of the Lord God walking in the garden in the cool of the day, and they hid from the Lord God among the trees."
        },
        {
            "id": "gen-3-q6", "questionNumber": 6,
            "question": "What question did the Lord God call out to the man in Genesis 3:9?",
            "options": ["'What have you done?'", "'Where are you?'", "'Who gave you permission?'", "'Why are you awake?'"],
            "correctAnswerIndex": 1, "correctAnswer": "'Where are you?'",
            "reference": "Genesis 3:9",
            "explanation": "Genesis 3:9 states: 'But the Lord God called to the man, Where are you?'"
        },
        {
            "id": "gen-3-q7", "questionNumber": 7,
            "question": "Whom did Adam blame when God asked if he had eaten from the forbidden tree?",
            "options": ["The serpent alone", "The woman God put with him ('The woman you put here with me—she gave me some fruit from the tree, and I ate it')", "His own lack of self-control", "The heat of the day"],
            "correctAnswerIndex": 1, "correctAnswer": "The woman God put with him ('The woman you put here with me—she gave me some fruit from the tree, and I ate it')",
            "reference": "Genesis 3:12",
            "explanation": "The man said: 'The woman you put here with me—she gave me some fruit from the tree, and I ate it.'"
        },
        {
            "id": "gen-3-q8", "questionNumber": 8,
            "question": "What prophetic judgment did God pronounce upon the serpent in Genesis 3:15 (the Protoevangelium)?",
            "options": ["The serpent would gain wings and fly away", "Enmity between the serpent and the woman, and between its offspring and hers; her offspring would crush its head, and it would strike his heel", "The serpent would be honored as the wisest beast", "The serpent would live forever in the sea"],
            "correctAnswerIndex": 1, "correctAnswer": "Enmity between the serpent and the woman, and between its offspring and hers; her offspring would crush its head, and it would strike his heel",
            "reference": "Genesis 3:15",
            "explanation": "God said: 'I will put enmity between you and the woman, and between your offspring and hers; he will crush your head, and you will strike his heel.'"
        },
        {
            "id": "gen-3-q9", "questionNumber": 9,
            "question": "What did the Lord God make for Adam and his wife to replace their fig leaf coverings?",
            "options": ["Garments of woven wool", "Garments of skin (leather) to clothe them", "Robes of purple linen", "Armor of brass"],
            "correctAnswerIndex": 1, "correctAnswer": "Garments of skin (leather) to clothe them",
            "reference": "Genesis 3:21",
            "explanation": "Genesis 3:21 states: 'The Lord God made garments of skin for Adam and his wife and clothed them.'"
        },
        {
            "id": "gen-3-q10", "questionNumber": 10,
            "question": "What was placed on the east side of the Garden of Eden to guard the way to the Tree of Life after mankind was expelled?",
            "options": ["A high stone wall and iron gate", "Cherubim and a flaming sword flashing back and forth", "A pack of ferocious wolves", "A ring of roaring desert fires"],
            "correctAnswerIndex": 1, "correctAnswer": "Cherubim and a flaming sword flashing back and forth",
            "reference": "Genesis 3:24",
            "explanation": "He placed on the east side of the Garden of Eden cherubim and a flaming sword flashing back and forth to guard the way to the Tree of Life."
        }
    ]

    # Chapter 4
    data[4] = [
        {
            "id": "gen-4-q1", "questionNumber": 1,
            "question": "What occupations did Cain and Abel have in Genesis 4:2?",
            "options": ["Abel was a builder, Cain was a metalworker", "Abel kept flocks (shepherd), and Cain worked the soil (farmer)", "Abel was a fisherman, Cain was a hunter", "Both were nomadic merchants"],
            "correctAnswerIndex": 1, "correctAnswer": "Abel kept flocks (shepherd), and Cain worked the soil (farmer)",
            "reference": "Genesis 4:2",
            "explanation": "Genesis 4:2 states: 'Now Abel kept flocks, and Cain worked the soil.'"
        },
        {
            "id": "gen-4-q2", "questionNumber": 2,
            "question": "What offerings did Cain and Abel bring to the Lord?",
            "options": ["Cain brought silver; Abel brought gold", "Cain brought some fruits of the soil; Abel brought fat portions from the firstborn of his flock", "Cain brought incense; Abel brought wine", "Both brought olive oil and bread"],
            "correctAnswerIndex": 1, "correctAnswer": "Cain brought some fruits of the soil; Abel brought fat portions from the firstborn of his flock",
            "reference": "Genesis 4:3–4",
            "explanation": "Cain brought some of the fruits of the soil as an offering, but Abel brought fat portions from some of the firstborn of his flock."
        },
        {
            "id": "gen-4-q3", "questionNumber": 3,
            "question": "How did the Lord respond to the offerings of the two brothers?",
            "options": ["He rejected both offerings", "He looked with favor on Abel and his offering, but on Cain and his offering He did not look with favor", "He accepted both offerings equally", "He commanded them to switch occupations"],
            "correctAnswerIndex": 1, "correctAnswer": "He looked with favor on Abel and his offering, but on Cain and his offering He did not look with favor",
            "reference": "Genesis 4:4–5",
            "explanation": "The Lord looked with favor on Abel and his offering, but on Cain and his offering he did not look with favor; so Cain was very angry, and his face was downcast."
        },
        {
            "id": "gen-4-q4", "questionNumber": 4,
            "question": "What warning did the Lord give Cain regarding sin crouching at the door in Genesis 4:7?",
            "options": ["'Sin is harmless if you ignore it'", "'Sin is crouching at your door; it desires to have you, but you must rule over it'", "'Sin will leave you alone tomorrow'", "'You cannot avoid sin, so give up'"],
            "correctAnswerIndex": 1, "correctAnswer": "'Sin is crouching at your door; it desires to have you, but you must rule over it'",
            "reference": "Genesis 4:7",
            "explanation": "God warned Cain: 'If you do not do what is right, sin is crouching at your door; it desires to have you, but you must rule over it.'"
        },
        {
            "id": "gen-4-q5", "questionNumber": 5,
            "question": "Where did Cain take Abel when he attacked and murdered him?",
            "options": ["Inside the family tent", "Out into the open field", "Beside the riverbank", "Near the gates of Eden"],
            "correctAnswerIndex": 1, "correctAnswer": "Out into the open field",
            "reference": "Genesis 4:8",
            "explanation": "Cain said to his brother Abel, 'Let’s go out to the field.' While they were in the field, Cain attacked his brother Abel and killed him."
        },
        {
            "id": "gen-4-q6", "questionNumber": 6,
            "question": "How did Cain reply when the Lord asked him, 'Where is your brother Abel?'",
            "options": ["'He went on a long journey'", "'I don't know. Am I my brother’s keeper?'", "'He is sleeping in the tent'", "'Forgive me, for I have sinned'"],
            "correctAnswerIndex": 1, "correctAnswer": "'I don't know. Am I my brother’s keeper?'",
            "reference": "Genesis 4:9",
            "explanation": "Cain lied and retorted with defiance: 'I don't know. Am I my brother's keeper?'"
        },
        {
            "id": "gen-4-q7", "questionNumber": 7,
            "question": "What did God say was crying out to Him from the ground in Genesis 4:10?",
            "options": ["The weeping of Eve", "The blood of Cain's brother Abel", "The groaning of the soil", "The cries of the sheep"],
            "correctAnswerIndex": 1, "correctAnswer": "The blood of Cain's brother Abel",
            "reference": "Genesis 4:10",
            "explanation": "The Lord said: 'What have you done? Listen! Your brother's blood cries out to me from the ground.'"
        },
        {
            "id": "gen-4-q8", "questionNumber": 8,
            "question": "What protection did the Lord place upon Cain when he feared he would be killed as a restless wanderer?",
            "options": ["An army of angelic bodyguards", "The Lord put a mark on Cain so that no one who found him would kill him", "A fortress of stone", "A chariot of fire"],
            "correctAnswerIndex": 1, "correctAnswer": "The Lord put a mark on Cain so that no one who found him would kill him",
            "reference": "Genesis 4:15",
            "explanation": "The Lord put a mark on Cain so that no one who found him would kill him, declaring sevenfold vengeance on anyone who killed Cain."
        },
        {
            "id": "gen-4-q9", "questionNumber": 9,
            "question": "To which land did Cain go to live after leaving the presence of the Lord, and what was the name of the city he built?",
            "options": ["The land of Ur; city of Babylon", "The land of Nod, east of Eden; city of Enoch (named after his son)", "The land of Canaan; city of Jerusalem", "The land of Egypt; city of Memphis"],
            "correctAnswerIndex": 1, "correctAnswer": "The land of Nod, east of Eden; city of Enoch (named after his son)",
            "reference": "Genesis 4:16–17",
            "explanation": "Cain lived in the land of Nod, east of Eden. He was then building a city, and he named it after his son Enoch."
        },
        {
            "id": "gen-4-q10", "questionNumber": 10,
            "question": "Who was born to Adam and Eve to replace Abel, and what did people begin to do during the time of his son Enosh?",
            "options": ["Lamech; they began to build towers", "Seth; at that time people began to call on the name of the Lord", "Tubal-Cain; they began to forge weapons", "Jubal; they began to write poetry"],
            "correctAnswerIndex": 1, "correctAnswer": "Seth; at that time people began to call on the name of the Lord",
            "reference": "Genesis 4:25–26",
            "explanation": "Eve gave birth to Seth, saying 'God has granted me another child in place of Abel.' To Seth also a son was born named Enosh; at that time people began to call on the name of the Lord."
        }
    ]

    # Chapter 5
    data[5] = [
        {
            "id": "gen-5-q1", "questionNumber": 1,
            "question": "How old was Adam when his son Seth was born in his own likeness and image?",
            "options": ["70 years", "100 years", "130 years", "250 years"],
            "correctAnswerIndex": 2, "correctAnswer": "130 years",
            "reference": "Genesis 5:3",
            "explanation": "Genesis 5:3 states: 'When Adam had lived 130 years, he had a son in his own likeness, in his own image; and he named him Seth.'"
        },
        {
            "id": "gen-5-q2", "questionNumber": 2,
            "question": "How long did Adam live altogether before he died?",
            "options": ["777 years", "930 years", "969 years", "1000 years"],
            "correctAnswerIndex": 1, "correctAnswer": "930 years",
            "reference": "Genesis 5:5",
            "explanation": "Genesis 5:5 records: 'Altogether, Adam lived a total of 930 years, and then he died.'"
        },
        {
            "id": "gen-5-q3", "questionNumber": 3,
            "question": "What refrain is repeated throughout Genesis 5 for almost every patriarch after recording their lifespan?",
            "options": ["'and he ascended to heaven'", "'and he was lost'", "'and then he died'", "'and he ruled with power'"],
            "correctAnswerIndex": 2, "correctAnswer": "'and then he died'",
            "reference": "Genesis 5:5–31",
            "explanation": "The solemn refrain 'and then he died' emphasizes the reality of physical death entering humanity after the Fall."
        },
        {
            "id": "gen-5-q4", "questionNumber": 4,
            "question": "What exceptional testimony is recorded about Enoch in Genesis 5:22 and 5:24?",
            "options": ["He conquered all surrounding nations", "He walked faithfully with God; then he was no more, because God took him away", "He built the first great library", "He invented the bronze plow"],
            "correctAnswerIndex": 1, "correctAnswer": "He walked faithfully with God; then he was no more, because God took him away",
            "reference": "Genesis 5:22–24",
            "explanation": "Genesis 5:24 states: 'Enoch walked faithfully with God; then he was no more, because God took him away.'"
        },
        {
            "id": "gen-5-q5", "questionNumber": 5,
            "question": "How long did Enoch live on the earth before God took him?",
            "options": ["120 years", "365 years", "500 years", "777 years"],
            "correctAnswerIndex": 1, "correctAnswer": "365 years",
            "reference": "Genesis 5:23",
            "explanation": "Genesis 5:23 records: 'Altogether, Enoch lived a total of 365 years.'"
        },
        {
            "id": "gen-5-q6", "questionNumber": 6,
            "question": "Who was the oldest recorded human in the Bible according to Genesis 5:27, and how old was he?",
            "options": ["Noah (950 years)", "Adam (930 years)", "Methuselah (969 years)", "Jared (962 years)"],
            "correctAnswerIndex": 2, "correctAnswer": "Methuselah (969 years)",
            "reference": "Genesis 5:27",
            "explanation": "Genesis 5:27 states: 'Altogether, Methuselah lived a total of 969 years, and then he died.'"
        },
        {
            "id": "gen-5-q7", "questionNumber": 7,
            "question": "Who was the father of Methuselah, and who was Methuselah's famous grandson?",
            "options": ["Adam was father; Seth was grandson", "Enoch was father; Noah was grandson", "Cain was father; Lamech was grandson", "Jared was father; Shem was grandson"],
            "correctAnswerIndex": 1, "correctAnswer": "Enoch was father; Noah was grandson",
            "reference": "Genesis 5:21–29",
            "explanation": "Enoch fathered Methuselah, Methuselah fathered Lamech, and Lamech fathered Noah."
        },
        {
            "id": "gen-5-q8", "questionNumber": 8,
            "question": "What prophecy did Lamech make when naming his son Noah in Genesis 5:29?",
            "options": ["'He will conquer our enemies'", "'He will comfort us in the labor and painful toil of our hands caused by the ground the Lord has cursed'", "'He will build the tallest tower on earth'", "'He will bring wealth from foreign lands'"],
            "correctAnswerIndex": 1, "correctAnswer": "'He will comfort us in the labor and painful toil of our hands caused by the ground the Lord has cursed'",
            "reference": "Genesis 5:29",
            "explanation": "Lamech named him Noah ('Rest/Comfort') and said, 'He will comfort us in the labor and painful toil of our hands caused by the ground the Lord has cursed.'"
        },
        {
            "id": "gen-5-q9", "questionNumber": 9,
            "question": "How old was Lamech when he died, having lived 595 years after Noah was born?",
            "options": ["500 years", "777 years", "850 years", "900 years"],
            "correctAnswerIndex": 1, "correctAnswer": "777 years",
            "reference": "Genesis 5:31",
            "explanation": "Genesis 5:31 records: 'Altogether, Lamech lived a total of 777 years, and then he died.'"
        },
        {
            "id": "gen-5-q10", "questionNumber": 10,
            "question": "Who were the three sons of Noah listed at the close of Genesis 5?",
            "options": ["Cain, Abel, and Seth", "Shem, Ham, and Japheth", "Abraham, Isaac, and Jacob", "Gomer, Magog, and Madai"],
            "correctAnswerIndex": 1, "correctAnswer": "Shem, Ham, and Japheth",
            "reference": "Genesis 5:32",
            "explanation": "Genesis 5:32 states: 'After Noah was 500 years old, he became the father of Shem, Ham and Japheth.'"
        }
    ]

    # Chapter 6
    data[6] = [
        {
            "id": "gen-6-q1", "questionNumber": 1,
            "question": "What limit did the Lord place on the human lifespan in Genesis 6:3?",
            "options": ["70 years", "120 years", "300 years", "500 years"],
            "correctAnswerIndex": 1, "correctAnswer": "120 years",
            "reference": "Genesis 6:3",
            "explanation": "The Lord said, 'My Spirit will not contend with humans forever, for they are mortal; their days will be 120 years.'"
        },
        {
            "id": "gen-6-q2", "questionNumber": 2,
            "question": "Who were the Nephilim mentioned in Genesis 6:4?",
            "options": ["An order of temple priests", "Heroes of old, men of renown who were on the earth in those days", "A species of winged reptiles", "A tribe of seafaring fishermen"],
            "correctAnswerIndex": 1, "correctAnswer": "Heroes of old, men of renown who were on the earth in those days",
            "reference": "Genesis 6:4",
            "explanation": "Genesis 6:4 describes the Nephilim as the heroes of old, men of renown who were on the earth in those days."
        },
        {
            "id": "gen-6-q3", "questionNumber": 3,
            "question": "How did the Lord evaluate the human condition in Genesis 6:5?",
            "options": ["Humans were mostly obedient with small flaws", "Every inclination of the thoughts of the human heart was only evil all the time", "Only the rulers were corrupt", "The earth was full of peace"],
            "correctAnswerIndex": 1, "correctAnswer": "Every inclination of the thoughts of the human heart was only evil all the time",
            "reference": "Genesis 6:5",
            "explanation": "The Lord saw how great the wickedness of the human race had become, and that every inclination of the thoughts of the human heart was only evil all the time."
        },
        {
            "id": "gen-6-q4", "questionNumber": 4,
            "question": "How did the Lord feel about having made human beings on the earth in Genesis 6:6?",
            "options": ["He was indifferent", "He was troubled, His heart was deeply troubled, and He regretted having made them", "He was amused", "He resolved to create a second moon"],
            "correctAnswerIndex": 1, "correctAnswer": "He was troubled, His heart was deeply troubled, and He regretted having made them",
            "reference": "Genesis 6:6",
            "explanation": "Genesis 6:6 states: 'The Lord regretted that he had made human beings on the earth, and his heart was deeply troubled.'"
        },
        {
            "id": "gen-6-q5", "questionNumber": 5,
            "question": "What remarkable statement is made about Noah in Genesis 6:8?",
            "options": ["Noah was the wealthiest man of his age", "Noah found favor (grace) in the eyes of the Lord", "Noah had traveled around the entire world", "Noah was a mighty warrior"],
            "correctAnswerIndex": 1, "correctAnswer": "Noah found favor (grace) in the eyes of the Lord",
            "reference": "Genesis 6:8",
            "explanation": "Genesis 6:8 records: 'But Noah found favor in the eyes of the Lord.'"
        },
        {
            "id": "gen-6-q6", "questionNumber": 6,
            "question": "How does Genesis 6:9 describe Noah's personal character?",
            "options": ["A proud conqueror", "A righteous man, blameless among the people of his time, who walked faithfully with God", "A skilled politician", "A quiet shepherd"],
            "correctAnswerIndex": 1, "correctAnswer": "A righteous man, blameless among the people of his time, who walked faithfully with God",
            "reference": "Genesis 6:9",
            "explanation": "Genesis 6:9 says: 'Noah was a righteous man, blameless among the people of his time, and he walked faithfully with God.'"
        },
        {
            "id": "gen-6-q7", "questionNumber": 7,
            "question": "What type of wood was Noah instructed to use to construct the Ark?",
            "options": ["Acacia wood", "Cedar of Lebanon", "Cypress wood (gopher wood)", "Olive wood"],
            "correctAnswerIndex": 2, "correctAnswer": "Cypress wood (gopher wood)",
            "reference": "Genesis 6:14",
            "explanation": "God told Noah: 'Make yourself an ark of gopher wood (cypress wood); make rooms in it and coat it with pitch inside and out.'"
        },
        {
            "id": "gen-6-q8", "questionNumber": 8,
            "question": "What were the dimensions of the Ark according to Genesis 6:15?",
            "options": ["100 cubits long, 20 wide, 10 high", "300 cubits long, 50 cubits wide, and 30 cubits high", "500 cubits long, 100 wide, 50 high", "1000 cubits long, 200 wide, 100 high"],
            "correctAnswerIndex": 1, "correctAnswer": "300 cubits long, 50 cubits wide, and 30 cubits high",
            "reference": "Genesis 6:15",
            "explanation": "The Ark was to be 300 cubits long (approx. 450 ft), 50 cubits wide (75 ft), and 30 cubits high (45 ft)."
        },
        {
            "id": "gen-6-q9", "questionNumber": 9,
            "question": "How many decks (stories) was Noah instructed to build inside the Ark?",
            "options": ["One wide floor", "Two levels", "Three decks: lower, middle, and upper", "Seven tiers"],
            "correctAnswerIndex": 2, "correctAnswer": "Three decks: lower, middle, and upper",
            "reference": "Genesis 6:16",
            "explanation": "Genesis 6:16 specifies: 'Put a door in the side of the ark and make lower, middle and upper decks.'"
        },
        {
            "id": "gen-6-q10", "questionNumber": 10,
            "question": "How did Noah respond to all of God's instructions in Genesis 6:22?",
            "options": ["He argued and questioned the dimensions", "Noah did everything just as God commanded him", "He delayed construction for forty years", "He built only half the Ark"],
            "correctAnswerIndex": 1, "correctAnswer": "Noah did everything just as God commanded him",
            "reference": "Genesis 6:22",
            "explanation": "Genesis 6:22 records: 'Noah did everything just as God commanded him.'"
        }
    ]

    # Chapter 7
    data[7] = [
        {
            "id": "gen-7-q1", "questionNumber": 1,
            "question": "How many of every kind of clean animal was Noah instructed to take on the Ark?",
            "options": ["One male only", "One pair (two)", "Seven pairs (or seven of each)", "Twelve pairs"],
            "correctAnswerIndex": 2, "correctAnswer": "Seven pairs (or seven of each)",
            "reference": "Genesis 7:2",
            "explanation": "God commanded: 'Take with you seven pairs of every kind of clean animal, a male and its mate, and one pair of every kind of unclean animal.'"
        },
        {
            "id": "gen-7-q2", "questionNumber": 2,
            "question": "How old was Noah when the floodwaters came on the earth?",
            "options": ["120 years", "365 years", "600 years", "777 years"],
            "correctAnswerIndex": 2, "correctAnswer": "600 years",
            "reference": "Genesis 7:6",
            "explanation": "Genesis 7:6 states: 'Noah was six hundred years old when the floodwaters came on the earth.'"
        },
        {
            "id": "gen-7-q3", "questionNumber": 3,
            "question": "How many humans entered the Ark in total according to Genesis 7:7 and 7:13?",
            "options": ["Two (Noah and wife)", "Four", "Eight (Noah, his wife, his three sons, and their three wives)", "Twelve"],
            "correctAnswerIndex": 2, "correctAnswer": "Eight (Noah, his wife, his three sons, and their three wives)",
            "reference": "Genesis 7:13",
            "explanation": "Eight people entered the Ark: Noah, his sons Shem, Ham, and Japheth, his wife, and the three wives of his sons."
        },
        {
            "id": "gen-7-q4", "questionNumber": 4,
            "question": "What two water sources were opened on the day the Flood began in Genesis 7:11?",
            "options": ["The rivers of Eden and the Red Sea", "All the springs of the great deep burst forth, and the floodgates of the heavens were opened", "Glaciers melted and geysers erupted", "A tidal wave from the Mediterranean"],
            "correctAnswerIndex": 1, "correctAnswer": "All the springs of the great deep burst forth, and the floodgates of the heavens were opened",
            "reference": "Genesis 7:11",
            "explanation": "On that day all the springs of the great deep burst forth, and the floodgates of the heavens were opened."
        },
        {
            "id": "gen-7-q5", "questionNumber": 5,
            "question": "How many days and nights did rain fall upon the earth during the Flood?",
            "options": ["7 days and 7 nights", "40 days and 40 nights", "100 days", "150 days"],
            "correctAnswerIndex": 1, "correctAnswer": "40 days and 40 nights",
            "reference": "Genesis 7:12",
            "explanation": "Genesis 7:12 states: 'And rain fell on the earth forty days and forty nights.'"
        },
        {
            "id": "gen-7-q6", "questionNumber": 6,
            "question": "Who shut the door of the Ark after Noah and the animals entered in Genesis 7:16?",
            "options": ["Noah's sons", "Noah with a heavy wooden bar", "The Lord shut him in", "A powerful wind blew it shut"],
            "correctAnswerIndex": 2, "correctAnswer": "The Lord shut him in",
            "reference": "Genesis 7:16",
            "explanation": "Genesis 7:16 says: 'The animals going in were male and female of every living thing, as God had commanded Noah. Then the Lord shut him in.'"
        },
        {
            "id": "gen-7-q7", "questionNumber": 7,
            "question": "How high did the floodwaters rise above the highest mountains under the heavens in Genesis 7:20?",
            "options": ["5 cubits", "15 cubits (more than 20 feet)", "50 cubits", "100 cubits"],
            "correctAnswerIndex": 1, "correctAnswer": "15 cubits (more than 20 feet)",
            "reference": "Genesis 7:20",
            "explanation": "Genesis 7:20 records: 'The waters rose and covered the mountains to a depth of more than fifteen cubits.'"
        },
        {
            "id": "gen-7-q8", "questionNumber": 8,
            "question": "What happened to every living creature on the dry land that had the breath of life in its nostrils?",
            "options": ["Some migrated to higher peaks", "Every living thing on the face of the earth was wiped out; only Noah and those with him in the ark remained", "Many adapted and learned to swim", "They built rafts"],
            "correctAnswerIndex": 1, "correctAnswer": "Every living thing on the face of the earth was wiped out; only Noah and those with him in the ark remained",
            "reference": "Genesis 7:22–23",
            "explanation": "Every living thing that moved on land perished—birds, livestock, wild animals, all creatures that swarm over the earth, and all mankind."
        },
        {
            "id": "gen-7-q9", "questionNumber": 9,
            "question": "For how many days did the floodwaters flood (prevail over) the earth in Genesis 7:24?",
            "options": ["40 days", "70 days", "150 days", "365 days"],
            "correctAnswerIndex": 2, "correctAnswer": "150 days",
            "reference": "Genesis 7:24",
            "explanation": "Genesis 7:24 states: 'The waters flooded the earth for a hundred and fifty days.'"
        },
        {
            "id": "gen-7-q10", "questionNumber": 10,
            "question": "What is the primary spiritual lesson illustrated by God preserving Noah in the Ark?",
            "options": ["That boats are superior to cities", "That God judges persistent wickedness while faithfully saving the righteous who trust and obey Him", "That humans can outsmart nature", "That mountains are unsafe"],
            "correctAnswerIndex": 1, "correctAnswer": "That God judges persistent wickedness while faithfully saving the righteous who trust and obey Him",
            "reference": "Genesis 7:1–24",
            "explanation": "The Flood demonstrates both God's holy justice against global corruption and His covenant mercy in preserving a righteous remnant through the Ark."
        }
    ]

    # Chapter 8
    data[8] = [
        {
            "id": "gen-8-q1", "questionNumber": 1,
            "question": "What did God remember at the start of Genesis 8, and what did He send over the earth?",
            "options": ["God remembered the gold of Eden and sent an earthquake", "God remembered Noah and all the animals, and He sent a wind over the earth, causing the waters to recede", "God remembered the garden and sent rain", "God remembered the Nephilim"],
            "correctAnswerIndex": 1, "correctAnswer": "God remembered Noah and all the animals, and He sent a wind over the earth, causing the waters to recede",
            "reference": "Genesis 8:1",
            "explanation": "Genesis 8:1 states: 'But God remembered Noah and all the wild animals and the livestock that were with him in the ark, and he sent a wind over the earth, and the waters receded.'"
        },
        {
            "id": "gen-8-q2", "questionNumber": 2,
            "question": "Where did the Ark come to rest on the seventeenth day of the seventh month?",
            "options": ["On Mount Sinai", "On the mountains of Ararat", "On Mount Carmel", "On Mount Moriah"],
            "correctAnswerIndex": 1, "correctAnswer": "On the mountains of Ararat",
            "reference": "Genesis 8:4",
            "explanation": "Genesis 8:4 records: 'and on the seventeenth day of the seventh month the ark came to rest on the mountains of Ararat.'"
        },
        {
            "id": "gen-8-q3", "questionNumber": 3,
            "question": "Which bird did Noah send out first from the Ark window, and what did it do?",
            "options": ["A dove; it built a nest on the roof", "A raven; it kept flying back and forth until the water had dried up from the earth", "An eagle; it flew to Egypt", "A swallow; it died immediately"],
            "correctAnswerIndex": 1, "correctAnswer": "A raven; it kept flying back and forth until the water had dried up from the earth",
            "reference": "Genesis 8:7",
            "explanation": "Noah sent out a raven, and it kept flying back and forth until the water had dried up from the earth."
        },
        {
            "id": "gen-8-q4", "questionNumber": 4,
            "question": "Why did the dove return to Noah the first time it was sent out in Genesis 8:9?",
            "options": ["It was attacked by birds of prey", "It could find nowhere to perch because there was water over all the surface of the earth", "It missed the other birds", "Noah called it back with a whistle"],
            "correctAnswerIndex": 1, "correctAnswer": "It could find nowhere to perch because there was water over all the surface of the earth",
            "reference": "Genesis 8:9",
            "explanation": "The dove could find nowhere to perch because there was water over all the surface of the earth; so it returned to Noah in the ark."
        },
        {
            "id": "gen-8-q5", "questionNumber": 5,
            "question": "What did the dove bring back in its beak when Noah sent it out the second time seven days later?",
            "options": ["A grain of wheat", "A freshly plucked olive leaf", "A twig of cedar", "A fish bone"],
            "correctAnswerIndex": 1, "correctAnswer": "A freshly plucked olive leaf",
            "reference": "Genesis 8:11",
            "explanation": "When the dove returned to him in the evening, there in its beak was a freshly plucked olive leaf! Then Noah knew that the water had receded from the earth."
        },
        {
            "id": "gen-8-q6", "questionNumber": 6,
            "question": "What happened when Noah sent the dove out the third time after waiting another seven days?",
            "options": ["It returned exhausted", "It did not return to him again", "It brought a branch of grapes", "It fell into the mud"],
            "correctAnswerIndex": 1, "correctAnswer": "It did not return to him again",
            "reference": "Genesis 8:12",
            "explanation": "He waited seven more days and sent the dove out again, but this time it did not return to him."
        },
        {
            "id": "gen-8-q7", "questionNumber": 7,
            "question": "What did Noah see when he removed the covering from the Ark on the first day of the first month of his 601st year?",
            "options": ["A second wave of floodwaters", "The surface of the ground was dry", "Smoke rising from cities", "Flocks of lions"],
            "correctAnswerIndex": 1, "correctAnswer": "The surface of the ground was dry",
            "reference": "Genesis 8:13",
            "explanation": "Noah removed the covering from the ark and saw that the surface of the ground was dry."
        },
        {
            "id": "gen-8-q8", "questionNumber": 8,
            "question": "What was the very first thing Noah built after coming out of the Ark onto dry land?",
            "options": ["A fortress house", "An altar to the Lord, sacrificing burnt offerings of every clean animal and clean bird", "A vineyard press", "A sheep pen"],
            "correctAnswerIndex": 1, "correctAnswer": "An altar to the Lord, sacrificing burnt offerings of every clean animal and clean bird",
            "reference": "Genesis 8:20",
            "explanation": "Then Noah built an altar to the Lord and, taking some of all the clean animals and clean birds, he sacrificed burnt offerings on it."
        },
        {
            "id": "gen-8-q9", "questionNumber": 9,
            "question": "How did the Lord respond to Noah's burnt offering on the altar?",
            "options": ["The Lord rejected the sacrifice", "The Lord smelled the pleasing aroma and said in His heart He would never again curse the ground because of humans", "The Lord sent fire to consume the mountain", "The Lord demanded more offerings"],
            "correctAnswerIndex": 1, "correctAnswer": "The Lord smelled the pleasing aroma and said in His heart He would never again curse the ground because of humans",
            "reference": "Genesis 8:21",
            "explanation": "The Lord smelled the pleasing aroma and said in his heart: 'Never again will I curse the ground because of humans, even though every inclination of the human heart is evil from childhood.'"
        },
        {
            "id": "gen-8-q10", "questionNumber": 10,
            "question": "What perpetual cycle did God promise would never cease as long as the earth endures in Genesis 8:22?",
            "options": ["Gold and silver mining", "Seedtime and harvest, cold and heat, summer and winter, day and night", "Storms and floods", "Kingdoms rising and falling"],
            "correctAnswerIndex": 1, "correctAnswer": "Seedtime and harvest, cold and heat, summer and winter, day and night",
            "reference": "Genesis 8:22",
            "explanation": "Genesis 8:22 declares: 'As long as the earth endures, seedtime and harvest, cold and heat, summer and winter, day and night will never cease.'"
        }
    ]

    # Chapter 9
    data[9] = [
        {
            "id": "gen-9-q1", "questionNumber": 1,
            "question": "What blessing and commandment did God speak to Noah and his sons in Genesis 9:1?",
            "options": ["'Build a kingdom of stone'", "'Be fruitful and increase in number and fill the earth'", "'Do not travel beyond the mountain'", "'Live only in tents'"],
            "correctAnswerIndex": 1, "correctAnswer": "'Be fruitful and increase in number and fill the earth'",
            "reference": "Genesis 9:1",
            "explanation": "God blessed Noah and his sons, saying to them, 'Be fruitful and increase in number and fill the earth.'"
        },
        {
            "id": "gen-9-q2", "questionNumber": 2,
            "question": "What change regarding diet was explicitly granted to mankind in Genesis 9:3?",
            "options": ["Humans could only eat figs and dates", "Just as God gave the green plants, He now gave everything that lives and moves as food", "Humans were forbidden to eat plants", "Meat could only be eaten on feast days"],
            "correctAnswerIndex": 1, "correctAnswer": "Just as God gave the green plants, He now gave everything that lives and moves as food",
            "reference": "Genesis 9:3",
            "explanation": "God said: 'Everything that lives and moves about will be food for you. Just as I gave you the green plants, I now give you everything.'"
        },
        {
            "id": "gen-9-q3", "questionNumber": 3,
            "question": "What strict dietary restriction was commanded regarding meat in Genesis 9:4?",
            "options": ["You must not cook it with salt", "You must not eat meat that has its lifeblood still in it", "You must not eat meat in winter", "You must not eat the fat"],
            "correctAnswerIndex": 1, "correctAnswer": "You must not eat meat that has its lifeblood still in it",
            "reference": "Genesis 9:4",
            "explanation": "Genesis 9:4 commands: 'But you must not eat meat that has its lifeblood still in it.'"
        },
        {
            "id": "gen-9-q4", "questionNumber": 4,
            "question": "Why does God demand an accounting for human life in Genesis 9:6 ('Whoever sheds human blood, by humans shall their blood be shed')?",
            "options": ["Because humans are weak", "Because in the image of God has God made mankind", "Because earth has limited space", "Because laws are necessary for trade"],
            "correctAnswerIndex": 1, "correctAnswer": "Because in the image of God has God made mankind",
            "reference": "Genesis 9:6",
            "explanation": "'Whoever sheds human blood, by humans shall their blood be shed; for in the image of God has God made mankind.'"
        },
        {
            "id": "gen-9-q5", "questionNumber": 5,
            "question": "With whom did God establish His covenant in Genesis 9:9–10?",
            "options": ["With Noah only", "With Noah, his descendants, and with every living creature that was with him", "With angels in heaven", "With the plants of the earth only"],
            "correctAnswerIndex": 1, "correctAnswer": "With Noah, his descendants, and with every living creature that was with him",
            "reference": "Genesis 9:9–10",
            "explanation": "God said, 'I now establish my covenant with you and with your descendants after you and with every living creature that was with you.'"
        },
        {
            "id": "gen-9-q6", "questionNumber": 6,
            "question": "What promise is at the heart of the covenant in Genesis 9:11?",
            "options": ["Never again will all life be destroyed by the waters of a flood; never again will there be a flood to destroy the earth", "That winter will never return", "That men will live 1000 years", "That the sun will never set"],
            "correctAnswerIndex": 0, "correctAnswer": "Never again will all life be destroyed by the waters of a flood; never again will there be a flood to destroy the earth",
            "reference": "Genesis 9:11",
            "explanation": "God promised: 'Never again will all life be destroyed by the waters of a flood; never again will there be a flood to destroy the earth.'"
        },
        {
            "id": "gen-9-q7", "questionNumber": 7,
            "question": "What visual sign did God set in the clouds as the token of His everlasting covenant?",
            "options": ["A pillar of smoke", "His rainbow in the clouds", "A blazing star", "A golden circle"],
            "correctAnswerIndex": 1, "correctAnswer": "His rainbow in the clouds",
            "reference": "Genesis 9:12–17",
            "explanation": "God said: 'I have set my rainbow in the clouds, and it will be the sign of the covenant between me and the earth.'"
        },
        {
            "id": "gen-9-q8", "questionNumber": 8,
            "question": "What did Noah plant, and what unfortunate incident followed in Genesis 9:20–21?",
            "options": ["An olive grove; he fell from a tree", "A vineyard; he drank some of its wine, became drunk, and lay uncovered inside his tent", "Wheat fields; locusts ate the crop", "Fig trees; he refused to share with his family"],
            "correctAnswerIndex": 1, "correctAnswer": "A vineyard; he drank some of its wine, became drunk, and lay uncovered inside his tent",
            "reference": "Genesis 9:20–21",
            "explanation": "Noah, a man of the soil, planted a vineyard. When he drank some of its wine, he became drunk and lay uncovered inside his tent."
        },
        {
            "id": "gen-9-q9", "questionNumber": 9,
            "question": "How did Shem and Japheth honor their father when Ham told them about his nakedness?",
            "options": ["They mocked him along with Ham", "They took a garment, walked backward, and covered their father's nakedness without looking at him", "They carried him out into the rain", "They called the neighbors"],
            "correctAnswerIndex": 1, "correctAnswer": "They took a garment, walked backward, and covered their father's nakedness without looking at him",
            "reference": "Genesis 9:23",
            "explanation": "Shem and Japheth took a garment and laid it across their shoulders; then they walked backward and covered their father’s naked body, keeping their faces turned away."
        },
        {
            "id": "gen-9-q10", "questionNumber": 10,
            "question": "How many years did Noah live in total before he died?",
            "options": ["600 years", "777 years", "950 years", "969 years"],
            "correctAnswerIndex": 2, "correctAnswer": "950 years",
            "reference": "Genesis 9:28–29",
            "explanation": "After the flood Noah lived 350 years. Altogether, Noah lived a total of 950 years, and then he died."
        }
    ]

    # Chapter 10
    data[10] = [
        {
            "id": "gen-10-q1", "questionNumber": 1,
            "question": "What is the common title given to the historical record in Genesis Chapter 10?",
            "options": ["The Book of the Wars of the Lord", "The Table of Nations (generations of Noah's sons)", "The Song of Moses", "The Law of the Priests"],
            "correctAnswerIndex": 1, "correctAnswer": "The Table of Nations (generations of Noah's sons)",
            "reference": "Genesis 10:1",
            "explanation": "Genesis 10 is traditionally known as the Table of Nations, listing the descendants of Shem, Ham, and Japheth through whom the nations spread after the Flood."
        },
        {
            "id": "gen-10-q2", "questionNumber": 2,
            "question": "Which son of Noah is associated with maritime coastland peoples such as Gomer, Magog, Madai, and Javan?",
            "options": ["Ham", "Shem", "Japheth", "Canaan"],
            "correctAnswerIndex": 2, "correctAnswer": "Japheth",
            "reference": "Genesis 10:2–5",
            "explanation": "From the sons of Japheth (Gomer, Magog, Madai, Javan, Tubal, Meshek, and Tiras) maritime peoples spread out into their territories by their clans within their nations."
        },
        {
            "id": "gen-10-q3", "questionNumber": 3,
            "question": "Who were the four primary sons of Ham listed in Genesis 10:6?",
            "options": ["Elam, Asshur, Arphaxad, Lud", "Cush, Mizraim (Egypt), Put, and Canaan", "Eber, Peleg, Joktan, Reu", "Gomer, Magog, Javan, Tubal"],
            "correctAnswerIndex": 1, "correctAnswer": "Cush, Mizraim (Egypt), Put, and Canaan",
            "reference": "Genesis 10:6",
            "explanation": "The sons of Ham were Cush, Egypt (Mizraim), Put, and Canaan."
        },
        {
            "id": "gen-10-q4", "questionNumber": 4,
            "question": "Who was Nimrod, and how is he famously described in Genesis 10:8–9?",
            "options": ["A humble shepherd in the desert", "A mighty warrior on the earth and a mighty hunter before the Lord", "A shipbuilder on the Mediterranean", "The high priest of Salem"],
            "correctAnswerIndex": 1, "correctAnswer": "A mighty warrior on the earth and a mighty hunter before the Lord",
            "reference": "Genesis 10:8–9",
            "explanation": "Cush was the father of Nimrod, who became a mighty warrior on the earth. He was a mighty hunter before the Lord."
        },
        {
            "id": "gen-10-q5", "questionNumber": 5,
            "question": "What cities formed the beginning of Nimrod's kingdom in the land of Shinar?",
            "options": ["Jerusalem, Hebron, Bethel, Shechem", "Babylon (Babel), Uruk (Erech), Akkad, and Kalneh", "Ur, Haran, Damascus, Tyre", "Nineveh, Tarshish, Sodom, Gomorrah"],
            "correctAnswerIndex": 1, "correctAnswer": "Babylon (Babel), Uruk (Erech), Akkad, and Kalneh",
            "reference": "Genesis 10:10",
            "explanation": "Genesis 10:10 states: 'The first centers of his kingdom were Babylon, Uruk, Akkad and Kalneh, in Shinar.'"
        },
        {
            "id": "gen-10-q6", "questionNumber": 6,
            "question": "From Nimrod's territory, who went into Assyria and built Nineveh and Calah?",
            "options": ["Canaan", "Asshur", "Japheth", "Peleg"],
            "correctAnswerIndex": 1, "correctAnswer": "Asshur",
            "reference": "Genesis 10:11–12",
            "explanation": "From that land he went to Assyria, where he built Nineveh, Rehoboth Ir, Calah and Resen."
        },
        {
            "id": "gen-10-q7", "questionNumber": 7,
            "question": "What infamous cities were included within the borders of the Canaanite clans in Genesis 10:19?",
            "options": ["Nineveh and Babylon", "Sodom, Gomorrah, Admah, and Zeboiim, as far as Lasha", "Tyre and Sidon exclusively", "Thebes and Memphis"],
            "correctAnswerIndex": 1, "correctAnswer": "Sodom, Gomorrah, Admah, and Zeboiim, as far as Lasha",
            "reference": "Genesis 10:19",
            "explanation": "The borders of Canaan reached from Sidon toward Gerar as far as Gaza, and then toward Sodom, Gomorrah, Admah and Zeboiim, as far as Lasha."
        },
        {
            "id": "gen-10-q8", "questionNumber": 8,
            "question": "Which son of Noah is designated as the ancestor of all the sons of Eber (the Semites/Hebrews)?",
            "options": ["Ham", "Japheth", "Shem", "Canaan"],
            "correctAnswerIndex": 2, "correctAnswer": "Shem",
            "reference": "Genesis 10:21",
            "explanation": "Sons were also born to Shem, whose older brother was Japheth; Shem was the ancestor of all the sons of Eber."
        },
        {
            "id": "gen-10-q9", "questionNumber": 9,
            "question": "Why was Eber's son named Peleg in Genesis 10:25?",
            "options": ["Because he was a mighty archer", "Because in his days the earth was divided", "Because he built a great altar", "Because he lived near the sea"],
            "correctAnswerIndex": 1, "correctAnswer": "Because in his days the earth was divided",
            "reference": "Genesis 10:25",
            "explanation": "One son was named Peleg, because in his time the earth was divided; his brother was named Joktan."
        },
        {
            "id": "gen-10-q10", "questionNumber": 10,
            "question": "How many total nation groups/clans are traditionally identified as originating from Noah's sons in Genesis 10?",
            "options": ["12 nations", "40 nations", "70 nations", "120 nations"],
            "correctAnswerIndex": 2, "correctAnswer": "70 nations",
            "reference": "Genesis 10:32",
            "explanation": "Genesis 10 enumerates 70 nations (14 Japhethite, 30 Hamitic, 26 Semitic), representing the totality of ancient post-flood humanity."
        }
    ]

    return data

if __name__ == "__main__":
    d = get_chapters_1_to_10()
    print(f"Chapters 1-10 ready: {len(d)} chapters.")
