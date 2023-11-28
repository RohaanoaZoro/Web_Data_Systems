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
question="What is the height of the Burj Khalifa?"
# text = "Caput Mundi (Latin)The Capital of the world Rome (Italian and Latin: Roma [ˈroːma] ⓘ) is the capital city of Italy. It is also the capital of the Lazio region, the centre of the Metropolitan City of Rome, and a special comune named Comune di Roma Capitale. With 2,860,009 residents in 1,285 km2 (496.1 sq mi),[2] Rome is the country's most populated comune and the third most populous city in the European Union by population within city limits. The Metropolitan City of Rome, with a population of 4,355,725 residents, is the most populous metropolitan city in Italy.[3] Its metropolitan area is the third-most populous within Italy.[4] Rome is located in the central-western portion of the Italian Peninsula, within Lazio (Latium), along the shores of the Tiber. Vatican City (the smallest country in the world)[5] is an independent country inside the city boundaries of Rome, the only existing example of a country within a city. Rome is often referred to as the City of Seven Hills due to its geographic location, and also as the Eternal City.[6] Rome is generally considered to be the cradle of Western civilization and Christian culture, and the centre of the Catholic Church.[7][8][9] Rome's history spans 28 centuries. While Roman mythology dates the founding of Rome at around 753 BC, the site has been inhabited for much longer, making it a major human settlement for almost three millennia and one of the oldest continuously occupied cities in Europe.[10] The city's early population originated from a mix of Latins, Etruscans, and Sabines. Eventually, the city successively became the capital of the Roman Kingdom, the Roman Republic and the Roman Empire, and is regarded by many as the first-ever Imperial city and metropolis.[11] It was first called The Eternal City (Latin: Urbs Aeterna; Italian: La Città Eterna) by the Roman poet Tibullus in the 1st century BC, and the expression was also taken up by Ovid, Virgil, and Livy.[12][13] Rome is also called Caput Mundi (Capital of the World).  After the fall of the Empire in the west, which marked the beginning of the Middle Ages, Rome slowly fell under the political control of the Papacy, and in the 8th century, it became the capital of the Papal States, which lasted until 1870. Beginning with the Renaissance, almost all popes since Nicholas V (1447–1455) pursued a coherent architectural and urban programme over four hundred years, aimed at making the city the artistic and cultural centre of the world.[14] In this way, Rome first became one of the major centres of the Renaissance[15] and then became the birthplace of both the Baroque style and Neoclassicism. Famous artists, painters, sculptors, and architects made Rome the centre of their activity, creating masterpieces throughout the city. In 1871, Rome became the capital of the Kingdom of Italy, which, in 1946, became the Italian Republic. In 2019, Rome was the 14th most visited city in the world, with 8.6 million tourists, the third most visited city in the European Union, and the most popular tourist destination in Italy.[16] Its historic centre is listed by UNESCO as a World Heritage Site.[17] The host city for the 1960 Summer Olympics, Rome is also the seat of several specialised agencies of the United Nations, such as the Food and Agriculture Organization (FAO), the World Food Programme (WFP) and the International Fund for Agricultural Development (IFAD). The city also hosts the Secretariat of the Parliamentary Assembly of the Union for the Mediterranean[18] (UfM) as well as the headquarters of many multinational companies, such as Eni, Enel, TIM, Leonardo, and banks such as BNL. Numerous companies are based within Rome's EUR business district, such as the luxury fashion house Fendi located in the Palazzo della Civiltà Italiana. The presence of renowned international brands in the city has made Rome an important centre of fashion and design, and the Cinecittà Studios have been the set of many Academy Award–winning movies.[19] According to the Ancient Romans' founding myth,[20] the name Roma came from the city's founder and first king, Romulus.[1] However, it is possible that the name Romulus was actually derived from Rome itself.[21] As early as the 4th century, there have been alternative theories proposed on the origin of the name Roma. Several hypotheses have been advanced focusing on its linguistic roots which however remain uncertain:[22] Rome has also been called in ancient times simply Urbs (central city),[23] from urbs roma, or identified with its ancient Roman symbol of SPQR, the symbol of its in Rome constituted republican government. Furthermore Rome has been called Urbs Aeterna (The Eternal City), Caput Mundi (The Capital of the world), Throne of St. Peter and Roma Capitale. Roman Kingdom 753–509 BC Roman Republic 509–27 BC Roman Empire 27 BC– 395 AD Western Roman Empire 286–476 Kingdom of Italy 476–493 Ostrogothic Kingdom 493–536  Eastern Roman Empire 536–546 Ostrogothic Kingdom 546–547  Eastern Roman Empire 547–549 Ostrogothic Kingdom 549–552  Eastern Roman Empire 552–751 Kingdom of the Lombards 751–756  Papal States 756–1798  Roman Republic 1798–1799  Papal States 1799–1809  First French Empire 1809–1814  Papal States 1814–1849  Roman Republic 1849  Papal States 1849–1870  Kingdom of Italy 1870–1943  Italian Social Republic 1943–1944  Kingdom of Italy 1944–1946  Italian Republic 1946–present While there have been discoveries of archaeological evidence of human occupation of the Rome area from approximately 14,000 years ago, the dense layer of much younger debris obscures Palaeolithic and Neolithic sites.[10] Evidence of stone tools, pottery, and stone weapons attest to about 10,000 years of human presence. Several excavations support the view that Rome grew from pastoral settlements on the Palatine Hill built above the area of the future Roman Forum. Between the end of the Bronze Age and the beginning of the Iron Age, each hill between the sea and the Capitoline Hill was topped by a village (on the Capitoline, a village is attested since the end of the 14th century BC).[24] However, none of them yet had an urban quality.[24] Nowadays, there is a wide consensus that the city developed gradually through the aggregation (synoecism) of several villages around the largest one, placed above the Palatine.[24] This aggregation was facilitated by the increase of agricultural productivity above the subsistence level, which also allowed the establishment of secondary and tertiary activities. These, in turn, boosted the development of trade with the Greek colonies of southern Italy (mainly Ischia and Cumae).[24] These developments, which according to archaeological evidence took place during the mid-eighth century BC, can be considered as the birth of the city.[24] Despite recent excavations at the Palatine hill, the view that Rome was founded deliberately in the middle of the eighth century BC, as the legend of Romulus suggests, remains a fringe hypothesis.[25] Traditional stories handed down by the ancient Romans themselves explain the earliest history of their city in terms of legend and myth. The most familiar of these myths, and perhaps the most famous of all Roman myths, is the story of Romulus and Remus, the twins who were suckled by a she-wolf.[20] They decided to build a city, but after an argument, Romulus killed his brother and the city took his name. According to the Roman annalists, this happened on 21 April 753 BC.[26] This legend had to be reconciled with a dual tradition, set earlier in time, that had the Trojan refugee Aeneas escape to Italy and found the line of Romans through his son Iulus, the namesake of the Julio-Claudian dynasty.[27] This was accomplished by the Roman poet Virgil in the first century BC. In addition, Strabo mentions an older story, that the city was an Arcadian colony founded by Evander. Strabo also writes that Lucius Coelius Antipater believed that Rome was founded by Greeks.[28][29] After the foundation by Romulus according to a legend,[26] Rome was ruled for a period of 244 years by a monarchical system, initially with sovereigns of Latin and Sabine origin, later by Etruscan kings. The tradition handed down seven kings: Romulus, Numa Pompilius, Tullus Hostilius, Ancus Marcius, Tarquinius Priscus, Servius Tullius and Lucius Tarquinius Superbus.[26] In 509 BC, the Romans expelled the last king from their city and established an oligarchic republic. Rome then began a period characterised by internal struggles between patricians (aristocrats) and plebeians (small landowners), and by constant warfare against the populations of central Italy: Etruscans, Latins, Volsci, Aequi, and Marsi.[32] After becoming master of Latium, Rome led several wars (against the Gauls, Osci-Samnites and the Greek colony of Taranto, allied with Pyrrhus, king of Epirus) whose result was the conquest of the Italian peninsula, from the central area up to Magna Graecia.[33] The third and second century BC saw the establishment of Roman hegemony over the Mediterranean and the Balkans, through the three Punic Wars (264–146 BC) fought against the city of Carthage and the three Macedonian Wars (212–168 BC) against Macedonia.[34] The first Roman provinces were established at this time: Sicily, Sardinia and Corsica, Hispania, Macedonia, Achaea and Africa.[35] From the beginning of the 2nd century BC, power was contested between two groups of aristocrats: the optimates, representing the conservative part of the Senate, and the populares, which relied on the help of the plebs (urban lower class) to gain power. In the same period, the bankruptcy of the small farmers and the establishment of large slave estates caused large-scale migration to the city. The continuous warfare led to the establishment of a professional army, which turned out to be more loyal to its generals"
# llm_text = "Yes, Rome is the capital city of Italy. The city has been the capital of Italy since the unification of the country in 1865 and is home to the Italian government, parliament, and many other national institutions. Rome is located in central-western Italy and is known for its rich history, culture, and architecture, including ancient ruins such as the Colosseum and Roman Forum, as well as numerous churches, palaces, and museums."
# llm_text = "No, the Statue of Liberty is not located in London. The Statue of Liberty is located on Liberty Island in New York Harbor, within the state of New Jersey, United States. It was a gift from France to the United States and was dedicated on October 28, 1886."
# llm_text = "The Statue of Liberty is a copper sculpture on Liberty Island, New York Harbor. The statue was designed by French artist Frédéric Auguste Bartholdi with Gustave Eiffel as its structural engineer and built by American designer Alexander Calder. It depicts the Roman goddess Libertas and was created to commemorate the centennial of the United States’ independence (1876). The statue is 305 feet tall, stands on a 2-acre island in New York Harbor, has 4 million visitors each year and cost $20 million dollars at its completion."
# llm_text = "nobody knows when the most famous scientist was born. Albert Einstein's birth certificate shows that he was born on 14 March, but this date has never been authenticated by the German government, and some experts have suggested an alternative date based on his parents' marriage certificate.[23] This claim is disputed;[24] in any case, it remains unclear which of these dates—if either—is correct."
# llm_text = "The Statue of Liberty (Liberty Enlightening the World; French: La Liberté éclairant le monde) is a colossal neoclassical sculpture on Liberty Island in New York Harbor in New York City, in the United States. The copper statue, a gift from the people of France, was designed by French sculptor Frédéric Auguste Bartholdi and its metal framework was built by Gustave Eiffel. The statue was dedicated on October 28, 1886.  The statue is a figure of Libertas, the Roman goddess of liberty. She holds a torch above her head with her right hand, and in her left hand carries a tabula ansata inscribed JULY IV MDCCLXXVI (July 4, 1776 in Roman numerals), the date of the U.S. Declaration of Independence. A broken chain and shackle lie at her feet as she walks forward, commemorating the national abolition of slavery following the American Civil War.[8] After its dedication the statue became an icon of freedom and of the United States, being subsequently seen as a symbol of welcome to immigrants arriving by sea.  The idea for the statue was born in 1865, when the French historian and abolitionist Édouard de Laboulaye proposed a monument to commemorate the upcoming centennial of U.S. independence (1876), the perseverance of American democracy and the liberation of the nation's slaves.[9] The Franco-Prussian War delayed progress until 1875, when Laboulaye proposed that the people of France finance the statue and the United States provide the site and build the pedestal. Bartholdi completed the head and the torch-bearing arm before the statue was fully designed, and these pieces were exhibited for publicity at international expositions.  The torch-bearing arm was displayed at the Centennial Exposition in Philadelphia in 1876, and in Madison Square Park in Manhattan from 1876 to 1882. Fundraising proved difficult, especially for the Americans, and by 1885 work on the pedestal was threatened by lack of funds. Publisher Joseph Pulitzer, of the New York World, started a drive for donations to finish the project and attracted more than 120,000 contributors, most of whom gave less than a dollar (equivalent to $33 in 2022). The statue was built in France, shipped overseas in crates, and assembled on the completed pedestal on what was then called Bedloe's Island. The statue's completion was marked by New York's first ticker-tape parade and a dedication ceremony presided over by President Grover Cleveland.  The statue was administered by the United States Lighthouse Board until 1901 and then by the Department of War; since 1933, it has been maintained by the National Park Service as part of the Statue of Liberty National Monument, and is a major tourist attraction. Limited numbers of visitors can access the rim of the pedestal and the interior of the statue's crown from within; public access to the torch has been barred since 1916. Design and construction process Origin Both the Roman goddess Libertas and Sun god Sol Invictus (The Unconquered Sun, pictured) influenced the design of Liberty Enlightening the World.  According to the National Park Service, the idea of a monument presented by the French people to the United States was first proposed by Édouard René de Laboulaye, president of the French Anti-Slavery Society and a prominent and important political thinker of his time. The project is traced to a mid-1865 conversation between Laboulaye, a staunch abolitionist, and Frédéric Bartholdi, a sculptor. In after-dinner conversation at his home near Versailles, Laboulaye, an ardent supporter of the Union in the American Civil War, is supposed to have said: If a monument should rise in the United States, as a memorial to their independence, I should think it only natural if it were built by united effort—a common work of both our nations.[10] The National Park Service, in a 2000 report, however, deemed this a legend traced to an 1885 fundraising pamphlet, and that the statue was most likely conceived in 1870.[11] In another essay on their website, the Park Service suggested that Laboulaye was minded to honor the Union victory and its consequences, With the abolition of slavery and the Union's victory in the Civil War in 1865, Laboulaye's wishes of freedom and democracy were turning into a reality in the United States. In order to honor these achievements, Laboulaye proposed that a gift be built for the United States on behalf of France. Laboulaye hoped that by calling attention to the recent achievements of the United States, the French people would be inspired to call for their own democracy in the face of a repressive monarchy.[12]  According to sculptor Frédéric Auguste Bartholdi, who later recounted the story, Laboulaye's alleged comment was not intended as a proposal, but it inspired Bartholdi.[10] Given the repressive nature of the regime of Napoleon III, Bartholdi took no immediate action on the idea except to discuss it with Laboulaye. Bartholdi was in any event busy with other possible projects; in the late 1860s, he approached Isma'il Pasha, Khedive of Egypt, with a plan to build Progress or Egypt Carrying the Light to Asia,[13] a huge lighthouse in the form of an ancient Egyptian female fellah or peasant, robed and holding a torch aloft, at the northern entrance to the Suez Canal in Port Said. Sketches and models were made of the proposed work, though it was never erected. There was a classical precedent for the Suez proposal, the Colossus of Rhodes: an ancient bronze statue of the Greek god of the sun, Helios. This statue is believed to have been over 100 feet (30 m) high, and it similarly stood at a harbor entrance and carried a light to guide ships.[14] Both the khedive and Lesseps declined the proposed statue from Bartholdi, citing the expensive cost.[15] The Port Said Lighthouse was built instead, by François Coignet in 1869.  Any large project was further delayed by the Franco-Prussian War, in which Bartholdi served as a major of militia. In the war, Napoleon III was captured and deposed. Bartholdi's home province of Alsace was lost to the Prussians, and a more liberal republic was installed in France.[10] As Bartholdi had been planning a trip to the United States, he and Laboulaye decided the time was right to discuss the idea with influential Americans.[16] In June 1871, Bartholdi crossed the Atlantic, with letters of introduction signed by Laboulaye.[17]  Arriving at New York Harbor, Bartholdi focused on Bedloe's Island (now named Liberty Island) as a site for the statue, struck by the fact that vessels arriving in New York had to sail past it. He was delighted to learn that the island was owned by the United States government—it had been ceded by the New York State Legislature in 1800 for harbor defense. It was thus, as he put it in a letter to Laboulaye: land common to all the states.[18] As well as meeting many influential New Yorkers, Bartholdi visited President Ulysses S. Grant, who assured him that it would not be difficult to obtain the site for the statue.[19] Bartholdi crossed the United States twice by rail, and met many Americans who he thought would be sympathetic to the project.[17] But he remained concerned that popular opinion on both sides of the Atlantic was insufficiently supportive of the proposal, and he and Laboulaye decided to wait before mounting a public campaign.[20] Bartholdi's 1880 sculpture, Lion of Belfort  Bartholdi had made a first model of his concept in 1870.[21] The son of a friend of Bartholdi's, artist John LaFarge, later maintained that Bartholdi made the first sketches for the statue during his visit to La Farge's Rhode Island studio. Bartholdi continued to develop the concept following his return to France.[21] He also worked on a number of sculptures designed to bolster French patriotism after the defeat by the Prussians. One of these was the Lion of Belfort, a monumental sculpture carved in sandstone below the fortress of Belfort, which during the war had resisted a Prussian siege for over three months. The defiant lion, 73 feet (22 m) long and half that in height, displays an emotional quality characteristic of Romanticism, which Bartholdi would later bring to the Statue of Liberty.[22] Design, style, and symbolism Detail from a 1855–56 fresco by Constantino Brumidi in the Capitol in Washington, D.C., showing two early symbols of America: Columbia (left) and the Indian princess  Bartholdi and Laboulaye considered how best to express the idea of American liberty.[23] In early American history, two female figures were frequently used as cultural symbols of the nation.[24] One of these symbols, the personified Columbia, was seen as an embodiment of the United States in the manner that Britannia was identified with the United Kingdom, and Marianne came to represent France. Columbia had supplanted the traditional European Personification of the Americas as an Indian princess, which had come to be regarded as uncivilized and derogatory toward Americans.[24] The other significant female icon in American culture was a representation of Liberty, derived from Libertas, the goddess of freedom widely worshipped in ancient Rome, especially among emancipated slaves. A Liberty figure adorned most American coins of the time,[23] and representations of Liberty appeared in popular and civic art, including Thomas Crawford's Statue of Freedom (1863) atop the dome of the United States Capitol Building.[23]  The statue's design evokes iconography evident in ancient history including the Egyptian goddess Isis, the ancient Greek deity of the same name, the Roman Columbia and the Christian iconography of the Virgin Mary.[25][26] Thomas Crawford's Statue of Freedom (1854–1857) tops the dome of the Capitol building in Washington  Artists of the 18th and 19th centuries striving to evoke republican ideals commonly used representations of Libertas as an allegorical symbol.[23] A figure of Liberty was also depicted on the Great Seal of France.[23] However, Bartholdi and Laboulaye avoided an image of revolutionary liberty such as that depicted in Eugène Delacroix's famed Liberty Leading the People (1830). In this painting, which commemorates France's July Revolution, a half-clothed Liberty leads an armed mob over the bodies of the fallen.[24] Laboulaye had no sympathy for revolution, and so Bartholdi's figure would be fully dressed in flowing robes.[24] Instead of the impression of violence in the Delacroix work, Bartholdi wished to give the statue a peaceful appearance and chose a torch, representing progress, for the figure to hold.[27] Its second toe on both feet is longer than its big toe, a condition known as Morton's toe or 'Greek foot'. This was an aesthetic staple of ancient Greek art and reflects the classical influences on the statue.[28]  Crawford's statue was designed in the early 1850s. It was originally to be crowned with a pileus, the cap given to emancipated slaves in ancient Rome. Secretary of War Jefferson Davis, a Southerner who would later serve as President of the Confederate States of America, was concerned that the pileus would be taken as an abolitionist symbol. He ordered that it be changed to a helmet.[29] Delacroix's figure wears a pileus,[24] and Bartholdi at first considered placing one on his figure as well. Instead, he used a radiate diadem, or crown, to top its head.[30] In so doing, he avoided a reference to Marianne, who invariably wears a pileus.[31] The seven rays form a halo or aureole.[32] They evoke the sun, the seven seas, and the seven continents,[33] and represent another means, besides the torch, whereby Liberty enlightens the world.[27]  Bartholdi's early models were all similar in concept: a female figure in neoclassical style representing liberty, wearing a stola and pella (gown and cloak, common in depictions of Roman goddesses) and holding a torch aloft. According to popular accounts, the face was modeled after that of Charlotte Beysser Bartholdi, the sculptor's mother,[34] but Regis Huber, the curator of the Bartholdi Museum is on record as saying that this, as well as other similar speculations, have no basis in fact.[35] He designed the figure with a strong, uncomplicated silhouette, which would be set off well by its dramatic harbor placement and allow passengers on vessels entering New York Bay to experience a changing perspective on the statue as they proceeded toward Manhattan. He gave it bold classical contours and applied simplified modeling, reflecting the huge scale of the project and its solemn purpose.[27] Bartholdi wrote of his technique:      The surfaces should be broad and simple, defined by a bold and clear design, accentuated in the important places. The enlargement of the details or their multiplicity is to be feared. By exaggerating the forms, in order to render them more clearly visible, or by enriching them with details, we would destroy the proportion of the work. Finally, the model, like the design, should have a summarized character, such as one would give to a rapid sketch. Only it is necessary that this character should be the product of volition and study, and that the artist, concentrating his knowledge, should find the form and the line in its greatest simplicity.[36]  Liberty is depicted with a raised right foot, showing that she is walking forward amidst a broken shackle and chain.  Bartholdi made alterations in the design as the project evolved. Bartholdi considered having Liberty hold a broken chain, but decided this would be too divisive in the days after the Civil War. The erected statue does stride over a broken chain, half-hidden by her robes and difficult to see from the ground.[30] Bartholdi was initially uncertain of what to place in Liberty's left hand; he settled on a tabula ansata,[37] used to evoke the concept of law.[38] Though Bartholdi greatly admired the United States Constitution, he chose to inscribe JULY IV MDCCLXXVI on the tablet, thus associating the date of the country's Declaration of Independence with the concept of liberty.[37]  Bartholdi interested his friend and mentor, architect Eugène Viollet-le-Duc, in the project.[35] As chief engineer,[35] Viollet-le-Duc designed a brick pier within the statue, to which the skin would be anchored.[39] After consultations with the metalwork foundry Gaget, Gauthier & Co., Viollet-le-Duc chose the metal which would be used for the skin, copper sheets, and the method used to shape it, repoussé, in which the sheets were heated and then struck with wooden hammers.[35][40] An advantage of this choice was that the entire statue would be light for its volume, as the copper need be only 0.094 inches (2.4 mm) thick. Bartholdi had decided on a height of just over 151 feet (46 m) for the statue, double that of Italy's Sancarlone and the German statue of Arminius, both made with the same method.[41] Announcement and early work  By 1875, France was enjoying improved political stability and a recovering postwar economy. Growing interest in the upcoming Centennial Exposition to be held in Philadelphia led Laboulaye to decide it was time to seek public support.[42] In September 1875, he announced the project and the formation of the Franco-American Union as its fundraising arm. With the announcement, the statue was given a name, Liberty Enlightening the World.[43] The French would finance the statue; Americans would be expected to pay for the pedestal.[44] The announcement provoked a generally favorable reaction in France, though many Frenchmen resented the United States for not coming to their aid during the war with Prussia.[43] French monarchists opposed the statue, if for no other reason than it was proposed by the liberal Laboulaye, who had recently been elected a senator for life.[44] Laboulaye arranged events designed to appeal to the rich and powerful, including a special performance at the Paris Opera on April 25, 1876, that featured a new cantata by the composer Charles Gounod. The piece was titled La Liberté éclairant le monde, the French version of the statue's announced name."
llm_text = "The buildings are 862 meters tall. How tall can a tree get? (height vs diameter) The World’s Tallest Building – Burj Khalifa -2016 What is the World's Highest Skyscraper? Burj Khalifa - World's Tallest Tower | Documentary 1080p HD What Is The World's Fastest Elevator? The World’s 5 Best Skyscrapers (& The Biggest Skyscraper Mistakes) "
text_entities = extract_entities(llm_text)
q_entities = extract_entities(question)


