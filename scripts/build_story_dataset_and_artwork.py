import os
import json
from manhwa_artist import create_manhwa_panel

OUTPUT_DIR = "public/assets/genesis"
STORY_DATA_FILE = "src/data/genesis_story_data.json"

# Narrative definitions for the 50 chapters of Genesis
CHAPTER_SCHEMAS = [
    {
        "chapter": 1,
        "title": "Genesis 1: The Beginning",
        "subtitle": "Creation of the Cosmos, Earth, and Life",
        "synopsis": "In the beginning, God brings forth light out of darkness, shapes the sky and the seas, commands the land to blossom, sets the sun, moon, and stars in the heavens, fills the world with living creatures, and crowns creation with humanity in His image.",
        "themeColor": "#0f172a",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 1:1–2",
                "image": "/assets/genesis/1/panel-1.jpg",
                "narration": "In the beginning, God created the heavens and the earth. The earth was formless and empty, darkness was over the deep, and the Spirit of God hovered over the waters.",
                "dialogue": [],
                "altText": "Cosmic waters in darkness with radiant Spirit of God hovering above the deep",
                "style": "cosmic",
                "colors": ((15, 23, 42), (2, 6, 23))
            },
            {
                "scene": 2,
                "reference": "Genesis 1:3–5",
                "image": "/assets/genesis/1/panel-2.jpg",
                "narration": "And God said, 'Let there be light,' and there was light. God saw that the light was good, and He separated the light from the darkness, calling the light 'Day' and the darkness 'Night'.",
                "dialogue": [{"speaker": "The Almighty", "text": "‘Let there be light!’", "isAdapted": False}],
                "altText": "Divine dawn breaking across the cosmic expanse, piercing through primeval darkness",
                "style": "light",
                "colors": ((255, 240, 180), (15, 23, 42))
            },
            {
                "scene": 3,
                "reference": "Genesis 1:6–8",
                "image": "/assets/genesis/1/panel-3.jpg",
                "narration": "God commanded a vast expanse to appear between the waters, parting the waters above from the waters below. God called the expanse 'Sky.'",
                "dialogue": [{"speaker": "The Almighty", "text": "‘A wide space will appear between the waters.’", "isAdapted": False}],
                "altText": "Atmospheric sky expanse parting cosmic waters with azure twilight horizons",
                "style": "cosmic",
                "colors": ((20, 80, 140), (8, 25, 50))
            },
            {
                "scene": 4,
                "reference": "Genesis 1:9–13",
                "image": "/assets/genesis/1/panel-4.jpg",
                "narration": "The waters under the sky gathered into one place, and dry ground appeared called 'Land.' Green vegetation, seed-bearing plants, and fruit trees burst forth across the earth.",
                "dialogue": [{"speaker": "The Almighty", "text": "‘Let the waters gather together, and let dry ground appear.’", "isAdapted": False}],
                "altText": "Verdant emerald continents emerging from azure oceans with lush plants and blooming trees",
                "style": "nature",
                "colors": ((30, 90, 60), (10, 35, 20))
            },
            {
                "scene": 5,
                "reference": "Genesis 1:14–19",
                "image": "/assets/genesis/1/panel-5.jpg",
                "narration": "God established lights in the expanse of the sky: the greater light to govern the day, the lesser light to govern the night, and countless stars to mark times, days, and years.",
                "dialogue": [],
                "altText": "Golden sun, silver moon, and swirling galaxies illuminating the celestial heavens",
                "style": "cosmic",
                "colors": ((25, 20, 65), (5, 5, 25))
            },
            {
                "scene": 6,
                "reference": "Genesis 1:20–23",
                "image": "/assets/genesis/1/panel-6.jpg",
                "narration": "The ocean depths surged with swimming creatures and majestic sea life, while birds of every kind took flight across the open sky. God blessed them to be fruitful and multiply.",
                "dialogue": [],
                "altText": "Whales and schools of fish leaping through sapphire waves while birds soar through clouds",
                "style": "water",
                "colors": ((14, 116, 144), (7, 40, 60))
            },
            {
                "scene": 7,
                "reference": "Genesis 1:24–25",
                "image": "/assets/genesis/1/panel-7.jpg",
                "narration": "The earth brought forth living creatures of every kind: cattle, creeping creatures, and wild beasts roaming across valleys and hills.",
                "dialogue": [],
                "altText": "Magnificent lions, deer, and creatures grazing peacefully across sunny plains",
                "style": "nature",
                "colors": ((180, 130, 60), (40, 60, 30))
            },
            {
                "scene": 8,
                "reference": "Genesis 1:26–31",
                "image": "/assets/genesis/1/panel-8.jpg",
                "narration": "Then God created humanity in His own image—male and female He created them—and blessed them to steward the earth. God saw everything that He had made, and it was very good.",
                "dialogue": [{"speaker": "The Almighty", "text": "‘Let us make human beings in our image, like ourselves.’", "isAdapted": False}],
                "altText": "Silhouettes of man and woman standing atop a sunlit ridge looking over the magnificent creation",
                "style": "light",
                "colors": ((254, 215, 170), (30, 41, 59))
            }
        ]
    },
    {
        "chapter": 2,
        "title": "Genesis 2: The Garden of Eden",
        "subtitle": "The Breath of Life and The Sacred Garden",
        "synopsis": "God rests on the seventh day and blesses it. He forms man from the dust of the ground, breathes life into him, plants the Garden of Eden with the Tree of Life, and forms woman as his companion.",
        "themeColor": "#065f46",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 2:1–3",
                "image": "/assets/genesis/2/panel-1.jpg",
                "narration": "By the seventh day God had completed the work He had been doing; so on the seventh day He rested from all His work, blessing it as a holy day.",
                "dialogue": [],
                "altText": "Sunlit tranquil Eden with the magnificent Tree of Life and pristine rivers",
                "style": "nature",
                "colors": ((40, 120, 80), (10, 40, 25))
            },
            {
                "scene": 2,
                "reference": "Genesis 2:7–9",
                "image": "/assets/genesis/2/panel-2.jpg",
                "narration": "The Lord God formed man from the dust of the ground and breathed into his nostrils the breath of life, and man became a living being. In the east, God planted the Garden of Eden.",
                "dialogue": [],
                "altText": "Ethereal golden breath of divine life infusing the newly formed man beneath paradise canopies",
                "style": "light",
                "colors": ((245, 158, 11), (20, 83, 45))
            },
            {
                "scene": 3,
                "reference": "Genesis 2:18–25",
                "image": "/assets/genesis/2/panel-3.jpg",
                "narration": "The Lord God observed, 'It is not good for the man to be alone.' From the man, God formed the woman, and brought her to him. They were both naked and felt no shame.",
                "dialogue": [{"speaker": "Adam", "text": "‘Finally, bone of my bones and flesh of my flesh!’", "isAdapted": False}],
                "altText": "Adam and Eve holding hands peacefully in the flowering Eden sanctuary",
                "style": "nature",
                "colors": ((52, 211, 153), (6, 78, 59))
            }
        ]
    },
    {
        "chapter": 3,
        "title": "Genesis 3: The Fall of Humanity",
        "subtitle": "The Serpent's Deception and Expulsion from Paradise",
        "synopsis": "The serpent deceives Eve into eating the forbidden fruit of the Tree of Knowledge. Adam eats as well. Their eyes are opened to shame; God confronts them and clothes them with garments of skin before sending them forth.",
        "themeColor": "#7c2d12",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 3:1–6",
                "image": "/assets/genesis/3/panel-1.jpg",
                "narration": "The serpent, more crafty than any wild animal, whispered doubt to Eve regarding God's command. Seeing the fruit pleasing to the eye and desirable for gaining wisdom, she took and ate, and gave some to her husband.",
                "dialogue": [
                    {"speaker": "The Serpent", "text": "‘Did God really say, “You must not eat from any tree in the garden”?’", "isAdapted": False},
                    {"speaker": "Eve", "text": "‘We may eat fruit from the trees, but God said of the tree in the middle, “Do not eat it or you will die.”’", "isAdapted": False}
                ],
                "altText": "The mysterious serpent coiled around the Tree of Knowledge, whispering softly in the shadows",
                "style": "nature",
                "colors": ((45, 20, 20), (15, 10, 10))
            },
            {
                "scene": 2,
                "reference": "Genesis 3:8–13",
                "image": "/assets/genesis/3/panel-2.jpg",
                "narration": "Hearing the sound of the Lord God walking in the garden in the cool of the day, Adam and Eve hid themselves among the trees, trembling in their nakedness.",
                "dialogue": [
                    {"speaker": "The Lord God", "text": "‘Where are you?’", "isAdapted": False},
                    {"speaker": "Adam", "text": "‘I heard your sound in the garden, and I was afraid because I was naked; so I hid.’", "isAdapted": False}
                ],
                "altText": "Adam and Eve crouching in the shadows of tangled thickets under dramatic rays of divine light",
                "style": "light",
                "colors": ((180, 83, 9), (30, 20, 15))
            },
            {
                "scene": 3,
                "reference": "Genesis 3:21–24",
                "image": "/assets/genesis/3/panel-3.jpg",
                "narration": "The Lord God made garments of skin for Adam and his wife and clothed them. To guard the way to the Tree of Life, He placed cherubim and a flaming sword flashing back and forth at the east of Eden.",
                "dialogue": [],
                "altText": "The blazing fiery sword of the Cherubim guarding the golden gates of Eden as travelers journey east",
                "style": "fire",
                "colors": ((220, 38, 38), (40, 10, 10))
            }
        ]
    },
    {
        "chapter": 4,
        "title": "Genesis 4: Cain and Abel",
        "subtitle": "The Two Offerings, Envy, and The First Murder",
        "synopsis": "Eve bears Cain, a tiller of soil, and Abel, a keeper of flocks. God looks with favor on Abel's offering. Overcome with jealousy, Cain slays his brother in the field and is marked by God as a wandering exile.",
        "themeColor": "#831843",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 4:1–5",
                "image": "/assets/genesis/4/panel-1.jpg",
                "narration": "In the course of time, Cain brought fruits of the soil as an offering, while Abel brought fat portions from some of the firstborn of his flock. The Lord looked with favor on Abel and his offering, but on Cain's He did not.",
                "dialogue": [],
                "altText": "Two stone altars: one offering smoking cleanly toward heaven, the other heavy with dark smoldering ash",
                "style": "fire",
                "colors": ((150, 40, 30), (30, 15, 20))
            },
            {
                "scene": 2,
                "reference": "Genesis 4:8–12",
                "image": "/assets/genesis/4/panel-2.jpg",
                "narration": "Cain attacked his brother Abel in the open field. When the Lord inquired of Abel, Cain retorted defiantly. God replied: 'Your brother’s blood cries out to me from the ground!'",
                "dialogue": [
                    {"speaker": "Cain", "text": "‘Am I my brother’s keeper?’", "isAdapted": False},
                    {"speaker": "The Lord", "text": "‘What have you done? Listen! Your brother’s blood cries out to me from the ground.’", "isAdapted": False}
                ],
                "altText": "Cain standing alone in a barren windswept field under an ominous crimson sunset",
                "style": "desert",
                "colors": ((190, 24, 93), (40, 10, 20))
            }
        ]
    },
    {
        "chapter": 5,
        "title": "Genesis 5: The Generations of Adam",
        "subtitle": "The Genealogy of the Patriarchs and Enoch Who Walked with God",
        "synopsis": "The sacred record of ten generations from Adam through Seth down to Noah. Enoch walks faithfully with God and is taken without seeing death. The chapter culminates in Lamech naming his son Noah: 'He will comfort us.'",
        "themeColor": "#312e81",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 5:21–24",
                "image": "/assets/genesis/5/panel-1.jpg",
                "narration": "Altogether, Enoch lived a total of 365 years. Enoch walked faithfully with God; then he was no more, because God took him away.",
                "dialogue": [],
                "altText": "Enoch ascending peacefully along a glowing stairway of starlight into the celestial heights",
                "style": "cosmic",
                "colors": ((67, 56, 202), (15, 23, 42))
            },
            {
                "scene": 2,
                "reference": "Genesis 5:28–32",
                "image": "/assets/genesis/5/panel-1.jpg", # Or distinct panel-2
                "image": "/assets/genesis/5/panel-2.jpg",
                "narration": "Lamech fathered a son and named him Noah, saying, 'He will comfort us in the labor and painful toil of our hands caused by the ground the Lord has cursed.'",
                "dialogue": [{"speaker": "Lamech", "text": "‘He will bring us rest and comfort from our painful toil.’", "isAdapted": False}],
                "altText": "Patriarch holding the newborn infant Noah against the backdrop of ancient timber forests",
                "style": "nature",
                "colors": ((120, 80, 50), (25, 20, 35))
            }
        ]
    },
    {
        "chapter": 6,
        "title": "Genesis 6: The Ark of Noah",
        "subtitle": "Human Wickedness and The Heavenly Blueprint",
        "synopsis": "Grief grips the Lord as corruption and violence spread across the earth. But Noah finds favor in His eyes. God commands Noah to build a massive wooden ark of gopher wood to preserve life from the coming flood.",
        "themeColor": "#1e293b",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 6:5–8",
                "image": "/assets/genesis/6/panel-1.jpg",
                "narration": "The Lord saw how great the wickedness of the human race had become. But Noah was a righteous man, blameless among the people of his time, and he walked faithfully with God.",
                "dialogue": [],
                "altText": "Noah standing in contemplative prayer on a hillside as dark storm clouds gather on the horizon",
                "style": "nature",
                "colors": ((71, 85, 105), (15, 23, 42))
            },
            {
                "scene": 2,
                "reference": "Genesis 6:13–22",
                "image": "/assets/genesis/6/panel-2.jpg",
                "narration": "God said to Noah: 'Make yourself an ark of cypress wood; coat it with pitch inside and out. I will establish my covenant with you, and you will enter the ark—you and your family and pairs of every living thing.'",
                "dialogue": [{"speaker": "The Lord", "text": "‘Make yourself an ark of cypress wood... I will establish my covenant with you.’", "isAdapted": False}],
                "altText": "The colossal wooden ribs of Noah's Ark rising against the forest hills under purposeful construction",
                "style": "nature",
                "colors": ((140, 90, 45), (20, 30, 45))
            }
        ]
    },
    {
        "chapter": 7,
        "title": "Genesis 7: The Great Deluge",
        "subtitle": "The Fountains of the Deep Burst and Rain Floods the Earth",
        "synopsis": "Noah, his family, and the creatures enter the Ark. The Lord shuts the door behind them. The springs of the great deep burst forth and the floodgates of heaven pour down rain for forty days and forty nights.",
        "themeColor": "#1e3a8a",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 7:1–16",
                "image": "/assets/genesis/7/panel-1.jpg",
                "narration": "Pairs of all creatures that have the breath of life came to Noah and entered the ark. Then the Lord shut him in.",
                "dialogue": [],
                "altText": "Pairs of animals boarding the great ramp of the Ark as the heavy timber door seals shut",
                "style": "water",
                "colors": ((30, 58, 138), (10, 20, 50))
            },
            {
                "scene": 2,
                "reference": "Genesis 7:17–24",
                "image": "/assets/genesis/7/panel-2.jpg",
                "narration": "For forty days the flood kept coming on the earth. The waters rose and lifted the ark high above the earth; all the high mountains under the entire heavens were covered.",
                "dialogue": [],
                "altText": "The Ark riding majestically atop churning ocean waves beneath torrential rain and lightning",
                "style": "water",
                "colors": ((23, 37, 84), (5, 10, 30))
            }
        ]
    },
    {
        "chapter": 8,
        "title": "Genesis 8: The Waters Recede",
        "subtitle": "The Raven, The Dove with the Olive Leaf, and The Altar",
        "synopsis": "God remembers Noah. The wind blows, the floodgates close, and the Ark rests on the mountains of Ararat. Noah sends forth a raven and a dove, which returns with an olive branch. Noah builds an altar of thanksgiving.",
        "themeColor": "#0369a1",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 8:6–12",
                "image": "/assets/genesis/8/panel-1.jpg",
                "narration": "When the dove returned to him in the evening, there in its beak was a freshly plucked olive leaf! Then Noah knew that the water had receded from the earth.",
                "dialogue": [],
                "altText": "A white dove with a green olive leaf flying toward Noah's hand at the Ark's window as sun rays pierce clouds",
                "style": "light",
                "colors": ((56, 189, 248), (12, 74, 96))
            },
            {
                "scene": 2,
                "reference": "Genesis 8:18–22",
                "image": "/assets/genesis/8/panel-2.jpg",
                "narration": "Noah built an altar to the Lord and sacrificed burnt offerings on it. The Lord smelled the pleasing aroma and said in His heart: 'Never again will I curse the ground because of humans.'",
                "dialogue": [{"speaker": "The Lord", "text": "‘As long as the earth endures, seedtime and harvest, cold and heat, summer and winter, day and night will never cease.’", "isAdapted": False}],
                "altText": "Noah and his family standing in reverence by a stone altar atop Mount Ararat as the waters gleam below",
                "style": "fire",
                "colors": ((234, 88, 12), (30, 40, 60))
            }
        ]
    },
    {
        "chapter": 9,
        "title": "Genesis 9: The Rainbow Covenant",
        "subtitle": "God's Everlasting Promise to Every Living Creature",
        "synopsis": "God blesses Noah and his sons. He establishes the rainbow in the clouds as the sign of His everlasting covenant never again to destroy all flesh by water.",
        "themeColor": "#0284c7",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 9:11–17",
                "image": "/assets/genesis/9/panel-1.jpg",
                "narration": "God said: 'I have set my rainbow in the clouds, and it will be the sign of the covenant between me and the earth... whenever the rainbow appears, I will remember my everlasting promise.'",
                "dialogue": [{"speaker": "The Lord", "text": "‘I set my rainbow in the clouds, and it will be the sign of the covenant.’", "isAdapted": False}],
                "altText": "A luminous, vibrant double rainbow spanning across a golden post-flood mountain valley",
                "style": "light",
                "colors": ((14, 165, 233), (254, 240, 138))
            }
        ]
    },
    {
        "chapter": 10,
        "title": "Genesis 10: The Table of Nations",
        "subtitle": "The Descendants of Shem, Ham, and Japheth",
        "synopsis": "The genealogy of the seventy nations arising from the three sons of Noah, spreading across maritime coastlands, ancient Mesopotamia, Canaan, and the fertile crescent.",
        "themeColor": "#854d0e",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 10:1–32",
                "image": "/assets/genesis/10/panel-1.jpg",
                "narration": "These are the clans of Noah's sons, according to their lines of descent, within their nations. From these the nations spread out over the earth after the flood.",
                "dialogue": [],
                "altText": "An ancient parchment map showing sea routes and migrations across the Mediterranean and Euphrates",
                "style": "desert",
                "colors": ((161, 98, 7), (66, 32, 6))
            }
        ]
    },
    {
        "chapter": 11,
        "title": "Genesis 11: The Tower of Babel",
        "subtitle": "Human Ambition and The Confusion of Tongues",
        "synopsis": "The whole world had one language. Men gather on the plain of Shinar to build a tower reaching to the heavens to make a name for themselves. The Lord confuses their speech and scatters them over the earth.",
        "themeColor": "#b45309",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 11:1–4",
                "image": "/assets/genesis/11/panel-1.jpg",
                "narration": "They said to each other, 'Come, let’s make bricks and bake them thoroughly.' Then they said, 'Come, let us build ourselves a city, with a tower that reaches to the heavens, so that we may make a name for ourselves.'",
                "dialogue": [{"speaker": "Builders of Babel", "text": "‘Let us build a city with a tower reaching to the heavens!’", "isAdapted": True}],
                "altText": "The monumental spiraling ziggurat tower rising into the clouds amidst bustling workers and kilns",
                "style": "desert",
                "colors": ((217, 119, 6), (69, 26, 3))
            },
            {
                "scene": 2,
                "reference": "Genesis 11:5–9",
                "image": "/assets/genesis/11/panel-2.jpg",
                "narration": "The Lord came down to see the city and tower. 'Come, let us go down and confuse their language so they will not understand each other.' So the Lord scattered them from there over all the earth.",
                "dialogue": [],
                "altText": "Scattered caravans and peoples departing in different directions away from the unfinished tower at sunset",
                "style": "desert",
                "colors": ((180, 83, 9), (40, 20, 20))
            }
        ]
    },
    {
        "chapter": 12,
        "title": "Genesis 12: The Call of Abram",
        "subtitle": "Go to the Land I Will Show You",
        "synopsis": "The Lord calls Abram to leave his country, people, and father's house for Canaan, promising to make him a great nation. Abram departs in faith. Famine leads him into Egypt where God protects Sarai.",
        "themeColor": "#ca8a04",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 12:1–4",
                "image": "/assets/genesis/12/panel-1.jpg",
                "narration": "The Lord said to Abram: 'Go from your country, your people and your father’s household to the land I will show you. I will make you into a great nation, and I will bless you... and all peoples on earth will be blessed through you.'",
                "dialogue": [{"speaker": "The Lord", "text": "‘Go from your country to the land I will show you... all peoples on earth will be blessed through you.’", "isAdapted": False}],
                "altText": "Abram holding his staff looking toward the open desert horizons as his caravan prepares to journey",
                "style": "desert",
                "colors": ((202, 138, 4), (66, 32, 6))
            },
            {
                "scene": 2,
                "reference": "Genesis 12:6–8",
                "image": "/assets/genesis/12/panel-2.jpg",
                "narration": "Abram traveled through the land as far as the site of the great tree of Moreh at Shechem. There the Lord appeared to Abram and said, 'To your offspring I will give this land.' Abram built an altar there to the Lord.",
                "dialogue": [],
                "altText": "Abram kneeling in prayer by an altar of uncut stones beneath the majestic oak tree of Moreh",
                "style": "nature",
                "colors": ((160, 110, 40), (30, 45, 25))
            }
        ]
    },
    {
        "chapter": 13,
        "title": "Genesis 13: Abram and Lot Separate",
        "subtitle": "Generosity in Canaan and The Plain of the Jordan",
        "synopsis": "Both Abram and his nephew Lot have vast flocks; quarreling arises between their herdsmen. Abram generously offers Lot first choice of the land. Lot chooses the fertile Jordan valley, while God reaffirms His promise to Abram.",
        "themeColor": "#15803d",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 13:8–12",
                "image": "/assets/genesis/13/panel-1.jpg",
                "narration": "Abram said to Lot, 'Let’s not have any quarreling between you and me... Is not the whole land before you? If you go to the left, I’ll go to the right.' Lot chose the well-watered plain of the Jordan.",
                "dialogue": [{"speaker": "Abram", "text": "‘We are brothers; let there be no strife between us. Choose where you wish to dwell.’", "isAdapted": True}],
                "altText": "Abram and Lot overlooking the rolling hills of Canaan and the lush green Jordan valley below",
                "style": "nature",
                "colors": ((22, 163, 74), (20, 83, 45))
            },
            {
                "scene": 2,
                "reference": "Genesis 13:14–18",
                "image": "/assets/genesis/13/panel-2.jpg",
                "narration": "The Lord said to Abram: 'Look around from where you are, to the north and south, to the east and west. All the land that you see I will give to you and your offspring forever.' Abram pitched his tents by the great trees of Mamre.",
                "dialogue": [{"speaker": "The Lord", "text": "‘All the land that you see I will give to you and your offspring forever.’", "isAdapted": False}],
                "altText": "Abram with arms outstretched on a windswept plateau gazing across the Promised Land at dusk",
                "style": "desert",
                "colors": ((217, 119, 6), (30, 40, 50))
            }
        ]
    },
    {
        "chapter": 14,
        "title": "Genesis 14: Abram Rescues Lot",
        "subtitle": "The War of Kings and The Blessing of Melchizedek",
        "synopsis": "Four eastern kings sack Sodom and capture Lot. Abram leads 318 trained men in a night assault to rescue Lot. Returning victorious, Abram is met by Melchizedek, king of Salem and priest of God Most High, who brings bread and wine.",
        "themeColor": "#7e22ce",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 14:14–16",
                "image": "/assets/genesis/14/panel-1.jpg",
                "narration": "Abram led out 318 trained men born in his household. During the night he divided his men to attack them, and routed the enemy, recovering his nephew Lot and all the possessions.",
                "dialogue": [],
                "altText": "Abram's warriors riding through the moonlit valley of Dan in swift nighttime pursuit",
                "style": "desert",
                "colors": ((126, 34, 206), (20, 10, 40))
            },
            {
                "scene": 2,
                "reference": "Genesis 14:18–20",
                "image": "/assets/genesis/14/panel-2.jpg",
                "narration": "Melchizedek king of Salem brought out bread and wine. He was priest of God Most High, and he blessed Abram, saying: 'Blessed be Abram by God Most High, Creator of heaven and earth.'",
                "dialogue": [{"speaker": "Melchizedek", "text": "‘Blessed be Abram by God Most High, Maker of heaven and earth!’", "isAdapted": False}],
                "altText": "Melchizedek in royal priestly robes offering bread and wine to Abram in the Valley of Shaveh",
                "style": "light",
                "colors": ((168, 85, 247), (59, 7, 100))
            }
        ]
    },
    {
        "chapter": 15,
        "title": "Genesis 15: The Covenant of Stars",
        "subtitle": "Count the Stars if You Can: Abram's Faith",
        "synopsis": "God appears to Abram in a vision. He takes him outside and tells him to count the stars—so shall his offspring be. Abram believes the Lord, and it is credited to him as righteousness. God makes a sacred covenant passing through the pieces.",
        "themeColor": "#1e1b4b",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 15:1–6",
                "image": "/assets/genesis/15/panel-1.jpg",
                "narration": "He took him outside and said, 'Look up at the sky and count the stars—if indeed you can count them.' Then He said to him, 'So shall your offspring be.' Abram believed the Lord, and He credited it to him as righteousness.",
                "dialogue": [
                    {"speaker": "The Lord", "text": "‘Look up at the sky and count the stars... So shall your offspring be.’", "isAdapted": False},
                    {"speaker": "Abram", "text": "‘Sovereign Lord, what can you give me since I remain childless?’", "isAdapted": False}
                ],
                "altText": "Abram standing in awe beneath a spectacular canopy of countless glittering desert stars",
                "style": "cosmic",
                "colors": ((30, 27, 75), (5, 5, 20))
            },
            {
                "scene": 2,
                "reference": "Genesis 15:12–18",
                "image": "/assets/genesis/15/panel-2.jpg",
                "narration": "When the sun had set and darkness had fallen, a smoking firepot with a blazing torch appeared and passed between the pieces. On that day the Lord made a covenant with Abram.",
                "dialogue": [],
                "altText": "A mysterious blazing torch of divine fire moving between the covenant offerings in the night",
                "style": "fire",
                "colors": ((239, 68, 68), (20, 10, 15))
            }
        ]
    },
    {
        "chapter": 16,
        "title": "Genesis 16: Hagar and The God Who Sees",
        "subtitle": "The Spring in the Desert and Ishmael's Birth",
        "synopsis": "Sarai gives her Egyptian servant Hagar to Abram. When mistreated, Hagar flees into the wilderness. The angel of the Lord finds her by a spring, comforts her with promises of her son Ishmael, and she names God El Roi: 'The God Who Sees Me.'",
        "themeColor": "#0d9488",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 16:7–14",
                "image": "/assets/genesis/16/panel-1.jpg",
                "narration": "The angel of the Lord found Hagar near a spring in the desert. She gave this name to the Lord who spoke to her: 'You are the God who sees me,' for she said, 'I have now seen the One who sees me.'",
                "dialogue": [{"speaker": "Hagar", "text": "‘You are the God who sees me—I have seen the One who looks after me.’", "isAdapted": False}],
                "altText": "Hagar kneeling beside a shimmering desert oasis spring as divine light comforts her",
                "style": "desert",
                "colors": ((13, 148, 136), (15, 23, 42))
            }
        ]
    },
    {
        "chapter": 17,
        "title": "Genesis 17: Abraham & The Covenant of Circumcision",
        "subtitle": "Father of Many Nations and Sarah's Promise",
        "synopsis": "When Abram is 99 years old, God appears as God Almighty (El Shaddai). He renames him Abraham and Sarai Sarah, establishes circumcision as the covenant sign, and promises that Sarah will give birth to Isaac.",
        "themeColor": "#4338ca",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 17:1–8",
                "image": "/assets/genesis/17/panel-1.jpg",
                "narration": "When Abram was ninety-nine years old, the Lord appeared to him: 'I am God Almighty; walk before me faithfully and be blameless... No longer will you be called Abram; your name will be Abraham, for I have made you a father of many nations.'",
                "dialogue": [{"speaker": "El Shaddai", "text": "‘I am God Almighty; walk before me faithfully and be blameless.’", "isAdapted": False}],
                "altText": "Abraham falling facedown in reverent worship before the radiant presence of God Almighty",
                "style": "light",
                "colors": ((79, 70, 229), (15, 23, 42))
            }
        ]
    },
    {
        "chapter": 18,
        "title": "Genesis 18: Three Heavenly Visitors",
        "subtitle": "Laughter, Hospitality, and Abraham's Plea for Sodom",
        "synopsis": "Three heavenly visitors appear near Abraham's tent at Mamre. Sarah hears the promise of a son next year and laughs in disbelief. As they look toward Sodom, Abraham intercedes boldly for the righteous.",
        "themeColor": "#b45309",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 18:1–10",
                "image": "/assets/genesis/18/panel-1.jpg",
                "narration": "The Lord appeared to Abraham near the great trees of Mamre while he was sitting at the entrance to his tent in the heat of the day. Abraham bowed low, washed their feet, and served choice meat and curds under a tree.",
                "dialogue": [{"speaker": "The Visitor", "text": "‘I will surely return to you about this time next year, and Sarah your wife will have a son.’", "isAdapted": False}],
                "altText": "Abraham serving three radiant celestial travelers seated beneath the shade of the great terebinth tree",
                "style": "nature",
                "colors": ((217, 119, 6), (40, 30, 20))
            },
            {
                "scene": 2,
                "reference": "Genesis 18:23–33",
                "image": "/assets/genesis/18/panel-2.jpg",
                "narration": "Abraham approached Him and said: 'Will you sweep away the righteous with the wicked? What if there are fifty righteous people in the city? Will not the Judge of all the earth do right?' Abraham pleaded down to ten.",
                "dialogue": [{"speaker": "Abraham", "text": "‘Will not the Judge of all the earth do right?’", "isAdapted": False}],
                "altText": "Abraham standing on the precipice overlooking the Jordan valley, interceding with intense reverence",
                "style": "desert",
                "colors": ((180, 83, 9), (20, 20, 30))
            }
        ]
    },
    {
        "chapter": 19,
        "title": "Genesis 19: The Fall of Sodom",
        "subtitle": "Angels at the Gate and The Morning of Judgment",
        "synopsis": "Two angels rescue Lot and his daughters from Sodom. As dawn breaks, sulfur and fire rain from heaven upon Sodom and Gomorrah. Lot's wife looks back and becomes a pillar of salt.",
        "themeColor": "#991b1b",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 19:15–26",
                "image": "/assets/genesis/19/panel-1.jpg",
                "narration": "The angels hurried Lot, taking his hand and fleeing to Zoar. Then the Lord rained down burning sulfur on Sodom and Gomorrah from the heavens. But Lot's wife looked back, and she became a pillar of salt.",
                "dialogue": [{"speaker": "The Angel", "text": "‘Flee for your lives! Do not look back, and do not stop anywhere in the plain!’", "isAdapted": False}],
                "altText": "Sulfur and crimson lightning falling upon the distant plains of Sodom as Lot flees up the mountain",
                "style": "fire",
                "colors": ((220, 38, 38), (30, 10, 10))
            }
        ]
    },
    {
        "chapter": 20,
        "title": "Genesis 20: Abraham and Abimelech",
        "subtitle": "Integrity of Heart and Intercession at Gerar",
        "synopsis": "Abraham journeys to the Negev and stays in Gerar. God warns King Abimelech in a dream regarding Sarah. Abimelech restores Sarah with gifts, and Abraham prays for the healing of the king's household.",
        "themeColor": "#0891b2",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 20:1–17",
                "image": "/assets/genesis/20/panel-1.jpg",
                "narration": "God spoke to Abimelech in a dream of the night: 'He is a prophet, and he will pray for you and you will live.' Abimelech brought sheep and cattle and restored Sarah to Abraham.",
                "dialogue": [{"speaker": "Abimelech", "text": "‘Lord, would you destroy an innocent nation? Did he not say to me, “She is my sister”?’", "isAdapted": False}],
                "altText": "King Abimelech waking from his dream in the royal palace court, addressing Abraham with gifts",
                "style": "palace",
                "colors": ((8, 145, 178), (20, 40, 50))
            }
        ]
    },
    {
        "chapter": 21,
        "title": "Genesis 21: The Birth of Isaac",
        "subtitle": "Laughter Fulfilled and The Well of Beersheba",
        "synopsis": "Sarah conceives and gives birth to Isaac just as God promised. Sarah rejoices: 'God has brought me laughter!' Later, Hagar and Ishmael are preserved in the desert at Beersheba by an angel of God.",
        "themeColor": "#f59e0b",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 21:1–7",
                "image": "/assets/genesis/21/panel-1.jpg",
                "narration": "Now the Lord was gracious to Sarah as He had said. Sarah became pregnant and bore a son to Abraham in his old age. Sarah said: 'God has brought me laughter, and everyone who hears about this will laugh with me.'",
                "dialogue": [{"speaker": "Sarah", "text": "‘God has brought me laughter; everyone who hears will rejoice with me!’", "isAdapted": False}],
                "altText": "Sarah smiling with radiant joy holding her newborn baby boy Isaac beside Abraham's tent",
                "style": "light",
                "colors": ((245, 158, 11), (254, 243, 199))
            },
            {
                "scene": 2,
                "reference": "Genesis 21:14–19",
                "image": "/assets/genesis/21/panel-2.jpg",
                "narration": "Hagar wept in the wilderness of Beersheba. God heard the boy crying, and the angel called from heaven: 'Do not be afraid.' Then God opened her eyes and she saw a well of water.",
                "dialogue": [{"speaker": "Angel of God", "text": "‘Do not be afraid, Hagar; God has heard the boy crying as he lies there. Lift him up.’", "isAdapted": False}],
                "altText": "A crystal spring of water appearing in the parched desert dunes before Hagar and young Ishmael",
                "style": "desert",
                "colors": ((14, 165, 233), (120, 80, 40))
            }
        ]
    },
    {
        "chapter": 22,
        "title": "Genesis 22: The Test on Mount Moriah",
        "subtitle": "The Lord Will Provide (Jehovah Jireh)",
        "synopsis": "God tests Abraham, asking him to offer his son Isaac on Mount Moriah. In unwavering faith, Abraham ascends the mountain. As he raises the knife, the angel of the Lord stops him, providing a ram caught in the thicket.",
        "themeColor": "#e11d48",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 22:1–8",
                "image": "/assets/genesis/22/panel-1.jpg",
                "narration": "Isaac spoke up and said, 'The fire and wood are here, but where is the lamb for the burnt offering?' Abraham answered, 'God Himself will provide the lamb for the burnt offering, my son.'",
                "dialogue": [
                    {"speaker": "Isaac", "text": "‘Father, the fire and wood are here, but where is the lamb for the offering?’", "isAdapted": False},
                    {"speaker": "Abraham", "text": "‘God Himself will provide the lamb, my son.’", "isAdapted": False}
                ],
                "altText": "Abraham and young Isaac walking up the rugged path of Mount Moriah carrying the wood and fire",
                "style": "desert",
                "colors": ((225, 29, 72), (40, 20, 25))
            },
            {
                "scene": 2,
                "reference": "Genesis 22:9–14",
                "image": "/assets/genesis/22/panel-2.jpg",
                "narration": "The angel of the Lord called from heaven: 'Abraham! Do not lay a hand on the boy!' Abraham looked up and there in a thicket he saw a ram caught by its horns. So Abraham called that place 'The Lord Will Provide.'",
                "dialogue": [{"speaker": "Angel of the Lord", "text": "‘Abraham, Abraham! Do not touch the boy... Now I know that you fear God.’", "isAdapted": False}],
                "altText": "The ram caught in the thorny bushes by the stone altar as golden light breaks over Mount Moriah",
                "style": "light",
                "colors": ((251, 146, 60), (30, 20, 30))
            }
        ]
    },
    {
        "chapter": 23,
        "title": "Genesis 23: The Cave of Machpelah",
        "subtitle": "Sarah's Death and Abraham Purchases a Burial Ground",
        "synopsis": "Sarah dies at Hebron at age 127. Abraham mourns her and purchases the field and cave of Machpelah from Ephron the Hittite for 400 shekels of silver, securing the patriarchs' first legal possession in the Promised Land.",
        "themeColor": "#57534e",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 23:16–20",
                "image": "/assets/genesis/23/panel-1.jpg",
                "narration": "Abraham weighed out the four hundred shekels of silver to Ephron. So the field and cave of Machpelah near Mamre were deeded to Abraham as a burial site. There he buried his wife Sarah.",
                "dialogue": [],
                "altText": "The solemn ancient cave tomb of Machpelah nestled among aged olive trees in the hills of Hebron",
                "style": "nature",
                "colors": ((87, 83, 78), (28, 25, 23))
            }
        ]
    },
    {
        "chapter": 24,
        "title": "Genesis 24: A Wife for Isaac",
        "subtitle": "The Servant's Prayer and Rebekah at the Well",
        "synopsis": "Abraham sends his chief servant to his ancestral homeland to find a wife for Isaac. At the town well in Nahor, the servant prays for a sign. Rebekah draws water for him and his ten camels. She departs in faith to marry Isaac.",
        "themeColor": "#0284c7",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 24:12–21",
                "image": "/assets/genesis/24/panel-1.jpg",
                "narration": "Before he had finished praying, Rebekah came out with her jar on her shoulder. She went down to the spring, filled her jar, and offered: 'Drink, my lord, and I’ll draw water for your camels too, until they have finished drinking.'",
                "dialogue": [
                    {"speaker": "Rebekah", "text": "‘Drink, and I will draw water for your camels as well.’", "isAdapted": False},
                    {"speaker": "The Servant", "text": "‘Praise be to the Lord, the God of my master Abraham, who has not abandoned His kindness!’", "isAdapted": False}
                ],
                "altText": "Rebekah pouring cool water from her clay jar into a stone trough for thirsty kneeling camels at sunset",
                "style": "nature",
                "colors": ((2, 132, 199), (180, 120, 50))
            },
            {
                "scene": 2,
                "reference": "Genesis 24:62–67",
                "image": "/assets/genesis/24/panel-2.jpg",
                "narration": "Isaac had gone out to the field in the evening to meditate. As he looked up, he saw camels approaching. Rebekah veiled herself, and Isaac brought her into the tent; she became his wife, and he loved her.",
                "dialogue": [],
                "altText": "Isaac walking across a golden wheat field at dusk meeting Rebekah's arriving caravan",
                "style": "nature",
                "colors": ((245, 158, 11), (30, 40, 60))
            }
        ]
    },
    {
        "chapter": 25,
        "title": "Genesis 25: Jacob and Esau",
        "subtitle": "Two Nations in the Womb and The Red Stew",
        "synopsis": "Abraham dies full of years and is buried beside Sarah. Rebekah gives birth to twin boys: Esau the rugged hunter and Jacob the quiet dweller in tents. Exhausted from hunting, Esau sells his birthright to Jacob for red lentil stew.",
        "themeColor": "#ea580c",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 25:21–26",
                "image": "/assets/genesis/25/panel-1.jpg",
                "narration": "The Lord said to Rebekah: 'Two nations are in your womb, and two peoples from within you will be separated; one will be stronger than the other, and the older will serve the younger.'",
                "dialogue": [{"speaker": "The Lord", "text": "‘Two nations are in your womb... and the older will serve the younger.’", "isAdapted": False}],
                "altText": "Rebekah praying by her desert tent beneath the constellations concerning the twin infants",
                "style": "cosmic",
                "colors": ((234, 88, 12), (15, 23, 42))
            },
            {
                "scene": 2,
                "reference": "Genesis 25:29–34",
                "image": "/assets/genesis/25/panel-2.jpg",
                "narration": "Esau came in famished from the open country: 'Quick, let me have some of that red stew!' Jacob said, 'First sell me your birthright.' Esau swore an oath, despising his birthright.",
                "dialogue": [
                    {"speaker": "Esau", "text": "‘I am famished! Give me some of that red stew!’", "isAdapted": False},
                    {"speaker": "Jacob", "text": "‘First sell me your birthright.’", "isAdapted": False}
                ],
                "altText": "Jacob stirring an earthenware pot of steaming red lentil stew by the tent fire as Esau throws down his bow",
                "style": "fire",
                "colors": ((194, 65, 12), (50, 20, 15))
            }
        ]
    },
    {
        "chapter": 26,
        "title": "Genesis 26: Isaac in Gerar",
        "subtitle": "Reopening the Wells of Abraham",
        "synopsis": "God appears to Isaac and renews the covenant promises. Isaac reopens the wells dug by Abraham. After disputes with local herdsmen at Esek and Sitnah, he digs Rehoboth: 'Now the Lord has made room for us.'",
        "themeColor": "#0284c7",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 26:22–25",
                "image": "/assets/genesis/26/panel-1.jpg",
                "narration": "He moved on and dug another well, and no one quarreled over it. He named it Rehoboth, saying, 'Now the Lord has given us room and we will flourish in the land.' There he built an altar.",
                "dialogue": [{"speaker": "Isaac", "text": "‘Now the Lord has made room for us, and we will be fruitful in the land.’", "isAdapted": False}],
                "altText": "Isaac's servants drawing fresh overflowing water from the stone-rimmed well of Rehoboth",
                "style": "nature",
                "colors": ((14, 165, 233), (40, 70, 45))
            }
        ]
    },
    {
        "chapter": 27,
        "title": "Genesis 27: The Stolen Blessing",
        "subtitle": "Deception, Sorrow, and The Broken Brotherhood",
        "synopsis": "Old and blind, Isaac prepares to bless Esau. Rebekah coaches Jacob to disguise himself in Esau's clothes and goatskins. Jacob receives the firstborn blessing. Esau returns, weeps bitterly, and vows revenge, prompting Jacob to flee.",
        "themeColor": "#9a3412",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 27:18–29",
                "image": "/assets/genesis/27/panel-1.jpg",
                "narration": "Isaac touched Jacob's hands covered in goatskins and said, 'The voice is the voice of Jacob, but the hands are the hands of Esau.' So he blessed him with the dew of heaven and richness of the earth.",
                "dialogue": [
                    {"speaker": "Isaac", "text": "‘The voice is the voice of Jacob, but the hands are the hands of Esau.’", "isAdapted": False},
                    {"speaker": "Jacob", "text": "‘I am Esau your firstborn; arise and eat that you may bless me.’", "isAdapted": False}
                ],
                "altText": "Blind elderly Isaac trembling in his bed touching the disguised goatskin hands of Jacob",
                "style": "desert",
                "colors": ((154, 52, 18), (35, 15, 10))
            },
            {
                "scene": 2,
                "reference": "Genesis 27:34–41",
                "image": "/assets/genesis/27/panel-2.jpg",
                "narration": "When Esau heard his father's words, he burst out with a loud and bitter cry: 'Bless me—me too, my father!' Esau held a grudge against Jacob and said in his heart: 'The days of mourning for my father are near; then I will kill my brother.'",
                "dialogue": [{"speaker": "Esau", "text": "‘Bless me also, O my father! Has he not rightly been named Jacob?’", "isAdapted": False}],
                "altText": "Esau kneeling in agonizing tears before Isaac holding his hunting spear",
                "style": "desert",
                "colors": ((185, 28, 28), (40, 20, 20))
            }
        ]
    },
    {
        "chapter": 28,
        "title": "Genesis 28: Jacob's Ladder at Bethel",
        "subtitle": "The Stairway to Heaven and The House of God",
        "synopsis": "Fleeing to Haran, Jacob stops at night using a stone for a pillow. He dreams of a stairway resting on earth with its top reaching to heaven, angels ascending and descending, and God standing above it promising His presence.",
        "themeColor": "#3730a3",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 28:10–15",
                "image": "/assets/genesis/28/panel-1.jpg",
                "narration": "He had a dream in which he saw a stairway resting on the earth, with its top reaching to heaven, and the angels of God were ascending and descending on it. Above it stood the Lord, who said: 'I am with you and will watch over you wherever you go.'",
                "dialogue": [{"speaker": "The Lord", "text": "‘I am with you and will watch over you wherever you go, and I will bring you back to this land.’", "isAdapted": False}],
                "altText": "A radiant celestial stairway of incandescent light connecting heaven and earth with descending luminous angels",
                "style": "cosmic",
                "colors": ((55, 48, 163), (15, 23, 42))
            },
            {
                "scene": 2,
                "reference": "Genesis 28:16–22",
                "image": "/assets/genesis/28/panel-2.jpg",
                "narration": "When Jacob awoke, he thought, 'Surely the Lord is in this place, and I was not aware of it!' He was afraid and said, 'How awesome is this place! This is none other than the house of God; this is the gate of heaven.'",
                "dialogue": [{"speaker": "Jacob", "text": "‘Surely the Lord is in this place! This is none other than the house of God (Bethel).’", "isAdapted": False}],
                "altText": "Jacob setting up his stone pillow as a sacred pillar, pouring fragrant oil upon its top at sunrise",
                "style": "light",
                "colors": ((251, 191, 36), (40, 30, 60))
            }
        ]
    },
    {
        "chapter": 29,
        "title": "Genesis 29: Leah and Rachel",
        "subtitle": "Arrival in Haran and The Seven Years of Love",
        "synopsis": "Jacob arrives in Haran and rolls the stone from the well for Rachel. He agrees to serve her father Laban seven years for Rachel, but on the wedding night Laban gives him Leah. Jacob serves seven more years for Rachel.",
        "themeColor": "#db2777",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 29:9–12",
                "image": "/assets/genesis/29/panel-1.jpg",
                "narration": "While he was still talking with them, Rachel came with her father’s sheep. Jacob went over and rolled the stone away from the mouth of the well and watered his uncle’s sheep. Then Jacob kissed Rachel and began to weep aloud.",
                "dialogue": [],
                "altText": "Jacob rolling the massive stone from the mouth of the well as young shepherdess Rachel watches with wonder",
                "style": "nature",
                "colors": ((219, 39, 119), (40, 60, 45))
            },
            {
                "scene": 2,
                "reference": "Genesis 29:18–20",
                "image": "/assets/genesis/29/panel-2.jpg",
                "narration": "Jacob was in love with Rachel and said, 'I’ll work for you seven years in return for your younger daughter Rachel.' So Jacob served seven years to get Rachel, but they seemed like only a few days to him because of his love for her.",
                "dialogue": [{"speaker": "Jacob", "text": "‘I will serve you seven years for your younger daughter Rachel.’", "isAdapted": False}],
                "altText": "Jacob tending sheep under sunlit pastures, gazing toward Rachel by the tents of Haran",
                "style": "nature",
                "colors": ((244, 114, 182), (30, 40, 50))
            }
        ]
    },
    {
        "chapter": 30,
        "title": "Genesis 30: Jacob's Flocks Flourish",
        "subtitle": "The Birth of the Tribes and The Spotted Sheep",
        "synopsis": "Leah, Rachel, and their maidservants bear sons to Jacob. Rachel gives birth to Joseph. Jacob agrees with Laban to take only the striped, speckled, and spotted sheep and goats, and through God's blessing Jacob grows exceedingly prosperous.",
        "themeColor": "#059669",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 30:22–24",
                "image": "/assets/genesis/30/panel-1.jpg",
                "narration": "Then God remembered Rachel; He listened to her and enabled her to conceive. She gave birth to a son and named him Joseph, saying, 'May the Lord add to me another son.'",
                "dialogue": [{"speaker": "Rachel", "text": "‘God has taken away my disgrace! May the Lord add to me another son (Joseph).’", "isAdapted": False}],
                "altText": "Rachel weeping with joy while cradling the newborn infant Joseph in her tent",
                "style": "light",
                "colors": ((5, 150, 105), (254, 240, 138))
            },
            {
                "scene": 2,
                "reference": "Genesis 30:37–43",
                "image": "/assets/genesis/30/panel-2.jpg",
                "narration": "Jacob peeled white stripes on poplar and almond branches by the watering troughs. The flocks produced striped, speckled and spotted young, and Jacob grew exceedingly prosperous.",
                "dialogue": [],
                "altText": "Vast herds of speckled and spotted sheep drinking by fresh mountain streams under Jacob's watchful eye",
                "style": "nature",
                "colors": ((16, 185, 129), (30, 50, 35))
            }
        ]
    },
    {
        "chapter": 31,
        "title": "Genesis 31: Jacob Flees from Laban",
        "subtitle": "The Departure and Covenant at Galeed",
        "synopsis": "Sensing Laban's hostility, Jacob departs secretly with his family and herds toward Canaan. Laban pursues and catches him in Gilead. God warns Laban in a dream, and the two men make a peace covenant at Galeed/Mizpah.",
        "themeColor": "#475569",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 31:44–54",
                "image": "/assets/genesis/31/panel-1.jpg",
                "narration": "Laban said, 'Come, let’s make a covenant.' Jacob took a stone and set it up as a pillar, and they heaped stones together. Laban called it Mizpah: 'May the Lord keep watch between you and me when we are away from each other.'",
                "dialogue": [{"speaker": "Laban", "text": "‘May the Lord watch between you and me when we are out of each other's sight.’", "isAdapted": False}],
                "altText": "Jacob and Laban standing before a memorial cairn of stones atop the misty mountains of Gilead",
                "style": "desert",
                "colors": ((71, 85, 105), (15, 23, 42))
            }
        ]
    },
    {
        "chapter": 32,
        "title": "Genesis 32: Jacob Wrestles at Peniel",
        "subtitle": "A New Name: Israel – Striving with God and Prevailing",
        "synopsis": "Jacob learns Esau is marching toward him with 400 men. He divides his camp and prays fervently. Left alone at the ford of Jabbok, a mysterious man wrestles with him until dawn, touches his hip socket, and renames him Israel.",
        "themeColor": "#4338ca",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 32:22–32",
                "image": "/assets/genesis/32/panel-1.jpg",
                "narration": "So Jacob was left alone, and a man wrestled with him till daybreak. The man said, 'Your name will no longer be Jacob, but Israel, because you have struggled with God and with humans and have overcome.' Jacob called the place Peniel: 'I saw God face to face, yet my life was spared.'",
                "dialogue": [
                    {"speaker": "The Wrestler", "text": "‘Let me go, for the dawn is breaking.’", "isAdapted": False},
                    {"speaker": "Jacob", "text": "‘I will not let you go unless you bless me!’", "isAdapted": False},
                    {"speaker": "The Lord", "text": "‘Your name shall no longer be Jacob, but Israel.’", "isAdapted": False}
                ],
                "altText": "Jacob locked in an intense, mystical wrestling embrace with the radiant Angel at the misty ford of the Jabbok",
                "style": "cosmic",
                "colors": ((67, 56, 202), (10, 15, 35))
            }
        ]
    },
    {
        "chapter": 33,
        "title": "Genesis 33: Jacob and Esau Reconcile",
        "subtitle": "The Brothers Embrace in Tears of Forgiveness",
        "synopsis": "Jacob looks up and sees Esau coming with 400 men. Jacob bows seven times as he approaches. But Esau runs to meet him, throws his arms around his neck, and kisses him; both weep in tears of reconciliation.",
        "themeColor": "#ea580c",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 33:1–4",
                "image": "/assets/genesis/33/panel-1.jpg",
                "narration": "Jacob bowed down to the ground seven times as he approached his brother. But Esau ran to meet Jacob and embraced him; he threw his arms around his neck and kissed him. And they wept.",
                "dialogue": [
                    {"speaker": "Jacob", "text": "‘To see your face is like seeing the face of God, now that you have received me favorably.’", "isAdapted": False},
                    {"speaker": "Esau", "text": "‘I already have plenty, my brother. Keep what you have for yourself.’", "isAdapted": False}
                ],
                "altText": "Esau embracing Jacob in a warm emotional reunion on the sunny plains of Succoth with camps looking on",
                "style": "nature",
                "colors": ((234, 88, 12), (50, 70, 40))
            }
        ]
    },
    {
        "chapter": 34,
        "title": "Genesis 34: The Dinah Incident at Shechem",
        "subtitle": "Grief, Deceit, and Vengeance",
        "synopsis": "Dinah, Jacob's daughter, is violated by Shechem, son of Hamor. Her brothers Simeon and Levi plot fierce vengeance, striking the city and bringing grief and fear upon Jacob's household in Canaan.",
        "themeColor": "#7f1d1d",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 34:25–31",
                "image": "/assets/genesis/34/panel-1.jpg",
                "narration": "Simeon and Levi took vengeance on the city of Shechem. Jacob said to them, 'You have brought trouble on me by making me obnoxious to the Canaanites.' But they replied, 'Should he have treated our sister like a prostitute?'",
                "dialogue": [{"speaker": "Jacob", "text": "‘You have brought trouble upon me, making me odious to the inhabitants of the land.’", "isAdapted": False}],
                "altText": "The fortified gates of ancient Shechem under a dark, brooding sky as Jacob's sons stand armed",
                "style": "fire",
                "colors": ((127, 29, 29), (20, 10, 10))
            }
        ]
    },
    {
        "chapter": 35,
        "title": "Genesis 35: Jacob Returns to Bethel",
        "subtitle": "Purifying the Household and The Passing of Rachel",
        "synopsis": "God directs Jacob to return to Bethel. Jacob commands his household to put away foreign idols. God renews His covenant promises with Israel. On the journey near Ephrath, Rachel dies giving birth to Benjamin.",
        "themeColor": "#4f46e5",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 35:1–15",
                "image": "/assets/genesis/35/panel-1.jpg",
                "narration": "God appeared to Jacob again at Bethel and blessed him: 'I am God Almighty; be fruitful and increase in number. A nation and a community of nations will come from you, and kings will be among your descendants.'",
                "dialogue": [{"speaker": "God Almighty", "text": "‘I am God Almighty; be fruitful and increase in number. Kings will come from you.’", "isAdapted": False}],
                "altText": "Jacob standing before the restored altar of Bethel bathed in celestial divine rays",
                "style": "light",
                "colors": ((79, 70, 229), (254, 240, 138))
            },
            {
                "scene": 2,
                "reference": "Genesis 35:16–20",
                "image": "/assets/genesis/35/panel-2.jpg",
                "narration": "Rachel went into hard labor near Ephrath. As she breathed her last, she named him Ben-Oni ('Son of my sorrow'), but his father named him Benjamin ('Son of my right hand'). Jacob set up a pillar over her tomb.",
                "dialogue": [],
                "altText": "Jacob weeping beside the stone memorial pillar on the roadside to Bethlehem as dusk falls",
                "style": "desert",
                "colors": ((120, 50, 80), (30, 20, 30))
            }
        ]
    },
    {
        "chapter": 36,
        "title": "Genesis 36: The Lineage of Esau",
        "subtitle": "The Chiefs and Kings of the Land of Edom",
        "synopsis": "The detailed genealogical record of Esau (who is Edom) and his descendants in the rugged red sandstone mountains of Seir, listing the clan chiefs and kings who reigned in Edom before any king ruled in Israel.",
        "themeColor": "#b91c1c",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 36:1–43",
                "image": "/assets/genesis/36/panel-1.jpg",
                "narration": "This is the account of the family line of Esau (that is, Edom). Esau took his wives, his sons and daughters and all his livestock, and went to a land some distance from his brother Jacob, settling in the hill country of Seir.",
                "dialogue": [],
                "altText": "The towering red rock canyon cliffs of Mount Seir and ancient Edomite watchtowers at sunrise",
                "style": "desert",
                "colors": ((185, 28, 28), (60, 20, 20))
            }
        ]
    },
    {
        "chapter": 37,
        "title": "Genesis 37: Joseph's Dreams and The Tunic",
        "subtitle": "The Robe of Many Colors, The Pit, and Midianite Traders",
        "synopsis": "Jacob loves seventeen-year-old Joseph more than all his sons and gives him an ornate multi-colored coat. Joseph dreams of sheaves and stars bowing to him, stoking his brothers' hatred. When sent to Dothan, they throw him into a pit and sell him to Ishmaelite traders.",
        "themeColor": "#7c3aed",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 37:1–11",
                "image": "/assets/genesis/37/panel-1.jpg",
                "narration": "Israel loved Joseph more than any of his other sons, and made him an ornate robe of many colors. Joseph had dreams of their sheaves bowing to his sheaf, and of the sun, moon, and eleven stars bowing to him.",
                "dialogue": [
                    {"speaker": "Joseph", "text": "‘Listen to this dream I had: We were binding sheaves of grain, and my sheaf stood upright while yours bowed down to mine!’", "isAdapted": False},
                    {"speaker": "Brothers", "text": "‘Do you intend to reign over us? Will you actually rule us?’", "isAdapted": False}
                ],
                "altText": "Young Joseph proudly wearing his magnificent flowing multi-colored tunic among the flocks of Hebron",
                "style": "nature",
                "colors": ((124, 58, 237), (245, 158, 11))
            },
            {
                "scene": 2,
                "reference": "Genesis 37:23–28",
                "image": "/assets/genesis/37/panel-2.jpg",
                "narration": "When Joseph came to his brothers, they stripped him of his ornate robe and threw him into an empty cistern. When Midianite merchants came by, they pulled Joseph up out of the cistern and sold him for twenty shekels of silver.",
                "dialogue": [{"speaker": "Judah", "text": "‘What will we gain if we kill our brother? Let’s sell him to the Ishmaelites and not lay our hands on him.’", "isAdapted": False}],
                "altText": "Joseph being pulled out of the dark stone cistern as the merchant camel caravan heads toward Egypt",
                "style": "desert",
                "colors": ((180, 83, 9), (20, 25, 35))
            }
        ]
    },
    {
        "chapter": 38,
        "title": "Genesis 38: Judah and Tamar",
        "subtitle": "Unfaithfulness, Righteousness, and The Messianic Line",
        "synopsis": "Judah settles near Adullam. His daughter-in-law Tamar is denied her rightful marriage to Shelah. She acts boldly to secure the lineage. Judah recognizes her righteousness, and she bears twin boys Perez and Zerah.",
        "themeColor": "#78350f",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 38:24–30",
                "image": "/assets/genesis/38/panel-1.jpg",
                "narration": "When confronted with the signet, cord, and staff, Judah recognized them and said, 'She is more righteous than I, since I wouldn’t give her to my son Shelah.' She gave birth to Perez, who carried forward the lineage of David.",
                "dialogue": [{"speaker": "Judah", "text": "‘She is more righteous than I, for I failed to give her my son Shelah.’", "isAdapted": False}],
                "altText": "Judah holding his signet seal and walking staff in solemn realization before the elders of the town",
                "style": "desert",
                "colors": ((120, 53, 15), (40, 20, 10))
            }
        ]
    },
    {
        "chapter": 39,
        "title": "Genesis 39: Joseph in Potiphar's House",
        "subtitle": "Integrity in Temptation and Favor in the Prison",
        "synopsis": "Joseph is bought by Potiphar, captain of Pharaoh's guard. The Lord prospers everything Joseph touches. Potiphar's wife falsely accuses Joseph when he refuses her advances. Cast into royal prison, the Lord remains with Joseph.",
        "themeColor": "#0f766e",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 39:1–9",
                "image": "/assets/genesis/39/panel-1.jpg",
                "narration": "The Lord was with Joseph so that he prospered, and Potiphar put him in charge of his household. When tempted day after day, Joseph refused: 'How could I do such a wicked thing and sin against God?'",
                "dialogue": [{"speaker": "Joseph", "text": "‘How then could I do such a wicked thing and sin against God?’", "isAdapted": False}],
                "altText": "Joseph fleeing the ornate Egyptian chamber, maintaining his purity of heart and faith in God",
                "style": "palace",
                "colors": ((15, 118, 110), (180, 140, 60))
            },
            {
                "scene": 2,
                "reference": "Genesis 39:20–23",
                "image": "/assets/genesis/39/panel-2.jpg",
                "narration": "Joseph's master put him in prison. But while Joseph was there in prison, the Lord was with him; He showed him kindness and granted him favor in the eyes of the prison warden.",
                "dialogue": [],
                "altText": "Joseph comforting fellow prisoners in the torch-lit stone arches of the royal Egyptian dungeon",
                "style": "palace",
                "colors": ((30, 41, 59), (180, 100, 30))
            }
        ]
    },
    {
        "chapter": 40,
        "title": "Genesis 40: The Cupbearer and The Baker",
        "subtitle": "Dreams in the Dungeon: Do Not Interpretations Belong to God?",
        "synopsis": "Pharaoh's cupbearer and baker are imprisoned with Joseph. Each has a perplexing dream on the same night. Joseph tells them: 'Do not interpretations belong to God?' He accurately interprets both dreams.",
        "themeColor": "#1e293b",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 40:1–23",
                "image": "/assets/genesis/40/panel-1.jpg",
                "narration": "Joseph said to them, 'Do not interpretations belong to God? Tell me your dreams.' Within three days, the chief cupbearer was restored to his position squeezing grapes into Pharaoh's cup, but he forgot Joseph.",
                "dialogue": [
                    {"speaker": "Joseph", "text": "‘Do not interpretations belong to God? Tell me your dreams.’", "isAdapted": False},
                    {"speaker": "Cupbearer", "text": "‘In my dream I saw a vine with three branches, and I squeezed grapes into Pharaoh’s cup.’", "isAdapted": False}
                ],
                "altText": "Joseph listening attentively to the two Egyptian officials by the flickering torchlight of the prison cell",
                "style": "palace",
                "colors": ((30, 41, 59), (160, 120, 50))
            }
        ]
    },
    {
        "chapter": 41,
        "title": "Genesis 41: Pharaoh's Dreams and Joseph's Exaltation",
        "subtitle": "Seven Years of Plenty and The Vizier of All Egypt",
        "synopsis": "Two years later, Pharaoh has disturbing dreams of seven fat cows eaten by seven lean cows, and seven full heads of grain swallowed by seven withered ones. Joseph is summoned from the pit. God reveals seven years of plenty followed by seven years of famine; Pharaoh appoints Joseph ruler over all Egypt.",
        "themeColor": "#eab308",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 41:14–36",
                "image": "/assets/genesis/41/panel-1.jpg",
                "narration": "Pharaoh said to Joseph, 'I had a dream, and no one can interpret it.' Joseph answered, 'I cannot do it, but God will give Pharaoh the answer he desires.' Joseph interpreted the seven years of abundance and seven years of famine.",
                "dialogue": [
                    {"speaker": "Pharaoh", "text": "‘I had a dream, and no one can interpret it. But I have heard that when you hear a dream you can interpret it.’", "isAdapted": False},
                    {"speaker": "Joseph", "text": "‘I cannot do it, but God will give Pharaoh the answer he desires.’", "isAdapted": False}
                ],
                "altText": "Clean-shaven Joseph in simple white linen standing before Pharaoh's golden throne beneath towering painted Egyptian pillars",
                "style": "palace",
                "colors": ((234, 179, 8), (40, 20, 10))
            },
            {
                "scene": 2,
                "reference": "Genesis 41:39–45",
                "image": "/assets/genesis/41/panel-2.jpg",
                "narration": "Pharaoh took his signet ring from his finger and put it on Joseph's finger. He dressed him in robes of fine linen and put a gold chain around his neck, declaring: 'Only with respect to the throne will I be greater than you.'",
                "dialogue": [{"speaker": "Pharaoh", "text": "‘Since God has made all this known to you, there is no one so discerning and wise. You shall be in charge of my palace.’", "isAdapted": False}],
                "altText": "Joseph riding in the second royal chariot of Egypt clothed in gold and fine white linen while people bow before him",
                "style": "palace",
                "colors": ((250, 204, 21), (30, 58, 138))
            }
        ]
    },
    {
        "chapter": 42,
        "title": "Genesis 42: The First Journey to Egypt",
        "subtitle": "Brothers Bow Down: The First Test",
        "synopsis": "Famine strikes Canaan. Jacob sends ten sons to Egypt to buy grain, keeping Benjamin at home. They bow before Joseph, unaware he is their brother. Joseph recognizes them, tests their honesty, holds Simeon, and sends them home with grain and secretly returned money.",
        "themeColor": "#854d0e",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 42:6–9",
                "image": "/assets/genesis/42/panel-1.jpg",
                "narration": "Joseph was the governor of the land. His brothers arrived and bowed down to him with their faces to the ground. As soon as Joseph saw his brothers, he recognized them, and remembered his dreams about them.",
                "dialogue": [
                    {"speaker": "Joseph (in Egyptian)", "text": "‘Where do you come from? You are spies to see where our land is unprotected!’", "isAdapted": False},
                    {"speaker": "Brothers", "text": "‘No, our lord, your servants have come to buy food. We are honest men, twelve brothers, the sons of one man in Canaan.’", "isAdapted": False}
                ],
                "altText": "The ten Hebrew brothers prostrate with their foreheads to the stone floor before the regal Egyptian Vizier",
                "style": "palace",
                "colors": ((161, 98, 7), (15, 23, 42))
            }
        ]
    },
    {
        "chapter": 43,
        "title": "Genesis 43: The Second Journey – Benjamin in Egypt",
        "subtitle": "Judah's Guarantee and The Feast at Joseph's House",
        "synopsis": "As grain runs out, Judah pledges his own life to bring Benjamin safely back. Jacob relents. The brothers arrive in Egypt with gifts and double money. Joseph sees Benjamin, is deeply moved to tears, and hosts a feast where Benjamin is served five times as much.",
        "themeColor": "#0284c7",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 43:29–34",
                "image": "/assets/genesis/43/panel-1.jpg",
                "narration": "As he looked about and saw his brother Benjamin, his own mother’s son, he asked, 'Is this your youngest brother?' Deeply moved at the sight of his brother, Joseph hurried out and looked for a place to weep.",
                "dialogue": [{"speaker": "Joseph", "text": "‘God be gracious to you, my son.’", "isAdapted": False}],
                "altText": "Joseph holding back tears of love looking upon his young brother Benjamin seated at the banquet table",
                "style": "palace",
                "colors": ((14, 165, 233), (250, 204, 21))
            }
        ]
    },
    {
        "chapter": 44,
        "title": "Genesis 44: The Silver Cup and Judah's Plea",
        "subtitle": "The Final Test and The Sacrifice of Love",
        "synopsis": "Joseph commands his silver divination cup hidden in Benjamin's grain sack. When overtaken on the road, the cup is found. Brought back in distress, Judah steps forward with a passionate plea, offering himself as a slave in Benjamin's place to spare his father's life.",
        "themeColor": "#991b1b",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 44:11–17",
                "image": "/assets/genesis/44/panel-1.jpg",
                "narration": "Each opened his sack. The cup was found in Benjamin’s sack! At this, they tore their clothes. They all loaded their donkeys and returned to the city.",
                "dialogue": [],
                "altText": "The gleaming silver cup pulled from the mouth of Benjamin's sack as the brothers tear their garments in anguish",
                "style": "desert",
                "colors": ((153, 27, 27), (30, 20, 20))
            },
            {
                "scene": 2,
                "reference": "Genesis 44:18–34",
                "image": "/assets/genesis/44/panel-2.jpg",
                "narration": "Judah went up to him: 'Now then, please let your servant remain here as my lord’s slave in place of the boy, and let the boy return with his brothers. How can I go back to my father if the boy is not with me?'",
                "dialogue": [{"speaker": "Judah", "text": "‘Please let your servant remain here as my lord’s slave in place of the boy, and let the boy return with his brothers.’", "isAdapted": False}],
                "altText": "Judah kneeling with intense earnestness before Joseph, offering his own freedom to save Benjamin and his father",
                "style": "palace",
                "colors": ((185, 28, 28), (20, 30, 50))
            }
        ]
    },
    {
        "chapter": 45,
        "title": "Genesis 45: Joseph Reveals Himself",
        "subtitle": "I Am Joseph! God Sent Me Ahead to Save Lives",
        "synopsis": "Joseph can no longer control himself. He orders all Egyptians to leave, weeps loudly, and reveals: 'I am Joseph! Is my father still living?' He comforts his terrified brothers, explaining that God orchestrated events to preserve a remnant. Pharaoh invites Jacob's family to settle in Goshen.",
        "themeColor": "#2563eb",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 45:1–8",
                "image": "/assets/genesis/45/panel-1.jpg",
                "narration": "Joseph wept so loudly that the Egyptians heard him. He said to his brothers: 'I am Joseph! Does my father still live?' He said: 'Do not be distressed or angry with yourselves for selling me here, because it was to save lives that God sent me ahead of you.'",
                "dialogue": [
                    {"speaker": "Joseph", "text": "‘I am Joseph! Is my father still alive? Come close to me... It was not you who sent me here, but God.’", "isAdapted": False}
                ],
                "altText": "Joseph weeping openly with tears streaming down his face, reaching out both arms to his stunned brothers",
                "style": "light",
                "colors": ((37, 99, 235), (254, 240, 138))
            },
            {
                "scene": 2,
                "reference": "Genesis 45:14–28",
                "image": "/assets/genesis/45/panel-2.jpg",
                "narration": "Then he threw his arms around his brother Benjamin and wept, and Benjamin embraced him, weeping. And he kissed all his brothers and wept over them. When Jacob heard that Joseph was alive and ruler of Egypt, his spirit revived.",
                "dialogue": [{"speaker": "Jacob (Israel)", "text": "‘I am convinced! My son Joseph is still alive. I will go and see him before I die.’", "isAdapted": False}],
                "altText": "Joseph and all his brothers embracing in tears of reconciliation and joy in the palace hall",
                "style": "palace",
                "colors": ((59, 130, 246), (251, 191, 36))
            }
        ]
    },
    {
        "chapter": 46,
        "title": "Genesis 46: Jacob Goes to Egypt",
        "subtitle": "Do Not Be Afraid to Go Down to Egypt",
        "synopsis": "Israel sets out for Egypt. At Beersheba, God speaks in visions of the night: 'Do not be afraid to go down to Egypt, for I will make you into a great nation there.' Israel and his seventy descendants travel in Pharaoh's wagons to Goshen, where Joseph rushes to embrace his father.",
        "themeColor": "#059669",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 46:1–4",
                "image": "/assets/genesis/46/panel-1.jpg",
                "narration": "God spoke to Israel in visions of the night: 'Jacob! Jacob! I am God, the God of your father. Do not be afraid to go down to Egypt, for I will make you into a great nation there. I will go down with you, and I will surely bring you back again.'",
                "dialogue": [{"speaker": "The Lord", "text": "‘Do not be afraid to go down to Egypt... I will go down with you and I will bring you back.’", "isAdapted": False}],
                "altText": "Aged Jacob offering sacrifices at the altar of Beersheba under the starlit canopy of the desert",
                "style": "cosmic",
                "colors": ((5, 150, 105), (15, 23, 42))
            },
            {
                "scene": 2,
                "reference": "Genesis 46:28–30",
                "image": "/assets/genesis/46/panel-2.jpg",
                "narration": "Joseph had his chariot made ready and went to Goshen to meet his father Israel. As soon as Joseph appeared before him, he threw his arms around his father and wept for a long time.",
                "dialogue": [{"speaker": "Israel", "text": "‘Now I am ready to die, since I have seen for myself that you are still alive.’", "isAdapted": False}],
                "altText": "Joseph stepping down from his royal chariot in Goshen, weeping on the neck of his elderly father Jacob",
                "style": "nature",
                "colors": ((34, 197, 94), (245, 158, 11))
            }
        ]
    },
    {
        "chapter": 47,
        "title": "Genesis 47: The Land of Goshen and Famine Wisdom",
        "subtitle": "Jacob Blesses Pharaoh and Sells Grain in Famine",
        "synopsis": "Joseph presents his father and brothers to Pharaoh. Jacob blesses the mighty ruler of Egypt. The family settles in the fertile land of Rameses/Goshen. As the famine worsens, Joseph wisely manages the grain supply, saving Egypt from starvation.",
        "themeColor": "#d97706",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 47:7–10",
                "image": "/assets/genesis/47/panel-1.jpg",
                "narration": "Joseph brought his father Jacob in and presented him before Pharaoh. Jacob blessed Pharaoh. Pharaoh asked him, 'How old are you?' Jacob answered, 'The years of my pilgrimage are a hundred and thirty.'",
                "dialogue": [{"speaker": "Jacob", "text": "‘The years of my pilgrimage are a hundred and thirty years; few and difficult have they been.’", "isAdapted": False}],
                "altText": "The venerable patriarch Jacob placing his hands in blessing upon the seated Pharaoh of Egypt",
                "style": "palace",
                "colors": ((217, 119, 6), (30, 40, 60))
            }
        ]
    },
    {
        "chapter": 48,
        "title": "Genesis 48: Jacob Blesses Joseph's Sons",
        "subtitle": "The Crossing of Hands: Ephraim and Manasseh",
        "synopsis": "Jacob falls ill. Joseph brings his two sons Manasseh and Ephraim. Though nearly blind, Jacob intentionally crosses his hands, placing his right hand upon the younger Ephraim and his left upon the firstborn Manasseh, blessing them with the covenant of Abraham.",
        "themeColor": "#6366f1",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 48:13–20",
                "image": "/assets/genesis/48/panel-1.jpg",
                "narration": "Israel reached out his right hand and put it on Ephraim’s head, though he was the younger, and crossing his arms, he put his left hand on Manasseh’s head. He blessed Joseph: 'May the God before whom my fathers walked bless these boys.'",
                "dialogue": [
                    {"speaker": "Joseph", "text": "‘Not so, my father; this one is the firstborn; put your right hand on his head.’", "isAdapted": False},
                    {"speaker": "Israel", "text": "‘I know, my son, I know... his younger brother will be greater than he.’", "isAdapted": False}
                ],
                "altText": "Elderly Jacob with crossed arms resting his hands on the heads of young Ephraim and Manasseh",
                "style": "light",
                "colors": ((99, 102, 241), (254, 243, 199))
            }
        ]
    },
    {
        "chapter": 49,
        "title": "Genesis 49: Jacob's Prophetic Blessing",
        "subtitle": "The Scepter of Judah and The Twelve Tribes of Israel",
        "synopsis": "Jacob gathers his twelve sons around his deathbed and delivers prophetic blessings concerning the destiny of the twelve tribes. He prophesies the royal scepter and Shiloh from Judah, and the fruitful bough of Joseph. He charges them to bury him in the Cave of Machpelah.",
        "themeColor": "#7c2d12",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 49:8–10",
                "image": "/assets/genesis/49/panel-1.jpg",
                "narration": "Jacob prophesied over Judah: 'Judah, your brothers will praise you... You are a lion’s cub, Judah. The scepter will not depart from Judah, nor the ruler’s staff from between his feet, until he to whom it belongs shall come.'",
                "dialogue": [{"speaker": "Jacob", "text": "‘The scepter will not depart from Judah... until He comes to whom it belongs; the obedience of the nations shall be His.’", "isAdapted": False}],
                "altText": "The silhouette of a majestic royal lion of Judah standing proudly beneath a blazing sunset horizon",
                "style": "nature",
                "colors": ((194, 65, 12), (30, 20, 20))
            },
            {
                "scene": 2,
                "reference": "Genesis 49:28–33",
                "image": "/assets/genesis/49/panel-2.jpg",
                "narration": "When Jacob had finished giving instructions to his sons, he drew his feet up into the bed, breathed his last and was gathered to his people.",
                "dialogue": [],
                "altText": "The twelve sons of Israel standing in solemn, reverent silence around their father's resting place",
                "style": "desert",
                "colors": ((120, 53, 15), (25, 20, 30))
            }
        ]
    },
    {
        "chapter": 50,
        "title": "Genesis 50: Forgiveness and Legacy",
        "subtitle": "God Meant It for Good: The Conclusion of Genesis",
        "synopsis": "Jacob is embalmed and carried with a great Egyptian and Hebrew procession to Canaan, buried in the Cave of Machpelah. The brothers fear Joseph will now take revenge. Joseph weeps and speaks comfort: 'You intended to harm me, but God intended it for good.' Joseph dies full of faith, instructing his bones to be carried up to the Promised Land.",
        "themeColor": "#1e3a8a",
        "panels": [
            {
                "scene": 1,
                "reference": "Genesis 50:1–14",
                "image": "/assets/genesis/50/panel-1.jpg",
                "narration": "Joseph threw himself on his father and wept over him and kissed him. A great cortege of Egyptian chariots, horsemen, and all the house of Israel accompanied Jacob’s body to the Cave of Machpelah in Canaan.",
                "dialogue": [],
                "altText": "A grand, dignified funeral procession of chariots and riders winding through the hills of Canaan toward Machpelah",
                "style": "desert",
                "colors": ((30, 58, 138), (180, 130, 50))
            },
            {
                "scene": 2,
                "reference": "Genesis 50:15–21",
                "image": "/assets/genesis/50/panel-2.jpg",
                "narration": "Joseph's brothers came and threw themselves down before him. But Joseph said to them: 'Don’t be afraid. Am I in the place of God? You intended to harm me, but God intended it for good to accomplish what is now being done, the saving of many lives.' And he spoke kindly to them and comforted them.",
                "dialogue": [
                    {"speaker": "Brothers", "text": "‘We are your slaves.’", "isAdapted": False},
                    {"speaker": "Joseph", "text": "‘Do not be afraid. You intended to harm me, but God intended it for good, to save many lives.’", "isAdapted": False}
                ],
                "altText": "Joseph gently lifting his kneeling brothers with eyes full of tears and forgiveness under warm palace arches",
                "style": "light",
                "colors": ((59, 130, 246), (254, 240, 138))
            },
            {
                "scene": 3,
                "reference": "Genesis 50:24–26",
                "image": "/assets/genesis/50/panel-3.jpg",
                "narration": "Then Joseph said to his brothers: 'I am about to die. But God will surely come to your aid and take you up out of this land to the land He promised on oath to Abraham, Isaac and Jacob.' Joseph died at age 110, embalmed and placed in a coffin in Egypt.",
                "dialogue": [{"speaker": "Joseph", "text": "‘God will surely come to your aid and take you up out of this land to the land He promised.’", "isAdapted": False}],
                "altText": "The coffin of Joseph in Egypt overlooking the distant eastern horizon pointing toward the Promised Land",
                "style": "palace",
                "colors": ((30, 41, 59), (234, 179, 8))
            }
        ]
    }
]

