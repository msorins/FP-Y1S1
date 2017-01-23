from model.gameModel import *
from repository.sentenceRepository import *
from controller.gameController import *
from ui.UI import *

sentenceRepositoryObject = SentenceRepository()

try:
    while True:
        print("New game ! Good luck :)")
        print("")
        print("")
        gameController = GameController()
        UiObject = UI(gameController)
except Exception as e:
    if e == "finished":
        print("")
        print("")
        print("Game FINISHED")
    else:
        print(e)