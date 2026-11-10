"""kit32_more: the second hundred rpg specs (characters with varied poses, monsters, props).
Imported by kit32 at the end of its module; registers into kit32.SPECS."""
from kit32 import (section, CROWN, HEAD, HEAD_ROUND, M, Recipe, bat, character, item, layer, meta, recolor, rows_of,
                   skeleton, slime, spec, still)

# ---------------------------------------------------------------- new monster grids
WOLF = """
.......OOo......
......OOOo..O...
.OOOOOOOOOOOOo..
OOOOOOOOOOOKOoo.
OOOOOOOOOOOOooo.
OOOOOOOOOOOOooMm
oOOOOOOOOOOoooo.
.ooOOOOOOOooo...
..Oo.Oo..Oo.Oo..
..Oo.Oo..Oo.Oo..
..oo.oo..oo.oo..
"""
SNAKE = """
..........EEE...
.........EEEEe..
.........EKEKe..
..........EEe...
..EEEEEE..EEe...
.EEEEEEEE.EEe...
.EEe..EEEEEEe...
.Ee....eeeeee...
..e.............
"""
GOLEM = """
.....mmmmmmm....
....mMMMMmmmd...
....mMKMMmKmd...
....mMMMMmmmd...
..mmmmMMMMmmmmd.
.mMMMmMMMMmmmmdd
.mMMmmMMMMmmmddd
.mMmmmMMMmmmmddd
.mmmdmmmmmmdddd.
.....mmmmmmd....
....mMMmdMMmd...
....mMmmdmmdd...
....ddddddddd...
"""
DRAGON = """
.........RRr....
........RRRRr...
.......RRKRRRr..
.......RRRRRrr..
....R...RRrr....
...RRR.RRRr.....
..RRRRRRRRRr....
.RRRRRRRRRRr....
RRYYYYRRRRRr....
.RYYYYRRRRr.....
..RYYYRRRRr.....
...RRRRRRr.r....
....Rr.Rr.rr....
"""
IMP = """
..R.....R..
..RR...RR..
..RRRRRRR..
.RRRRRRRRr.
.RRKRRRKRr.
.RRRRRRRRr.
..RRRRRRr..
...RRRRr...
.RRRRRRRRr.
.RRRRRRRRrr
...RRrRRr.r
...Rr.Rr...
"""
RAT = """
.........mm..
........mMMm.
mm...mmmmMKmm
.mmmmmmmmmmmm
..mmmmmmmmmdm
...mdd.mdd...
"""
CRAB = """
.R........R.
RRr......RRr
RRr......RRr
.Rr.RRRR.Rr.
..RRRRRRRR..
..RRKRRKRRr.
.RRRRRRRRRRr
..rRRRRRRrr.
.Rr.Rr.Rr.Rr
"""
BEE = """
...WW..WW...
..WwW..WwW..
...WYYYYW...
..YYKYYKYY..
.YYYYYYYYYG.
.YDDYYDDYYG.
.YYYYYYYYYG.
..DDYYDDYG..
...YYYYYG...
.....YG.....
"""
FROG = """
..EE......EE..
.EKEe....EKEe.
.EEEEEEEEEEEe.
EEEEEEEEEEEEee
EEEEEEEEEEEEee
EEEqqqqqqqqEee
.EEEEEEEEEEee.
EEe.eeeeee.eEe
ee..........ee
"""
WISP = """
....YYY....
..YYYYYYY..
.YYYYYYYYY.
.YYKYYYKYY.
YYYYYYYYYYY
YYYYYYYYYYY
.YYYYYYYYY.
..YYYYYYY..
...Y.YY.Y..
...Y....Y..
"""
TREANT = """
....EEEEEE....
..EEEEEEEEEE..
.EEEEEEEEEEEe.
.EEEEEEEEEEEe.
..EEEEEEEEEe..
....OOOOOo....
...OOKOOKOo...
...OOOOOOOo...
...OOOKKOOo...
Oo.OOOOOOOo.Oo
.OOOOOOOOOOOo.
...OOOOOOOo...
...OOo.OOOo...
...oo..oooo...
"""
MIMIC = """
..OOOOOOOOOOOOo..
.OOOOOOOOOOOOOOo.
OOOOOOKOOOOOKOOoo
OOOOOOOOOOOOOOOoo
OKKKKKKKKKKKKKKKo
OKMKMKMKMKMKMKMKo
OKKKKKKKKKKKKKKKo
OKMKMKMKMKMKMKMKo
OKKKKKKKKKKKKKKKo
OOOOOOOOOOOOOOOoo
OOOOOOOOOOOOOOOoo
ooooooooooooooooo
"""
SCORPION = """
..............AAa
.............AAaa
..............Aa.
.............Aa..
..AAA.......AAa..
.AAAA..AAAAAAa...
AAa..AAAAAAAAa...
AAa..AAKAAAAa....
.AAAAAAAAAAaa....
...a.a.a.a.a.....
"""
WORM = """
.....PPP..........
....PKPKP.........
....PPPPP.........
....PPPPp.........
....PPPPp.....PPP.
....PPPPpPPPPPPPPp
....PPPPPPPPPPPPPp
.....PPPPPPpppppp.
......pppppp......
"""
OWL = """
...OOo..OOo...
..OOOOOOOOOo..
.OOYKOOOOYKOo.
.OOKYOOOOKYOo.
.OOOOOGOOOOOo.
.OOSSSSSSSSOo.
.OOSSSSSSSSoo.
.OOOSSSSSSOoo.
..OOOOOOOOoo..
...GG....GG...
"""
JELLY = """
....VVVVVV....
..VVVVVVVVVV..
.VVVVVVVVVVVv.
.VVKVVVVVVKVv.
.VVVVVVVVVVVv.
..vvvvvvvvvv..
..V.V.V.V.V.v.
..V.v.V.v.V.v.
..v...v...v...
"""
CYCLOPS_HEAD = """
...EEEEEEEEE...
..EEEEEEEEEEE..
.EEEEEEEEEEEEe.
.EEEMMMMMMEEEe.
.EEMMMRRRMMMEe.
.EEMMRRKRRMMEe.
.EEEMMRRRMMEEe.
.EEEEMMMMMEEEe.
..EEEEEEEEEEe..
..EEEEKKKEEEe..
...eeeeeeeee...
"""
HORNS = ".D......D.\nDD......DD\nDDD....DDD"
BONE_PILE = "....MMMM........\n..MMMMMMMM...MM.\nMMMMKKMMKKMMMMMM\n.MMMMMMMMMMMMMM.\nMM.MMMMMMMMM.MM."
ARMOR_GHOST = """
......MMMM......
....MMMMmmmd....
...MMMMmmmmdd...
...MMCCCCmmdd...
...MMMMmmmmdd...
....ddddddddd...
..MMMMMMmmmmmd..
.MMMMMMMmmmmmmd.
.MMmMMMMmmmmdmd.
.MMm.MMMmmmm.md.
.....MMMmmdd....
.....MMMmmdd....
......dddddd....
"""
# ---------------------------------------------------------------- new prop grids
BOOKSHELF = """
OOOOOOOOOOOOOOo
ORRLLGGVVRRLLOo
ORRLLGGVVRRLLOo
ORRLLGGVVRRLLOo
OOOOOOOOOOOOOOo
OLLRRVVGGLLRROo
OLLRRVVGGLLRROo
OLLRRVVGGLLRROo
OOOOOOOOOOOOOOo
OGGVVLLRRGGVVOo
OGGVVLLRRGGVVOo
OGGVVLLRRGGVVOo
ooooooooooooooo
"""
CHAIR = "OOOOOo\nOo..Oo\nOo..Oo\nOOOOOo\nOOOOOo\nOo..Oo\nOo..Oo\noo..oo"
STOOL = "OOOOOOOo\nooooooo.\n.Oo..Oo.\n.Oo..Oo.\n.oo..oo."
CANDLE = ".Y.\nYAY\n.R.\nWWw\nWWw\nWWw\nWWw\nmMd\nmmd"
BUCKET = "OOOOOOo\nOo...Oo\nmMMMMmd\nmMMMMmd\nmMMMMmd\nmmmmmdd\n.ddddd."
HAY = "...GGGGGG...\n.GGYGGGGGGg.\nGGGGGGYGGGgg\nGGYGGGGGGGgg\nGGGGGGGGYGgg\n.ggggggggggg"
LOG = "..OOOOOOOOOOo\n.OOOOOOOOOOOo\nOmOOOOOOOOOOo\nOOoOOOOOOOOOo\n.ooooooooooo."
STUMP = "..OOOOOOOO..\n.OOmmmmmmOo.\nOOmOOOOOOmOo\nOOmOOmmOOmOo\nOOmOOOOOOmOo\n.OOmmmmmmOoo\n.OOOOOOOOOoo\n.OOOOOOOOOoo\n..oooooooo.."
MUSHROOMS = "...RRR......\n..RMRRr.RRR.\n..rrrrr.RMRr\n...SSs..rrrr\n...SSs...SSs\nRRR.SSs..SSs\nRMRr.......\nrrrr.......\n.SSs........"
PUMPKIN = "......Eq......\n.....Ee.......\n..AAAAAAAAAA..\n.AAYAAAAAAAAa.\nAAYAAAAAAAAAaa\nAAAAAAAAAAAAaa\nAAAAAAAAAAAAaa\n.AAAAAAAAAAaa.\n..aaaaaaaaaa.."
JACK = "......Eq......\n.....Ee.......\n..AAAAAAAAAA..\n.AAYAAAAAAAAa.\nAAYKKAAAAKKAaa\nAAAAKAAAAKAAaa\nAAAKAAAAAAKAaa\n.AAAKKKKKKAaa.\n..aaaaaaaaaa.."
CACTUS = "....EEe.....\n....EEe..Ee.\nEe..EEe..Ee.\nEe..EEe..Ee.\nEEEEEEe..Ee.\n.eeeEEEEEEe.\n....EEeeee..\n....EEe.....\n....EEe.....\n....EEe.....\n....eee....."
DEAD_TREE = "..Oo......Oo..\n...Oo....Oo...\n....Oo..Oo....\n.....OoOo.....\n......OOo.....\n......OOo..Oo.\n......OOo.Oo..\n......OOoOo...\n......OOOo....\n......OOo.....\n......OOo.....\n.....oOOoo...."
SNOWMAN = ".....OOo.....\n.....OOo.....\n...WWWWWWw...\n..WWKWWWKWw..\n..WWWWAAAWw..\n...WWWWWWw...\n.OOWWWWWWwOo.\n..oWWKWWWwo..\n.WWWWWWWWWWw.\nWWWWWKWWWWWww\nWWWWWWWWWWWww\n.WWWWWWWWWww.\n..wwwwwwwww.."
BRAZIER = ".....R......\n....RAR.....\n...RAYAR....\n...RAYYAR...\n..RAAYAAr...\n...RAAAr....\nmMMMMMMMMMd.\n.mmmmmmmmmd.\n....mMMd....\n....mMMd....\n..mMMMMMMd..\n..dddddddd.."
ALTAR = "....mMMMMMMd....\n...mMMMMMMMMd...\n..mMMMMYMMMMMd..\n..mMMMYYYMMMMd..\n..mMMMMYMMMMMd..\n...mMMMMMMMMd...\n.mMMMMMMMMMMMMd.\nmMMMMMMMMMMMMMMd\nmmmmmmmmmmmmmmdd"
PORTAL_0 = "....VVVVVV....\n..VVvvvvvvVV..\n.VvvCCCCCCvvV.\n.VvCCCCCCCCvV.\nVvCCCMMCCCCCvV\nVvCCMMMMCCCCvV\nVvCCCMMCCCCCvV\nVvCCCCCCCCCCvV\n.VvCCCCCCCCvV.\n.VvvCCCCCCvvV.\n..VVvvvvvvVV..\n....VVVVVV...."
PORTAL_1 = "....VVVVVV....\n..VVvvvvvvVV..\n.VvvCCCCCCvvV.\n.VvCCCCCCCCvV.\nVvCCCCCCMCCCvV\nVvCCMCCCMMCCvV\nVvCCMMCCCCCCvV\nVvCCCCCCCCCCvV\n.VvCCCMCCCCvV.\n.VvvCCCCCCvvV.\n..VVvvvvvvVV..\n....VVVVVV...."
FOUNTAIN = "......CC......\n.....CCCC.....\n....mMMMMd....\n.....mMMd.....\n..CC.mMMd.CC..\n.mMMMMMMMMMMd.\nmMCCCCCCCCCCmd\nmMCCCCCCCCCCmd\nmmMMMMMMMMMMmd\n.mmmmmmmmmmmd."
BRIDGE = """
OOOOOOOOOOOOOOOOOOOOOOOOOOOO
OoOoOoOoOoOoOoOoOoOoOoOoOoOo
OOOOOOOOOOOOOOOOOOOOOOOOOOOO
nOnOnOnOnOnOnOnOnOnOnOnOnOnO
oooooooooooooooooooooooooooo
"""
LADDER = "Oo......Oo\nOOOOOOOOOo\nOo......Oo\nOo......Oo\nOOOOOOOOOo\nOo......Oo\nOo......Oo\nOOOOOOOOOo\nOo......Oo\nOo......Oo\nOOOOOOOOOo\noo......oo"
VASE = "..LLLLb..\n...LLb...\n..LLLLb..\n.LLLBLLb.\nLLLBLBLLb\nLLLLBLLLb\nLLLLLLLbb\n.LLLLLbb.\n..bbbbb.."
CAGE = ".DDDDDDDDDD.\nDDDDDDDDDDDD\nDD.D.DD.D.DD\nDD.D.DD.D.DD\nDD.D.DD.D.DD\nDD.D.DD.D.DD\nDD.D.DD.D.DD\nDD.D.DD.D.DD\nDDDDDDDDDDDD\nDDDDDDDDDDDD"
SPIKES = "M...M...M...M\nMm..Mm..Mm..Mm\nMm..Mm..Mm..Mm\nmmmmmmmmmmmmmm\ndddddddddddddd"
PLATE = "mmmmmmmmmmmm\nmMMMMMMMMMmd\nmMMMMMMMMMmd\nmmmmmmmmmmdd\ndddddddddddd"
LEVER = "......Oo..\n.....Oo...\n....Oo....\n...Oo.....\nmmMMMMmmd.\nmMMMMMMMmd\nmmmmmmmmdd"
BANNER = "GGGGGGGGGGg\nRRRRRRRRRrg\nRRRRRRRRRr.\nRRRYYYRRRr.\nRRYYYYYRRr.\nRRRYYYRRRr.\nRRRRRRRRRr.\nRRRRRRRRRr.\nRRRrRRrRRr.\nRRr.RRr.Rr."
BELL = "....GG....\n...GGGg...\n..GGGGGg..\n..GYGGGg..\n.GGYGGGGg.\n.GGGGGGGg.\nGGGGGGGGGg\nggggggggg.\n....Gg...."
BENCH = "OOOOOOOOOOOOOOOo\nooooooooooooooo.\n.Oo..........Oo.\n.Oo..........Oo.\n.oo..........oo."
WINDOW = "OOOOOOOOOOo\nOCCCCoCCCOo\nOCCCCoCCCOo\nOCCMCoCCCOo\nOoooooooooo\nOCCCCoCCCOo\nOCCCCoCCCOo\nOCCCCoCCCOo\nooooooooooo"
TORCH_STAND = "....R....\n...RAR...\n...RAYAR.\n..RAYYAR.\n..RAAAr..\n...mMd...\n...mMd...\n...OOo...\n...OOo...\n...OOo...\n...OOo...\n...OOo...\n.mMMMMMd.\n.ddddddd."
GRAVE_CROSS = "....OOo....\n....OOo....\n.OOOOOOOOo.\n.ooooooooo.\n....OOo....\n....OOo....\n....OOo....\n....OOo....\n..mmmmmmd..\n..dddddddd."
SACK = "....Nn....\n...NNNn...\n..NNNNNn..\n.NNNNNNNn.\n.NNNNNNNn.\n.NNNNNNNn.\n..NNNNNn..\n...nnnnn.."
POT_GOLD = "..DDDDDDDD..\n.DGYGGYGGGD.\n.DDDDDDDDDD.\nDDDDDDDDDDDD\nDDDDDDDDDDDD\nDDDDDDDDDDDD\n.DDDDDDDDDD.\n..DDDDDDDD.."
CHEST_GOLD = "..GGGGGGGGGGGGGGg..\n.GGGGGGGGGGGGGGGGg.\nGGGGGGGGGGGGGGGGGgg\nGGGGGGGGGKKGGGGGGgg\nGGGGGGGGGgKgGGGGGgg\nGGGGGGGGGGGGGGGGGgg\nGGGGGGGGGGGGGGGGGgg\nGGGGGGGGGGGGGGGGGgg\n.gggggggggggggggggg"
CRATES = "......OOOOOOOo\n......OoooooOo\n......OoOOOoOo\n......OoooooOo\nOOOOOOOOOOOOOo\nOoooooOoooooOo\nOoOOOoOoOOOoOo\nOoooooOoooooOo\nOOOOOOOOOOOOOo\noooooooooooooo"
SIGN_ARROW = "OOOOOOOOOOOo..\nOhhhhhhhhhOOo.\nOOOOOOOOOOOOOo\nooooooooooooo.\n.....Oo.......\n.....Oo.......\n.....Oo.......\n.....oo......."
WAGON_WHEEL = "...DDDD...\n..DMDDMD..\n.DDDMMDDD.\nDMDDMMDDMD\nDDMMMMMMDD\nDDMMMMMMDD\nDMDDMMDDMD\n.DDDMMDDD.\n..DMDDMD..\n...DDDD..."

