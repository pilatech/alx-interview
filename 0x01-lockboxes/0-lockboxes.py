#!/usr/bin/python3
"""Of n boxes, are all of them unlockable?"""


def canUnlockAll(boxes):

    """Implement lockboxes to check if all boxes are unlockable
    Args:
        boxes(list): list of lists(boxes)
    Return:
        (bool)True if unlockable, otherwise false
    """
    num_boxes = len(boxes)
    if num_boxes == 1:
        return True

    opened = [0]
    for i in range(num_boxes):
        if len(opened) == num_boxes:
            break
        for key in boxes[i]:
            if len(opened) == num_boxes:
                break
            if ((key != i) and (key not in opened) and
                    key > 0 and key < num_boxes):
                opened.append(key)
    if (len(opened) == num_boxes):
        return True
    return False
