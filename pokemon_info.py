# CST205: Mulitmedia Design and Programming
# Nyra Usi
# 12/11/2020
# This program contains all the pokemon information and classifies strenghts as moves that are super effective. Pokemon #674 - 719 done by Daniel and Jasmine.

# Sources: https://www.serebii.net/xy/pokemon.shtml
# Sources: https://pokestop.io/

pokemon_info = [
    {
        "name" : "Chespin",
        "type1" : "Grass",
        "type2" : "Neutral",
        "strengths" : ["Ground", "Water", "Rock"],
        "image_id" : "650"
    },
    {
        "name" : "Quilladin",
        "type1" : "Grass",
        "type2" : "Neutral",
        "strengths" : ["Ground", "Water", "Rock"],
        "image_id" : "651"
    },
    {
        "name" : "Chesnaught",
        "type1" : "Grass",
        "type2" : "Fighting",
        "strengths" : ["Ground", "Water", "Rock", "Normal", "Steel", "Ice", "Dark"],
        "image_id" : "652"
    },
    {
        "name" : "Fennekin",
        "type1" : "Fire",
        "type2" : "Neutral",
        "strengths" : ["Bug", "Steel", "Grass", "Ice"],
        "image_id" : "653"
    },
    {
        "name" : "Braixen",
        "type1" : "Fire",
        "type2" : "Neutral",
        "strengths" : ["Bug", "Steel", "Grass", "Ice"],
        "image_id" : "654"
    },
    {
        "name" : "Delphox",
        "type1" : "Fire",
        "type2" : "Psychic",
        "strengths" : ["Bug", "Steel", "Grass", "Ice", "Fighting", "Poison"],
        "image_id" : "655"
    },
    {
        "name" : "Froakie",
        "type1" : "Water",
        "type2" : "Neutral",
        "strengths" : ["Ground", "Rock", "Fire"],
        "image_id" : "656"
    },
    {
        "name" : "Frogadier",
        "type1" : "Water",
        "type2" : "Neutral",
        "strengths" : ["Ground", "Rock", "Fire"],
        "image_id" : "657"
    },
    {
        "name" : "Greninja",
        "type1" : "Water",
        "type2" : "Dark",
        "strengths" : ["Ground", "Rock", "Fire", "Ghost", "Psychic"],
        "image_id" : "658"
    },
    {
        "name" : "Bunnelby",
        "type1" : "Normal",
        "type2" : "Neutral",
        "strengths" : [],
        "image_id" : "659"
    },
    {
        "name" : "Diggersby",
        "type1" : "Normal",
        "type2" : "Ground",
        "strengths" : ["Poison", "Rock", "Steel", "Fire", "Electric"],
        "image_id" : "660"
    },
    {
        "name" : "Fletchling",
        "type1" : "Normal",
        "type2" : "Flying",
        "strengths" : ["Fighting", "Bug", "Grass"],
        "image_id" : "661"
    },
    {
        "name" : "Fletchinder",
        "type1" : "Fire",
        "type2" : "Flying",
        "strengths" : ["Fighting", "Bug", "Grass", "Steel", "Ice"],
        "image_id" : "662"
    },
    {
        "name" : "Talonflame",
        "type1" : "Fire",
        "type2" : "Flying",
        "strengths" : ["Fighting", "Bug", "Grass", "Steel", "Ice"],
        "image_id" : "663"
    },
    {
        "name" : "Scatterbug",
        "type1" : "Bug",
        "type2" : "Neutral",
        "strengths" : ["Grass", "Psychic", "Dark"],
        "image_id" : "664"
    },
    {
        "name" : "Spewpa",
        "type1" : "Bug",
        "type2" : "Neutral",
        "strengths" : ["Grass", "Psychic", "Dark"],
        "image_id" : "665"
    },
    {
        "name" : "Vivillon",
        "type1" : "Bug",
        "type2" : "Flying",
        "strengths" : ["Grass", "Psychic", "Dark", "Bug", "Fighting"],
        "image_id" : "666"
    },
    {
        "name" : "Litleo",
        "type1" : "Fire",
        "type2" : "Normal",
        "strengths" : ["Bug", "Steel", "Grass", "Ice"],
        "image_id" : "667"
    },
    {
        "name" : "Pyroar",
        "type1" : "Fire",
        "type2" : "Normal",
        "strengths" : ["Bug", "Steel", "Grass", "Ice"],
        "image_id" : "668"
    },
    {
        "name" : "Flabebe",
        "type1" : "Fairy",
        "type2" : "Neutral",
        "strengths" : ["Dragon", "Fighting", "Dark"],
        "image_id" : "669"
    },
    {
        "name" : "Floette",
        "type1" : "Fairy",
        "type2" : "Neutral",
        "strengths" : ["Dragon", "Fighting", "Dark"],
        "image_id" : "670"
    },
    {
        "name" : "Florges",
        "type1" : "Fairy",
        "type2" : "Neutral",
        "strengths" : ["Dragon", "Fighting", "Dark"],
        "image_id" : "671"
    },
    {
        "name" : "Skiddo",
        "type1" : "Grass",
        "type2" : "Neutral",
        "strengths" : ["Ground", "Water", "Rock"],
        "image_id" : "672"
    },
    {
        "name" : "Gogoat",
        "type1" : "Grass",
        "type2" : "Neutral",
        "strengths" : ["Ground", "Water", "Rock"],
        "image_id" : "673"
    },
        {
        "name" : "Pancham",
        "type1" : "Fight",
        "type2" : "Neutral",
        "strengths" : ["Normal", "Rock", "Steel", "Ice", "Dark"],
        "image_id" : "674"
    },
    {
        "name" : "Pangoro",
        "type1" : "Fight",
        "type2" : "Dark",
        "strengths" : ["Normal", "Rock", "Steel", "Ice", "Dark", "Ghost", "Psychic"],
        "image_id" : "675"
    },
    {
        "name" : "Furfrou",
        "type1" : "Normal",
        "type2" : "Neutral",
        "strengths" : [],
        "image_id" : "676"
    },
    {
        "name" : "Espurr",
        "type1" : "Psychic",
        "type2" : "Neutral",
        "strengths" : ["Fighting", "Poison"],
        "image_id" : "677"
    },
    {
        "name" : "Meowstic",
        "type1" : "Psychic",
        "type2" : "Neutral",
        "strengths" : ["Fighting", "Poison"],
        "image_id" : "678"
    },
    {
        "name" : "Honedge",
        "type1" : "Steel",
        "type2" : "Ghost",
        "strengths" : ["Rock", "Ghost", "Psychic", "Ice", "Fairy"],
        "image_id" : "679"
    },
    {
        "name" : "Doublade",
        "type1" : "Steel",
        "type2" : "Ghost",
        "strengths" : ["Rock", "Ghost", "Psychic", "Ice", "Fairy"],
        "image_id" : "680"
    },
    {
        "name" : "Aegislash",
        "type1" : "Steel",
        "type2" : "Ghost",
        "strengths" : ["Rock", "Ghost", "Psychic", "Ice", "Fairy"],
        "image_id" : "681"
    },
    {
        "name" : "Spritzee",
        "type1" : "Fairy",
        "type2" : "Neutral",
        "strengths" : ["Dragon", "Fighting", "Dark"],
        "image_id" : "682"
    },
    {
        "name" : "Aromatisse",
        "type1" : "Fairy",
        "type2" : "Neutral",
        "strengths" : ["Dragon", "Fighting", "Dark"],
        "image_id" : "683"
    },
    {
        "name" : "Swirlix",
        "type1" : "Fairy",
        "type2" : "Neutral",
        "strengths" : ["Dragon", "Fighting", "Dark"],
        "image_id" : "684"
    },
    {
        "name" : "Slurpuff",
        "type1" : "Fairy",
        "type2" : "Neutral",
        "strengths" : ["Dragon", "Fighting", "Dark"],
        "image_id" : "685"
    },
    {
        "name" : "Inkay",
        "type1" : "Dark",
        "type2" : "Psychic",
        "strengths" : ["Psychic", "Ghost", "Poison", "Fighting"],
        "image_id" : "686"
    },
    {
        "name" : "Malamar",
        "type1" : "Dark",
        "type2" : "Psychic",
        "strengths" : ["Psychic", "Ghost", "Poison", "Fighting"],
        "image_id" : "687"
    },
    {
        "name" : "Binacle",
        "type1" : "Rock",
        "type2" : "Water",
        "strengths" : ["Fire", "Flying", "Ground", "Rock", "Bug", "Ice"],
        "image_id" : "688"
    },
    {
        "name" : "Barbaracle",
        "type1" : "Rock",
        "type2" : "Water",
        "strengths" : ["Fire", "Flying", "Ground", "Rock", "Bug", "Ice"],
        "image_id" : "689"
    },
    {
        "name" : "Skrelp",
        "type1" : "Poison",
        "type2" : "Water",
        "strengths" : ["Ground", "Rock", "Fire", "Grass", "Fairy"],
        "image_id" : "690"
    },
    {
        "name" : "Dragalge",
        "type1" : "Poison",
        "type2" : "Dragon",
        "strengths" : ["Grass", "Dragon", "Fairy"],
        "image_id" : "691"
    },
    {
        "name" : "Clauncher",
        "type1" : "Water",
        "type2" : "Neutral",
        "strengths" : ["Ground", "Rock", "Fire"],
        "image_id" : "692"
    },
    {
        "name" : "Clawitzer",
        "type1" : "Water",
        "type2" : "Neutral",
        "strengths" : ["Ground", "Rock", "Fire"],
        "image_id" : "693"
    },
    {
        "name" : "Helioptile",
        "type1" : "Electric",
        "type2" : "Normal",
        "strengths" : ["Flying", "Water"],
        "image_id" : "694"
    },
    {
        "name" : "Helioptile",
        "type1" : "Electric",
        "type2" : "Normal",
        "strengths" : ["Flying", "Water"],
        "image_id" : "695"
    },
    {
        "name" : "Tyrunt",
        "type1" : "Rock",
        "type2" : "Dragon",
        "strengths" : ["Flying", "Bug", "Fire", "Ice", "Dragon"],
        "image_id" : "696"
    },
    {
        "name" : "Tyrantrum",
        "type1" : "Rock",
        "type2" : "Dragon",
        "strengths" : ["Flying", "Bug", "Fire", "Ice", "Dragon"],
        "image_id" : "697"
    },
        {
        "name" : "Amaura",
        "type1" : "Rock",
        "type2" : "Ice",
        "strengths" : ["Normal", "Flying", "Poison", "Ice"],
        "image_id" : "698"
    },
    {
        "name" : "Aurorus",
        "type1" : "Rock",
        "type2" : "Ice",
        "strengths" : ["Flying", "Ground", "Bug", "Fire", "Grass", "Ice", "Dragon"],
        "image_id" : "699"
    },
    {
        "name" : "Sylveon",
        "type1" : "Fairy",
        "type2" : "Neutral",
        "strengths" : ["Dragon", "Fighting", "Dark"],
        "image_id" : "700"
    },
    {
        "name" : "Hawlucha",
        "type1" : "Fighting",
        "type2" : "Flying",
        "strengths" : ["Normal", "Fighting", "Rock", "Bug", "Steel", "Grass", "Ice", "Dark"],
        "image_id" : "701"
    },
    {
        "name" : "Dedenne",
        "type1" : "Electric",
        "type2" : "Fairy",
        "strengths" : ["Fighting", "Flying", "Water", "Dragon", "Dark"],
        "image_id" : "702"
    },
    {
        "name" : "Carbink",
        "type1" : "Rock",
        "type2" : "Fairy",
        "strengths" : ["Fighting", "Flying", "Bug", "Fire", "Ice", "Dragon", "Dark"],
        "image_id" : "703"
    },
    {
        "name" : "Goomy",
        "type1" : "Dragon",
        "type2" : "Neutral",
        "strengths" : ["Dragon"],
        "image_id" : "704"
    },
    {
        "name" : "Sliggoo",
        "type1" : "Dragon",
        "type2" : "Neutral",
        "strengths" : ["Dragon"],
        "image_id" : "705"
    },
    {
        "name" : "Goodra",
        "type1" : "Dragon",
        "type2" : "Neutral",
        "strengths" : ["Dragon"],
        "image_id" : "706"
    },
    {
        "name" : "Klefki",
        "type1" : "Steel",
        "type2" : "Fairy",
        "strengths" : ["Fighting", "Rock", "Ice", "Dragon", "Dark", "Fairy"],
        "image_id" : "707"
    },
    {
        "name" : "Phantump",
        "type1" : "Ghost",
        "type2" : "Grass",
        "strengths" : ["Ground", "Rock", "Ghost", "Water", "Pyschic"],
        "image_id" : "708"
    },
    {
        "name" : "Trevenant",
        "type1" : "Ghost",
        "type2" : "Grass",
        "strengths" : ["Ground", "Rock", "Ghost", "Water", "Pyschic"],
        "image_id" : "709"
    },
    {
        "name" : "Pumpkaboo",
        "type1" : "Ghost",
        "type2" : "Grass",
        "strengths" : ["Ground", "Rock", "Ghost", "Water", "Pyschic"],
        "image_id" : "710"
    },
    {
        "name" : "Gourgeist",
        "type1" : "Ghost",
        "type2" : "Grass",
        "strengths" : ["Ground", "Rock", "Ghost", "Water", "Pyschic"],
        "image_id" : "711"
    },
    {
        "name" : "Bergmite",
        "type1" : "Ice",
        "type2" : "Neutral",
        "strengths" : ["Flying", "Ground", "Grass", "Dragon"],
        "image_id" : "712"
    },
    {
        "name" : "Avalugg",
        "type1" : "Ice",
        "type2" : "Neutral",
        "strengths" : ["Flying", "Ground", "Grass", "Dragon"],
        "image_id" : "713"
    },
    {
        "name" : "Noibat",
        "type1" : "Flying",
        "type2" : "Dragon",
        "strengths" : ["Fighting", "Bug", "Grass", "Dragon"],
        "image_id" : "714"
    },
    {
        "name" : "Noivern",
        "type1" : "Flying",
        "type2" : "Dragon",
        "strengths" : ["Fighting", "Bug", "Grass", "Dragon"],
        "image_id" : "715"
    },
    {
        "name" : "Xerneas",
        "type1" : "Fairy",
        "type2" : "Neutral",
        "strengths" : ["Fighting", "Dragon", "Dark"],
        "image_id" : "716"
    },
    {
        "name" : "Yveltal",
        "type1" : "Dark",
        "type2" : "Flying",
        "strengths" : ["Fighting", "Bug", "Ghost", "Grass", "Psychic"],
        "image_id" : "717"
    },
    {
        "name" : "Zygarde",
        "type1" : "Dragon",
        "type2" : "Ground",
        "strengths" : ["Poison", "Rock", "Steel", "Fire", "Electric", "Dragon"],
        "image_id" : "718"
    },
    {
        "name" : "Diancie",
        "type1" : "Rock",
        "type2" : "Fairy",
        "strengths" : ["Fighting", "Flying", "Bug", "Fire", "Ice", "Dragon", "Dark"],
        "image_id" : "719"
    }
]