# ---------------------------------------------------------------- characters with poses (45)
section("characters")
C = character


def ch(aid, desc, **kw):
    title = kw.pop("title")
    spec(aid, desc, lambda: C(aid, title, **kw))


ch("swordsman_raise", "검을 머리 위로 치켜든 검사. 공격 직전의 자세.", title="Swordsman, sword raised", hair="brown", cloth="red", back="sword", pose="raise")
ch("knight_thrust", "앞으로 검을 찌르는 기사. 방패는 위로 들었다.", title="Knight, thrusting", hair="brown", cloth="iron", back="sword", pose="thrust", front="shield", front_pos=(18, 18), hat="helmet")
ch("samurai", "어깨에 칼을 걸친 사무라이. 검은 머리, 붉은 갑옷.", title="Samurai, sword on shoulder", hair="black", cloth="red", back="sword", pose="shoulder", trim="Dd")
ch("lancer_thrust", "창을 수평으로 내지르는 창기병.", title="Lancer, thrusting", hair="blonde", cloth="blue", back="spear", pose="thrust", hat="helmet")
ch("berserker", "도끼를 머리 위로 휘두르는 광전사.", title="Berserker, axe overhead", hair="red", cloth="brown", back="axe", pose="overhead", beard=True)
ch("warhammer_knight", "망치를 어깨에 멘 중장기사.", title="Knight with warhammer on shoulder", hair="grey", cloth="iron", back="hammer", pose="shoulder", hat="helmet")
ch("archer_aim", "활을 앞으로 겨눈 궁수.", title="Archer, aiming", hair="green", cloth="green", back="bow", pose="guard", head="hood")
ch("mage_cast", "지팡이를 앞으로 내밀고 주문을 외는 마법사.", title="Mage, casting", hair="purple", cloth="purple", back="staff", pose="thrust", hat="witch", robe=True, long_hair=True)
ch("sorceress", "지팡이를 높이 든 여마법사. 붉은 머리, 검은 로브.", title="Sorceress, staff raised", hair="red", cloth="black", back="staff", pose="raise", robe=True, long_hair=True)
ch("druid", "드루이드. 초록 로브, 어깨에 걸친 나무 지팡이, 수염.", title="Druid", hair="brown", cloth="green", back="staff", pose="shoulder", robe=True, beard=True, head="round")
ch("shaman", "주술사. 주황 머리, 보라 옷, 지팡이를 앞으로.", title="Shaman", hair="orange", cloth="purple", back="staff", pose="guard", skin="tan")
ch("assassin", "암살자. 단검을 거꾸로 낮게 든 검은 후드.", title="Assassin, dagger low", hair="black", cloth="black", head="hood", back="dagger", pose="low")
ch("ninja", "닌자. 단검을 앞으로 찌르는 자세.", title="Ninja, striking", hair="black", cloth="black", head="hood", back="dagger", pose="thrust", trim="Rr")
ch("gladiator", "검투사. 검을 앞으로, 방패를 낮게.", title="Gladiator", hair="black", skin="tan", cloth="gold", back="sword", pose="thrust", front="shield", front_pos=(18, 21))
ch("guard", "성문 경비병. 창을 세워 들었다.", title="Gate guard", hair="brown", cloth="blue", back="spear", pose="guard", hat="helmet")
ch("farmer", "농부. 쇠스랑(창)을 어깨에 멨다.", title="Farmer", hair="brown", cloth="green", back="spear", pose="shoulder", head="round")
ch("fisher", "낚시꾼. 긴 낚싯대(창)를 앞으로 드리웠다.", title="Fisher", hair="blue", cloth="cyan", back="spear", pose="thrust", head="round")
ch("miner", "광부. 곡괭이(도끼)를 어깨에 멨다, 투구.", title="Miner", hair="brown", cloth="brown", back="axe", pose="shoulder", hat="helmet")
ch("lumberjack", "나무꾼. 도끼를 들어 올린 수염 난 거한.", title="Lumberjack", hair="orange", cloth="red", back="axe", pose="raise", beard=True)
ch("bandit", "산적. 도끼를 낮게 든 붉은 두건.", title="Bandit", hair="black", cloth="red", head="hood", back="axe", pose="low")
ch("dwarf", "드워프. 둥근 머리에 긴 수염, 망치를 치켜들었다.", title="Dwarf with hammer", hair="orange", cloth="iron", back="hammer", pose="raise", beard=True, head="round")
ch("elf_m", "남성 엘프. 금발, 초록 옷, 검을 어깨에.", title="Elf swordsman", hair="blonde", cloth="green", back="sword", pose="shoulder")
ch("queen", "여왕. 보라 드레스와 금관, 지팡이를 앞으로.", title="Queen", hair="black", cloth="purple", robe=True, hat="crown", long_hair=True, back="wand", pose="guard", trim="Gg")
ch("prince", "왕자. 푸른 옷과 작은 금관, 검을 낮게.", title="Prince", hair="blonde", cloth="blue", hat="crown", back="sword", pose="low", trim="Gg")
ch("wizard_old", "노마법사. 흰 수염, 보라 로브, 지팡이를 높이.", title="Old wizard", hair="white", cloth="purple", back="staff", pose="raise", robe=True, beard=True, hat="witch")
ch("alchemist", "연금술사. 하늘색 로브, 마법봉을 앞으로.", title="Alchemist", hair="brown", cloth="cyan", back="wand", pose="thrust", robe=True)
ch("jester", "광대. 분홍 머리, 보라·금 옷, 류트를 높이.", title="Jester", hair="pink", cloth="purple", back="lute", pose="raise", trim="Gg")
ch("dancer", "무희. 붉은 긴 머리, 분홍 옷, 두 팔 벌림(빈손).", title="Dancer", hair="red", cloth="pink", long_hair=True, robe=True, head="round")
ch("nun", "수녀. 검은 후드에 흰 띠, 책을 품에.", title="Nun", hair="black", cloth="black", head="hood", front="book", robe=True, trim="Ww")
ch("sailor", "선원. 흰 옷에 푸른 띠, 검을 낮게.", title="Sailor", hair="brown", cloth="white", trim="Bb", back="sword", pose="low")
ch("zombie", "좀비. 회색 피부, 찢어진 초록 옷, 팔을 앞으로.", title="Zombie", hair="brown", skin="grey", cloth="green", back="bone_arm", pose="thrust", head="round")
ch("zombie_knight", "좀비 기사. 녹슨 갑옷, 검을 낮게 끈다.", title="Zombie knight", hair="black", skin="grey", cloth="grey", back="sword", pose="low", hat="helmet")
ch("vampire", "뱀파이어. 창백한 피부, 검은 옷, 붉은 띠.", title="Vampire", hair="black", skin="pale", cloth="black", trim="Rr", robe=True)
ch("demon_lord", "마왕. 붉은 피부 대신 보라 로브, 뿔 모자, 지팡이를 높이.", title="Demon lord", hair="black", skin="tan", cloth="purple", back="staff", pose="raise", robe=True, hat="horns")
ch("fairy", "요정. 분홍 머리에 하늘색 옷, 마법봉을 앞으로.", title="Fairy", hair="pink", cloth="cyan", back="wand", pose="guard", head="round", long_hair=True)
ch("paladin_m", "남성 성기사. 흰 갑옷, 망치를 앞으로, 방패.", title="Paladin with hammer", hair="brown", cloth="white", back="hammer", pose="thrust", front="shield", front_pos=(18, 18), trim="Gg")
ch("templar", "성전기사. 붉은 띠 흰 갑옷, 검을 어깨에.", title="Templar", hair="blonde", cloth="white", trim="Rr", back="sword", pose="shoulder", hat="helmet")
ch("ice_knight", "얼음 기사. 하늘색 갑옷, 창을 높이.", title="Ice knight", hair="cyan", cloth="cyan", back="spear", pose="raise", hat="helmet")
ch("fire_knight", "화염 기사. 붉은 갑옷, 검을 머리 위로.", title="Fire knight", hair="orange", cloth="red", back="sword", pose="overhead", hat="helmet")
ch("shadow_archer", "그림자 궁수. 보라 후드, 활을 낮게.", title="Shadow archer", hair="purple", cloth="purple", head="hood", back="bow", pose="low")
ch("monk_staff", "봉술 수도승. 지팡이를 수평으로 앞에.", title="Monk with staff", hair="black", cloth="orange", back="staff", pose="thrust", head="round")
ch("villager_old_f", "할머니. 흰 머리, 갈색 옷, 지팡이를 낮게.", title="Old woman", hair="white", cloth="brown", back="wand", pose="low", head="round", long_hair=True)
ch("boy", "소년. 검은 머리, 하늘색 옷, 빈손.", title="Boy", hair="black", cloth="cyan", head="round")
ch("girl", "소녀. 주황 머리, 초록 옷, 빈손.", title="Girl", hair="orange", cloth="green", head="round", long_hair=True)
ch("goblin_archer", "고블린 궁수. 활을 앞으로.", title="Goblin archer", hair="black", skin="green", cloth="brown", back="bow", pose="guard", head="round")
ch("orc_chief", "오크 족장. 도끼를 머리 위로, 금관.", title="Orc chief", hair="black", skin="green", cloth="red", back="axe", pose="overhead", hat="crown")
ch("goblin_shaman", "고블린 주술사. 지팡이를 높이.", title="Goblin shaman", hair="white", skin="green", cloth="purple", back="staff", pose="raise", head="round")

