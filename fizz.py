from os import system
from json import dump, load
from textwrap import fill
from getpass import getpass

# create text wrap function
# dry

NC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RED = '\033[91m'
MAGENTA = '\033[95m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
CYAN = '\033[96m'
BLUE = '\033[94m'


def embold(strIn):
    return BOLD + strIn + NC


def read():
    global data
    f = open("./config.json")
    data = load(f)
    f.close()
    return data


data = read()

sectIndex = {}


def cleanup():
    system("/usr/bin/clear")
    global data
    del data


def header():
    system("/usr/bin/clear")
    print("───────────────────────────────────────────────")
    print(BOLD + "      ____________________" + NC)
    print(BOLD + "     / ____/  _/__  /__  /" + CYAN + "\tcopyright (c)" + NC)
    print(BOLD + "    / /_   / /   / /  / / " + CYAN + "\t2024 axiom" + NC)
    print(BOLD + "   / __/ _/ /   / /__/ /__" + RED + "\tno warranty" + NC)
    print(BOLD + "  /_/   /___/  /____/____/" + MAGENTA + "\tv0.1.7" + NC)
    print("\n───────────────────────────────────────────────\n")


def write():
    f = open("./config.json", 'w')
    dump(data, f, indent=4)
    f.close()


def ent(color, strIn):
    return BOLD + "[" + color + str(strIn) + NC + BOLD + "]" + NC


def opt(color, name, status):
    symbol = " "
    if status:
        symbol = "+"
    return BOLD + "[" + color + symbol + NC + BOLD + "]" + NC + " - " + str(name)


def generate():
    global data

    data = read()

    with open('fizz.sh', 'a') as fizzOut:
        fizzOut.write("NC='\\033[0m'\n")
        fizzOut.write("RED='\\033[1;31m'\n")
        fizzOut.write("GREEN='\\033[1;32m'\n")
        fizzOut.write("YELLOW='\\033[1;33m'\n")
        fizzOut.write("BLUE='\\033[1;34m'\n")
        fizzOut.write("PURPLE='\\033[1;35m'\n")
        fizzOut.write("CYAN='\\033[1;36m'\n")
        fizzOut.write("\n")
        fizzOut.write("NRERR=87\n")
        fizzOut.write("\n")
        fizzOut.write("if ! $(sudo -l &> /dev/null); then\n")
        fizzOut.write(
            "\techo -e \"${RED}[!]${NC} exit (${NRERR}): " +
            "elevated privileges required\"\n")
        fizzOut.write("\texit $NRERR\n")
        fizzOut.write("fi\n")
        fizzOut.write("\n")
        fizzOut.write("echo -e \"───────────────────────────────────────────────\n")
        fizzOut.write("      ____________________\n")
        fizzOut.write("     / ____/  _/__  /__  /	${CYAN}copyright (c)${NC}\n")
        fizzOut.write("    / /_   / /   / /  / / 	${CYAN}2024 axiom${NC}\n")
        fizzOut.write("   / __/ _/ /   / /__/ /__	${RED}no warranty${NC}\n")
        fizzOut.write("  /_/   /___/  /____/____/	${PURPLE}v0.1.7${NC}\n")
        fizzOut.write("\n")
        fizzOut.write("───────────────────────────────────────────────\"\n")
        fizzOut.write("\n")
        fizzOut.write("sudo apt-get -y update > /dev/null")
        fizzOut.write("\n")
        for key in data["data"][1]:
            count = 0
            for _ in data["data"][1][key]:
                if data["data"][1][key][count]["active"]:
                    fizzOut.write(
                        "echo -e \"${GREEN}[+]${NC} " +
                        "Installing: ${BLUE}" +
                        data["data"][1][key][count]["name"] +
                        ":${NC}\"\n")
                    for cmd in data["data"][1][key][count]["exec"]:
                        fizzOut.write(cmd + "\n")
                count += 1


def getOptions(section):
    global data
    data = read()
    dataRange = len(data["data"][1][section])
    selectedData = data["data"][1][section]

    count = 0
    while count < 3 or count < dataRange:
        temp = ""
        tabbing = "\t"
        if count < dataRange:
            temp = "  " + opt(
                GREEN, selectedData[count]["name"],
                selectedData[count]["active"])
            if len(selectedData[count]["name"]) <= 7:
                tabbing += "\t"
        else:
            tabbing += "\t\t"
        if count < 3:
            match count:
                case 0:
                    temp += tabbing + ent(BLUE, "?") + " - help"
                case 1:
                    temp += tabbing + ent(RED, "B") + " - back"
                case 2:
                    temp += tabbing + ent(RED, "X") + " - quit"
                case _:
                    pass
        print(temp)
        count += 1


