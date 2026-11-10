"""kit32: parametric chibi32 asset templates for the rpg100 set.

Every asset in SPECS is built from shared 32x32 grids (the hero's head, body, legs and a few new ones),
recolored through key maps and combined with hand-drawn extras. assets/<id>/recipe.py calls make(id).
Characters reuse the hero walk cycle; tiles are drawn by key functions and wrap seamlessly.
"""
from __future__ import annotations

import random

from drawkit import Layer, Recipe

PALETTE = "../../styles/chibi32/palette.txt"

# ---------------------------------------------------------------- shared grids (chibi32 hero parts)
HEAD = """
.......W....W...
......WW...WW...
...W.WWW..WWW...
...WWWWWWWWWWW..
.WWWWWWWWWWWWWW.
WWWWWWWWWWWWWWww
.WWWWWWWWWWWWwww
..wWWWwWWWwSwww.
.WwwWwhSSShSSSh.
..hwwhSSSSSSSSS.
..hhwSSSSKSSSKS.
...hhSSSSKSSSKS.
...hhsSSpSSSSpS.
....hsSSSSSSSs..
......sSSSSs....
"""
HEAD_ROUND = """
....WWWWWWWW....
..WWWWWWWWWWWW..
.WWWWWWWWWWWWWw.
WWWWWWWWWWWWWwww
WWWWWWWWWWWWwwww
WWwWWWwWWWwSwwww
WwwWwhSSShSSShww
.hwwhSSSSSSSSSh.
.hhwSSSSKSSSKSh.
..hhSSSSKSSSKS..
..hhsSSpSSSSpS..
...hsSSSSSSSs...
.....sSSSSs.....
"""
HAIR_BACK = """
.wwwwwwwwwwww.
wwwwwwhwwwwwww
wwwwwhhwwwwwww
.wwwwhhwwwwww.
.hwwwhhwwwwwh.
.hhwwhhwwwwhh.
..hhhhhhhhhh..
"""
BODY = """
.LLBBBBBb.
LLBBBBBBbb
LBBBBBBBbb
NNNNGgNNNn
LBBBBBBBbb
.BBBBBBBb.
"""
ROBE = """
.LLBBBBBb.
LLBBBBBBbb
LBBBBBBBbb
NNNNGgNNNn
LBBBBBBBbb
LBBBBBBBbb
LLBBBBBBbbb
LLBBBBBBbbbb
.bbbbbbbbbb.
"""
LEGS = {
    "stand": ".Bb..Bb.\n.Bb..Bb.\n.NNN.NNN\n.nnn.nnn",
    "near_fwd": "...bbBB...\n..bb...BB.\n.nnn...NNN\n.nn....nnn",
    "far_fwd": "...BBbb...\n..BB...bb.\n.NNN...nnn\n.nn....nnn",
    "near_support": "..bbBB..\n..bbBB..\n.nnnBB..\n.nn.NNN.\n....nnn.",
    "far_support": "..bbBB..\n..bbBB..\n..bbNNN.\n..bbnnn.\n..nnn...",
}
SHIELD = """
..mmmmm..
.mOOOOOd.
mOOOOOOod
mOOOGOOod
mOOGGgOod
mOOOgOOod
mOOOOOood
.doooood.
..ddddd..
"""
HAT_WITCH = """
......V.........
.....VVv........
....VVVv........
....VVVvv.......
...VVVVvv.......
...VVVGGvv......
..VVVVVVvvv.....
VVVVVVVVVvvvvvvv
"""
HELMET = """
......MMMM......
....MMMMMMMm....
...MMMMMMMmmm...
..MMMMMMMmmmdd..
..MMMMMMmmmmdd..
"""
CROWN = """
.G..G..G.
.GRGGGRG.
.GGGGGGg.
"""
HALO = "..YYYY..\n.YYYYYY.\n..YYYY.."
# held things. Weapons are drawn without hands or sleeves: the character template adds a 2x2 fist over the
# cells marked '+' (the grip), so the same grid works in every pose and as a loose item icon.
SWORD = ".M..\n.Mm.\n.Mm.\n.Mm.\n.Mm.\n.Mm.\n.Mm.\n.Md.\nGGgg\n.++.\n.++.\n.gg."
DAGGER = ".M..\n.Mm.\n.Md.\nGGgg\n.++.\n.++.\n.gg."
AXE = "..MMM..\n.MMMMm.\n.MMmOod\n..mmOo.\n....Oo.\n....Oo.\n....Oo.\n....++.\n....++.\n....Oo.\n....oo."
SPEAR = "..M.\n.MMm\n.Mm.\n.Od.\n.Oo.\n.Oo.\n.Oo.\n.Oo.\n.Oo.\n.++.\n.++.\n.Oo.\n.Oo.\n.oo."
WAND = ".Y..\nYRY.\n.Y..\n.Oo.\n.Oo.\n.++.\n.++.\n.oo."
HAMMER = "mMMMMd\nmMMMMd\nmmmmdd\n..Oo..\n..Oo..\n..Oo..\n..++..\n..++..\n..Oo..\n..oo.."
STAFF = "..GYg\n.GCCGg\n.GCcGg\n..Ggg\n...Oo\n...Oo\n...Oo\n...Oo\n...Oo\n...Oo\n...++\n...++\n...Oo\n...Oo\n...Oo\n...Oo\n...oo"
BOW = "..O.\n.OoW\nOo.W\nOo.W\nOo.W\n++.W\n++.W\nOo.W\nOo.W\nOo.W\n.OoW\n..O."
BOOK = "RRRRr\nRMMRr\nRMMRr\nRRRRr\nrrrrr"
LUTE = ".++o\n.++o\n.Oo.\nOOOo\nOGOo\nOOoo\n.ooo"
BAG = "..++..\n..++..\n.NNNn.\nNNNNNn\nNNnNNn\nnnnnnn"
LANTERN_HELD = ".++.\n.++.\n.mm.\nmYYd\nmYYd\n.dd."