# ---------------------------------------------------------------- monsters (30)
section("monsters")


def mon(aid, desc, title, grid, *maps, bottom=28):
    spec(aid, desc, lambda: item(aid, title, grid, *maps, bottom=bottom))


mon("wolf", "회색 늑대.", "Wolf", WOLF, ("Oo", "md"))
mon("wolf_brown", "갈색 늑대.", "Brown wolf", WOLF)
mon("wolf_dire", "검은 다이어울프.", "Dire wolf", WOLF, ("Oo", "DK"))
mon("snake", "초록 뱀.", "Snake", SNAKE)
mon("snake_purple", "독사. 보라색.", "Viper", SNAKE, ("Ee", "Vv"))
mon("golem", "돌 골렘.", "Stone golem", GOLEM)
mon("golem_ice", "얼음 골렘.", "Ice golem", GOLEM, ("Mmd", "CCc"))
mon("golem_lava", "용암 골렘.", "Lava golem", GOLEM, ("Mmd", "RAr"))
mon("dragon_red", "붉은 새끼 용.", "Red dragon whelp", DRAGON)
mon("dragon_green", "초록 새끼 용.", "Green dragon whelp", DRAGON, ("Rr", "Eq"))
mon("dragon_blue", "푸른 새끼 용.", "Blue dragon whelp", DRAGON, ("Rr", "LB"))
mon("imp", "임프. 붉은 작은 악마.", "Imp", IMP)
mon("imp_purple", "보라 임프.", "Shadow imp", IMP, ("Rr", "Vv"))
mon("rat", "쥐.", "Rat", RAT)
mon("rat_plague", "역병 쥐. 초록빛.", "Plague rat", RAT, ("Mm", "Ee"))
mon("crab", "게.", "Crab", CRAB)
mon("crab_blue", "푸른 게.", "Blue crab", CRAB, ("Rr", "LB"))
mon("bee", "큰 벌.", "Giant bee", BEE, bottom=26)
mon("frog", "개구리.", "Frog", FROG)
mon("frog_poison", "독개구리. 보라색.", "Poison frog", FROG, ("Eeq", "VVv"))
mon("wisp", "도깨비불.", "Wisp", WISP, bottom=24)
mon("wisp_blue", "푸른 도깨비불.", "Blue wisp", WISP, ("Y", "C"), bottom=24)
mon("wisp_green", "초록 도깨비불.", "Green wisp", WISP, ("Y", "E"), bottom=24)
mon("treant", "트렌트. 걸어다니는 나무.", "Treant", TREANT)
mon("mimic", "미믹. 이빨 난 보물상자.", "Mimic", MIMIC)
mon("scorpion", "전갈.", "Scorpion", SCORPION)
mon("scorpion_black", "검은 전갈.", "Black scorpion", SCORPION, ("Aa", "DK"))
mon("worm", "분홍 벌레.", "Worm", WORM)
mon("owl", "올빼미.", "Owl", OWL)
mon("jellyfish", "보라 해파리.", "Jellyfish", JELLY, bottom=24)
mon("bone_pile", "뼈 무더기. 해골 소환 장소.", "Bone pile", BONE_PILE)
mon("armor_ghost", "빈 갑옷 유령. 눈만 푸르게 빛난다.", "Haunted armor", ARMOR_GHOST)
spec("cyclops", "외눈박이 거인(머리만 32px).", lambda: item("cyclops", "Cyclops", CYCLOPS_HEAD))
spec("slime_ice", "얼음 슬라임.", lambda: slime("slime_ice", "Ice slime", "CCc"))
spec("slime_dark", "어둠 슬라임.", lambda: slime("slime_dark", "Dark slime", "dDD"))
spec("slime_metal", "금속 슬라임. 잡기 어렵다.", lambda: slime("slime_metal", "Metal slime", "Mmd"))
spec("bat_gold", "황금 박쥐.", lambda: bat("bat_gold", "Gold bat", "Gg", "K"))
spec("skeleton_mage", "해골 마법사. 지팡이.", lambda: skeleton("skeleton_mage", "Skeleton mage", held="staff"))
spec("skeleton_archer", "해골 궁수. 활.", lambda: skeleton("skeleton_archer", "Skeleton archer", held="bow"))
spec("skeleton_dark", "암흑 해골.", lambda: skeleton("skeleton_dark", "Dark skeleton", "dDD", held="axe"))