for entity, label in q_entities:
    print(f"Entity: {entity}, Label: {label}")

print("XXXXXXXXXXXXXXXXXXXXX")

for entity, label in text_entities:
    print(f"Entity: {entity}, Label: {label}")

s1 = nlp(question)
s2 = nlp(llm_text)
# s3 = nlp(text)

s1_verbs = " ".join([token.lemma_ for token in s1 if token.pos_ == "VERB"])
s1_adj = " ".join([token.lemma_ for token in s1 if token.pos_ == "ADJ"])
s1_nouns = " ".join([token.lemma_ for token in s1 if token.pos_ == "NOUN"])
s1_propn = " ".join([token.lemma_ for token in s1 if token.pos_ == "PROPN"])


s2_verbs = " ".join([token.lemma_ for token in s2 if token.pos_ == "VERB"])
s2_adj = " ".join([token.lemma_ for token in s2 if token.pos_ == "ADJ"])
s2_nouns = " ".join([token.lemma_ for token in s2 if token.pos_ == "NOUN"])
s2_propn = " ".join([token.lemma_ for token in s2 if token.pos_ == "PROPN"])

# print("S1 Verbs", s1_verbs)
# print("S1 s1_adj", s1_adj)
# print("S1 s1_nouns", s1_nouns)

for token in s1:
    print(token.pos_, token.lemma_)

