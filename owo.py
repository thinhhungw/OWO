import pyautogui
import pygetwindow as gw
import random
import time

window_title = "Discord"
windows = [window for window in pyautogui.getAllWindows() if window_title in window.title]
window_title2 = "Google"
windows2 = [window for window in pyautogui.getAllWindows() if window_title2 in window.title]

r1 = ["owoh", "owohunt", "oh", "ohunt"]
r2 = ["owobattle", "owob", "obattle", "ob"]
r3 = ["opray", "owopray", "ocurse <@1120391144442966097>", "owocurse <@1120391144442966097>"]
r5 = ["owocoinflip 1", "ocoinflip 1", "owocf 1", "ocf 1", "owocoin 1", "ocoin 1", "owoflip 1", "oflip 1", "owoslots 1", "oslots 1", "owoslot 1", "oslot 1", "owos 1", "os 1"]
r61 = ["owoah", "oah", "owocl", "ocl", "owocash", "ocash", "owoowo", "oowo", "owochecklist", "ochecklist", "owodrake <@1223227016749514872> <@1120391144442966097>"]
r62 = ["owoq", "oq", "owoquest", "oquest", "owoautohunt", "oautohunt", "owoteam", "oteam", "owoz", "oz", "owovote", "owodistractedbf <@1223227016749514872> <@1120391144442966097>"]
r63 = ["owozoo", "ozoo", "owolvl", "olvl", "owolevel", "olevel", "owows", "ows", "owohelp", "ohelp", "odaily", "odrake <@1223227016749514872> <@1120391144442966097>"]
r64 = ["owoinv", "oinv", "owoinventory", "oinventory", "owoshop", "oshop", "owohb", "ohb", "owotm", "otm", "ovote", "odistractedbf <@1223227016749514872> <@1120391144442966097>"]
r65 = ["owodt", "odt", "owopiku", "opiku", "oworun", "orun", "owopup", "opup", "owoweapon", "oweapon", "owodaily", "owoify", "oify", "oarmy", "owopet", "opets"]
r66 = ["owow", "ow", "owolottery", "olottery", "owomy", "omy", "owoemoji", "oemoji", "owoprofile", "oprofile", "owolb", "olb", "owolootbox", "olootbox", "owocrate", "ocrate", "owc", "owowc"]
r67 = ["owoowoify", "oowoify", "owomarry", "omarry", "owocookie", "ocookie", "owoavatar", "oavatar", "owostats", "ostats", "owoemergency", "owoarmy"]
r68 = ["owoping", "oping", "owolink", "olink", "owoguildlink", "oguildlink", "owopatreon", "opatreon", "owocowoncy", "ocowoncy", "oemergency", "owopets"]
r69 = ["owoannouncement", "oannouncement", "oworules", "orules", "owoshards", "oshards", "owocolor", "ocolor", "owoxp", "oxp", "oship <@1223227016749514872> <@1120391144442966097>"]
r71 = ["owopic animal_cat", "opic animal_cat", "owogif animal_cat", "ogif animal_cat", "owopic animal_dog", "opic animal_dog", "owogif animal_dog", "ogif animal_dog", "owopic awoo", "opic awoo"]
r72 = ["owogif awoo", "ogif awoo", "owopic baka", "opic baka", "owogif baka", "ogif baka", "owopic bang", "opic bang", "owogif bang", "ogif bang", "opet"]
r73 = ["owopic banghead", "opic banghead", "owogif banghead", "ogif banghead", "owopic bite", "opic bite", "owogif bite", "ogif bite", "owopic blush", "opic blush"]
r74 = ["owogif blush", "ogif blush", "owopic clagwimoth", "opic clagwimoth", "owogif clagwimoth", "ogif clagwimoth", "owopic cry", "opic cry", "owogif cry", "ogif cry"]
r75 = ["owopic cuddle", "opic cuddle", "owogif cuddle", "ogif cuddle", "owopic dab", "opic dab", "owogif dab", "ogif dab", "owopic dance", "opic dance"]
r76 = ["owogif dance", "ogif dance", "owopic delet_this", "opic delet_this", "owogif delet_this", "ogif delet_this", "owopic deredere", "opic deredere", "owogif deredere", "ogif deredere"]
r77 = ["owopic discord_memes", "opic discord_memes", "owogif discord_memes", "ogif discord_memes", "owopic gaming", "opic gaming", "owogif gaming", "ogif gaming", "owopic greet", "opic greet"]
r78 = ["owogif greet", "ogif greet", "owopic handholding", "opic handholding", "owogif handholding", "ogif handholding", "owopic highfive", "opic highfive", "owogif highfive", "ogif highfive"]
r79 = ["owopic hug", "opic hug", "owogif hug", "ogif hug", "owopic initial_d", "opic initial_d", "owogif initial_d", "ogif initial_d", "owopic insult", "opic insult"]
r710 = ["owogif insult", "ogif insult", "owopic jojo", "opic jojo", "owogif jojo", "ogif jojo", "owopic kemonomimi", "opic kemonomimi", "owogif kemonomimi", "ogif kemonomimi"]
r711 = ["owopic kiss", "opic kiss", "owogif kiss", "ogif kiss", "owopic lewd", "opic lewd", "owogif lewd", "ogif lewd", "owopic lick", "opic lick", "owogif nsfw"]
r712 = ["owogif lick", "ogif lick", "owopic megumin", "opic megumin", "owogif megumin", "ogif megumin", "owopic nani", "opic nani", "owogif nani", "ogif nani"]
r713 = ["owopic neko", "opic neko", "owogif neko", "ogif neko", "owopic nom", "opic nom", "owogif nom", "ogif nom", "owopic owo", "opic owo", "opic nsfw"]
r714 = ["owogif owo", "ogif owo", "owopic pat", "opic pat", "owogif pat", "ogif pat", "owopic poi", "opic poi", "owogif poi", "ogif poi", "owopic nsfw"]
r715 = ["owopic poke", "opic poke", "owogif poke", "ogif poke", "owopic pout", "opic pout", "owogif pout", "ogif pout", "owopic punch", "opic punch"]
r716 = ["owogif punch", "ogif punch", "owopic rem", "opic rem", "owogif rem", "ogif rem", "owopic shrug", "opic shrug", "owogif shrug", "ogif shrug", "ogif nsfw"]
r717 = ["owopic slap", "opic slap", "owogif slap", "ogif slap", "owopic sleepy", "opic sleepy", "owogif sleepy", "ogif sleepy", "owopic smile", "opic smile"]
r718 = ["owogif smile", "ogif smile", "owopic smug", "opic smug", "owogif smug", "ogif smug", "owopic stare", "opic stare", "owogif stare", "ogif stare"]
r719 = ["owopic sumfuk", "opic sumfuk", "owogif sumfuk", "ogif sumfuk", "owopic teehee", "opic teehee", "owogif teehee", "ogif teehee", "owopic thinking", "opic thinking"]
r720 = ["owogif thinking", "ogif thinking", "owopic thumbsup", "opic thumbsup", "owogif thumbsup", "ogif thumbsup", "owopic tickle", "opic tickle", "owogif tickle", "ogif tickle"]
r721 = ["owopic trap", "opic trap", "owogif trap", "ogif trap", "owopic triggered", "opic triggered", "owogif triggered", "ogif triggered", "owopic wag", "opic wag"]
r722 = ["owogif wag", "ogif wag", "owopic waifu_insult", "opic waifu_insult", "owogif waifu_insult", "ogif waifu_insult", "owopic wasted", "opic wasted", "owogif wasted", "ogif wasted"]
r81 = ["owospongebobchicken", "ospongebobchicken", "owoslapcar", "oslapcar", "owoisthisa", "oisthisa", "owocommunismcat sus", "ocommunismcat sus", "owocommunismcat VN", "ocommunismcat SIGMA"]
r81 = ["owocommunismcat SIGMA", "ocommunismcat VN", "owoeject <@1120391144442966097>", "oeject <@1120391144442966097>", "owoemergencymeeting", "oemergencymeeting", "owoheadpat", "oheadpat", "owowaddle", "owaddle"]
r91 = ["owoblush", "oblush", "owocry", "ocry", "owodance", "odance", "owolewd", "olewd", "owopout", "opout"]
r92 = ["owoshrug", "oshrug", "owosleepy", "osleepy", "owosmile", "osmile", "owosmug", "osmug", "owothumbsup", "othumbsup"]
r93 = ["owowag", "owag", "owothinking", "othinking", "owotriggered", "otriggered", "owoteehee", "oteehee", "owoderedere", "oderedere"]
r94 = ["owothonking", "othonking", "owoscoff", "oscoff", "owohappy", "ohappy", "owothumbs", "othumbs", "owogrin", "ogrin"]
r101 = ["owocuddle <@1120391144442966097>", "ocuddle <@1120391144442966097>", "owohug <@1120391144442966097>", "ohug <@1120391144442966097>", "owokiss <@1120391144442966097>", "okiss <@1120391144442966097>", "owolick <@1120391144442966097>", "olick <@1120391144442966097>", "owonom <@1120391144442966097>", "onom <@1120391144442966097>", "obully <@1120391144442966097>"]
r102 = ["owopat <@1120391144442966097>", "opat <@1120391144442966097>", "owopoke <@1120391144442966097>", "opoke <@1120391144442966097>", "owoslap <@1120391144442966097>", "oslap <@1120391144442966097>", "owostare <@1120391144442966097>", "ostare <@1120391144442966097>", "owohighfive <@1120391144442966097>", "ohighfive <@1120391144442966097>", "owosnuggle <@1120391144442966097>"]
r103 = ["owobite <@1120391144442966097>", "obite <@1120391144442966097>", "owogreet <@1120391144442966097>", "ogreet <@1120391144442966097>", "owopunch <@1120391144442966097>", "opunch <@1120391144442966097>", "owohandholding <@1120391144442966097>", "ohandholding <@1120391144442966097>", "owotickle <@1120391144442966097>", "otickle <@1120391144442966097>", "osnuggle <@1120391144442966097>"]
r104 = ["owokill <@1120391144442966097>", "okill <@1120391144442966097>", "owohold <@1120391144442966097>", "ohold <@1120391144442966097>", "owopats <@1120391144442966097>", "opats <@1120391144442966097>", "owowave <@1120391144442966097>", "owave <@1120391144442966097>", "owoboop <@1120391144442966097>", "oboop <@1120391144442966097>", "owobully <@1120391144442966097>"]