# ---------------------------------------------------------------- monsters, items and props (hand grids)
SLIME = """
.....EEEEEE.....
...EEEEEEEEEE...
..EMMEEEEEEEEe..
.EMMEEEEEEEEEee.
.EMEEEEEEEEEEee.
EEEEEEKEEEKEEeee
EEEEEEKEEEKEEeee
EEEEEpEEEEEpEeee
eEEEEEEEEEEEEeee
.eEEEEEEEEEEeee.
..qeeeeeeeeeeq..
"""
SLIME_SQUASH = """
......EEEEEE......
...EEEEEEEEEEEE...
.EEMMEEEEEEEEEEee.
EEMEEEEEEEEEEEEeee
EEEEEEEKEEEKEEEeee
EEEEEEEKEEEKEEEeee
EEEEEEpEEEEEpEEeee
.eEEEEEEEEEEEEeee.
..qeeeeeeeeeeeeq..
"""
BAT_BODY = ".V......v.\n.VV....Vv.\n.VVVVVVVv.\nVVVVVVVVvv\nVVRVVVRVvv\nVVRVVVRVvv\nVVVMVMVvvv\n.VVMvMvvv.\n..vv..vv.."
BAT_WING_L = ".....VVVV\n..VVVVvvV\nVVVvvvvvv\nVvvvvvvvv\nv.vv.vvvv\n...v...vv"
BAT_WING_R = "VVVV.....\nVvvVVVV..\nvvvvvvVVV\nvvvvvvvvV\nvvvv.vv.v\nvv...v..."
BAT_UP_L = "VV......\n.VVV....\nvvVVV...\n.vvvVVV.\nvvvvvvVV\n.vvvvvvV\n..vvvvvV\n....vvvV"
BAT_UP_R = "......VV\n....VVV.\n...VVVvv\n.VVVvvv.\nVVvvvvvv\nVvvvvvv.\nVvvvvv..\nVvvv...."
GHOST = """
.....WWWWWW.....
...WWWWWWWWWW...
..WWWWWWWWWWWw..
.WWWWWWWWWWWWww.
.WWWKKWWWWKKWww.
WWWWKKWWWWKKWwww
WWWWWWWWWWWWwwww
WWWWWWWKKWWWwwww
WWWWWWWWWWWWwwww
WWWWWWWWWWWwwwww
.WWWWWWWWWWwwww.
.WWwWWwwWWwwwww.
.Ww.Ww.ww.ww.ww.
"""
MUSHROOM = """
.....RRRRRR.....
...RRRMMRRRRRR..
..RRRMMRRRRMMRr.
.RRRRRRRRRRMMRrr
.RRMMRRRRRRRRRrr
RRRMMRRRRRRRRrrr
RRRRRRRRRMMRRrrr
rrrrrrrrrrrrrrrr
....SSSSSSSs....
....SSKSSKSs....
....SSKSSKSs....
....SSSSSSSs....
....SSSSSSSs....
....sssssssss...
"""
SKELETON_HEAD = """
...MMMMMMMM...
..MMMMMMMMMm..
.MMMMMMMMMMmm.
.MMMMMMMMMMmm.
.MMKKMMMMKKmm.
.MMKKMMMMKKmm.
.MMMMMMMMMMmm.
..MMMKMMKMmm..
..mmmmmmmmmm..
...MdMdMdMd...
"""
SKELETON_BODY = ".MMMMMMm.\nMdMdMdMdm\n.MMMMMMm.\nMdMdMdMdm\n.mmmmmmm."
SKELETON_LEGS = "Mm...Mm\nMm...Mm\nMm...Mm\nmmm.mmm"
EYE = """
......KKKKK......
...KKKMMMMMKKK...
.KKMMMMMMMMMMMKK.
KMMMMMMRRRMMMMMMK
KMMMMMRRKRRMMMMMK
KMMMMMRKKKRMMMMMK
KMMMMMRRKRRMMMMMK
KMMMMMMRRRMMMMMMK
.KKMMMMMMMMMMMKK.
...KKKmmmmmKKK...
......KKKKK......
"""
SPIDER = """
..v....VVVV....v..
...v..VVVVVv..v...
....vVVRVVRVvv....
.vvvvVVVVVVVvvvvv.
v....VVVVVVVvv...v
.....vVVVVVvv.....
..vvvv.vvvvv.vvvv.
.v....v.....v....v
"""
POTION = """
....NNNn....
....NNnn....
...mMMMMd...
....MRRd....
....MRRd....
..mMRRRRmd..
.mMRRRRRRrd.
mRMRRRRRRrrd
mRMRRRRRRrrd
mRRRRRRRRrrd
mRRRRRRRrrrd
.mRRRRRRrrd.
..drrrrrrd..
...dddddd...
"""
GEM = """
...CCCC...
..CMCCCCc.
.CMCCCCCcc
CMCCCCCCcc
CCCCCCCCcc
.CCCCCCcc.
..CCCCcc..
...CCcc...
....cc....
"""
RING = "..GGGG..\n.GYGGGg.\n.GGRRGg.\nGGRRRRGg\nGgRRRRgg\n.ggRRgg.\n.gGggGg.\n..gggg.."
APPLE = "....Oo..\n...Oo...\n.RRRRRR.\nRYRRRRRr\nRYRRRRRr\nRRRRRRrr\n.RRRRrr.\n..rrrr.."
BREAD = "..OOOOOO..\n.OYOOOOOo.\nOOOOYOOOoo\nOOOOOOOooo\n.oooooooo."
MEAT = "RRRRRr....\nRRRRRRr...\nrRRRRRRMmm\n.rRRRRrrMm\n..rrrr..mm"
CHEESE = "......YYYY\n...YYYYYYG\nYYYYYYYGGG\nYYGYYYYYGG\nYGYYYYGYYG\nGGGGGGGGGG"
FISH = "....CCC..C\n..CCCCCCCC\nCCKCCCCCCc\n.CCCCCCCCC\n..ccccc..c"
EGG = "..WWW..\n.WWWWw.\nWWWWWww\nWWWWwww\nWWWwwww\n.Wwwww.\n..www.."
BOMB = "....Oo.Y\n....Oo..\n..DDDD..\n.DDMDDD.\nDDMDDDDD\nDDDDDDDD\nDDDDDDDD\n.DDDDDD.\n..DDDD.."
BOOK_ITEM = "LLLLLLLLb\nLMMMMMMLb\nLMhhhMMLb\nLMMMMMMLb\nLMhhhhMLb\nLMMMMMMLb\nLLLLLLLLb\nbbbbbbbbb"
MAP = "SSSSSSSSSSSs\nSSqqSSSSSSSs\nSSqqqSSRSSSs\nSSSqSSSSSSSs\nSSSSSCCSSSSs\nSSSSCCCCSSSs\nSSSSSCCSSSSs\nssssssssssss"
COIN_BAG = "...GGg...\n..NNNNn..\n.NNNNNNn.\nNNNNNNNNn\nNNNGGGNNn\nNNNNNNNNn\n.NNNNNNn.\n..nnnnn.."
FEATHER = "......W\n.....WW\n....WWw\n...WWWw\n..WWWw.\n.WWWw..\nWWWw...\nOo....."
BONE = "MM....MM\nMMMMMMMM\nMM....MM"
SHARD = "..C..\n.CCc.\n.CCc.\nCCCcc\nCCCcc\n.Ccc.\n..c.."
HEART = ".RR.RR.\nRYRRRRr\nRRRRRRr\n.RRRRr.\n..RRr..\n...r..."
STAR = "...Y...\n..YYY..\nYYYGYYY\n.YGGGY.\n.YYYYY.\nYY...YY"
KEY_ITEM = ".GGGG.............\nGYYGGg............\nGY..Gg............\nGY..GGGGGGGGGGGGGg\nGg..Gggggggggggggg\n.gggg.......gg.gg.\n............gg.g.."
ARROW = "..M\n.MMm\nOOOo\n.Oo.\n.Oo.\n.Oo.\n.Oo.\nWWw.\nWw.."
BOOTS = "NNNn..\nNNNn..\nNNNn..\nNNNNNn\nnnnnnn"
CHESTPLATE = ".MMMMMMMm.\nMMMMMMMMmm\nMMMMMMMMmm\n.MMMMMMmm.\n.MMMGMMmm.\n.mmmmmmmm."
HELMET_ITEM = "...MMMM...\n.MMMMMMMm.\nMMMMMMMMmm\nMMMMMMMmmm\nMMMMMMmmmd\nMM.mmmd.dd"
BARREL = """
.OOOOOOOOo.
mmmmmmmmmmm
OOOOOOOOOoo
OOOOOOOOOoo
mmmmmmmmmmm
OOOOOOOOOoo
OOOOOOOOOoo
OOOOOOOOOoo
mmmmmmmmmmm
OOOOOOOOOoo
.ooooooooo.
"""
CRATE = "OOOOOOOOOOOo\nOooooooooOoo\nOoOOOOOOoOoo\nOoOOOOOOoOoo\nOoOOOOOOoOoo\nOoOOOOOOoOoo\nOooooooooOoo\nOOOOOOOOOOOo\noooooooooooo"
SIGN = "OOOOOOOOOOOOOo\nOhhhhhhhhhhhOo\nOOOOOOOOOOOOOo\nOhhhhhhhhOOOOo\nOOOOOOOOOOOOOo\nooooooooooooo.\n......Oo......\n......Oo......\n......Oo......\n......Oo......\n......oo......"
TOMB = "..mmmmm..\n.mMMMMMd.\nmMMMMMMMd\nmMMKMMMMd\nmMKKKMMMd\nmMMKMMMMd\nmMMKMMMMd\nmMMMMMMMd\nmMMMMMMMd\nddddddddd"
FIRE_LOGS = "oOOOOOOOOOOo\nnOOOOOOOOOon\nnnnnnnnnnnnn"
FIRE_0 = "....R....\n...RR....\n...RAR...\n..RAYAR..\n..RAYYAR.\n.RAYYYAR.\n.RAAYAAr.\n..RAAAr..\n...RRr..."
FIRE_1 = ".....R...\n....RR...\n...RAR...\n..RAYAR..\n.RAYYYAR.\n.RAYYYAR.\n.RAAYAAr.\n..RAAAr..\n...RRr..."
BUSH = "....EEEE....\n..EEEEEEEE..\n.EEEEEEEEEe.\nEEEEEEEEEEee\nEEEEEEEEEeee\n.EEEEEEEeee.\n..eeeeeeee.."
TREE = """
......EEEE......
....EEEEEEEE....
...EEEEEEEEEe...
..EEEEEEEEEEee..
.EEEEEEEEEEEeee.
.EEEEEEEEEEeeee.
EEEEEEEEEEEeeeee
.EEEEEEEEEeeeee.
..eEEEEEEeeeee..
...eeeeeeeeee...
......OOoo......
......OOoo......
......OOoo......
......OOoo......
.....oOOooo.....
"""
PINE = """
.......E.......
......EEE......
.....EEEEe.....
....EEEEEee....
...EEEEEEeee...
......EEe......
....EEEEEee....
...EEEEEEEee...
..EEEEEEEEeee..
.....EEEee.....
...EEEEEEeee...
..EEEEEEEeeee..
.EEEEEEEEeeeee.
......OOo......
......OOo......
"""
ROCK = "...mmmm...\n..mMMMmd..\n.mMMMMmdd.\nmMMMMmmddd\nmMMMmmmddd\n.mmmmmddd.\n..dddddd.."
CRYSTAL = "....C.......\n...CCc..C...\n...CCc.CCc..\n..CCCc.CCc..\n..CCCcCCCcc.\n.CCCCcCCCcc.\n.CCCccCCccc.\nmCCCccCCcccd\nmmmmmmmmmmdd"
CAULDRON = "..DD......DD..\n.DDDDDDDDDDDD.\n..DEEEEEEEED..\n.DDDDDDDDDDDD.\nDDDDDDDDDDDDDD\nDDDDDDDDDDDDDD\nDDDDDDDDDDDDDD\n.DDDDDDDDDDDD.\n..DDDDDDDDDD..\n..DD......DD.."
ANVIL = "mMMMMMMMMMMd\n.mMMMMMMMMd.\n....mMMd....\n....mMMd....\n..mMMMMMMd..\n..dddddddd.."
FENCE = "Oo....Oo....Oo\nOo....Oo....Oo\nOOOOOOOOOOOOOo\nOo....Oo....Oo\nOOOOOOOOOOOOOo\nOo....Oo....Oo\noo....oo....oo"
WELL = """
.......OOOOOOo.....
.....OOOOOOOOOOo...
...OOOOOOOOOOOOOOo.
...Oo..........Oo..
...Oo..........Oo..
...Oo..mmMMmd..Oo..
...Oo.mMMMMMMd.Oo..
...OommMMMMMMmmOo..
..mmMMMMMMMMMMMmd..
.mmMMMKKKKKKKKMMmd.
mmMMMKKKKKKKKKKMmdd
mmMMMMMMMMMMMMMMmdd
mmmdMMMMdMMMMMdmddd
mmmmMMMMMMMMMMmmddd
.ddddddddddddddddd.
"""
TABLE = "OOOOOOOOOOOOOOOo\nooooooooooooooo.\n.Oo..........Oo.\n.Oo..........Oo.\n.Oo..........Oo.\n.oo..........oo."
BED = "OOOOo.........\nORRRRRRRRRRRo.\nOMMMRRRRRRRRo.\nOMMMRRRRRRRRo.\nORRRRRRRRRRRo.\nOrrrrrrrrrrro.\nOo.........Oo."
LANTERN = "....mm....\n...mMMd...\n..mMMMMd..\n..mYYYYd..\n..mYYYYd..\n..mYYYYd..\n..mMMMMd..\n...mddd...\n....Oo....\n....Oo...."
DOOR = """
...OOOOOOOO...
..OOOOOOOOOo..
.OOOoOOOOoOOo.
.OOOoOOOOoOOo.
.OOOoOOOOoOOo.
.OoooooooooOo.
.OOOoOOOOoOOo.
.OOOoOOOOoOOo.
.OOOoOOOGoOOo.
.OOOoOOOGoOOo.
.OoooooooooOo.
.OOOoOOOOoOOo.
.OOOoOOOOoOOo.
.OOOoOOOOoOOo.
.oooooooooooo.
"""
PILLAR = "mMMMMMMd\n.mMMMMd.\n.mMMMMd.\n.mMMMMd.\n.mMMMMd.\n.mMMMMd.\n.mMMMMd.\n.mMMMMd.\n.mMMMMd.\n.mMMMMd.\nmMMMMMMd\nmmmmmmdd"
STATUE = """
......M.........
.....MMm........
.....MMm........
....MMMMm.......
....MMMMm.......
.....MMm..MMm...
....MMMMMMMMmm..
...MMKMMKMMMmmd.
..MMmMMMMMMmMmd.
..MMm.MmmMm.Mmd.
......MMMmd.....
......MMMmd.....
.....MMm.Mmd....
.....MMm.Mmd....
...mMMMMMMMMMmd.
..mMMMMMMMMMMmmd
..mmmmmmmmmmmddd
"""
MAILBOX = "..LLLLLLLL..\n.LLLLLLLLLb.\nLLLLLLLLLLbb\nLLMMLLLLLLbb\nLLLLLLLLLLbb\n.bbbbbbbbbb.\n.....Oo.....\n.....Oo.....\n.....Oo.....\n.....Oo....."
CAMPTENT = ".......NNn.......\n......NNNNn......\n.....NNNNNNn.....\n....NNNNNNNNn....\n...NNNNNNNNNNn...\n..NNNNnnnnNNNNn..\n.NNNNnKKKKnNNNNn.\nNNNNnKKKKKKnNNNNn\nnnnnnKKKKKKnnnnnn"
STAIRS = "............MMMMd\n.........MMMmmmmd\n......MMMmmmmmmmd\n...MMMmmmmmmmmmmd\nMMMmmmmmmmmmmmmmd\ndddddddddddddddd."
CART = ".OOOOOOOOOOo.\nOOOOOOOOOOOOo\nOoOOOOOOOOoOo\nooooooooooooo\n.DDD....DDD..\nDDMDD..DDMDD.\n.DDD....DDD.."
FLOWERPOT = ".P.PP.P.\nPPPEEPPP\n.PEEEEP.\n..EEEE..\n.OOOOOOo\n.OOOOOOo\n..OOOOo.\n..oooooo"
SCARECROW = "....Oo....\n...NNNNn..\n..NNNNNNn.\n..NSKSKSn.\n...SSSSs..\nOOOOLLLOOOo\n...LLLLb..\n...LLLLb..\n...bbbbb..\n....Oo....\n....Oo....\n....Oo....\n....Oo...."

