import sys
import unittest

def height_stack(boxes, last_box=None, total_height=0):
    last_box = last_box or (sys.maxsize, sys.maxsize, sys.maxsize)
    last_w, last_h, last_d = last_box
    last_height = total_height
    for box in boxes:
        w, h, d, = box
        if w < last_w and h < last_h and d < last_d:
            remaining_boxes = tuple(list(b for b in boxes if b != box))
            new_height = height_stack(remaining_boxes, box, last_height+h)
            if new_height > total_height:
                total_height = new_height
    return total_height

class Test(unittest.TestCase):

    def test_height_stack(self):
        boxes = (
            (4,5,6),
            (1,1,1),
            (2,3,5),
            (2,8,2),
            (7,3,5),
            (6,2,9)
        )
        boxes2 = (
            (1, 1, 1),
            (2, 2, 2),
            (3, 3, 3),
            (1, 1, 1),  # ignored
        )
        self.assertEqual(height_stack(boxes), 9)
        self.assertEqual(height_stack(boxes2), 6)

if __name__ == '__main__':
    unittest.main()