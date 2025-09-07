class Solution:
    def defangIPaddr(self, address: str) -> str:
        transformer= str.maketrans({".":"[.]"})
        defanged_add=address.translate(transformer)
        return defanged_add
