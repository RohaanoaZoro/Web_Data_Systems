import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

def extract_entities(text):
    # Process the text with spaCy
    doc = nlp(text)

    # Extract entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Example usage
# text = Apple Inc. is a technology company based in Cupertino, California. It was founded by Steve Jobs.

# Example usage 
text = "Caput Mundi (Latin)The Capital of the world Rome (Italian and Latin: Roma [ˈroːma] ⓘ) is the capital city of Italy. It is also the capital of the Lazio region, the centre of the Metropolitan City of Rome, and a special comune named Comune di Roma Capitale. With 2,860,009 residents in 1,285 km2 (496.1 sq mi),[2] Rome is the country's most populated comune and the third most populous city in the European Union by population within city limits. The Metropolitan City of Rome, with a population of 4,355,725 residents, is the most populous metropolitan city in Italy.[3] Its metropolitan area is the third-most populous within Italy.[4] Rome is located in the central-western portion of the Italian Peninsula, within Lazio (Latium), along the shores of the Tiber. Vatican City (the smallest country in the world)[5] is an independent country inside the city boundaries of Rome, the only existing example of a country within a city. Rome is often referred to as the City of Seven Hills due to its geographic location, and also as the Eternal City.[6] Rome is generally considered to be the cradle of Western civilization and Christian culture, and the centre of the Catholic Church.[7][8][9] Rome's history spans 28 centuries. While Roman mythology dates the founding of Rome at around 753 BC, the site has been inhabited for much longer, making it a major human settlement for almost three millennia and one of the oldest continuously occupied cities in Europe.[10] The city's early population originated from a mix of Latins, Etruscans, and Sabines. Eventually, the city successively became the capital of the Roman Kingdom, the Roman Republic and the Roman Empire, and is regarded by many as the first-ever Imperial city and metropolis.[11] It was first called The Eternal City (Latin: Urbs Aeterna; Italian: La Città Eterna) by the Roman poet Tibullus in the 1st century BC, and the expression was also taken up by Ovid, Virgil, and Livy.[12][13] Rome is also called Caput Mundi (Capital of the World).  After the fall of the Empire in the west, which marked the beginning of the Middle Ages, Rome slowly fell under the political control of the Papacy, and in the 8th century, it became the capital of the Papal States, which lasted until 1870. Beginning with the Renaissance, almost all popes since Nicholas V (1447–1455) pursued a coherent architectural and urban programme over four hundred years, aimed at making the city the artistic and cultural centre of the world.[14] In this way, Rome first became one of the major centres of the Renaissance[15] and then became the birthplace of both the Baroque style and Neoclassicism. Famous artists, painters, sculptors, and architects made Rome the centre of their activity, creating masterpieces throughout the city. In 1871, Rome became the capital of the Kingdom of Italy, which, in 1946, became the Italian Republic. In 2019, Rome was the 14th most visited city in the world, with 8.6 million tourists, the third most visited city in the European Union, and the most popular tourist destination in Italy.[16] Its historic centre is listed by UNESCO as a World Heritage Site.[17] The host city for the 1960 Summer Olympics, Rome is also the seat of several specialised agencies of the United Nations, such as the Food and Agriculture Organization (FAO), the World Food Programme (WFP) and the International Fund for Agricultural Development (IFAD). The city also hosts the Secretariat of the Parliamentary Assembly of the Union for the Mediterranean[18] (UfM) as well as the headquarters of many multinational companies, such as Eni, Enel, TIM, Leonardo, and banks such as BNL. Numerous companies are based within Rome's EUR business district, such as the luxury fashion house Fendi located in the Palazzo della Civiltà Italiana. The presence of renowned international brands in the city has made Rome an important centre of fashion and design, and the Cinecittà Studios have been the set of many Academy Award–winning movies.[19] According to the Ancient Romans' founding myth,[20] the name Roma came from the city's founder and first king, Romulus.[1] However, it is possible that the name Romulus was actually derived from Rome itself.[21] As early as the 4th century, there have been alternative theories proposed on the origin of the name Roma. Several hypotheses have been advanced focusing on its linguistic roots which however remain uncertain:[22] Rome has also been called in ancient times simply Urbs (central city),[23] from urbs roma, or identified with its ancient Roman symbol of SPQR, the symbol of its in Rome constituted republican government. Furthermore Rome has been called Urbs Aeterna (The Eternal City), Caput Mundi (The Capital of the world), Throne of St. Peter and Roma Capitale. Roman Kingdom 753–509 BC Roman Republic 509–27 BC Roman Empire 27 BC– 395 AD Western Roman Empire 286–476 Kingdom of Italy 476–493 Ostrogothic Kingdom 493–536  Eastern Roman Empire 536–546 Ostrogothic Kingdom 546–547  Eastern Roman Empire 547–549 Ostrogothic Kingdom 549–552  Eastern Roman Empire 552–751 Kingdom of the Lombards 751–756  Papal States 756–1798  Roman Republic 1798–1799  Papal States 1799–1809  First French Empire 1809–1814  Papal States 1814–1849  Roman Republic 1849  Papal States 1849–1870  Kingdom of Italy 1870–1943  Italian Social Republic 1943–1944  Kingdom of Italy 1944–1946  Italian Republic 1946–present While there have been discoveries of archaeological evidence of human occupation of the Rome area from approximately 14,000 years ago, the dense layer of much younger debris obscures Palaeolithic and Neolithic sites.[10] Evidence of stone tools, pottery, and stone weapons attest to about 10,000 years of human presence. Several excavations support the view that Rome grew from pastoral settlements on the Palatine Hill built above the area of the future Roman Forum. Between the end of the Bronze Age and the beginning of the Iron Age, each hill between the sea and the Capitoline Hill was topped by a village (on the Capitoline, a village is attested since the end of the 14th century BC).[24] However, none of them yet had an urban quality.[24] Nowadays, there is a wide consensus that the city developed gradually through the aggregation (synoecism) of several villages around the largest one, placed above the Palatine.[24] This aggregation was facilitated by the increase of agricultural productivity above the subsistence level, which also allowed the establishment of secondary and tertiary activities. These, in turn, boosted the development of trade with the Greek colonies of southern Italy (mainly Ischia and Cumae).[24] These developments, which according to archaeological evidence took place during the mid-eighth century BC, can be considered as the birth of the city.[24] Despite recent excavations at the Palatine hill, the view that Rome was founded deliberately in the middle of the eighth century BC, as the legend of Romulus suggests, remains a fringe hypothesis.[25] Traditional stories handed down by the ancient Romans themselves explain the earliest history of their city in terms of legend and myth. The most familiar of these myths, and perhaps the most famous of all Roman myths, is the story of Romulus and Remus, the twins who were suckled by a she-wolf.[20] They decided to build a city, but after an argument, Romulus killed his brother and the city took his name. According to the Roman annalists, this happened on 21 April 753 BC.[26] This legend had to be reconciled with a dual tradition, set earlier in time, that had the Trojan refugee Aeneas escape to Italy and found the line of Romans through his son Iulus, the namesake of the Julio-Claudian dynasty.[27] This was accomplished by the Roman poet Virgil in the first century BC. In addition, Strabo mentions an older story, that the city was an Arcadian colony founded by Evander. Strabo also writes that Lucius Coelius Antipater believed that Rome was founded by Greeks.[28][29] After the foundation by Romulus according to a legend,[26] Rome was ruled for a period of 244 years by a monarchical system, initially with sovereigns of Latin and Sabine origin, later by Etruscan kings. The tradition handed down seven kings: Romulus, Numa Pompilius, Tullus Hostilius, Ancus Marcius, Tarquinius Priscus, Servius Tullius and Lucius Tarquinius Superbus.[26] In 509 BC, the Romans expelled the last king from their city and established an oligarchic republic. Rome then began a period characterised by internal struggles between patricians (aristocrats) and plebeians (small landowners), and by constant warfare against the populations of central Italy: Etruscans, Latins, Volsci, Aequi, and Marsi.[32] After becoming master of Latium, Rome led several wars (against the Gauls, Osci-Samnites and the Greek colony of Taranto, allied with Pyrrhus, king of Epirus) whose result was the conquest of the Italian peninsula, from the central area up to Magna Graecia.[33] The third and second century BC saw the establishment of Roman hegemony over the Mediterranean and the Balkans, through the three Punic Wars (264–146 BC) fought against the city of Carthage and the three Macedonian Wars (212–168 BC) against Macedonia.[34] The first Roman provinces were established at this time: Sicily, Sardinia and Corsica, Hispania, Macedonia, Achaea and Africa.[35] From the beginning of the 2nd century BC, power was contested between two groups of aristocrats: the optimates, representing the conservative part of the Senate, and the populares, which relied on the help of the plebs (urban lower class) to gain power. In the same period, the bankruptcy of the small farmers and the establishment of large slave estates caused large-scale migration to the city. The continuous warfare led to the establishment of a professional army, which turned out to be more loyal to its generals"
entities = extract_entities(text)

for entity, label in entities:
    print(f"Entity: {entity}, Label: {label}")