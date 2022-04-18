import zipfile

import nextcord
from nextcord.ext import commands, menus
import tokens as tk
from musescore_scraper import MuseScraper
import nest_asyncio
nest_asyncio.apply()
import pdfretreive
import asyncio
import os
from zipfile import ZipFile
DiscordToken = tk.DiscordToken

client = commands.Bot(command_prefix="!cpc ")

@client.event
async def on_ready():
    game = nextcord.Game("Type !cpchelp for help")
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def info(client, *message):
    embedVar = nextcord.Embed(title="Cadenza Piano Bot - Information", description="General purpose bot for the Cadenza Piano Club @ Purdue",
                              color=0xceb888)
    embedVar.add_field(name="Sorairo", value="Developer", inline=False)
    embedVar.set_image(url = "https://cdn.discordapp.com/attachments/908217476511305739/964651362317127760/unknown.png")
    await client.send(embed=embedVar)


@client.command()
async def get(client, *message):
    url = message[0]
    #pth = asyncio.gather(pdfretreive.main(url))
    await client.send("Received Request - PDF takes a few seconds to generate please be patient!")

    pth = MuseScraper().to_pdf(url = url)
    MuseScraper().close()
    # except Exception as e:
    #     print(e.__traceback__)
    #     await client.send("Something went wrong with the download process! Please try again later")
    title = pth.name.split(".")[0]

    embedVar = nextcord.Embed(title="Piece Requested", description=title)
    embedVar.add_field(name="URL", value=message[0])
    embedVar.set_image(
        url="https://cdn.discordapp.com/attachments/908217476511305739/964651362317127760/unknown.png")
    await client.send(embed=embedVar)

    zipObj = ZipFile(title + ".zip", 'w', zipfile.ZIP_DEFLATED)

    zipObj.write(title + ".pdf")
    zipObj.close()
    with open(title + ".zip", 'rb') as fp:
        await client.send(file=nextcord.File(fp, title + ".zip"))
    os.remove(pth)
    os.remove(title + ".zip")




def getPDF(url):
    with MuseScraper() as ms:
        ms.to_pdf(url, output = "./pdf")
# while (len(url) != 0):
#     print("reached")
#     pth = pdfretreive.getPDF(url)
#     url = ''




client.run(DiscordToken)