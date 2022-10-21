class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dct = {}

        for path in paths:
            dct[path[0]] = path[1]


        for item in dct.items():
            if item[1] not in dct.keys():
                return item[1]