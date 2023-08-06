import time
import cv2 as cv
import numpy as np

from process_pool import ProcessPool
from multiprocessing import Queue
from reader import ReaderOutput


def is_ready(img_index: int, input: ReaderOutput, n_bg_imgs):
    start = (
        img_index
        if img_index + n_bg_imgs < len(input.images)
        else len(input.images) - n_bg_imgs
    )
    for i in range(start, start + n_bg_imgs):
        if input.images[i] is None:
            return False
    return True


def correct_img(
    img_index: int, input: ReaderOutput, output: Queue, n_bg_imgs: int, index=0
):
    while not is_ready(img_index, input, n_bg_imgs):
        time.sleep(0.1)
    img, fn = input.images[img_index]
    mean = np.mean(img)
    start = (
        img_index
        if img_index + n_bg_imgs < len(input.images)
        else len(input.images) - n_bg_imgs
    )
    bg = np.max([img[0] for img in input.images[start : start + n_bg_imgs]], axis=0)
    correct_img = cv.absdiff(img, bg)
    cleaned_img = cv.absdiff(correct_img, mean)
    output.put((correct_img, cleaned_img, mean, fn))


def run_bg_correction(input: ReaderOutput, output: Queue, n_bg_imgs: int):
    pool = ProcessPool(
        lambda img_index, index: correct_img(
            img_index, input, output, n_bg_imgs, index
        ),
        -1,
    )
    pool.start(4)
    for i in range(len(input.images)):
        pool.add_task(i)
    pool.stop(slow=True)

    # while pool.is_running():
    #     time.sleep(1)

    # print("Bg correction finished")