def main():
    print("Building Genesis 1-50 Story Dataset and Graphic Artworks...")
    processed_chapters = []

    for item in CHAPTER_SCHEMAS:
        ch = item["chapter"]
        print(f"Processing Chapter {ch}: {item['title']} ({len(item['panels'])} panels)")
        
        chapter_pages = []
        panels_for_page = []

        for p_idx, p in enumerate(item["panels"]):
            scene_num = p["scene"]
            # Target image path
            img_rel_path = f"/assets/genesis/{ch}/panel-{scene_num}.jpg"
            img_disk_path = os.path.join(OUTPUT_DIR, str(ch), f"panel-{scene_num}.jpg")

            # Generate panel artwork if not already high-res AI asset
            style = p.get("style", "nature")
            colors = p.get("colors", ((40, 60, 80), (10, 20, 30)))
            create_manhwa_panel(img_disk_path, width=1280, height=720, colors=colors, style=style, title=item["title"], ref=p["reference"])

            panel_data = {
                "panelId": f"gen-{ch}-{scene_num}",
                "scene": scene_num,
                "reference": p["reference"],
                "image": img_rel_path,
                "narration": p["narration"],
                "dialogue": p.get("dialogue", []),
                "altText": p.get("altText", f"Scene from {item['title']}"),
                "style": style
            }
            panels_for_page.append(panel_data)

            # Paginate: 2 panels per page or single if wide
            if len(panels_for_page) >= 2 or p_idx == len(item["panels"]) - 1:
                chapter_pages.append({
                    "page": len(chapter_pages) + 1,
                    "panels": panels_for_page
                })
                panels_for_page = []

        processed_chapters.append({
            "book": "Genesis",
            "chapter": ch,
            "title": item["title"],
            "subtitle": item["subtitle"],
            "synopsis": item["synopsis"],
            "themeColor": item.get("themeColor", "#0f172a"),
            "totalPages": len(chapter_pages),
            "totalPanels": len(item["panels"]),
            "pages": chapter_pages
        })

    dataset = {
        "version": "1.0.0",
        "book": "Genesis",
        "totalChapters": len(processed_chapters),
        "chapters": processed_chapters
    }

    with open(STORY_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully created story dataset at {STORY_DATA_FILE}!")
    print(f"Total illustrated chapters: {len(processed_chapters)} (Genesis 1 to 50)")

if __name__ == "__main__":
    main()