# ---------------------------------------------------------------- props (30)
section("props")


def prop(aid, desc, title, grid, *maps, bottom=28):
    spec(aid, desc, lambda: item(aid, title, grid, *maps, bottom=bottom))


prop("bookshelf", "책장.", "Bookshelf", BOOKSHELF, bottom=29)
prop("chair", "의자.", "Chair", CHAIR)
prop("stool", "등받이 없는 의자.", "Stool", STOOL)
prop("candle", "촛불.", "Candle", CANDLE, bottom=26)
prop("bucket", "양동이.", "Bucket", BUCKET)
prop("haystack", "건초 더미.", "Haystack", HAY)
prop("log", "통나무.", "Log", LOG)
prop("stump", "그루터기.", "Tree stump", STUMP)
prop("mushrooms", "버섯 군락.", "Mushroom patch", MUSHROOMS)
prop("pumpkin", "호박.", "Pumpkin", PUMPKIN)
prop("jack_o_lantern", "잭오랜턴.", "Jack-o'-lantern", JACK)
prop("cactus", "선인장.", "Cactus", CACTUS, bottom=29)
prop("dead_tree", "고목.", "Dead tree", DEAD_TREE, bottom=29)
prop("snowman", "눈사람.", "Snowman", SNOWMAN, bottom=29)
prop("brazier", "화로.", "Brazier", BRAZIER, bottom=29)
prop("altar", "제단. 빛나는 문양.", "Altar", ALTAR)
prop("fountain", "분수.", "Fountain", FOUNTAIN)
prop("bridge", "나무 다리 조각.", "Bridge piece", BRIDGE)
prop("ladder", "사다리.", "Ladder", LADDER, bottom=29)
prop("vase", "푸른 도자기.", "Vase", VASE)
prop("cage", "철창.", "Cage", CAGE)
prop("spike_trap", "가시 함정.", "Spike trap", SPIKES)
prop("pressure_plate", "압력판.", "Pressure plate", PLATE)
prop("lever", "레버.", "Lever", LEVER)
prop("banner_red", "붉은 깃발.", "Red banner", BANNER, bottom=26)
prop("banner_blue", "푸른 깃발.", "Blue banner", BANNER, ("Rr", "LB"), bottom=26)
prop("bell", "종.", "Bell", BELL, bottom=26)
prop("bench", "벤치.", "Bench", BENCH)
prop("window", "창문.", "Window", WINDOW, bottom=26)
prop("torch_stand", "횃불 받침대.", "Torch stand", TORCH_STAND, bottom=29)
prop("grave_cross", "나무 십자가 무덤.", "Grave cross", GRAVE_CROSS)
prop("sack", "자루.", "Sack", SACK)
prop("pot_gold", "금화 항아리.", "Pot of gold", POT_GOLD)
prop("chest_gold", "황금 상자.", "Golden chest", CHEST_GOLD)
prop("crates", "쌓인 상자.", "Crate stack", CRATES, bottom=29)
prop("sign_arrow", "화살표 이정표.", "Arrow sign", SIGN_ARROW)
prop("wagon_wheel", "수레바퀴.", "Wagon wheel", WAGON_WHEEL)


def portal():
    layers = [layer("p0", rows_of(PORTAL_0), 9, 16), layer("p1", rows_of(PORTAL_1), 9, 16)]
    return Recipe(meta=meta("portal", "Portal", (16, 27)), layers=layers,
                  frames={"base": [("p0", 0, 0)], "swirl": [("p1", 0, 0)]}, anims={"swirl": [("base", 160), ("swirl", 160)]})


spec("portal", "차원문. 소용돌이 2프레임.", portal)