# ---------------------------------------------------------------- recoloring
HAIR = {  # hair tone triples: light, mid, shadow
    "white": "Wwh", "blonde": "YGg", "brown": "OoN", "black": "dDK", "red": "RAa", "pink": "PPx",
    "blue": "LBb", "green": "Eeq", "purple": "VVv", "orange": "AAa", "cyan": "CCc", "grey": "mmd",
}
CLOTH = {
    "blue": "LBb", "red": "RRr", "green": "Eeq", "purple": "VVv", "white": "WwM", "black": "dDD",
    "brown": "OoN", "pink": "PPx", "gold": "YGg", "cyan": "CCc", "orange": "AAa", "grey": "Mmd", "iron": "Mmd",
}
SKIN = {"light": "Ssp", "tan": "sNp", "green": "Eeq", "blue": "CLB", "grey": "mdD", "pale": "WwP"}


def recolor(text: str, *maps: tuple[str, str]) -> list[str]:
    table = {}
    for src, dst in maps:
        table.update(dict(zip(src, dst)))
    return ["".join(table.get(ch, ch) for ch in row) for row in text.strip("\n").split("\n")]


def rows_of(text: str) -> list[str]:
    return text.strip("\n").split("\n")


def layer(name: str, rows: list[str], x: int, y: int, outline: bool = True) -> Layer:
    lay = Layer(name, outline=outline)
    lay.rows(x, y, "\n".join(rows))
    return lay


