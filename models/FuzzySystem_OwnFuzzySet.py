import simpful as sf

FS = sf.FuzzySystem()

# Service
S_1 = sf.FuzzySet(points=[[0, 1], [2.5, 1], [5, 0]], term="poor")
S_2 = sf.FuzzySet(points=[[2.5, 0], [5, 1], [7.5, 0]], term="average")
S_3 = sf.FuzzySet(points=[[5, 0], [7.5, 1], [10, 1]], term="wonderful")
FS.add_linguistic_variable("service", sf.LinguisticVariable([S_1, S_2, S_3], universe_of_discourse=[0, 10]))

# Food quality
F_1 = sf.FuzzySet(points=[[0, 1], [2.5, 1], [5, 0]], term="bad")
F_2 = sf.FuzzySet(points=[[2.5, 0], [5, 1], [7.5, 0]], term="average")
F_3 = sf.FuzzySet(points=[[5, 0], [7.5, 1], [10, 1]], term="wonderful")
FS.add_linguistic_variable("food_quality", sf.LinguisticVariable([F_1, F_2, F_3], universe_of_discourse=[0, 10]))

# Tip
T_1 = sf.FuzzySet(points=[[0, 1], [6.5, 1], [13, 0]], term="low")
T_2 = sf.FuzzySet(points=[[6.5, 0], [13, 1], [19.5, 0]], term="average")
T_3 = sf.FuzzySet(points=[[13, 0], [19.5, 1], [25, 1]], term="high")
FS.add_linguistic_variable("tip", sf.LinguisticVariable([T_1, T_2, T_3], universe_of_discourse=[0, 25]))

# Inference rules
R1 = "IF (service IS wonderful) OR (food_quality IS wonderful) THEN (tip IS high)"
R2 = "IF (service IS average) THEN (tip IS average)"
R3 = "IF (service IS poor) AND (food_quality IS bad) THEN (tip IS low)"
FS.add_rules([R1, R2, R3])

def test_system(service, food_quality):
    FS.set_variable("service", service)
    FS.set_variable("food_quality", food_quality)
    result = FS.inference(["tip"])
    return result["tip"]

test_cases = [
    (10, 9),
    (7, 7),
    (6, 4),
    (3, 5),
    (1, 2)
]

results = []
for service, food_quality in test_cases:
    tip = test_system(service, food_quality)
    results.append((service, food_quality, tip))

with open('../results/results_Own_set.txt', 'w') as f:
    for service, food_quality, tip in results:
        f.write(
            f' Service: {service},'
            f' Food quality: {food_quality},'
            f' Suggested tip: {tip:.1f}%\n')

for service, food_quality, tip in results:
    print(
        f' Service: {service},'
        f' Food quality: {food_quality},'
        f' Suggested tip: {tip:.1f}%\n')
