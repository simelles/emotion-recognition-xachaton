from fer import FER
import matplotlib.pyplot as plt
import os


def main_2(jpg_folder):
    jpg_folder_walk = os.walk(jpg_folder)
    for jpg in jpg_folder_walk:
        emotions = []
        for item in jpg[2]:
            test_image_one = plt.imread(f'{jpg_folder}/{item}')
            emo_detector = FER(mtcnn=True)
            dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
            captured_emotions = emo_detector.detect_emotions(test_image_one)
            a = dominant_emotion
            print(item[7:14])
            print(captured_emotions)
            print(dominant_emotion, emotion_score)
            if a is None:
                continue
            else:
                a = ''.join(a)
                emotions.append(a)
        if emotions:
            emotions = max(set(emotions), key=emotions.count)
        with open('prometey.csv', 'a', encoding='utf-8') as file:
            if emotions is None:
                file.write('None, ')
            else:
                if emotions == 'angry':
                    emotions = 0
                if emotions == 'disgust':
                    emotions = 1
                if emotions == 'fear':
                    emotions = 2
                if emotions == 'happy':
                    emotions = 3
                if emotions == 'sad':
                    emotions = 4
                if emotions == 'surprise':
                    emotions = 5
                if emotions == 'neutral':
                    emotions = 6
                b = jpg_folder.find('-')
                file.write(f'{jpg_folder[7:b]}.mp4, {emotions}\n')


def main_3(jpg_folder):
    jpg_folder_walk = os.walk(jpg_folder)
    for jpg in jpg_folder_walk:
        for item in jpg[2]:
            test_image_one = plt.imread(f'{jpg_folder}/{item}')
            emo_detector = FER(mtcnn=True)
            dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
            captured_emotions = emo_detector.detect_emotions(test_image_one)
            print(item[7:14])
            print(captured_emotions)
            print(dominant_emotion, emotion_score)
            with open(f'emotions_{jpg_folder[7:]}.csv', 'a', encoding='utf-8') as file:
                file.write(f'{item[10:14]}, {dominant_emotion}, {emotion_score}\n')
