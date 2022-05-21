alien_0 = {'color':'green','points':'5'}
print(alien_0['color'])
print(alien_0['points'])
new_point = alien_0['points']
print("You just earned " + str(new_point) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
del alien_0['color']
print(alien_0)