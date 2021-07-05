from selenium import webdriver
import pickle
import threading


def ds():
    import discord
    TOKEN = 'token'  # insert your bot token in this row

    client = discord.Client()

    @client.event
    async def on_ready():
        channel = client.get_channel(discord_chanel)  # insert your discord chanels id in this row
        await channel.send("Notifications")  # insert your notification in this row

    client.run(TOKEN)


def chek_online():
    options = webdriver.ChromeOptions()

    url = "https://www.twitch.tv/streamername"  # insert streamer link instead of url
    options.add_argument("--headless")  # this row starts the browser in the background
    driver = webdriver.Chrome(
        executable_path='path_to_webdriver',
        # insert path to webdriver Chrome instead of path_to_webdriver, use \\ istead of \ if u useing windows
        options=options)

    # you can also enter multiple streamers by duplicating the previous block or useing function "chek_online" vith input argument url 
    try:
        driver.get(url=url)
        time.sleep(5)
        tt = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div['
            '1]/div/div/div/div[1]/div/div/div/a/div[2]/div/div/div/div/p')
        if tt.text == "LIVE":  # LIVE relevant if u use english version, if u use another lenguage check previus xpath and put intaed of "LIVE"
            print(tt.text)
            ds()

    except Exception as ex:
        print(ex)
        t = threading.Timer(300, chek_online).start()
    finally:
        driver.close()
        driver.quit()


chek_online()
