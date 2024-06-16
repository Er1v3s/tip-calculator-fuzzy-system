import simpful as sf

FS = sf.FuzzySystem()

# Service
S_1 = sf.FuzzySet(function=sf.Triangular_MF(a=0, b=0, c=4), term="poor")
S_2 = sf.FuzzySet(function=sf.Triangular_MF(a=3, b=5, c=7), term="average")
S_3 = sf.FuzzySet(function=sf.Triangular_MF(a=7, b=10, c=10), term="wonderful")
FS.add_linguistic_variable("service", sf.LinguisticVariable([S_1, S_2, S_3], concept="Quality of Service", universe_of_discourse=[0,10]))

# Food Quality
F_1 = sf.FuzzySet(function=sf.Triangular_MF(a=0, b=0, c=4), term="bad")
F_2 = sf.FuzzySet(function=sf.Triangular_MF(a=3, b=5, c=7), term="average")
F_3 = sf.FuzzySet(function=sf.Triangular_MF(a=7, b=10, c=10), term="wonderful")
FS.add_linguistic_variable("food_quality", sf.LinguisticVariable([F_1, F_2, F_3],concept="Quality of Food", universe_of_discourse=[0,10]))

# Decor
D_1 = sf.FuzzySet(function=sf.Triangular_MF(a=0, b=0, c=4), term="poor")
D_2 = sf.FuzzySet(function=sf.Triangular_MF(a=3, b=5, c=7), term="average")
D_3 = sf.FuzzySet(function=sf.Triangular_MF(a=7, b=10, c=10), term="wonderful")
FS.add_linguistic_variable("decor", sf.LinguisticVariable([D_1, D_2, D_3], concept="Interior Decor", universe_of_discourse=[0,10]))

# Location
L_1 = sf.FuzzySet(function=sf.Triangular_MF(a=0, b=0, c=4), term="bad")
L_2 = sf.FuzzySet(function=sf.Triangular_MF(a=3, b=5, c=7), term="average")
L_3 = sf.FuzzySet(function=sf.Triangular_MF(a=7, b=10, c=10), term="wonderful")
FS.add_linguistic_variable("location", sf.LinguisticVariable([L_1, L_2, L_3], concept="Location", universe_of_discourse=[0,10]))

# Price
P_1 = sf.FuzzySet(function=sf.Triangular_MF(a=0, b=0, c=4), term="high")
P_2 = sf.FuzzySet(function=sf.Triangular_MF(a=3, b=5, c=7), term="average")
P_3 = sf.FuzzySet(function=sf.Triangular_MF(a=7, b=10, c=10), term="low")
FS.add_linguistic_variable("price", sf.LinguisticVariable([P_1, P_2, P_3], concept="Prices", universe_of_discourse=[0,10]))

# Tip
T_1 = sf.FuzzySet(function=sf.Triangular_MF(a=0, b=0, c=10), term="low")
T_2 = sf.FuzzySet(function=sf.Triangular_MF(a=0, b=15, c=25), term="medium")
T_3 = sf.FuzzySet(function=sf.Triangular_MF(a=15, b=25, c=25), term="high")
FS.add_linguistic_variable("tip", sf.LinguisticVariable([T_1, T_2, T_3], concept="Tip Amount", universe_of_discourse=[0,25]))

# Inference rules
R1 = "IF (service IS wonderful) THEN (tip IS high)"
R2 = "IF (food_quality IS wonderful) THEN (tip IS high)"
R3 = "IF (decor IS wonderful) THEN (tip IS high)"
R4 = "IF (location IS wonderful) THEN (tip IS high)"
R5 = "IF (price IS low) THEN (tip IS high)"
R6 = "IF (service IS average) THEN (tip IS medium)"
R7 = "IF (food_quality IS average) THEN (tip IS medium)"
R8 = "IF (decor IS average) THEN (tip IS medium)"
R9 = "IF (location IS average) THEN (tip IS medium)"
R10 = "IF (price IS average) THEN (tip IS medium)"
R11 = "IF (service IS poor) THEN (tip IS low)"
R12 = "IF (food_quality IS bad) THEN (tip IS low)"
R13 = "IF (decor IS poor) THEN (tip IS low)"
R14 = "IF (location IS bad) THEN (tip IS low)"
R15 = "IF (price IS high) THEN (tip IS low)"
FS.add_rules([R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15])

def test_system(service, food_quality, decor, location, price):
    FS.set_variable("service", service)
    FS.set_variable("food_quality", food_quality)
    FS.set_variable("decor", decor)
    FS.set_variable("location", location)
    FS.set_variable("price", price)
    result = FS.inference(["tip"])
    return result["tip"]

test_cases = [
    (10, 9, 10, 8, 10),
    (7, 7, 9, 5, 8),
    (6, 4, 5, 5, 5),
    (3, 5, 4, 2, 1),
    (1, 1, 1, 2, 1)
]

results = []
for service, food_quality, decor, location, price in test_cases:
    tip = test_system(service, food_quality, decor, location, price)
    results.append((service, food_quality, decor, location, price, tip))

with open('../results/results_Triangular.txt', 'w') as f:
    for service, food_quality, decor, location, price, tip in results:
        f.write(
            f' Service: {service},'
            f' Food quality: {food_quality},'
            f' Decor: {decor},'
            f' Location: {location},'
            f' Price: {price},'
            f' Suggested tip: {tip:.1f}%\n')

for service, food_quality, decor, location, price, tip in results:
    print(
        f' Service: {service},'
        f' Food quality: {food_quality},'
        f' Decor: {decor},'
        f' Location: {location},'
        f' Price: {price},'
        f' Suggested tip: {tip:.1f}%\n')
