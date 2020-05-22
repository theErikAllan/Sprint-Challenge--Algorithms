class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        # The robot starts on the left side, position = 0
        # The robot starts with empty hands
        # The robot picks up the item at position 0 if the robot is not holding one already
        if self.can_move_left() == False and self.compare_item() is None:
            self.swap_item()
            print("Robot is holding this after initial if: ", self._item)

        # The robot checks to see if it can move right
        if self.can_move_right() == True:
            # If the robot can move right, it moves right by 1
            self.move_right()
            print("Robot position is: ", self._position)

            # The robot compares the item in its hands with the item in front of it
            if self.compare_item() <= 0:
                # If the held item is less than or equal to the item in front, the robot moves left and drops (swaps) the item in its original place, and then moves right again to pick up the next item to compare
                self.move_left()
                self.swap_item()
                self.move_right()
                self.swap_item()
                # Then we recursively call the sort() method and move down the list
                print("Robot is holding this after held < front: ", self._item)
                return self.sort()

            elif self.compare_item() > 0:
                # If the held item is greater than the item in front, we recursively call the sort() method and move down the list
                print("Robot is holding this after held > front: ", self._item)
                return self.sort()
        else:
            # If the robot cannot move to the right, we have reached the end of the list and need to drop the current item as it is the maximum, and start from the beginning of the list
            print("Before end swap, Robot is holding: ", self._item)
            self.swap_item()
            print("After end swap, Robot is holding: ", self._item)
            while self.can_move_left() == True:
                self.move_left()
                print("This is robot's position: ", self._position)
            return self.sort()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    biglist = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    l = [15, 41, 58, 49, 26, 4, 28]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)