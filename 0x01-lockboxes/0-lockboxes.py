#!/usr/bin/python3
'''
Lockboxes Module
'''


def canUnlockAll(boxes):
    '''
    Determines if all the boxes can be opened given the keys inside them.

    Args:
        boxes (list of list of int): A list of boxes,
        each containing a list of keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    '''

    total_boxes = len(boxes)
    unlocked_boxes = set([0])
    keys_to_check = set(boxes[0]).difference([0])

    while keys_to_check:
        current_key = keys_to_check.pop()
        if current_key >= total_boxes or current_key < 0:
            continue
        if current_key not in unlocked_boxes:
            keys_to_check.update(boxes[current_key])
            unlocked_boxes.add(current_key)

    return total_boxes == len(unlocked_boxes)
