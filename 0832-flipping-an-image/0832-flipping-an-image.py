class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for png in image:
            for j in range(len(image)):
                if png[j] == 1:
                    png[j] = 0
                else:
                    png[j] = 1
            png.reverse()
        return image