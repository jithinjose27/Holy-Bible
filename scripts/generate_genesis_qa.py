import json
import os

OUTPUT_FILE = "src/data/genesis_qa.json"

# We will compile the 500 questions (50 chapters x 10 questions)
# Each question contains: id, questionNumber, question, options (4), correctAnswerIndex (0-3), correctAnswer, reference, explanation

def build_qa_dataset():
    chapters_qa = {}
    
    # -------------------------------------------------------------
    # Chapter 1: The Creation
    # -------------------------------------------------------------
    chapters_qa[1] = [
        {
            "id": "gen-1-q1",
            "questionNumber": 1,
            "question": "What did God create in the beginning according to Genesis 1:1?",
            "options": ["The heavens and the earth", "The sun and the stars", "The Garden of Eden", "The sea creatures and birds"],
            "correctAnswerIndex": 0,
            "correctAnswer": "The heavens and the earth",
            "reference": "Genesis 1:1",
            "explanation": "Genesis 1:1 declares: 'In the beginning God created the heavens and the earth.'"
        },
        {
            "id": "gen-1-q2",
            "questionNumber": 2,
            "question": "What did God command to appear on the first day of creation?",
            "options": ["Dry land", "Light", "The expanse / sky", "Vegetation"],
            "correctAnswerIndex": 1,
            "correctAnswer": "Light",
            "reference": "Genesis 1:3",
            "explanation": "God said, 'Let there be light,' and there was light, separating light from darkness on Day One."
        },
        {
            "id": "gen-1-q3",
            "questionNumber": 3,
            "question": "On the second day, what was created to separate the waters above from the waters below?",
            "options": ["A mountain barrier", "An expanse (firmament/sky)", "The ocean floor", "Clouds of vapor"],
            "correctAnswerIndex": 1,
            "correctAnswer": "An expanse (firmament/sky)",
            "reference": "Genesis 1:6–8",
            "explanation": "God made the expanse on Day Two to separate the waters under the expanse from the waters above it, calling it 'sky'."
        },
        {
            "id": "gen-1-q4",
            "questionNumber": 4,
            "question": "What two things appeared when the waters under the heavens gathered together on Day Three?",
            "options": ["Sun and moon", "Dry land (earth) and gathered seas", "Fish and whales", "Reptiles and cattle"],
            "correctAnswerIndex": 1,
            "correctAnswer": "Dry land (earth) and gathered seas",
            "reference": "Genesis 1:9–10",
            "explanation": "The waters gathered into one place and dry ground appeared; God called the dry ground 'land' and the gathered waters 'seas'."
        },
        {
            "id": "gen-1-q5",
            "questionNumber": 5,
            "question": "What kind of vegetation did the earth produce on the third day?",
            "options": ["Only moss and lichen", "Plants bearing seed and fruit trees bearing fruit according to their kinds", "Thorny briars and thistles", "Floating seaweed only"],
            "correctAnswerIndex": 1,
            "correctAnswer": "Plants bearing seed and fruit trees bearing fruit according to their kinds",
            "reference": "Genesis 1:11–12",
            "explanation": "The earth produced vegetation: seed-bearing plants and trees bearing fruit with seed in it according to their kinds."
        },
        {
            "id": "gen-1-q6",
            "questionNumber": 6,
            "question": "What purpose was given for the two great lights set in the expanse on the fourth day?",
            "options": ["To separate the day from the night and serve as signs for seasons, days, and years", "To illuminate only the angels", "To test the faith of mankind", "To consume the water of the deep"],
            "correctAnswerIndex": 0,
            "correctAnswer": "To separate the day from the night and serve as signs for seasons, days, and years",
            "reference": "Genesis 1:14–18",
            "explanation": "God set lights in the expanse to separate day from night, govern the day and night, and serve as signs to mark sacred times, days, and years."
        },
        {
            "id": "gen-1-q7",
            "questionNumber": 7,
            "question": "Which living creatures were created on the fifth day?",
            "options": ["Cattle and beasts of the field", "Creatures that swarm in the waters and winged birds that fly above the earth", "Creeping insects and reptiles", "Human beings"],
            "correctAnswerIndex": 1,
            "correctAnswer": "Creatures that swarm in the waters and winged birds that fly above the earth",
            "reference": "Genesis 1:20–22",
            "explanation": "On Day Five, God created great sea creatures and every living thing with which the waters teem, as well as winged birds."
        },
        {
            "id": "gen-1-q8",
            "questionNumber": 8,
            "question": "Before creating humanity on Day Six, what category of creatures did God make?",
            "options": ["Fish and sea monsters", "Livestock, creeping things, and beasts of the earth according to their kinds", "Celestial beings", "Coral reefs"],
            "correctAnswerIndex": 1,
            "correctAnswer": "Livestock, creeping things, and beasts of the earth according to their kinds",
            "reference": "Genesis 1:24–25",
            "explanation": "God commanded the earth to produce living creatures according to their kinds: livestock, creatures that move along the ground, and wild animals."
        },
        {
            "id": "gen-1-q9",
            "questionNumber": 9,
            "question": "According to Genesis 1:26–27, in whose image and likeness was humanity created?",
            "options": ["In the image of the angels", "In the image and likeness of God", "In the image of the stars", "In the likeness of the beasts"],
            "correctAnswerIndex": 1,
            "correctAnswer": "In the image and likeness of God",
            "reference": "Genesis 1:26–27",
            "explanation": "God said, 'Let us make mankind in our image, in our likeness.' Male and female He created them in the image of God."
        },
        {
            "id": "gen-1-q10",
            "questionNumber": 10,
            "question": "How did God evaluate everything that He had made at the conclusion of Day Six?",
            "options": ["It was imperfect", "It was partially good", "It was very good", "It was incomplete"],
            "correctAnswerIndex": 2,
            "correctAnswer": "It was very good",
            "reference": "Genesis 1:31",
            "explanation": "Genesis 1:31 states: 'God saw all that he had made, and it was very good. And there was evening, and there was morning—the sixth day.'"
        }
    ]

    # -------------------------------------------------------------
    # Chapter 2: The Garden of Eden & The First Union
    # -------------------------------------------------------------
    chapters_qa[2] = [
        {
            "id": "gen-2-q1",
            "questionNumber": 1,
            "question": "What did God do on the seventh day after finishing the work of creation?",
            "options": ["He planted another world", "He rested from all His work, blessed the seventh day, and made it holy", "He created more animals", "He sent rain over the earth"],
            "correctAnswerIndex": 1,
            "correctAnswer": "He rested from all His work, blessed the seventh day, and made it holy",
            "reference": "Genesis 2:2–3",
            "explanation": "By the seventh day God completed His work, rested from all His labor, blessed the seventh day, and sanctified it."
        },
        {
            "id": "gen-2-q2",
            "questionNumber": 2,
            "question": "How was the ground watered before rain had fallen upon the earth?",
            "options": ["By underground pipes", "A mist (or spring) went up from the earth and watered the whole surface", "By melting glaciers", "By ocean tsunamis"],
            "correctAnswerIndex": 1,
            "correctAnswer": "A mist (or spring) went up from the earth and watered the whole surface",
            "reference": "Genesis 2:5–6",
            "explanation": "The Lord God had not yet caused it to rain, but a mist or stream came up from the earth and watered the whole face of the ground."
        },
        {
            "id": "gen-2-q3",
            "questionNumber": 3,
            "question": "From what did the Lord God form the first man, and how did he become a living soul?",
            "options": ["From gold and silver, energized by lightning", "From the dust of the ground, and breathed into his nostrils the breath of life", "From sea foam, infused by celestial light", "From the bark of the Tree of Life"],
            "correctAnswerIndex": 1,
            "correctAnswer": "From the dust of the ground, and breathed into his nostrils the breath of life",
            "reference": "Genesis 2:7",
            "explanation": "The Lord God formed man of the dust of the ground and breathed into his nostrils the breath of life, and man became a living soul."
        },
        {
            "id": "gen-2-q4",
            "questionNumber": 4,
            "question": "Where did the Lord God plant the garden for man, and in which direction?",
            "options": ["In the desert to the west", "Eastward, in Eden", "On Mount Ararat to the north", "In the land of Ur"],
            "correctAnswerIndex": 1,
            "correctAnswer": "Eastward, in Eden",
            "reference": "Genesis 2:8",
            "explanation": "Genesis 2:8 states that the Lord God planted a garden eastward in Eden, placing the man He had formed there."
        },
        {
            "id": "gen-2-q5",
            "questionNumber": 5,
            "question": "Which two special trees are specifically named as growing in the midst of the Garden of Eden?",
            "options": ["The Cedar of Lebanon and the Olive Tree", "The Tree of Life and the Tree of the Knowledge of Good and Evil", "The Fig Tree and the Oak Tree", "The Almond Tree and the Palm Tree"],
            "correctAnswerIndex": 1,
            "correctAnswer": "The Tree of Life and the Tree of the Knowledge of Good and Evil",
            "reference": "Genesis 2:9",
            "explanation": "In the middle of the garden were the Tree of Life and the Tree of the Knowledge of Good and Evil."
        },
        {
            "id": "gen-2-q6",
            "questionNumber": 6,
            "question": "How many headwaters did the river flowing out of Eden divide into, and what were their names?",
            "options": ["Two: Nile and Jordan", "Three: Red Sea, Dead Sea, Mediterranean", "Four: Pishon, Gihon, Tigris (Hiddekel), and Euphrates", "Seven rivers"],
            "correctAnswerIndex": 2,
            "correctAnswer": "Four: Pishon, Gihon, Tigris (Hiddekel), and Euphrates",
            "reference": "Genesis 2:10–14",
            "explanation": "A river flowed from Eden to water the garden, dividing from there into four heads: Pishon, Gihon, Tigris, and Euphrates."
        },
        {
            "id": "gen-2-q7",
            "questionNumber": 7,
            "question": "What primary duty did God give Adam when placing him into the Garden of Eden?",
            "options": ["To build a fortress city", "To cultivate (dress) and keep (guard) the garden", "To build a boat for trade", "To hunt the animals for leather"],
            "correctAnswerIndex": 1,
            "correctAnswer": "To cultivate (dress) and keep (guard) the garden",
            "reference": "Genesis 2:15",
            "explanation": "The Lord God took the man and placed him in the Garden of Eden to tend and keep it."
        },
        {
            "id": "gen-2-q8",
            "questionNumber": 8,
            "question": "What command and consequence did God give to Adam regarding the Tree of the Knowledge of Good and Evil?",
            "options": ["He could eat it on the Sabbath", "He must not eat of it; for in the day he eats of it he would surely die", "He could eat the leaves but not the fruit", "He must burn its branches"],
            "correctAnswerIndex": 1,
            "correctAnswer": "He must not eat of it; for in the day he eats of it he would surely die",
            "reference": "Genesis 2:16–17",
            "explanation": "God commanded: 'You must not eat from the tree of the knowledge of good and evil, for when you eat from it you will certainly die.'"
        },
        {
            "id": "gen-2-q9",
            "questionNumber": 9,
            "question": "What observation did the Lord God make before bringing the animals to Adam to be named?",
            "options": ["'The garden needs more flowers'", "'It is not good that the man should be alone; I will make him an help meet for him'", "'The animals need masters'", "'Man is too wise'"],
            "correctAnswerIndex": 1,
            "correctAnswer": "'It is not good that the man should be alone; I will make him an help meet for him'",
            "reference": "Genesis 2:18",
            "explanation": "The Lord God said, 'It is not good for the man to be alone. I will make a helper suitable for him.'"
        },
        {
            "id": "gen-2-q10",
            "questionNumber": 10,
            "question": "How was the first woman created, and what was Adam's joyful response?",
            "options": ["From clay by the riverbank; Adam called her sister", "From one of Adam's ribs during a deep sleep; Adam declared: 'This is now bone of my bones, and flesh of my flesh'", "From a sunbeam; Adam called her daughter", "She descended from heaven on a chariot"],
            "correctAnswerIndex": 1,
            "correctAnswer": "From one of Adam's ribs during a deep sleep; Adam declared: 'This is now bone of my bones, and flesh of my flesh'",
            "reference": "Genesis 2:21–23",
            "explanation": "God caused a deep sleep to fall on Adam, took one of his ribs, and made it into a woman. Adam exclaimed: 'This is now bone of my bones and flesh of my flesh; she shall be called Woman!'"
        }
    ]

    return chapters_qa

if __name__ == "__main__":
    qa_data = build_qa_dataset()
    print(f"Generated Q&A for {len(qa_data)} chapters.")
