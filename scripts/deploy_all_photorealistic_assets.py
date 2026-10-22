import os
import urllib.request
import shutil

PUBLIC_DIR = "public/assets/genesis"
DIST_DIR = "dist/assets/genesis"

# Full mapping of remaining chapters to photorealistic high-res cinematic photography
REMAINING_CHAPTER_PHOTOS = [
    # Genesis 5 - Adam's Lineage & Enoch Walking with God
    (5, 1, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1280&q=85",
     "Photorealistic mountain ridgeline where Enoch walked in fellowship with God into the golden dawn"),
    (5, 2, "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1280&q=85",
     "Ancient mountain valley settlements across the centuries of the early patriarchs"),

    # Genesis 10 - The Table of Nations / Ancient Maritime Coastlands
    (10, 1, "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1280&q=85",
     "Vast Mediterranean coastlines and maritime islands where the nations spread across the known earth"),

    # Genesis 13 - Abram and Lot Separate
    (13, 1, "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1280&q=85",
     "Lush, fertile Jordan river valley stretching towards the southern plain"),
    (13, 2, "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1280&q=85",
     "Abram gazing across the rugged Canaanite highlands from north to south, east to west"),

    # Genesis 14 - Abram Rescues Lot / King Melchizedek
    (14, 1, "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1280&q=85",
     "Rugged rocky desert canyons where the kings fought across the valley of Siddim"),
    (14, 2, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1280&q=85",
     "Valley of Shaveh bathed in warm golden sunset as bread and wine are offered in peace"),

    # Genesis 16 - Hagar and The God Who Sees
    (16, 1, "https://images.unsplash.com/photo-1472214103451-9374bd1c798e?auto=format&fit=crop&w=1280&q=85",
     "A crystal freshwater spring welling up beside desert dunes at Beer-lahai-roi"),

    # Genesis 17 - The Covenant of Circumcision
    (17, 1, "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=1280&q=85",
     "Abram prostrate on the desert earth under an incandescent expanse of stars"),

    # Genesis 18 - Three Heavenly Visitors at Mamre
    (18, 1, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1280&q=85",
     "Venerable ancient oak trees of Mamre casting cool deep shade in the heat of midday"),
    (18, 2, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1280&q=85",
     "High mountain overlook looking down upon the Dead Sea rift valley at twilight"),

    # Genesis 19 - The Fall of Sodom
    (19, 1, "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1280&q=85",
     "Dark, brooding tempest clouds and crimson lightning strikes over rocky desert wastes"),

    # Genesis 20 - Abraham and Abimelech
    (20, 1, "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1280&q=85",
     "Stony rolling hills and olive orchards of Gerar under clear southern skies"),

    # Genesis 21 - The Birth of Isaac & Water in the Wilderness
    (21, 1, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1280&q=85",
     "Warm patriarchal tent encampment in morning sunlight on the slopes of Beersheba"),
    (21, 2, "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1280&q=85",
     "The parched wilderness of Beersheba where God opened Hagar's eyes to see a well of water"),

    # Genesis 23 - The Cave of Machpelah
    (23, 1, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1280&q=85",
     "Ancient limestone cave entrance shrouded by centuries-old olive trees in the field of Ephron"),

    # Genesis 25 - Jacob and Esau / The Lentil Stew
    (25, 1, "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=1280&q=85",
     "The night sky over the desert tents where Rebekah inquired of the Lord"),
    (25, 2, "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1280&q=85",
     "Campfire smoke rising at sunset as the weary hunter returns from the open fields"),

    # Genesis 26 - Isaac's Wells in Gerar
    (26, 1, "https://images.unsplash.com/photo-1472214103451-9374bd1c798e?auto=format&fit=crop&w=1280&q=85",
     "Deep stone-lined water well surrounded by green reeds in the dry Gerar valley"),

    # Genesis 27 - The Stolen Blessing
    (27, 1, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1280&q=85",
     "Warm interior glow of the patriarchal tent with woven wool and earthen vessels"),
    (27, 2, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1280&q=85",
     "Rugged rocky mountain heights where Esau wept bitterly under the open heaven"),

    # Genesis 29 - Jacob Meets Rachel at Haran
    (29, 1, "https://images.unsplash.com/photo-1472214103451-9374bd1c798e?auto=format&fit=crop&w=1280&q=85",
     "Pastoral stone well in the golden fields of the east with sheep resting at noon"),
    (29, 2, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1280&q=85",
     "Rolling green hills and pastures of Paddan-Aram under summer skies"),

    # Genesis 30 - Jacob's Flocks Flourish
    (30, 1, "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1280&q=85",
     "Sunrise over the pastoral highland camp with family tents and morning dew"),
    (30, 2, "https://images.unsplash.com/photo-1433086966358-54859d0ed716?auto=format&fit=crop&w=1280&q=85",
     "Pristine mountain stream running over stones where the herds gathered to drink"),

    # Genesis 31 - The Memorial Cairn of Gilead
    (31, 1, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1280&q=85",
     "High windy summit of Mount Gilead where a memorial heap of stones was raised in covenant"),

    # Genesis 33 - Jacob and Esau Reconcile
    (33, 1, "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1280&q=85",
     "Vast dusty valley of the Jabbok where twin brothers and their camps met in peace"),

    # Genesis 34 - Ancient Shechem
    (34, 1, "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1280&q=85",
     "Massive ancient stone walls and city ramparts under heavy stormy skies"),

    # Genesis 35 - Return to Bethel & Road to Ephrath
    (35, 1, "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1280&q=85",
     "Solitary stone altar on the rocky plateau of Bethel under magnificent mountain skies"),
    (35, 2, "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1280&q=85",
     "Stone pillar standing beside the ancient hillside road leading toward Ephrath"),

    # Genesis 36 - Mount Seir / Edomite Canyons
    (36, 1, "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1280&q=85",
     "Towering red sandstone cliffs and deep rugged chasms of Mount Seir"),

    # Genesis 38 - The Hills of Timnah
    (38, 1, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1280&q=85",
     "Golden terraced hills and stone walls of Timnah where sheep-shearers gathered"),

    # Genesis 39 - Joseph in Egyptian Palace & Prison
    (39, 1, "https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=1280&q=85",
     "Sunlit Egyptian palace colonnades with carved limestone pillars and courtyards"),
    (39, 2, "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1280&q=85",
     "Atmospheric underground stone arches and fortress corridors lit by flickering torches"),

    # Genesis 40 - Joseph in the Prison Vaults
    (40, 1, "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1280&q=85",
     "Ancient Egyptian royal prison quarters with heavy masonry and narrow slit of daylight"),

    # Genesis 42 - The Sons of Israel Bow in Egypt
    (42, 1, "https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=1280&q=85",
     "Vast Egyptian audience hall with polished stone pavement and towering lotus columns"),

    # Genesis 43 - The Feast in Joseph's House
    (43, 1, "https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=1280&q=85",
     "Ornate dining court in Egypt with ceremonial bowls and warm afternoon sunlight"),

    # Genesis 44 - The Silver Cup / Judah Pleading
    (44, 1, "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1280&q=85",
     "Caravan donkeys bearing sacks of grain on the desert road just outside the Egyptian gates"),
    (44, 2, "https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=1280&q=85",
     "High judgment hall of Egypt where Judah stood with impassioned plea before the ruler"),

    # Genesis 46 - Beersheba Altar & Arrival in Goshen
    (46, 1, "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=1280&q=85",
     "Night sacrifice at the solitary stone altar of Beersheba under glowing starlight"),
    (46, 2, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1280&q=85",
     "The verdant, fertile pasturelands of Goshen meeting the open eastern horizon"),

    # Genesis 47 - Jacob Blessing Pharaoh
    (47, 1, "https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=1280&q=85",
     "Royal Egyptian throne room with ceremonial sunlight bathing the limestone pillars"),

    # Genesis 48 - Blessing Ephraim and Manasseh
    (48, 1, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1280&q=85",
     "Peaceful room in Goshen with soft golden afternoon light filling the space"),

    # Genesis 49 - The Lion of Judah & The Twelve Tribes
    (49, 1, "https://images.unsplash.com/photo-1534188753412-3e26d0d618d6?auto=format&fit=crop&w=1280&q=85",
     "Magnificent male lion atop a rugged rock ridge surveying the plains at golden hour"),
    (49, 2, "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1280&q=85",
     "Solemn assembly of the twelve sons of Israel on a hilltop overlooking the ancient lands")
]

def download_and_save(ch, scene, url, alt):
    pub_path = os.path.join(PUBLIC_DIR, str(ch), f"panel-{scene}.jpg")
    dist_path = os.path.join(DIST_DIR, str(ch), f"panel-{scene}.jpg")
    os.makedirs(os.path.dirname(pub_path), exist_ok=True)
    os.makedirs(os.path.dirname(dist_path), exist_ok=True)
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            with open(pub_path, "wb") as f:
                f.write(data)
            with open(dist_path, "wb") as f:
                f.write(data)
            print(f"Downloaded photoreal panel Gen {ch}:{scene} ({len(data)} bytes)")
            return True
    except Exception as e:
        print(f"Error downloading Gen {ch}:{scene}: {e}")
        return False

def main():
    print("Deploying photorealistic photography across remaining chapters...")
    success_count = 0
    for ch, scene, url, alt in REMAINING_CHAPTER_PHOTOS:
        if download_and_save(ch, scene, url, alt):
            success_count += 1
    print(f"\nSuccessfully downloaded and saved {success_count}/{len(REMAINING_CHAPTER_PHOTOS)} photorealistic panels.")

if __name__ == "__main__":
    main()
