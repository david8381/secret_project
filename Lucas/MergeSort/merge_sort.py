from numba import njit # optimize code to run faster


@njit(fastmath=True)
def merge(left_half, right_half):
        print("merging", left_half, right_half)

        l = 0
        r = 0
        combined = []
        while l < len(left_half) and r < len(right_half):
                if left_half[l] < right_half[r]:
                        combined.append(left_half[l])
                        l += 1
                else:
                        combined.append(right_half[r])
                        r += 1
        while l < len(left_half):
                combined.append(left_half[l])
                l+=1
        while r < len(right_half):
                combined.append(right_half[r])
                r+=1

        print("merged", combined)
        return combined


@njit(fastmath=True)
def merge_sort(list):
        if len(list) == 1:
                return list

        left_half = list[0:len(list)/2]
        right_half = list[len(list)/2:]
        print("left", left_half, "right", right_half)
        left_half_sorted = merge_sort(left_half)
        right_half_sorted = merge_sort(right_half)

        return merge(left_half_sorted, right_half_sorted)

getting_list = True
to_sort = []
while getting_list:
        to_add = input("Type a number to add, or type Q to quit")
        if to_add == 'Q' or to_add == 'q':
                getting_list = False
        else:
                to_sort.append(int(to_add))

print(merge_sort(to_sort))