def meta(aid: str, title: str, anchor=(16, 29), margin=1) -> dict:
    m = {"id": aid, "title": title, "size": "32 32", "anchor": f"{anchor[0]} {anchor[1]}", "palette": PALETTE}
    if margin != 1:
        m["margin"] = str(margin)
    return m


# ---------------------------------------------------------------- templates
def rot90(rows):
    """Clockwise quarter turn: a vertical weapon with its grip at the bottom ends up pointing right."""
    h = len(rows)
    return ["".join(rows[h - 1 - i][j] for i in range(h)) for j in range(len(rows[0]))]


def lean(rows, direction=1):
    """Shears a vertical grid into a 2:1 diagonal. direction 1 leans the top to the right, -1 to the left."""
    h = len(rows)
    shift = [(h - 1 - y) // 2 for y in range(h)]
    width = len(rows[0]) + max(shift)
    out = []
    for y, row in enumerate(rows):
        s = shift[y] if direction > 0 else max(shift) - shift[y]
        out.append("." * s + row + "." * (width - s - len(row)))
    return out


def tilt_down(rows):
    """A rot90 (pointing right) grid tipped 1:2 downward: every second column toward the tip drops one row."""
    w, h = len(rows[0]), len(rows)
    drop = [x // 2 for x in range(w)]
    out = [["."] * w for _ in range(h + max(drop))]
    for y, row in enumerate(rows):
        for x, key in enumerate(row):
            if key != ".":
                out[y + drop[x]][x] = key
    return ["".join(r) for r in out]


# Hands: a 2x2 fist that always touches the body, so no pose needs a stretched arm.
# The body spans x 11..20, y 20..25; its outline is x 10 and x 21.
BACK_HAND, RAISED_HAND, FRONT_HAND, GUARD_HAND = (8, 22), (23, 20), (22, 22), (23, 22)
# pose -> (transform of the upright grid, hand top-left, side). "back": weapon and fist behind the body;
# "front": both in front of everything; "mid": weapon behind the head so it never covers the face, fist in front.
POSES = {
    "rest": (None, BACK_HAND, "back"),                           # upright in the back hand at the hip
    "raise": (lambda r: lean(r, 1), RAISED_HAND, "mid"),         # front fist at the chin, tip up past the head
    "thrust": (rot90, FRONT_HAND, "front"),                      # level in the front hand, pointing ahead
    "guard": (None, GUARD_HAND, "front"),                        # upright in the front hand beside the face
    "low": (lambda r: tilt_down(rot90(r)), FRONT_HAND, "front"),  # front hand, tip lowered toward the ground
}
POSES["shoulder"] = POSES["raise"]
POSES["overhead"] = POSES["raise"]
FORCED_POSE = {"bow": "guard", "lute": "guard", "bag": "rest", "lantern": "rest"}  # things held only one way
FIST = "SS\nSs"


def grip_weapon(grid: str, transform, maps, handle: str = "n"):
    """Applies the pose transform and returns (rows, top-left of the 2x2 grip cells) in the result."""
    rows = recolor(grid, *maps)
    if transform:
        rows = transform(rows)
    cells = [(x, y) for y, r in enumerate(rows) for x, k in enumerate(r) if k == "+"]
    rows = [r.replace("+", handle) for r in rows]
    if not cells:
        return rows, (0, len(rows) - 2)
    return rows, (min(x for x, _ in cells), min(y for _, y in cells))


def placed(rows, grip, hand, margin=3):
    """Top-left for the weapon and the fist so the grip sits under the fist; shifts both together
    when the weapon would cross the frame border (the lifted walk frames need 1 more row at the top)."""
    x, y = hand[0] - grip[0], hand[1] - grip[1]
    w, h = len(rows[0]), len(rows)
    dx = max(0, margin - x) - max(0, x + w - (32 - margin))
    dy = max(0, margin + 1 - y) - max(0, y + h - (32 - margin))
    return (x + dx, y + dy), (hand[0] + dx, hand[1] + dy)


BEARD = """.WWWWWW.
WWWWWWWw
.WWWWWh.
..hhhh.."""


def character(aid, title, hair="white", skin="light", cloth="blue", head="spiky", back=None, front=None,
              robe=False, hat=None, trim="Nn", long_hair=False, pose="rest", beard=False, front_pos=None):
    hm = ("Wwh", HAIR[hair])
    sm = ("Ssp", SKIN[skin])
    cm = ("LBb", CLOTH[cloth])
    tm = ("Nn", trim)
    hg = HEAD_ROUND if head == "round" else HEAD
    if head == "hood":
        hm = ("Wwh", CLOTH[cloth])
    layers, base, w0, w1, w2, w3 = [], [], [], [], [], []

    def add(name, rows, x, y, offsets, outline=True):
        layers.append(layer(name, rows, x, y, outline))
        for frame, (dx, dy) in zip((base, w0, w1, w2, w3), offsets):
            frame.append((name, dx, dy))

    up = [(0, 0), (0, 0), (0, -1), (0, 0), (0, -1)]
    legs = {k: recolor(v, cm, tm) for k, v in LEGS.items()}
    for name, (x, y) in (("legs_stand", (12, 26)), ("legs_near_fwd", (11, 26)), ("legs_near_support", (12, 25)),
                         ("legs_far_fwd", (11, 26)), ("legs_far_support", (12, 25))):
        layers.append(layer(name, legs[name[5:]], x, y))
    base.append(("legs_stand", 0, 0)); w0.append(("legs_near_fwd", 0, 0)); w1.append(("legs_near_support", 0, 0))
    w2.append(("legs_far_fwd", 0, 0)); w3.append(("legs_far_support", 0, 0))
    if long_hair:
        add("hair_back", recolor(HAIR_BACK, hm), 9, 17, up)
    sway = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, -1)]
    held = None
    if back:
        transform, hand, side = POSES[FORCED_POSE.get(back, pose)]
        rows, grip = grip_weapon(WEAPONS[back], transform, (cm, sm), HANDLE.get(back, "n"))
        pos, hand = placed(rows, grip, hand)
        held = (rows, pos, hand, side)
        if side == "back":
            add("back_item", rows, pos[0], pos[1], sway)
            if back != "bone_arm":
                add("back_hand", recolor(FIST, sm), hand[0], hand[1], sway)
    add("body", recolor(ROBE if robe else BODY, cm, tm), 11, 20, up)
    if front:
        grid, pos = FRONT[front]
        pos = front_pos or pos
        add("front_item", [r.replace("+", "N") for r in recolor(grid, cm)], pos[0], pos[1], up)
    if held and held[3] == "mid":
        add("held_item", held[0], held[1][0], held[1][1], up)
    add("head", recolor(hg, hm, sm), 8, 6 if head != "round" else 8, up)
    if beard:
        add("beard", recolor(BEARD, hm), 13, 19, up, outline=False)
    if held and held[3] in ("front", "mid"):
        rows, pos, hand, side = held
        if side == "front":
            add("held_item", rows, pos[0], pos[1], up)
        if back != "bone_arm":
            add("front_hand", recolor(FIST, sm), hand[0], hand[1], up)
    if hat:
        grid, pos = HATS[hat]
        add("hat", recolor(grid, cm), pos[0], pos[1], up)
    frames = {"base": base, "walk_0": w0, "walk_1": w1, "walk_2": w2, "walk_3": w3}
    anims = {"walk": [("walk_0", 150), ("walk_1", 150), ("walk_2", 150), ("walk_3", 150)]}
    return Recipe(meta=meta(aid, title), layers=layers, frames=frames, anims=anims)


