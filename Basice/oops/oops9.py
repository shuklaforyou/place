class dad:
    basketball=1

class son(dad):
    dance=1
    basketball=8
    def isdance(self):
        return f"yes I dance {self.dance} no of time "
class grandson(son):
    dance=6
    def isdance( self):
        return f"Jackson yeah "\
              f"Yes I dance very awesomely {self.dance} no of time "



darry=dad()
larry=son()
harry=grandson()

print(harry.isdance())
print(harry.basketball)