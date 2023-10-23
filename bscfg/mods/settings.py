import bs
import bsGame
from terminal import Colors
from datetime import datetime
date = datetime.now().strftime('%d')

enableTop5effects = True
enableTop5commands = False
enableCoinSystem = True

enableStats = True

# More Settings On setchat.py
spamProtection = True
shieldBomb = False
shieldBomb = False  # shield on bomb
bombLights = False
bombLights = False  # light on bomb

bombName = False # name on bomb

bigBomb = False  # hehe extra

k_msg = False  # Killing Message

k_pop = False  # Killing Message PopUp
nightMode = False
nightMode = True

enableChatFilter = True

showTextsInBottom = False

gameTexts = ['Welcome To Blitz Server', 'Use "/shop commands" to see commands available to buy.', 'Use "/shop effects" to see effects available and their price.', 'Use "/me" or "/stats" to see your '+bs.getSpecialChar(
    'ticket')+' and your stats in this server', 'Use "/buy" to buy effects that you like', 'Use "/donate" to give some of your tickets to other players', 'Use "/scoretocash" to convert some of your score to '+bs.getSpecialChar('ticket')+'\nCurrent Rate: 5scores = '+bs.getSpecialChar('ticket')+'1']

questionDelay = 90  # 60 #seconds
questionsList = {'esta en el final del sol y el comienzo de la luna?': 'l', 'todos lo tenemos atras es arrugado comienza con "C" y termina con "O"?': 'codo', 'entra duro, seco y sale mojado, blando?': 'chicle', 'blanco por dentro verde por afuera?, si no sabes espera...': 'pera',
                 'add': None,
                 'multiply': None}

availableCommands = {'/nv': 50,
                     '/ooh': 1,
                     '/playSound': 10,
                     '/box': 30,
                     '/boxall': 60,
                     '/spaz': 50,
                     '/spazall': 100,
                     '/inv': 400,
                     '/invall': 800,
                     '/tex': 10,
                     '/texall': 40,
                     '/freeze': 600,
                     '/freezeall': 1000,
                     '/sleep': 400,
                     '/sleepall': 800,
                     '/thaw': 50,
                     '/thawall': 70,
                     '/kill': 800,
                     '/killall': 1050,
                     '/end': 250,
                     '/hug': 60,
                     '/hugall': 100,
                     '/tint': 999999,
                     '/sm': 500,
                     '/fly': 500,
                     '/flyall': 1000,
                     '/heal': 50,
                     '/healall': 70,
                     '/gm': 1000}

availableEffects = {'ice': 500,
                    'sweat': 750,
                    'scorch': 500,
                    'glow': 400,
                    'distortion': 750,
                    'slime': 500,
                    'metal': 500,
                    'surrounder': 1000,
                    'tag': 0}

nameOnPowerUps = False  # Whether or not to show the powerup's name on top of powerups

shieldOnPowerUps = False  # Whether or not to add shield on powerups

# Whether or not to show disco lights on powerup's location
discoLightsOnPowerUps = False

FlyMaps = False  # Whether or not to enable the 3D flying maps in games playlist


# Powerup distribution
dist = (('tripleBombs', 2),
        ('iceBombs', 0),
        ('punch', 0),
        ('impactBombs', 2),
        ('landMines', 2),
        ('stickyBombs', 3),
        ('shield', 0),
        ('health', 2),
        ('curse', 0),
        ('Troll', 1),
        ('Bot', 1),
        ('Rchar', 1),
        ('Bunny', 1),
        ('Tunner', 3))


def return_yielded_game_texts():
    for text in gameTexts:
        yield text


def return_players_yielded(bs):
    for player in bs.getSession().players:
        yield player

# ** TERMINAL **

# STATS
print Colors.LIGHT_CYAN+ 'Enable Stats : '+ Colors.END+ Colors.LIGHT_GREEN+ 'ON'+ Colors.END if enableStats else Colors.RED+ 'OFF'+ Colors.END
# COIN SYSTEM
print Colors.LIGHT_CYAN+ 'CoinSystem : '+ Colors.END+ Colors.LIGHT_GREEN+ 'ON'+ Colors.END if enableCoinSystem else Colors.RED+ 'OFF'+ Colors.END
# NIGHT MODE
print Colors.LIGHT_CYAN+ 'Modo Noche Activado!'+ Colors.END if nightMode else 'Modo Noche Desactivado'
# TOPS
print Colors.LIGHT_CYAN+ 'Top Effects : '+ Colors.END+ Colors.LIGHT_GREEN+ 'ON'+ Colors.END if enableTop5effects else Colors.RED+ 'OFF'+ Colors.END