if len(windows) > 0 and len(windows2) > 0:
    ds_window = windows[0]
    gg = windows2[0]

    for _ in range(3000):
        try:
            ds_window.activate()
            ss = random.randint(0, 4)
            if ss == 0:
                pyautogui.typewrite(random.choice(r1) + "\n")
                et = random.randint(1, 3)
                time.sleep(et)
                pyautogui.typewrite(random.choice(r2) + "\n")
            elif ss == 1:
                pyautogui.typewrite(random.choice(r2) + "\n")
                et = random.randint(1, 3)
                time.sleep(et)
                pyautogui.typewrite(random.choice(r1) + "\n")
            elif ss == 2:
                pyautogui.typewrite(random.choice(r1) + "\n")
                et = random.randint(1, 3)
                time.sleep(et)
                pyautogui.typewrite(random.choice(r2) + "\n")
            elif ss == 3:
                pyautogui.typewrite(random.choice(r2) + "\n")
                et = random.randint(1, 3)
                time.sleep(et)
                pyautogui.typewrite(random.choice(r1) + "\n")
            ed = random.randint(5, 10)
            time.sleep(ed)
            
            if random.randint(0, 5) == 5:
                pyautogui.typewrite(random.choice(r3) + "\n")
                ed = random.randint(5, 10)
                time.sleep(ed)

            if random.randint(0, 3) == 3:
                pyautogui.typewrite(random.choice(r5) + "\n")
                ed = random.randint(5, 10)
                time.sleep(ed)

            for _ in range(random.randint(0, 2)):
                asd = random.randint(1, 9)
                if asd == 1:
                    pyautogui.typewrite(random.choice(r61) + "\n")
                elif asd == 2:
                    pyautogui.typewrite(random.choice(r62) + "\n")
                elif asd == 3:
                    pyautogui.typewrite(random.choice(r63) + "\n")
                elif asd == 4:
                    pyautogui.typewrite(random.choice(r64) + "\n")
                elif asd == 5:
                    pyautogui.typewrite(random.choice(r65) + "\n")
                elif asd == 6:
                    pyautogui.typewrite(random.choice(r66) + "\n")
                elif asd == 7:
                    pyautogui.typewrite(random.choice(r67) + "\n")
                elif asd == 8:
                    pyautogui.typewrite(random.choice(r68) + "\n")
                elif asd == 9:
                    pyautogui.typewrite(random.choice(r69) + "\n")
                ed = random.randint(5, 10)    
                time.sleep(ed)

            for _ in range(random.randint(0, 2)):
                asd = random.randint(1, 22)
                if asd == 1:
                    pyautogui.typewrite(random.choice(r71) + "\n")
                elif asd == 2:
                    pyautogui.typewrite(random.choice(r72) + "\n")
                elif asd == 3:
                    pyautogui.typewrite(random.choice(r73) + "\n")
                elif asd == 4:
                    pyautogui.typewrite(random.choice(r74) + "\n")
                elif asd == 5:
                    pyautogui.typewrite(random.choice(r75) + "\n")
                elif asd == 6:
                    pyautogui.typewrite(random.choice(r76) + "\n")
                elif asd == 7:
                    pyautogui.typewrite(random.choice(r77) + "\n")
                elif asd == 8:
                    pyautogui.typewrite(random.choice(r78) + "\n")
                elif asd == 9:
                    pyautogui.typewrite(random.choice(r79) + "\n")
                elif asd == 10:
                    pyautogui.typewrite(random.choice(r710) + "\n")
                elif asd == 11:
                    pyautogui.typewrite(random.choice(r711) + "\n")
                elif asd == 12:
                    pyautogui.typewrite(random.choice(r712) + "\n")
                elif asd == 13:
                    pyautogui.typewrite(random.choice(r713) + "\n")
                elif asd == 14:
                    pyautogui.typewrite(random.choice(r714) + "\n")
                elif asd == 15:
                    pyautogui.typewrite(random.choice(r715) + "\n")
                elif asd == 16:
                    pyautogui.typewrite(random.choice(r716) + "\n")
                elif asd == 17:
                    pyautogui.typewrite(random.choice(r717) + "\n")
                elif asd == 18:
                    pyautogui.typewrite(random.choice(r718) + "\n")
                elif asd == 19:
                    pyautogui.typewrite(random.choice(r719) + "\n")
                elif asd == 20:
                    pyautogui.typewrite(random.choice(r720) + "\n")
                elif asd == 21:
                    pyautogui.typewrite(random.choice(r721) + "\n")
                elif asd == 22:
                    pyautogui.typewrite(random.choice(r722) + "\n")
                ed = random.randint(5, 10)    
                time.sleep(ed)

            for _ in range(random.randint(0, 2)):
                asd = random.randint(1, 2)
                if asd == 1:
                    pyautogui.typewrite(random.choice(r81) + "\n")
                elif asd == 2:
                    pyautogui.typewrite(random.choice(r82) + "\n")
                ed = random.randint(5, 10)    
                time.sleep(ed)

            for _ in range(random.randint(0, 2)):
                asd = random.randint(1, 9)
                if asd == 1:
                    pyautogui.typewrite(random.choice(r91) + "\n")
                elif asd == 2:
                    pyautogui.typewrite(random.choice(r92) + "\n")
                elif asd == 3:
                    pyautogui.typewrite(random.choice(r93) + "\n")
                elif asd == 4:
                    pyautogui.typewrite(random.choice(r94) + "\n")
                ed = random.randint(5, 10)    
                time.sleep(ed)

            for _ in range(random.randint(0, 2)):
                asd = random.randint(1, 9)
                if asd == 1:
                    pyautogui.typewrite(random.choice(r101) + "\n")
                elif asd == 2:
                    pyautogui.typewrite(random.choice(r102) + "\n")
                elif asd == 3:
                    pyautogui.typewrite(random.choice(r103) + "\n")
                elif asd == 4:
                    pyautogui.typewrite(random.choice(r104) + "\n")
                ed = random.randint(5, 10)    
                time.sleep(ed)

            gg.activate()

        except Exception as e:
            print(f"Error occurred: {e}")
else:
    print(f"Window with title '{window_title}' or '{window_title2}' not found.")