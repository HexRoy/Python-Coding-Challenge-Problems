# Problem
# =====================================================================================================================
# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.
#
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
#
# For example, inverting [0,1,1] results in [1,0,0].
#
#
# Example 1:
#
# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:
#
# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#
#
# Constraints:
#
# n == image.length
# n == image[i].length
# 1 <= n <= 20
# images[i][j] is either 0 or 1.


# Solution
# ====================================================================================================================

# 48 ms
class Solution:
    def flipAndInvertImage(self, image):
        flipped = self.flip_image(image)
        inverted = self.inverted(image)
        return image

    def flip_image(self, image):
        for pixel_row in image:
            pixel_row.reverse()

    def inverted(self, image):
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0


# Input
# =====================================================================================================================
obj = Solution()
print(obj.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))