WEAPONS = {"sword": SWORD, "dagger": DAGGER, "axe": AXE, "spear": SPEAR, "wand": WAND, "hammer": HAMMER,
           "staff": STAFF, "bow": BOW, "lute": LUTE, "bag": BAG, "lantern": LANTERN_HELD,
           "bone_arm": "SS\nSS\nBB\nBB\nBB"}  # a zombie's outstretched arm: no fist, the grid is the arm
HANDLE = {"axe": "O", "spear": "O", "wand": "O", "hammer": "O", "staff": "O", "bow": "O", "lute": "O", "bag": "N",
          "lantern": "m", "bone_arm": "S"}
FRONT = {"shield": (SHIELD, (18, 19)), "book": (BOOK, (19, 21)), "bag": (BAG, (19, 22))}
HATS = {"witch": (HAT_WITCH, (6, 3)), "helmet": (HELMET, (8, 4)), "crown": (CROWN, (11, 3)), "halo": (HALO, (12, 3)),
        "horns": (""".D......D.
DD......DD
DDD....DDD""", (11, 4))}


def still(aid, title, parts, anchor=(16, 28), margin=1):
    """parts: list of (name, rows, x, y[, outline]) drawn back to front."""
    layers = [layer(p[0], p[1], p[2], p[3], p[4] if len(p) > 4 else True) for p in parts]
    return Recipe(meta=meta(aid, title, anchor, margin), layers=layers,
                  frames={"base": [(p[0], 0, 0) for p in parts]})


def centered(rows: list[str], y_bottom: int = 28) -> tuple[int, int]:
    w, h = len(rows[0]), len(rows)
    return (32 - w) // 2, y_bottom - h + 1


def item(aid, title, grid, *maps, bottom=24):
    rows = [r.replace("+", "n") for r in recolor(grid, *maps)]  # a weapon's grip shows as a leather wrap
    x, y = centered(rows, bottom)
    return still(aid, title, [("item", rows, x, y)], anchor=(16, bottom))


def slime(aid, title, tones="Eeq", mark=None):
    cm = ("Eeq", tones)
    mid, squash = recolor(SLIME, cm), recolor(SLIME_SQUASH, cm)
    parts = [("slime_mid", mid, 8, 19)]
    layers = [layer("slime_mid", mid, 8, 19), layer("slime_squash", squash, 7, 21)]
    base, sq = [("slime_mid", 0, 0)], [("slime_squash", 0, 0)]
    if mark:
        rows, (x, y) = mark
        layers.append(layer("mark", rows, x, y))
        base.append(("mark", 0, 0)); sq.append(("mark", 0, 2))
    return Recipe(meta=meta(aid, title), layers=layers, frames={"base": base, "squash": sq},
                  anims={"idle": [("base", 260), ("squash", 160)]})


def bat(aid, title, tones="Vv", eye="R"):
    cm = ("Vv", tones)
    em = ("R", eye)
    layers = [layer("body", recolor(BAT_BODY, cm, em), 11, 14), layer("wl", recolor(BAT_WING_L, cm), 2, 16),
              layer("wr", recolor(BAT_WING_R, cm), 21, 16), layer("ul", recolor(BAT_UP_L, cm), 3, 10),
              layer("ur", recolor(BAT_UP_R, cm), 21, 10)]
    return Recipe(meta=meta(aid, title, (16, 22)), layers=layers,
                  frames={"base": [("wl", 0, 0), ("wr", 0, 0), ("body", 0, 0)],
                          "up": [("ul", 0, 0), ("ur", 0, 0), ("body", 0, 0)]},
                  anims={"fly": [("base", 110), ("up", 110)]})


def skeleton(aid, title, tones="Mmd", held=None):
    cm = ("Mmd", tones)
    layers = [layer("legs", recolor(SKELETON_LEGS, cm), 12, 26), layer("body", recolor(SKELETON_BODY, cm), 11, 21),
              layer("head", recolor(SKELETON_HEAD, cm), 9, 11)]
    base = [("legs", 0, 0), ("body", 0, 0), ("head", 0, 0)]
    if held:
        transform, hand, _ = POSES[FORCED_POSE.get(held, "rest")]
        rows, grip = grip_weapon(WEAPONS[held], transform, (("S", "M"), ("B", "m"), ("b", "d")), HANDLE.get(held, "n"))
        pos, hand = placed(rows, grip, (hand[0], hand[1] - 1))
        side = 1 if hand[0] < 16 else len(layers)
        layers[side:side] = [layer("item", rows, *pos), layer("fist", ["MM", "Mm"], *hand)]
        base[side:side] = [("item", 0, 0), ("fist", 0, 0)]
    return Recipe(meta=meta(aid, title), layers=layers, frames={"base": base})


