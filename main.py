from framerate import main_1, get_filename
from emotion_recognitions import main_2, main_3
import os

if __name__ == '__main__':
    choice = int(input('Выберете режим работы программы: 1(короткие видео) или 2(длинные видео) -- '))
    if choice == 1:
        videos_folder_walk = os.walk('videos')
        for video in videos_folder_walk:
            for item in video[2]:
                if item[-4:].lower() == '.mp4':
                    main_1(f'videos/{item}')
                    main_2(get_filename())
    elif choice == 2:
        videos_folder_walk = os.walk('videos')
        for video in videos_folder_walk:
            for item in video[2]:
                if item[-4:].lower() == '.mp4':
                    main_1(f'videos/{item}')
                    main_3(get_filename())
    else:
        print('Вы ввели неправильное число')

