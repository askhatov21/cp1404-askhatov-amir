# class Monitor:
#
#     def __init__(self, model:str, width:int, height:int):
#         """Initialize model, width and height"""
#         self.model = model
#         self.width = width
#         self.height = height
#
#     def get_resolution(self) -> tuple:
#         """Returns the resolution as a tuple (height, weight)"""
#         return self.width, self.height
#
#     def get_total_pixels(self) -> int:
#         """Returns the total pixels as  int"""
#         return self.width * self.height
#
#
# monitor = Monitor("Asus Rox", 3800, 1200)
# print(monitor.get_resolution())
# print(monitor.get_total_pixels())





# x = isinstance("5", int)
# print(x
#
#       )

# e = (9, 7)
# f = (9, 9)
# print(e + f)

class User:

    def __init__(self, name, number_of_tacos:5, score,):
        """Initialize name, number of tacos and score"""
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score


    def give_taco(self, other_user):
        """pass"""
        if self.number_of_tacos > 0:
            self.number_of_tacos -= 1
            other_user.score += 1
        else:
            print(f"{self.name} has no taco left to give!")
