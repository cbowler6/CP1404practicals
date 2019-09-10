from prac_06.guitar import Guitar
guitar1 = Guitar("guitar1", 2000, 400000)
guitar2 = Guitar("guitar2", 1000, 500000)

print("{}, get_age() - expected 19. got {}".format(guitar1.name, guitar1.get_age()))
print("{}, get_age() - expected 1019. got {}".format(guitar2.name, guitar2.get_age()))
print("{}, is_vintage() - expected False. got {}".format(guitar1.name, guitar1.is_vintage()))
print("{}, is_vintage() - expected True. got {}".format(guitar2.name, guitar2.is_vintage()))

# Gibson L-5 CES get_age() - Expected 96. Got 96
# Another Guitar get_age() - Expected 6. Got 6
# Gibson L-5 CES is_vintage() - Expected True. Got True
# Another Guitar is_vintage() - Expected False. Got False