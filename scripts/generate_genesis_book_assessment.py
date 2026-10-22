import json
import os

questions = [
    # --- Part 1: Primeval History (Genesis 1-11) ---
    {
        "id": "gen-book-q1",
        "questionNumber": 1,
        "question": "What phrase is repeatedly used by God at the end of each creative act in Genesis 1 to evaluate His creation?",
        "options": [
            "And God saw that it was good",
            "And heaven and earth were glad",
            "And the work was established forever",
            "And God rested from His labor"
        ],
        "correctAnswerIndex": 0,
        "correctAnswer": "And God saw that it was good",
        "reference": "Genesis 1:4, 10, 12, 18, 21, 25, 31",
        "explanation": "Throughout Genesis 1, God examines His creative work and repeatedly declares it 'good', concluding on Day Six that everything was 'very good'."
    },
    {
        "id": "gen-book-q2",
        "questionNumber": 2,
        "question": "On which day of creation did God create man and woman in His own image and give them dominion over the earth?",
        "options": [
            "Fourth day",
            "Fifth day",
            "Sixth day",
            "Seventh day"
        ],
        "correctAnswerIndex": 2,
        "correctAnswer": "Sixth day",
        "reference": "Genesis 1:26–31",
        "explanation": "God created humanity (male and female) on the sixth day of creation, giving them responsibility over living creatures."
    },
    {
        "id": "gen-book-q3",
        "questionNumber": 3,
        "question": "Which tree were Adam and Eve specifically commanded NOT to eat from in the Garden of Eden?",
        "options": [
            "The Tree of Life",
            "The Tree of the Knowledge of Good and Evil",
            "The Tree of Eternal Wisdom",
            "The Tree of Celestial Fruit"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "The Tree of the Knowledge of Good and Evil",
        "reference": "Genesis 2:16–17",
        "explanation": "The LORD God commanded Adam that he could eat freely of every tree except the tree of the knowledge of good and evil."
    },
    {
        "id": "gen-book-q4",
        "questionNumber": 4,
        "question": "What consequence did God pronounce on the serpent immediately following the Fall in Genesis 3?",
        "options": [
            "It would be banished to the barren wilderness",
            "It would crawl upon its belly and eat dust all the days of its life",
            "Its voice would be silenced forever",
            "It would have no offspring on the earth"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "It would crawl upon its belly and eat dust all the days of its life",
        "reference": "Genesis 3:14",
        "explanation": "In Genesis 3:14, the LORD God cursed the serpent to go upon its belly and eat dust all the days of its life."
    },
    {
        "id": "gen-book-q5",
        "questionNumber": 5,
        "question": "Why did Cain kill his brother Abel in Genesis 4?",
        "options": [
            "They fought over their boundary stones",
            "Cain was angry because God accepted Abel's offering but not his own",
            "Abel took Cain's inheritance",
            "God instructed Cain to test Abel"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Cain was angry because God accepted Abel's offering but not his own",
        "reference": "Genesis 4:3–8",
        "explanation": "Cain grew angry and envious because the LORD had regard for Abel and his firstling offering, but not for Cain and his offering."
    },
    {
        "id": "gen-book-q6",
        "questionNumber": 6,
        "question": "Which patriarch in Genesis 5 is recorded as having 'walked with God, and he was not, for God took him' without dying a physical death?",
        "options": [
            "Methuselah",
            "Enoch",
            "Jared",
            "Lamech"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Enoch",
        "reference": "Genesis 5:24",
        "explanation": "Genesis 5:24 states that Enoch walked with God; then he was no more, because God took him away without recording his death."
    },
    {
        "id": "gen-book-q7",
        "questionNumber": 7,
        "question": "Who was the oldest man mentioned in the Bible, living a total of 969 years according to Genesis 5?",
        "options": [
            "Adam",
            "Noah",
            "Methuselah",
            "Seth"
        ],
        "correctAnswerIndex": 2,
        "correctAnswer": "Methuselah",
        "reference": "Genesis 5:27",
        "explanation": "Methuselah lived for 969 years before he died, making him the longest-lived individual recorded in Scripture."
    },
    {
        "id": "gen-book-q8",
        "questionNumber": 8,
        "question": "What type of wood was Noah commanded to use to build the Ark?",
        "options": [
            "Cedar of Lebanon",
            "Acacia wood",
            "Gopher wood",
            "Oak wood"
        ],
        "correctAnswerIndex": 2,
        "correctAnswer": "Gopher wood",
        "reference": "Genesis 6:14",
        "explanation": "God commanded Noah to build an ark of gopher wood, with rooms coated inside and out with pitch."
    },
    {
        "id": "gen-book-q9",
        "questionNumber": 9,
        "question": "How many human souls in total were saved aboard Noah's Ark through the Great Flood?",
        "options": [
            "Four",
            "Eight",
            "Twelve",
            "Seventy"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Eight",
        "reference": "Genesis 7:13; 1 Peter 3:20",
        "explanation": "Noah, his wife, his three sons (Shem, Ham, Japheth), and their three wives made a total of eight people saved in the Ark."
    },
    {
        "id": "gen-book-q10",
        "questionNumber": 10,
        "question": "On which mountains did Noah's Ark come to rest after the waters abated in Genesis 8?",
        "options": [
            "Mount Sinai",
            "Mountains of Ararat",
            "Mount Moriah",
            "Mount Nebo"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Mountains of Ararat",
        "reference": "Genesis 8:4",
        "explanation": "The ark rested in the seventh month, on the seventeenth day of the month, upon the mountains of Ararat."
    },
    {
        "id": "gen-book-q11",
        "questionNumber": 11,
        "question": "What sign did God establish in the clouds as a token of His everlasting covenant never again to destroy all flesh with a flood?",
        "options": [
            "A pillar of fire",
            "The rainbow",
            "A golden constellation",
            "A dove with an olive leaf"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "The rainbow",
        "reference": "Genesis 9:12–17",
        "explanation": "God set His bow in the cloud as the sign of the covenant between God and the earth that floodwaters would never again destroy all life."
    },
    {
        "id": "gen-book-q12",
        "questionNumber": 12,
        "question": "What was the purpose of the people constructing the Tower of Babel in the land of Shinar in Genesis 11?",
        "options": [
            "To escape future floodwaters",
            "To build a city and a tower reaching to heaven and make a name for themselves",
            "To worship the sun and moon",
            "To store grain for impending famines"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "To build a city and a tower reaching to heaven and make a name for themselves",
        "reference": "Genesis 11:4",
        "explanation": "The people said, 'Come, let us build ourselves a city and a tower with its top in the heavens, and let us make a name for ourselves, lest we be dispersed.'"
    },

    # --- Part 2: Abraham and Sarah (Genesis 12-25) ---
    {
        "id": "gen-book-q13",
        "questionNumber": 13,
        "question": "How old was Abram when God called him to leave his country and family in Haran to go to Canaan?",
        "options": [
            "50 years old",
            "75 years old",
            "99 years old",
            "100 years old"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "75 years old",
        "reference": "Genesis 12:4",
        "explanation": "Genesis 12:4 records that Abram was 75 years old when he departed out of Haran following God's call."
    },
    {
        "id": "gen-book-q14",
        "questionNumber": 14,
        "question": "Who was the King of Salem and priest of God Most High who brought out bread and wine to bless Abram in Genesis 14?",
        "options": [
            "Abimelech",
            "Melchizedek",
            "Jethro",
            "Eliezer"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Melchizedek",
        "reference": "Genesis 14:18–20",
        "explanation": "Melchizedek king of Salem, priest of God Most High, blessed Abram, and Abram gave him a tenth of everything."
    },
    {
        "id": "gen-book-q15",
        "questionNumber": 15,
        "question": "What key verse in Genesis 15 states that Abram's faith was accounted to him for righteousness?",
        "options": [
            "Genesis 12:3",
            "Genesis 15:6",
            "Genesis 17:1",
            "Genesis 22:12"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Genesis 15:6",
        "reference": "Genesis 15:6",
        "explanation": "Genesis 15:6 declares: 'And he believed the LORD, and he counted it to him as righteousness.'"
    },
    {
        "id": "gen-book-q16",
        "questionNumber": 16,
        "question": "Who was Hagar, and what was the name of the son she bore to Abram in Genesis 16?",
        "options": [
            "Sarai's Egyptian maidservant; Ishmael",
            "A woman of Canaan; Isaac",
            "A priestess from Ur; Midian",
            "Lot's daughter; Moab"
        ],
        "correctAnswerIndex": 0,
        "correctAnswer": "Sarai's Egyptian maidservant; Ishmael",
        "reference": "Genesis 16:1–15",
        "explanation": "Hagar was Sarai's Egyptian maid who bore Abram a son named Ishmael when Abram was 86 years old."
    },
    {
        "id": "gen-book-q17",
        "questionNumber": 17,
        "question": "What physical sign did God institute in Genesis 17 as the token of His covenant with Abraham and his descendants?",
        "options": [
            "A rainbow in the sky",
            "Circumcision of every male",
            "Anointing with consecrated oil",
            "Wearing blue tassels"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Circumcision of every male",
        "reference": "Genesis 17:9–14",
        "explanation": "God instituted circumcision on the eighth day for every male child as the sign of the covenant between God and Abraham's descendants."
    },
    {
        "id": "gen-book-q18",
        "questionNumber": 18,
        "question": "For the sake of how many righteous people did the LORD ultimately agree to spare Sodom in Abraham's intercession in Genesis 18?",
        "options": [
            "Fifty",
            "Thirty",
            "Twenty",
            "Ten"
        ],
        "correctAnswerIndex": 3,
        "correctAnswer": "Ten",
        "reference": "Genesis 18:32",
        "explanation": "Abraham progressively interceded from fifty down to ten, and the LORD promised: 'For the sake of ten I will not destroy it.'"
    },
    {
        "id": "gen-book-q19",
        "questionNumber": 19,
        "question": "What happened to Lot's wife when she looked back toward burning Sodom contrary to the angels' command in Genesis 19?",
        "options": [
            "She was blinded by the smoke",
            "She became a pillar of salt",
            "She was swallowed up by an earthquake",
            "She turned into a desert rock"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "She became a pillar of salt",
        "reference": "Genesis 19:26",
        "explanation": "Genesis 19:26 records that Lot's wife looked back from behind him, and she became a pillar of salt."
    },
    {
        "id": "gen-book-q20",
        "questionNumber": 20,
        "question": "How old were Abraham and Sarah when their promised son Isaac was born in Genesis 21?",
        "options": [
            "Abraham was 75, Sarah was 65",
            "Abraham was 90, Sarah was 80",
            "Abraham was 100, Sarah was 90",
            "Abraham was 120, Sarah was 110"
        ],
        "correctAnswerIndex": 2,
        "correctAnswer": "Abraham was 100, Sarah was 90",
        "reference": "Genesis 17:17; 21:5",
        "explanation": "Abraham was 100 years old when his son Isaac was born to him, and Sarah was 90 years old."
    },
    {
        "id": "gen-book-q21",
        "questionNumber": 21,
        "question": "Where did God command Abraham to take Isaac to offer him as a burnt offering in Genesis 22?",
        "options": [
            "Mount Sinai",
            "The land of Moriah",
            "Mount Carmel",
            "The wilderness of Paran"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "The land of Moriah",
        "reference": "Genesis 22:2",
        "explanation": "God told Abraham: 'Take now your son, your only son Isaac, whom you love, and go to the land of Moriah, and offer him there as a burnt offering.'"
    },
    {
        "id": "gen-book-q22",
        "questionNumber": 22,
        "question": "What did Abraham sacrifice in place of his son Isaac after the angel of the LORD stopped him in Genesis 22?",
        "options": [
            "A bullock from his herds",
            "A ram caught in a thicket by its horns",
            "A young lamb without blemish",
            "Two turtledoves"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "A ram caught in a thicket by its horns",
        "reference": "Genesis 22:13",
        "explanation": "Abraham looked up and saw behind him a ram caught in a thicket by its horns, which he offered as a burnt offering instead of his son."
    },
    {
        "id": "gen-book-q23",
        "questionNumber": 23,
        "question": "What piece of property did Abraham purchase from Ephron the Hittite to bury Sarah in Genesis 23?",
        "options": [
            "The well of Beersheba",
            "The cave of Machpelah near Mamre (Hebron)",
            "The threshing floor of Araunah",
            "The oaks of Moreh at Shechem"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "The cave of Machpelah near Mamre (Hebron)",
        "reference": "Genesis 23:17–20",
        "explanation": "Abraham weighed out 400 shekels of silver to purchase the field and cave of Machpelah facing Mamre as a permanent burial possession."
    },
    {
        "id": "gen-book-q24",
        "questionNumber": 24,
        "question": "How did Abraham's senior servant identify Rebekah as the chosen bride for Isaac at the well in Genesis 24?",
        "options": [
            "She was wearing a golden veil",
            "She offered water to him and drew water for all his camels as well",
            "She addressed him by his Hebrew name",
            "She recited the blessing of Abraham"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "She offered water to him and drew water for all his camels as well",
        "reference": "Genesis 24:14–20",
        "explanation": "The servant prayed for a sign: the maiden who offered him a drink and offered to water his camels also would be the one appointed for Isaac."
    },

    # --- Part 3: Isaac and Jacob (Genesis 25-36) ---
    {
        "id": "gen-book-q25",
        "questionNumber": 25,
        "question": "What did Esau sell his birthright to his twin brother Jacob for in Genesis 25?",
        "options": [
            "A flock of prize sheep",
            "A bowl of red lentil stew and bread",
            "Thirty pieces of silver",
            "A coat of dyed wool"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "A bowl of red lentil stew and bread",
        "reference": "Genesis 25:29–34",
        "explanation": "Returning exhausted and famished from hunting, Esau sold his birthright to Jacob for some bread and red lentil stew."
    },
    {
        "id": "gen-book-q26",
        "questionNumber": 26,
        "question": "How did Jacob deceive his blind father Isaac to steal Esau's blessing in Genesis 27?",
        "options": [
            "He spoke with an altered accent",
            "He wore Esau's best garments and covered his hands and neck with goatskins",
            "He claimed Esau had renounced the blessing",
            "He brought an official scroll written by Rebekah"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "He wore Esau's best garments and covered his hands and neck with goatskins",
        "reference": "Genesis 27:15–16",
        "explanation": "Rebekah put Esau's clothes on Jacob and covered his smooth hands and neck with the skins of young goats so Isaac would feel hair like Esau."
    },
    {
        "id": "gen-book-q27",
        "questionNumber": 27,
        "question": "What did Jacob see in his dream at Bethel while fleeing from Esau toward Haran in Genesis 28?",
        "options": [
            "A burning bush that was not consumed",
            "A ladder set upon the earth reaching to heaven, with angels ascending and descending",
            "Seven golden lampstands",
            "A chariot of fire in the sky"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "A ladder set upon the earth reaching to heaven, with angels ascending and descending",
        "reference": "Genesis 28:12",
        "explanation": "Jacob dreamed of a ladder set up on the earth reaching to heaven, with the angels of God ascending and descending on it, and the LORD standing above it."
    },
    {
        "id": "gen-book-q28",
        "questionNumber": 28,
        "question": "How did Laban deceive Jacob on his wedding night after Jacob served seven years for Rachel in Genesis 29?",
        "options": [
            "He demanded double the dowry",
            "He gave him Leah, the older sister, instead of Rachel",
            "He postponed the wedding another year",
            "He sent him away with no bride"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "He gave him Leah, the older sister, instead of Rachel",
        "reference": "Genesis 29:21–25",
        "explanation": "In the darkness of evening, Laban brought his older daughter Leah to Jacob, explaining that in their country the younger daughter could not be given before the firstborn."
    },
    {
        "id": "gen-book-q29",
        "questionNumber": 29,
        "question": "Who was Jacob's firstborn son born to Leah in Genesis 29?",
        "options": [
            "Simeon",
            "Levi",
            "Judah",
            "Reuben"
        ],
        "correctAnswerIndex": 3,
        "correctAnswer": "Reuben",
        "reference": "Genesis 29:32",
        "explanation": "Leah conceived and bore a son and named him Reuben, saying, 'Because the LORD has looked upon my affliction.'"
    },
    {
        "id": "gen-book-q30",
        "questionNumber": 30,
        "question": "What were the names of the two sons born to Rachel in Genesis 30 and 35?",
        "options": [
            "Dan and Naphtali",
            "Joseph and Benjamin",
            "Gad and Asher",
            "Ephraim and Manasseh"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Joseph and Benjamin",
        "reference": "Genesis 30:22–24; 35:16–18",
        "explanation": "Rachel gave birth to Joseph in Paddan-aram, and later died giving birth to Benjamin on the way to Ephrath (Bethlehem)."
    },
    {
        "id": "gen-book-q31",
        "questionNumber": 31,
        "question": "What new name was given to Jacob after he wrestled with a man until daybreak at the ford of Jabbok in Genesis 32?",
        "options": [
            "Israel",
            "Abraham",
            "Jeshurun",
            "Ephraim"
        ],
        "correctAnswerIndex": 0,
        "correctAnswer": "Israel",
        "reference": "Genesis 32:28",
        "explanation": "The man said to him: 'Your name shall no longer be called Jacob, but Israel, for you have striven with God and with men, and have prevailed.'"
    },
    {
        "id": "gen-book-q32",
        "questionNumber": 32,
        "question": "What physical ailment did Jacob sustain from his encounter at Peniel?",
        "options": [
            "Loss of sight in one eye",
            "His hip socket was dislocated, causing him to limp",
            "A withered hand",
            "Temporary loss of speech"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "His hip socket was dislocated, causing him to limp",
        "reference": "Genesis 32:25, 31",
        "explanation": "The man touched the socket of Jacob's hip, dislocating it as he wrestled, so Jacob limped as he passed Penuel."
    },
    {
        "id": "gen-book-q33",
        "questionNumber": 33,
        "question": "How did Esau react when he finally met his brother Jacob in Genesis 33 after twenty years of separation?",
        "options": [
            "He attacked Jacob's camp with 400 men",
            "He ran to meet him, embraced him, fell on his neck, kissed him, and wept",
            "He refused to look at Jacob until gifts were paid",
            "He demanded half of Jacob's flocks"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "He ran to meet him, embraced him, fell on his neck, kissed him, and wept",
        "reference": "Genesis 33:4",
        "explanation": "Instead of seeking vengeance, Esau ran to meet Jacob, embraced him, threw his arms around his neck, kissed him, and they wept together."
    },
    {
        "id": "gen-book-q34",
        "questionNumber": 34,
        "question": "Which two sons of Jacob took their swords and slaughtered the men of Shechem to avenge their sister Dinah in Genesis 34?",
        "options": [
            "Reuben and Judah",
            "Simeon and Levi",
            "Dan and Naphtali",
            "Issachar and Zebulun"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Simeon and Levi",
        "reference": "Genesis 34:25–26",
        "explanation": "On the third day, Simeon and Levi, Dinah's full brothers, took their swords, attacked the unsuspecting city, and killed every male."
    },

    # --- Part 4: Joseph and His Brothers (Genesis 37-50) ---
    {
        "id": "gen-book-q35",
        "questionNumber": 35,
        "question": "Why did Joseph's brothers hate him even before he told them his dreams in Genesis 37?",
        "options": [
            "Joseph took their flocks to another land",
            "Jacob loved Joseph more than all his sons and made him a richly ornamented coat",
            "Joseph refused to work in the fields",
            "Joseph claimed the rights of the firstborn"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Jacob loved Joseph more than all his sons and made him a richly ornamented coat",
        "reference": "Genesis 37:3–4",
        "explanation": "Israel loved Joseph more than any of his other sons because he was born in his old age, and gave him an ornate robe, provoking his brothers' hatred."
    },
    {
        "id": "gen-book-q36",
        "questionNumber": 36,
        "question": "What did Joseph see bowing down to him in his two prophetic dreams in Genesis 37?",
        "options": [
            "Twelve cedar trees, and then twelve mountains",
            "Sheaves of grain, and then the sun, moon, and eleven stars",
            "Twelve silver chalices, and then twelve crowns",
            "Twelve eagles, and then a cloud of fire"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Sheaves of grain, and then the sun, moon, and eleven stars",
        "reference": "Genesis 37:5–9",
        "explanation": "Joseph dreamed that his brothers' sheaves bowed down to his sheaf, and later that the sun, moon, and eleven stars bowed down to him."
    },
    {
        "id": "gen-book-q37",
        "questionNumber": 37,
        "question": "For how much silver did Joseph's brothers sell him to the Ishmaelite/Midianite merchants in Genesis 37?",
        "options": [
            "Ten shekels",
            "Twenty shekels",
            "Thirty shekels",
            "Fifty shekels"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Twenty shekels",
        "reference": "Genesis 37:28",
        "explanation": "Genesis 37:28 states that the brothers pulled Joseph up out of the pit and sold him to the Ishmaelites for twenty shekels of silver."
    },
    {
        "id": "gen-book-q38",
        "questionNumber": 38,
        "question": "Who bought Joseph in Egypt as a servant from the Midianite traders?",
        "options": [
            "Pharaoh himself",
            "Potiphar, an officer of Pharaoh and captain of the guard",
            "The chief baker of Egypt",
            "The high priest of On"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Potiphar, an officer of Pharaoh and captain of the guard",
        "reference": "Genesis 37:36; 39:1",
        "explanation": "Potiphar, an Egyptian officer of Pharaoh and captain of the guard, bought Joseph from the Ishmaelites who had brought him down."
    },
    {
        "id": "gen-book-q39",
        "questionNumber": 39,
        "question": "Why was Joseph thrown into the royal prison in Genesis 39 despite having done nothing wrong?",
        "options": [
            "He was accused of stealing Potiphar's silver",
            "Potiphar's wife falsely accused him after he fled from her advances",
            "He interpreted a dream predicting Pharaoh's downfall",
            "He refused to bow to the Egyptian gods"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Potiphar's wife falsely accused him after he fled from her advances",
        "reference": "Genesis 39:7–20",
        "explanation": "When Joseph refused Potiphar's wife's seductions and ran out leaving his garment, she falsely accused him, and Potiphar cast him into prison."
    },
    {
        "id": "gen-book-q40",
        "questionNumber": 40,
        "question": "Whose dreams did Joseph interpret while imprisoned in Genesis 40?",
        "options": [
            "The prison warden and the royal scribe",
            "Pharaoh's chief cupbearer and chief baker",
            "Two Midianite prisoners of war",
            "The captain of the guard and his son"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Pharaoh's chief cupbearer and chief baker",
        "reference": "Genesis 40:1–23",
        "explanation": "Joseph accurately interpreted the dreams of Pharaoh's chief cupbearer (restoration in three days) and chief baker (execution in three days)."
    },
    {
        "id": "gen-book-q41",
        "questionNumber": 41,
        "question": "What did Pharaoh's dreams of seven fat cows eaten by seven lean cows, and seven full heads of grain swallowed by seven thin heads, signify in Genesis 41?",
        "options": [
            "Seven years of war followed by seven years of peace",
            "Seven years of great abundance followed by seven years of severe famine",
            "Seven foreign kings arriving in Egypt",
            "Seven plagues that would strike the Nile"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Seven years of great abundance followed by seven years of severe famine",
        "reference": "Genesis 41:25–32",
        "explanation": "Joseph revealed that God was showing Pharaoh that seven years of great plenty throughout all Egypt would be followed by seven years of devastating famine."
    },
    {
        "id": "gen-book-q42",
        "questionNumber": 42,
        "question": "How old was Joseph when he entered Pharaoh's service and was appointed ruler over all the land of Egypt in Genesis 41?",
        "options": [
            "20 years old",
            "30 years old",
            "40 years old",
            "50 years old"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "30 years old",
        "reference": "Genesis 41:46",
        "explanation": "Genesis 41:46 records: 'Joseph was thirty years old when he stood before Pharaoh king of Egypt.'"
    },
    {
        "id": "gen-book-q43",
        "questionNumber": 43,
        "question": "What were the names of Joseph's two sons born in Egypt before the years of famine arrived?",
        "options": [
            "Ephraim and Manasseh",
            "Manasseh and Ephraim",
            "Gershom and Eliezer",
            "Nadab and Abihu"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Manasseh and Ephraim",
        "reference": "Genesis 41:50–52",
        "explanation": "Joseph named his firstborn Manasseh ('God has made me forget all my hardship') and his second son Ephraim ('God has made me fruitful in the land of my suffering')."
    },
    {
        "id": "gen-book-q44",
        "questionNumber": 44,
        "question": "Which brother did Joseph keep bound as a hostage in Egypt while the others returned to Canaan to bring Benjamin in Genesis 42?",
        "options": [
            "Reuben",
            "Simeon",
            "Judah",
            "Levi"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Simeon",
        "reference": "Genesis 42:24",
        "explanation": "Joseph took Simeon from them and bound him before their eyes as security that they would return with Benjamin."
    },
    {
        "id": "gen-book-q45",
        "questionNumber": 45,
        "question": "In whose sack was Joseph's personal silver divining cup discovered when the brothers departed Egypt in Genesis 44?",
        "options": [
            "Reuben's sack",
            "Judah's sack",
            "Benjamin's sack",
            "Simeon's sack"
        ],
        "correctAnswerIndex": 2,
        "correctAnswer": "Benjamin's sack",
        "reference": "Genesis 44:11–12",
        "explanation": "Joseph's steward searched beginning with the oldest and ending with the youngest, and the silver cup was found in Benjamin's sack."
    },
    {
        "id": "gen-book-q46",
        "questionNumber": 46,
        "question": "Which brother stepped forward in Genesis 44 and offered to become Joseph's slave in place of Benjamin to spare their father's grief?",
        "options": [
            "Reuben",
            "Judah",
            "Levi",
            "Dan"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "Judah",
        "reference": "Genesis 44:33–34",
        "explanation": "Judah pleaded with Joseph to let Benjamin return with his brothers while Judah remained as a slave in his place, demonstrating complete transformation."
    },
    {
        "id": "gen-book-q47",
        "questionNumber": 47,
        "question": "In which region of Egypt did Pharaoh allow Jacob and his family to settle and graze their flocks in Genesis 47?",
        "options": [
            "The land of Goshen",
            "The city of Alexandria",
            "The valley of Memphis",
            "The delta of Thebes"
        ],
        "correctAnswerIndex": 0,
        "correctAnswer": "The land of Goshen",
        "reference": "Genesis 47:5–6",
        "explanation": "Pharaoh told Joseph: 'The land of Egypt is before you. Settle your father and your brothers in the best of the land. Let them dwell in the land of Goshen.'"
    },
    {
        "id": "gen-book-q48",
        "questionNumber": 48,
        "question": "When Jacob blessed Joseph's sons in Genesis 48, what unexpected gesture did he make?",
        "options": [
            "He placed both hands on Manasseh's head",
            "He intentionally crossed his hands, putting his right hand on younger Ephraim and his left on firstborn Manasseh",
            "He refused to bless them until they received circumcision",
            "He gave Joseph's coat to Manasseh"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "He intentionally crossed his hands, putting his right hand on younger Ephraim and his left on firstborn Manasseh",
        "reference": "Genesis 48:13–19",
        "explanation": "Israel stretched out his right hand and laid it on Ephraim's head, who was the younger, and his left hand on Manasseh's head, crossing his hands knowingly."
    },
    {
        "id": "gen-book-q49",
        "questionNumber": 49,
        "question": "What famous prophecy concerning the coming ruler (Shiloh) and the scepter did Jacob give to the tribe of Judah in Genesis 49?",
        "options": [
            "Judah will build a temple of stone in Jerusalem",
            "The scepter shall not depart from Judah, nor a lawgiver from between his feet, until Shiloh come",
            "Judah will wander forty years in the wilderness",
            "Judah will be divided among the twelve tribes"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "The scepter shall not depart from Judah, nor a lawgiver from between his feet, until Shiloh come",
        "reference": "Genesis 49:10",
        "explanation": "Jacob prophesied in Genesis 49:10: 'The scepter shall not depart from Judah, nor the ruler's staff from between his feet, until Shiloh comes, and to him shall be the obedience of the peoples.'"
    },
    {
        "id": "gen-book-q50",
        "questionNumber": 50,
        "question": "What profound theological statement did Joseph make to comfort his brothers concerning their past betrayal in Genesis 50:20?",
        "options": [
            "Time heals all grief, so let us forget the past",
            "You meant evil against me, but God meant it for good, to bring it about that many people should be kept alive",
            "Pharaoh has forgiven you, therefore I hold no grudge",
            "The silver was returned to your sacks by divine decree"
        ],
        "correctAnswerIndex": 1,
        "correctAnswer": "You meant evil against me, but God meant it for good, to bring it about that many people should be kept alive",
        "reference": "Genesis 50:20",
        "explanation": "Joseph revealed God's sovereign providence in Genesis 50:20: 'As for you, you meant evil against me, but God meant it for good, to bring it about that many people should be kept alive, as they are today.'"
    }
]

book_review_data = {
    "book": "Genesis",
    "bookId": "GEN",
    "title": "The Book of Genesis — Comprehensive Book Assessment",
    "totalQuestions": 50,
    "questions": questions
}

output_path = "src/data/books/GEN/book_qa.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(book_review_data, f, indent=2, ensure_ascii=False)

print(f"Generated {len(questions)} Genesis Book Assessment questions at {output_path}")
