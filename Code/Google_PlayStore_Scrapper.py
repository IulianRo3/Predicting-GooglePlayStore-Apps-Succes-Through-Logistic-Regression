from google_play_scraper import app
from pprint import pprint
import json
import pandas as pd
'''
################################  ENGLISH ###############################################################################
Sadly I could not find a way to take all the apps from a category since the library I used would give me an error message.
So I had to take every app ID by hand.. In order to do that: 
1.You will go to Google PlayStore site
2.Press on the needed app
3.Check its link. At the end of the link you should see something like: "id=Something"
4.Copy eveything after the ID=

################################  ROMÂNĂ  ###############################################################################
Din păcate nu am putut găsi o cale de a lua toate aplicațiile dintr-o anumite categorie, întrucât librăria folosită va da eroare la câmpul Tip.
Prin urmare a trebuit să iar ID-ul fiecărui app de mână.. Pentru a face asta:
1.Am mers pe siteul Google PlayStore
2.Am apăsat pe aplicația de o voiam
3.Am verificat linkul acesteia. La sfârșitul linkului ar trebui să fie ceva precum: "id=ceva"
4.Copiați totul de după ID=
'''
key = {"com.mojang.minecraftpe","com.robtopx.geometryjump","com.rockstargames.gtasa","com.astragon.cs2014", "com.rockstargames.gtavc","com.giantssoftware.fs20.google","com.agaming.thesun.origin","com.sofarsogood.incredibox"
,"com.chucklefish.stardewvalley","com.sega.score","com.marmalade.monopoly","com.ninjakiwi.bloonstd6","com.ubisoft.assassinscreed.identity"
,"com.hg.townsmen7","com.giantssoftware.fs18.google","air.com.flipline.papasmochariatogo","com.scottgames.fivenightsatfreddys","com.and.games505.TerrariaPaid","it.rortos.realflightsimulator"
,"com.astragon.cs3","com.rockstar.gta3","com.turner.teenyttg","cc.peacedeath.peacedeath","com.scottgames.fnaf2","com.squareenixmontreal.hitmansniperandroid"
,"com.halfbrick.fruitninja","com.trueaxis.trueskate","com.clickteam.ultimatecustomnight","com.notdoppler.earntodie","com.piratesoutlaws.fabledgame","com.ea.games.nfs13_row"
,"com.scottgames.fnaf3","com.astragon.cs2016","com.mageeks.farmingpro3","com.rockstargames.gtalcs","com.pastagames.ro1mobile","com.playdigious.deadcells.mobile","com.ironhidegames.android.kingdomrushfrontiers"
,"com.nekki.shadowfight2.paid","com.RobotGentleman.game60SecondsReatomized","com.wb.goog.lnjgo","com.kozgames.motordepot","air.com.flipline.papashotdoggeriatogo","air.com.flipline.papascheeseriatogo"
,"com.devolver.reigns","com.ustwo.monumentvalley","age.of.civilizations2.jakowski.lukasz","com.FireproofStudios.TheRoom","com.turner.ben10uptospeed","com.disney.castleofillusion_goo","com.jds.batim",
"com.wb.goog.lbbg","com.bitzooma.blackborder","com.rockstar.maxpayne","com.humble.SlayTheSpire","com.mageeks.android.trucksim18"
,"com.marmalade.cluedogame","com.realdrift.sipon","nz.co.codepoint.minimetro","com.robotgentleman.game60seconds","com.astragon.trucksim","com.ChubbyPixel.SuicideGuy","com.FYQD.BrightMemory"
,"air.com.flipline.papasdonuteriatogo","com.wb.lego.tcs","com.and.games505.humanfallflat","com.tipsworks.android.pascalswager.google","com.beamdog.pstee","amanita_design.samorost3.GP","com.fds.infiniteflight","com.jumpgames.RealSteel"
,"com.gameloft.android.ANMP.GloftICHM","com.EtherGaming.PocketRoguesUltimate","com.fizzd.connectedworlds","air.com.flipline.papasburgeriatogo","com.TheLonelyDeveloper.TheLonelyHacker","com.humblebundle.forager"
,"com.FireproofStudios.TheRoom3","com.peppapig.holiday","com.rockstargames.gtactw","air.com.flipline.papaspastariatogo","com.headupgames.bridgeconstructorportal","com.mtvn.pawpatrolgooglehanintl","sirec.net.viatadecartier","com.scottgames.fnaf4","com.coffeestainstudios.goatsimulator.wasteofspace"
,"com.younghorses.octodad"}

Title = []
AppId= []
Installs= []
Score= []
Ratings= []
Reviews= []
Size= []
Release=[]
Price=[]

for key in key:
    print(key)
    result = app(
        key,
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )

    Title.append(result.get('title'))
    AppId.append(result.get('appId'))
    Installs.append(result.get('minInstalls'))
    Score.append(result.get('score'))
    Ratings.append(result.get('ratings'))
    Reviews.append(result.get('reviews'))
    Size.append(result.get('size'))
    Release.append(result.get('released'))
    Price.append(result.get('price'))

df = pd.DataFrame(columns=['Title','AppId','Installs','Score','Ratings','Reviews','Size','Release','Price'])
df['Title'] = Title 
df['AppId'] = AppId
df['Installs'] = Installs
df['Score'] = Score
df['Ratings'] = Ratings
df['Reviews'] = Reviews
df['Size'] = Size
df['Release'] = Release
df['Price'] = Price

writer = pd.ExcelWriter('D:\Java\VS-CodPitonul\Serii_Timp\\GAMEE2.xlsx')
df.to_excel(writer)
writer.save()
