def item_on_top(arr):
    arr_len = len(arr)
    if arr_len == 0:
        return None
    return arr[len(arr) - 1]


def get_spare_peg(peg_1, peg_2):
    indexes = [0, 1, 2]
    indexes.remove(peg_1)
    indexes.remove(peg_2)
    return indexes[0]


class TowersOfHanoi:
    def __init__(self):
        self.total_disks = 0
        self.towers = [
            [],
            [],
            []
        ]

    def set_initial_state(self, n):
        self.total_disks = n
        del self.towers[0][:]
        del self.towers[1][:]
        del self.towers[2][:]
        first_tower = self.towers[0]
        while True:
            if n == 0:
                break
            first_tower.append(n)
            n -= 1

    def move_top_from_to(self, start_tower_index, end_tower_index):
        on_top = item_on_top(self.towers[start_tower_index])
        self.towers[end_tower_index].append(on_top)
        self.towers[start_tower_index].pop()

    def hanoi(self, n, start_peg=0, final_peg=1):
        if n > 0:
            spare_peg = get_spare_peg(start_peg, final_peg)
            self.hanoi(n - 1, start_peg, spare_peg)
            self.move_top_from_to(start_peg, final_peg)
            self.hanoi(n - 1, spare_peg, final_peg)

    def solve(self):
        self.hanoi(self.total_disks)