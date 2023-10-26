samelen =[]
for i in data:
    if len(i) ==len(stage) and len(samelen)<3:
        samelen.append(i)
if stage not in samelen:
    samelen.append(stage)
random.shuffle(samelen)
while len(samelen) <4:
    word=random.choice(data)
    if word not in samelen:
        samelen.append(word)