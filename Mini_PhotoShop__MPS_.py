from Main_Window import MainWindow
from ImageState import ImageState
from history_manager import HistoryManager
from Image_controller import ImageController

def main():
    app = MainWindow()

    image_state = ImageState()

    history_manager = HistoryManager(max_steps=10)

    controller = ImageController(app, image_state, history_manager)
    controller.BindEvents()

    app.mainloop()

if __name__ == "__main__":
    main()