print("YYYYYYYYYYYYYY")

for token in s2:
    print(token.pos_, token.lemma_)

question_POS = " ".join([token.lemma_ for token in s1])

# # Approach 1
# # We compare all the POS and Tokens Lemmas match
s2_sentences = [sent.text for sent in s2.sents]
x = " ".join([token3.lemma_ for token3 in s1])
y=[]
for sentence in s2_sentences:
    print(sentence)
    temp = nlp(sentence)    
    for token in s1:
        for token2 in temp:
            if(token.pos_ == token2.pos_ and token2.lemma_ == token.lemma_):
                print(token.pos_, token.lemma_)
                y.append(token.lemma_)
    
    print("y", y)

    print("\n\n")

print("x", x.split(" "))
x = x.split(" ")
# print("Left in s1", x)
# unique_to_list1 = list(set(x) - set(y))
# unique_to_list2 = list(set(y) - set(x))

# Combine the unique elements from both lists
# result = unique_to_list1

for x1 in x:
    if x1 not in y:
        print(x1)

# print("Elements not common in both lists:", result)

# Approach 2
# We check similarity of a sentence and question
# for sentence in s2_sentences:
#     temp = nlp(sentence).similarity(nlp(question))
#     print(temp)
#     print(sentence)

# # Approach 3
# for sentence in s2_sentences:
#     temp_propn = " ".join([token.lemma_ for token in nlp(sentence) if token.pos_ == "PROPN"])
#     temp = nlp(s1_propn).similarity(nlp(temp_propn))
#     print(temp)