def getSections():
    global data

    data = read()
    dataRange = len(data["data"][1])
    selectedData = data["data"][1]

    id = 1
    for key in selectedData:
        sectIndex[id] = key
        id += 1

    count = 0
    while count < 5 or count < dataRange:
        temp = ""
        tabbing = "\t"
        if count < dataRange:
            temp = "  " + ent(GREEN, count + 1) + " - " + sectIndex.get(count + 1)
            if len(sectIndex.get(count + 1)) <= 7:
                tabbing += "\t"
        else:
            tabbing += "\t\t"
        if dataRange < 5:
            match count:
                case 0:
                    temp += tabbing + ent(BLUE, "?") + " - help"
                case 1:
                    temp += tabbing + ent(RED, "B") + " - back"
                case 2:
                    temp += tabbing + ent(RED, "X") + " - quit"
                case 3:
                    temp += tabbing + ent(GREEN, "-") + " - aliasing"
                case 4:
                    temp += tabbing + ent(GREEN, "-") + " - git credentials"
                case _:
                    pass
        else:
            match count:
                case 0:
                    temp += tabbing + ent(BLUE, "?") + " - help"
                case 1:
                    temp += tabbing + ent(RED, "B") + " - back"
                case 2:
                    temp += tabbing + ent(RED, "X") + " - quit"
                case _:
                    if count == dataRange-1:
                        temp += tabbing + ent(GREEN, "-") + " - git credentials"
                    elif count == dataRange-2:
                        temp += tabbing + ent(GREEN, "-") + " - aliasing"
        print(temp)
        count += 1


def helpMenu(name, desc, referrer):
    header()
    print("  " + ent(BLUE, "?") + "\t" + embold(name))
    print("\n", fill(desc, 38, initial_indent=("\t"), subsequent_indent="\t"))
    print("\n  " + ent(BLUE, "i") + "\tpress enter to return")
    getpass("")
    if referrer == "fizzconfigmenu":
        confMenu()
    elif referrer == "fizzmainmenu":
        mainMenu()
    else:
        optMenu(referrer)


def mainMenu():
    header()
    print("  Select an option:\n")
    print("  " + ent(GREEN, 1) + " - generate\t" + ent(BLUE, "?") + " - help")
    print("  " + ent(GREEN, 2) + " - configure\t" + ent(RED, "X") + " - quit")
    print("\n───────────────────────────────────────────────")
    answer = str(input("\n >> ")).lower()
    if answer in ("?", "help"):
        helpMenu(
            "help",
            "welcome to fizz, the pop!_os desktop provisioning" +
            "/configuration wizard. from the main menu, enter 2 to begin " +
            "configuring your installation. if you already have a valid " +
            "configuration file (config.json) within the fizz directory" +
            ", enter 1 to begin.", "fizzmainmenu")
    elif answer in ("x", "quit", "exit"):
        cleanup()
        return
    elif answer in ("1", "generate", "gen"):
        generate()
    elif answer in ("2", "configure", "config", "conf"):
        confMenu()
    else:
        mainMenu()


def confMenu():
    header()
    print("  select an option:\n")
    getSections()
    print("\n───────────────────────────────────────────────")
    answer = str(input("\n >> ")).lower()
    if answer in ("?", "help"):
        helpMenu("Configuration", "Config help", "fizzconfigmenu")
    elif answer in ("b", "back"):
        mainMenu()
    elif answer in ("x", "quit", "exit"):
        cleanup()
        return
    elif answer.isnumeric() and (0 < int(answer) <= len(sectIndex)):
        optMenu(sectIndex.get(int(answer)))
    elif answer.isalpha():
        id = list(sectIndex.keys())[list(sectIndex.values()).index(answer)]
        if 0 < id <= 8:
            optMenu(sectIndex.get(int(id)))
    else:
        confMenu()


def optMenu(sect):
    header()
    print("  enable/disable " + sect + " modules:\n")
    getOptions(sect)
    print("\n───────────────────────────────────────────────")
    answer = str(input("\n >> ")).lower()
    if answer in ("?", "help"):
        print("help")
    elif answer in ("b", "back"):
        confMenu()
    elif answer in ("x", "quit", "exit"):
        cleanup()
        return
    else:
        dataRange = len(data["data"][1][sect])
        count = 0
        while count < dataRange:
            if answer == data["data"][1][sect][count]["name"]:
                stat = data["data"][1][sect][count]["active"]
                data["data"][1][sect][count]["active"] = not stat
                write()
                break
            if answer == "?" + data["data"][1][sect][count]["name"]:
                tempCount = count
                count = dataRange  # prevent further iteration
                helpMenu(
                    data["data"][1][sect][tempCount]["name"],
                    data["data"][1][sect][tempCount]["desc"],
                    sect)
                return
            count += 1
        optMenu(sect)


try:
    mainMenu()
except KeyboardInterrupt:
    cleanup()
