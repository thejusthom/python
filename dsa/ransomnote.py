ransomNote = "a", magazine = "b"

for ran in ransomNote:
        if ran not in magazine:
            return False
        else:
            magazine.replace(ran,"")
return True