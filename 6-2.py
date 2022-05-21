favourite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name, language in favourite_languages.items():
    print(name.title() + "'s favourites laguages is " + language.title() + ".")

for name in favourite_languages.keys():
    print(name)

for language in favourite_languages.values():
    print(language)