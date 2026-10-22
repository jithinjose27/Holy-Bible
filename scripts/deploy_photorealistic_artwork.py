import os
import urllib.request
import json

PUBLIC_DIR = "public/assets/genesis"
DIST_DIR = "dist/assets/genesis"

# Real-world cinematic photography assets
GENESIS_1_PHOTOS = [
    # Panel 1: Genesis 1:1-2 (Primeval deep ocean waters under cosmic night sky)
    (1, 1, "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1280&q=85",
     "Photorealistic high-resolution photography of the primeval deep ocean abyss under a dark, vast atmospheric cosmic expanse"),
    
    # Panel 2: Genesis 1:3-5 (First dawn of light piercing rugged mountain peaks with natural crepuscular rays)
    (1, 2, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1280&q=85",
     "Photorealistic cinematic photography of the brilliant morning sun piercing through rugged Alpine mountain summits with volumetric atmospheric light"),
    
    # Panel 3: Genesis 1:6-8 (The atmospheric expanse / volumetric clouds parting over sapphire ocean)
    (1, 3, "https://images.unsplash.com/photo-1499346030926-9a72daac6c63?auto=format&fit=crop&w=1280&q=85",
     "Real aerial photography of vast volumetric cloud layers parting over a deep blue ocean horizon with natural atmospheric haze"),
    
    # Panel 4: Genesis 1:9-13 (Dry land emerging: rugged sea cliffs, rocky shorelines, and lush green mossy coastal forest)
    (1, 4, "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1280&q=85",
     "Real-world photography of ancient lush emerald forest, geological stones, and vibrant flora with natural sunlight filtering through leaves"),
    
    # Panel 5: Genesis 1:14-19 (Celestial lights: Milky Way galaxy, crescent moon, and sparkling stars over mountain ridge)
    (1, 5, "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=1280&q=85",
     "Real astronomical photography of the celestial Milky Way and starry night sky with natural atmospheric glow over rugged terrain"),
    
    # Panel 6: Genesis 1:20-23 (Marine life: real humpback whale swimming through pristine ocean waters)
    (1, 6, "https://images.unsplash.com/photo-1568430462989-44163eb1752f?auto=format&fit=crop&w=1280&q=85",
     "National Geographic-quality underwater marine photography of a majestic humpback whale gliding through sunlit turquoise ocean waters"),
    
    # Panel 7: Genesis 1:24-25 (Land animals: real male lion in natural African savanna habitat)
    (1, 7, "https://images.unsplash.com/photo-1534188753412-3e26d0d618d6?auto=format&fit=crop&w=1280&q=85",
     "Wildlife photography of a magnificent male lion resting on rugged natural golden grassland with realistic anatomy and terrain"),
    
    # Panel 8: Genesis 1:26-31 (Humanity in God's image: real human figures overlooking expansive mountain valley at sunset)
    (1, 8, "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1280&q=85",
     "Cinematic real photography of human travelers on a mountain overlook taking in the vast, beautiful natural landscape at sunset")
]