def campfire(aid, title):
    layers = [layer("logs", rows_of(FIRE_LOGS), 10, 26), layer("f0", rows_of(FIRE_0), 11, 16), layer("f1", rows_of(FIRE_1), 11, 16)]
    return Recipe(meta=meta(aid, title, (16, 28)), layers=layers,
                  frames={"base": [("f0", 0, 0), ("logs", 0, 0)], "flick": [("f1", 0, 0), ("logs", 0, 0)]},
                  anims={"burn": [("base", 130), ("flick", 130)]})


def tile(aid, title, fn, speckle=None, seed=1):
    rng = random.Random(seed)
    lay = Layer("tile", outline=False)
    lay.fill(((x, y) for x in range(32) for y in range(32)), fn)
    if speckle:
        key, count = speckle
        for _ in range(count):
            lay.set((rng.randrange(32), rng.randrange(32)), key)
    return Recipe(meta=meta(aid, title, (16, 31), 0), layers=[lay], frames={"base": [("tile", 0, 0)]})


def bricks(light, mid, dark, mortar, bw=16, bh=8):
    def fn(x, y):
        row = y // bh
        bx = (x + (bw // 2) * (row % 2)) % bw
        by = y % bh
        if by == bh - 1 or bx == bw - 1:
            return mortar
        if by == 0 or bx == 0:
            return light
        if by == bh - 2 or bx == bw - 2:
            return dark
        return mid
    return fn


def planks(light, mid, dark):
    def fn(x, y):
        by = y % 8
        if by == 7:
            return dark
        if by == 0:
            return light
        if (x + (y // 8) * 11) % 32 == 0:
            return dark
        return mid
    return fn


def waves(base, crest, trough):
    def fn(x, y):
        v = (x + (y // 4) * 5) % 16
        if y % 4 == 1 and v < 6:
            return crest
        if y % 4 == 3 and 8 <= v < 12:
            return trough
        return base
    return fn


def cobble(light, mid, dark, mortar):
    def fn(x, y):
        cx, cy = x % 8, y % 8
        if cx == 7 or cy == 7:
            return mortar
        if cx == 0 or cy == 0:
            return light
        if cx == 6 or cy == 6:
            return dark
        return mid
    return fn


def checker(a, b):
    return lambda x, y: a if ((x // 8) + (y // 8)) % 2 == 0 else b


# ---------------------------------------------------------------- the 100 specs: id -> (description, builder)
def M(rows, x, y):
    return (rows_of(rows), (x, y))


SPECS: dict[str, tuple[str, object]] = {}
CATEGORY: dict[str, str] = {}  # id -> gallery section, set by section() before each group
_section = ["misc"]


def section(name: str) -> None:
    _section[0] = name


def spec(aid, desc, fn):
    SPECS[aid] = (desc, fn)
    CATEGORY[aid] = _section[0]


# characters (30)
section("characters")
spec("mage_f", "여성 마법사. 긴 보라색 머리에 마녀 모자, 푸른 로브, 수정 지팡이를 들었다.",
     lambda: character("mage_f", "Female mage with crystal staff", hair="purple", cloth="blue", back="staff", robe=True, hat="witch", long_hair=True))
spec("witch", "초록 피부의 마녀. 검은 로브와 뾰족 모자, 손에는 마법 지팡이.",
     lambda: character("witch", "Witch with wand", hair="black", skin="green", cloth="black", back="wand", robe=True, hat="witch", long_hair=True))
spec("priestess", "여사제. 흰 로브에 금 장식, 치유서를 품에 안았다.",
     lambda: character("priestess", "Priestess with holy book", hair="blonde", cloth="white", front="book", robe=True, long_hair=True, trim="Gg"))
spec("knight", "성기사. 은빛 투구와 갑옷, 장검과 방패.",
     lambda: character("knight", "Knight in plate", hair="brown", cloth="iron", back="sword", front="shield", hat="helmet"))
spec("archer_f", "엘프 궁수. 초록 망토와 긴 활, 금발 머리.",
     lambda: character("archer_f", "Elf archer", hair="blonde", cloth="green", back="bow", long_hair=True))
spec("rogue", "도적. 검은 후드와 단검, 조용히 움직인다.",
     lambda: character("rogue", "Hooded rogue with dagger", hair="black", cloth="black", head="hood", back="dagger"))
spec("barbarian", "야만전사. 붉은 머리, 가죽 옷, 커다란 도끼.",
     lambda: character("barbarian", "Barbarian with great axe", hair="red", cloth="brown", back="axe"))
spec("bard", "음유시인. 분홍 머리, 보라 옷, 류트를 들고 노래한다.",
     lambda: character("bard", "Bard with lute", hair="pink", cloth="purple", back="lute", long_hair=True))
spec("merchant", "상인. 주황 옷에 커다란 짐 가방, 금화를 좋아한다.",
     lambda: character("merchant", "Merchant with travel bag", hair="brown", cloth="orange", front="bag"))
spec("blacksmith", "대장장이. 검은 머리, 갈색 앞치마, 망치.",
     lambda: character("blacksmith", "Blacksmith with hammer", hair="black", cloth="brown", back="hammer", trim="Dd"))
spec("king", "왕. 금관을 쓰고 붉은 로브를 입었다.",
     lambda: character("king", "King in red robe", hair="grey", cloth="red", robe=True, hat="crown", trim="Gg"))
spec("princess", "공주. 분홍 드레스와 작은 금관, 긴 금발.",
     lambda: character("princess", "Princess with tiara", hair="blonde", cloth="pink", robe=True, hat="crown", long_hair=True, trim="Gg"))
spec("healer_f", "여성 힐러. 초록 로브에 하얀 머리, 치유 지팡이.",
     lambda: character("healer_f", "Healer with staff", hair="white", cloth="green", back="staff", robe=True, long_hair=True))
spec("necromancer", "강령술사. 창백한 피부, 검은 후드 로브, 해골 지팡이.",
     lambda: character("necromancer", "Necromancer", hair="white", skin="pale", cloth="purple", head="hood", back="staff", robe=True))
spec("paladin_f", "여성 성기사. 흰 갑옷과 황금 장식, 검과 방패.",
     lambda: character("paladin_f", "Female paladin", hair="blonde", cloth="white", back="sword", front="shield", long_hair=True, trim="Gg"))
spec("spearman", "창병. 푸른 갑옷에 긴 창과 투구.",
     lambda: character("spearman", "Spearman", hair="brown", cloth="blue", back="spear", hat="helmet"))
spec("monk", "수도승. 주황 승복, 맨손 격투가.",
     lambda: character("monk", "Monk", hair="black", cloth="orange", head="round"))
spec("villager_m", "마을 청년. 갈색 머리에 초록 튜닉.",
     lambda: character("villager_m", "Villager (young man)", hair="brown", cloth="green", head="round"))
spec("villager_f", "마을 처녀. 붉은 긴 머리에 흰 원피스.",
     lambda: character("villager_f", "Villager (young woman)", hair="red", cloth="white", robe=True, long_hair=True, head="round"))
spec("elder", "마을 장로. 흰 수염 대신 흰 머리, 회색 로브, 지팡이.",
     lambda: character("elder", "Village elder", hair="white", cloth="grey", back="staff", robe=True, head="round"))
spec("child", "꼬마 모험가. 주황 머리, 나무 검 대신 단검.",
     lambda: character("child", "Child adventurer", hair="orange", cloth="cyan", back="dagger", head="round"))
spec("dark_knight", "암흑기사. 검은 갑옷과 붉은 눈빛의 검.",
     lambda: character("dark_knight", "Dark knight", hair="black", cloth="black", back="sword", front="shield", hat="helmet"))
spec("ice_mage", "얼음 마법사. 하늘색 머리와 로브, 서리 지팡이.",
     lambda: character("ice_mage", "Ice mage", hair="cyan", cloth="cyan", back="staff", robe=True, hat="witch"))
spec("fire_mage", "화염 마법사. 붉은 로브, 주황 머리, 불꽃 지팡이.",
     lambda: character("fire_mage", "Fire mage", hair="orange", cloth="red", back="staff", robe=True))
spec("ranger", "순찰자. 초록 후드에 활과 화살.",
     lambda: character("ranger", "Hooded ranger", hair="brown", cloth="green", head="hood", back="bow"))
spec("angel", "천사. 후광과 흰 로브, 금발.",
     lambda: character("angel", "Angel", hair="blonde", cloth="white", robe=True, hat="halo", long_hair=True, trim="Gg"))
spec("goblin", "고블린. 초록 피부, 갈색 누더기, 단검.",
     lambda: character("goblin", "Goblin with dagger", hair="black", skin="green", cloth="brown", back="dagger", head="round"))
spec("orc", "오크 전사. 초록 피부, 검은 머리, 큰 도끼.",
     lambda: character("orc", "Orc warrior", hair="black", skin="green", cloth="grey", back="axe"))
spec("lantern_keeper", "등불지기. 밤길을 밝히는 노인, 손에 등불.",
     lambda: character("lantern_keeper", "Lantern keeper", hair="grey", cloth="brown", back="lantern", head="round"))
spec("pirate", "해적. 붉은 두건, 검은 옷, 커틀러스.",
     lambda: character("pirate", "Pirate", hair="red", cloth="black", head="hood", back="sword"))

# monsters (14)
section("monsters")
CROSS = M(".M.\nMMM\n.M.", 15, 23)
spec("slime_healer", "슬라임 힐러. 하얀 십자 표식이 있는 분홍 슬라임, 아군을 회복한다.",
     lambda: slime("slime_healer", "Healer slime", "PPx", CROSS))
spec("slime_red", "불 슬라임. 뜨거운 붉은 슬라임.", lambda: slime("slime_red", "Fire slime", "RRr"))
spec("slime_blue", "물 슬라임. 차가운 푸른 슬라임.", lambda: slime("slime_blue", "Water slime", "CLB"))
spec("slime_king", "슬라임 왕. 작은 금관을 쓴 보라 슬라임.", lambda: slime("slime_king", "Slime king", "VVv", M(CROWN, 12, 16)))
spec("slime_gold", "황금 슬라임. 잡으면 금화를 떨군다.", lambda: slime("slime_gold", "Gold slime", "YGg"))
spec("bat_red", "화염 박쥐. 붉은 날개에 노란 눈.", lambda: bat("bat_red", "Fire bat", "Rr", "Y"))
spec("bat_ice", "서리 박쥐. 하늘색 날개.", lambda: bat("bat_ice", "Frost bat", "Cc", "W"))
spec("ghost", "유령. 반쯤 웃는 하얀 유령.", lambda: item("ghost", "Ghost", GHOST, bottom=27))
spec("mushroom_mon", "버섯 괴물. 붉은 갓에 흰 점, 작은 다리.", lambda: item("mushroom_mon", "Mushroom monster", MUSHROOM, bottom=28))
spec("skeleton", "해골 전사. 뼈만 남은 병사.", lambda: skeleton("skeleton", "Skeleton"))
spec("skeleton_sword", "해골 검사. 녹슨 검을 든 해골.", lambda: skeleton("skeleton_sword", "Skeleton swordsman", held="sword"))
spec("eyeball", "떠다니는 눈알. 붉은 홍채.", lambda: item("eyeball", "Floating eyeball", EYE, bottom=22))
spec("spider", "동굴 거미. 보라색 몸통에 붉은 눈.", lambda: item("spider", "Cave spider", SPIDER, bottom=28))
spec("spider_green", "독거미. 초록 몸통.", lambda: item("spider_green", "Poison spider", SPIDER, ("Vv", "Eq"), bottom=28))

# items (30)
section("items")
spec("potion_purple", "독 포션. 보라색 병.", lambda: item("potion_purple", "Poison potion", POTION, ("Rr", "Vv")))
spec("potion_gold", "엘릭서. 황금빛 만능 포션.", lambda: item("potion_gold", "Elixir", POTION, ("Rr", "YG")))
spec("potion_cyan", "속도 포션. 하늘색 병.", lambda: item("potion_cyan", "Speed potion", POTION, ("Rr", "Cc")))
spec("potion_orange", "힘 포션. 주황색 병.", lambda: item("potion_orange", "Strength potion", POTION, ("Rr", "Aa")))
spec("gem_blue", "사파이어. 푸른 보석.", lambda: item("gem_blue", "Sapphire", GEM, ("Cc", "LB")))
spec("gem_red", "루비. 붉은 보석.", lambda: item("gem_red", "Ruby", GEM, ("Cc", "Rr")))
spec("gem_green", "에메랄드. 초록 보석.", lambda: item("gem_green", "Emerald", GEM, ("Cc", "Ee")))
spec("gem_purple", "자수정. 보라 보석.", lambda: item("gem_purple", "Amethyst", GEM, ("Cc", "Vv")))
spec("diamond", "다이아몬드. 투명하게 빛나는 보석.", lambda: item("diamond", "Diamond", GEM, ("Cc", "Mm")))
spec("ring_ruby", "루비 반지.", lambda: item("ring_ruby", "Ruby ring", RING))
spec("ring_sapphire", "사파이어 반지.", lambda: item("ring_sapphire", "Sapphire ring", RING, ("R", "L")))
spec("apple", "사과. 체력을 조금 회복한다.", lambda: item("apple", "Apple", APPLE))
spec("bread", "빵. 여행자의 식량.", lambda: item("bread", "Bread", BREAD))
spec("meat", "고기. 뼈가 붙은 구운 고기.", lambda: item("meat", "Roast meat", MEAT))
spec("cheese", "치즈. 구멍 뚫린 노란 치즈.", lambda: item("cheese", "Cheese", CHEESE))
spec("fish", "물고기. 호수에서 낚은 것.", lambda: item("fish", "Fish", FISH))
spec("egg", "알. 무엇이 나올까.", lambda: item("egg", "Egg", EGG))
spec("bomb", "폭탄. 심지에 불이 붙었다.", lambda: item("bomb", "Bomb", BOMB))
spec("spellbook", "마법서. 푸른 표지의 책.", lambda: item("spellbook", "Spellbook", BOOK_ITEM))
spec("map_item", "보물 지도. 붉은 X가 표시되어 있다.", lambda: item("map_item", "Treasure map", MAP))
spec("coin_bag", "돈주머니. 금화가 가득.", lambda: item("coin_bag", "Coin bag", COIN_BAG))
spec("feather", "깃털. 가볍고 하얗다.", lambda: item("feather", "Feather", FEATHER))
spec("bone", "뼈. 해골이 남긴 것.", lambda: item("bone", "Bone", BONE))
spec("shard", "마나 결정 조각.", lambda: item("shard", "Mana shard", SHARD))
spec("heart", "하트. 생명력 회복.", lambda: item("heart", "Heart", HEART))
spec("star_item", "별. 무적 아이템.", lambda: item("star_item", "Star", STAR))
spec("key_silver", "은 열쇠. 작은 상자를 연다.", lambda: item("key_silver", "Silver key", KEY_ITEM, ("YGg", "MMd")))
spec("arrow", "화살. 궁수의 탄약.", lambda: item("arrow", "Arrow", ARROW))
spec("boots", "가죽 장화.", lambda: item("boots", "Leather boots", BOOTS))
spec("chestplate", "강철 흉갑.", lambda: item("chestplate", "Steel chestplate", CHESTPLATE))
spec("helmet_item", "강철 투구.", lambda: item("helmet_item", "Steel helmet", HELMET_ITEM))
spec("sword_item", "장검. 바닥에 놓인 아이템 아이콘.", lambda: item("sword_item", "Longsword (item)", SWORD, bottom=26))
spec("axe_item", "전투 도끼.", lambda: item("axe_item", "Battle axe (item)", AXE, bottom=26))
spec("staff_item", "수정 지팡이.", lambda: item("staff_item", "Crystal staff (item)", STAFF, bottom=28))
spec("bow_item", "장궁.", lambda: item("bow_item", "Longbow (item)", BOW, bottom=26))
spec("wand_item", "마법봉.", lambda: item("wand_item", "Wand (item)", WAND, bottom=24))
spec("hammer_item", "대장장이 망치.", lambda: item("hammer_item", "Hammer (item)", HAMMER, bottom=26))
spec("shield_item", "둥근 나무 방패.", lambda: item("shield_item", "Round shield (item)", SHIELD, bottom=24))

# props (22)
section("props")
spec("barrel", "나무 통. 술집과 창고에.", lambda: item("barrel", "Barrel", BARREL, bottom=28))
spec("crate", "나무 상자. 부수면 아이템이.", lambda: item("crate", "Crate", CRATE, bottom=28))
spec("signpost", "이정표. 두 줄 글씨.", lambda: item("signpost", "Signpost", SIGN, bottom=28))
spec("tombstone", "묘비. 십자가가 새겨졌다.", lambda: item("tombstone", "Tombstone", TOMB, bottom=28))
spec("campfire", "모닥불. 두 프레임으로 타오른다.", lambda: campfire("campfire", "Campfire"))
spec("bush", "덤불. 숨기 좋다.", lambda: item("bush", "Bush", BUSH, bottom=28))
spec("tree", "둥근 나무.", lambda: item("tree", "Round tree", TREE, bottom=29))
spec("pine", "소나무. 겹겹이 뾰족한 잎.", lambda: item("pine", "Pine tree", PINE, bottom=29))
spec("rock", "바위.", lambda: item("rock", "Rock", ROCK, bottom=28))
spec("crystal_cluster", "수정 군락. 동굴에서 빛난다.", lambda: item("crystal_cluster", "Crystal cluster", CRYSTAL, bottom=28))
spec("cauldron", "가마솥. 초록 물약이 끓는다.", lambda: item("cauldron", "Cauldron", CAULDRON, bottom=28))
spec("anvil", "모루.", lambda: item("anvil", "Anvil", ANVIL, bottom=28))
spec("fence", "나무 울타리.", lambda: item("fence", "Wooden fence", FENCE, bottom=28))
spec("well", "우물. 지붕이 있는 돌 우물.", lambda: item("well", "Well", WELL, bottom=29))
spec("table", "나무 탁자.", lambda: item("table", "Table", TABLE, bottom=28))
spec("bed", "침대. 붉은 이불.", lambda: item("bed", "Bed", BED, bottom=28))
spec("lantern", "등불. 기둥에 매단 등.", lambda: item("lantern", "Lantern post", LANTERN, bottom=28))
spec("door", "나무 문. 금빛 손잡이.", lambda: item("door", "Wooden door", DOOR, bottom=29))
spec("pillar", "돌기둥.", lambda: item("pillar", "Stone pillar", PILLAR, bottom=29))
spec("statue", "석상. 검을 치켜든 영웅.", lambda: item("statue", "Hero statue", STATUE, bottom=29))
spec("mailbox", "우편함.", lambda: item("mailbox", "Mailbox", MAILBOX, bottom=28))
spec("tent", "텐트. 가죽 천막.", lambda: item("tent", "Tent", CAMPTENT, bottom=28))
spec("stairs", "돌계단.", lambda: item("stairs", "Stone stairs", STAIRS, bottom=28))
spec("cart", "손수레.", lambda: item("cart", "Cart", CART, bottom=28))
spec("flowerpot", "화분. 분홍 꽃.", lambda: item("flowerpot", "Flower pot", FLOWERPOT, bottom=28))
spec("scarecrow", "허수아비.", lambda: item("scarecrow", "Scarecrow", SCARECROW, bottom=29))

# tiles (12)
section("tiles")
spec("tile_dirt", "흙 바닥 타일.", lambda: tile("tile_dirt", "Dirt tile", lambda x, y: "O", ("o", 40), 11))
spec("tile_sand", "모래 타일.", lambda: tile("tile_sand", "Sand tile", lambda x, y: "S", ("s", 30), 12))
spec("tile_snow", "눈 타일.", lambda: tile("tile_snow", "Snow tile", lambda x, y: "W", ("w", 24), 13))
spec("tile_water", "물 타일. 물결 무늬.", lambda: tile("tile_water", "Water tile", waves("L", "C", "B")))
spec("tile_lava", "용암 타일.", lambda: tile("tile_lava", "Lava tile", waves("R", "Y", "A"), ("r", 20), 14))
spec("tile_wood", "나무 바닥.", lambda: tile("tile_wood", "Wood plank floor", planks("O", "O", "o"), ("o", 12), 15))
spec("tile_brick_red", "붉은 벽돌 벽.", lambda: tile("tile_brick_red", "Red brick wall", bricks("A", "a", "r", "K")))
spec("tile_cobble", "자갈길.", lambda: tile("tile_cobble", "Cobblestone", cobble("M", "m", "d", "D")))
spec("tile_cave", "동굴 바닥.", lambda: tile("tile_cave", "Cave floor", lambda x, y: "D", ("d", 50), 16))
spec("tile_ice", "얼음 타일.", lambda: tile("tile_ice", "Ice tile", lambda x, y: "C", ("M", 30), 17))
spec("tile_carpet", "체크 카펫.", lambda: tile("tile_carpet", "Checkered carpet", checker("R", "r")))
spec("tile_grass_dark", "짙은 풀밭.", lambda: tile("tile_grass_dark", "Dark grass", lambda x, y: "q", ("e", 40), 18))


import kit32_more  # noqa: E402  registers the second hundred specs
import kit32_nature  # noqa: E402  the third hundred: scenery and outdoor props
import kit32_gaps  # noqa: E402  50 gap fillers: animals, buildings, effects, UI, furniture


def make(aid: str) -> Recipe:
    return SPECS[aid][1]()