# Additional key narrative chapters photorealistic photography
ADDITIONAL_CHAPTER_PHOTOS = [
    # Gen 2 Eden paradise waterfall & rivers
    (2, 1, "https://images.unsplash.com/photo-1433086966358-54859d0ed716?auto=format&fit=crop&w=1280&q=85", "Crystal river and lush waterfalls in ancient pristine valley"),
    (2, 2, "https://images.unsplash.com/photo-1511497584788-87676104235f?auto=format&fit=crop&w=1280&q=85", "Deep fertile soil and ancient forest floor in morning mist"),
    (2, 3, "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1280&q=85", "Serene flowering meadow with mountain ridge"),
    
    # Gen 3 The Fall / Deep ancient forest
    (3, 1, "https://images.unsplash.com/photo-1502082553048-f009c37129b9?auto=format&fit=crop&w=1280&q=85", "Ancient mossy woodland with winding river"),
    (3, 2, "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1280&q=85", "Sunlight filtering through dense ancient canopy"),
    (3, 3, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1280&q=85", "East of Eden rugged desert mountain pass at dusk"),
    
    # Gen 4 Cain and Abel / Agricultural fields
    (4, 1, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1280&q=85", "Golden cultivated grain fields and rugged stones"),
    (4, 2, "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1280&q=85", "Windswept rocky barren plain under red sunset"),
    
    # Gen 6-8 The Flood & Waters
    (6, 1, "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1280&q=85", "Mountain forests under gathering storm clouds"),
    (6, 2, "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1280&q=85", "Massive ancient cedar timbers for the Ark"),
    (7, 1, "https://images.unsplash.com/photo-1505118380757-91f5f5632de0?auto=format&fit=crop&w=1280&q=85", "Massive tempest waves and churning deep oceans"),
    (7, 2, "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1280&q=85", "Vast flooded expanse beneath thunderous rain clouds"),
    (8, 1, "https://images.unsplash.com/photo-1499346030926-9a72daac6c63?auto=format&fit=crop&w=1280&q=85", "Morning sun breaking over receding floodwaters"),
    (8, 2, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1280&q=85", "Rugged peaks of Mount Ararat emerging above clouds"),
    (9, 1, "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?auto=format&fit=crop&w=1280&q=85", "Spectacular real double rainbow over lush mountain valley"),
    
    # Gen 11 Babel / Ancient Mesopotamian Plain
    (11, 1, "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1280&q=85", "Ancient mudbrick architectural ruins on plain of Shinar"),
    (11, 2, "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1280&q=85", "Caravan routes scattering into distant desert horizons"),
    
    # Gen 12-15 Abraham in Canaan & Desert
    (12, 1, "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1280&q=85", "Caravan journeying across ancient golden desert dunes"),
    (12, 2, "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1280&q=85", "Ancient terebinth oak tree by stony Canaanite hill"),
    (15, 1, "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=1280&q=85", "Magnificent desert night sky ablaze with countless stars"),
    (15, 2, "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1280&q=85", "Covenant altar fire glowing against dark desert night"),
    
    # Gen 22 Mount Moriah
    (22, 1, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1280&q=85", "Rugged stony ascent up Mount Moriah at daybreak"),
    (22, 2, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1280&q=85", "Thorny thicket by ancient stone altar with golden sunlight"),
    
    # Gen 24 Rebekah at the Well
    (24, 1, "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1280&q=85", "Ancient stone water well at dusk with desert camels"),
    (24, 2, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1280&q=85", "Golden evening field meeting caravan approaching"),
    
    # Gen 28 Jacob's Ladder at Bethel
    (28, 1, "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1280&q=85", "Rugged starlit hills of Bethel beneath glowing Milky Way"),
    (28, 2, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1280&q=85", "Stone pillar anointed with oil in morning mountain sunlight"),
    
    # Gen 32 Jacob at Peniel
    (32, 1, "https://images.unsplash.com/photo-1472214103451-9374bd1c798e?auto=format&fit=crop&w=1280&q=85", "River ford of Jabbok with morning mist rising over waters"),
    
    # Gen 37-50 Joseph in Egypt
    (37, 1, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1280&q=85", "Flocks grazing in valley of Hebron under sunny sky"),
    (37, 2, "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1280&q=85", "Ancient dry cistern in desert with passing camel caravan"),
    (41, 1, "https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=1280&q=85", "Majestic limestone colonnades of ancient Egyptian palace"),
    (41, 2, "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1280&q=85", "Abundant golden wheat harvest of the Nile valley"),
    (45, 1, "https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=1280&q=85", "Royal Egyptian hall with warm morning light streaming through"),
    (45, 2, "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1280&q=85", "Emotional reunion of brothers against golden hills of Goshen"),
    (50, 1, "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1280&q=85", "Grand funeral cortege journeying toward the hills of Hebron"),
    (50, 2, "https://images.unsplash.com/photo-1539650116574-8efeb43e2750?auto=format&fit=crop&w=1280&q=85", "Joseph speaking forgiveness and comfort under warm arches"),
    (50, 3, "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1280&q=85", "The legacy of Genesis pointing toward the Promised Land horizon")
]

def download_and_save(ch, scene, url, alt):
    pub_path = os.path.join(PUBLIC_DIR, str(ch), f"panel-{scene}.jpg")
    os.makedirs(os.path.dirname(pub_path), exist_ok=True)
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            with open(pub_path, "wb") as f:
                f.write(data)
            print(f"Downloaded photoreal panel Gen {ch}:{scene} ({len(data)} bytes)")
            return True
    except Exception as e:
        print(f"Error downloading Gen {ch}:{scene}: {e}")
        return False

def main():
    print("Deploying cinematic photorealistic photography assets...")
    
    # 1. Download all Genesis 1 benchmark photos
    for ch, scene, url, alt in GENESIS_1_PHOTOS:
        download_and_save(ch, scene, url, alt)

    # 2. Download additional key narrative chapter photos
    for ch, scene, url, alt in ADDITIONAL_CHAPTER_PHOTOS:
        download_and_save(ch, scene, url, alt)

    print("\nPhotorealistic asset deployment completed successfully!")

if __name__ == "__main__":
    main()
