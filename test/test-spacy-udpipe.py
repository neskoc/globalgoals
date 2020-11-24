#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:55:56 2020

@author: nesko
"""

import spacy
import spacy_udpipe
from spacy import displacy
from pytextrank import TextRank

# download (if necessary) Swedish udpipe pretrained model
spacy_udpipe.download("sv")
udpipe_model = spacy_udpipe.UDPipeModel("sv")

# nlp.to_disk("../inc/sv/udpipe-spacy-model")
# nlp = spacy_udpipe.load_from_path(lang="sv",
#                                   path="../inc/sv/udpipe-spacy-model",
#                                   meta={"description": "Custom 'sv' model"})
# nlp = spacy.load("../inc/sv/udpipe-spacy-model", udpipe_model=udpipe_model)

text = """Ingen fattigdom


Fattigdom omfattar fler dimensioner än den ekonomiska. Fattigdom innebär även brist på frihet, inflytande, hälsa, utbildning och säkerhet. Det brukar kallas för multidimensionell fattigdom. Idag lever 1,3 miljarder människor i multidimensionell fattigdom och av dessa är hälften under 18 år.
Brist på mat, sjukvård, säkerhet och rent vatten dödar tusentals människor varje dag, men det blir bättre och sedan 1990 har den extrema fattigdomen halverats. Mål 1 handlar om att avskaffa fattigdom i alla dess former och ge alla människor i världen chans till ett värdigt och tryggt liv.

1.1 Utrota den extrema fattigdomen
1.2 Minska fattigdomen med minst 50 %
1.3 Inför sociala trygghetssystem
1.4 Lika rätt till egendom, grundläggande tjänster, teknologi och ekonomiska resurser
1.5 Bygg motståndskraft mot ekonomiska, sociala och miljökatastrofer
1.A Mobilisera resurser till implementering av politik för fattigdomsbekämpning
1.B Skapa policyramverk med fattigdoms- och jämställdhetsperspektiv

Senast 2030 avskaffa den extrema fattigdomen för alla människor överallt. Med extrem fattigdom avses för närvarande människor som lever på mindre än 1,25 US-dollar per dag*.
*År 2015 var gränsen för extrem fattigdom 1.25 USD/dag. Siffran har sedan dess justerats till 1.90 USD/dag.
Till 2030 minst halvera den andel män, kvinnor och barn i alla åldrar som lever i någon form av fattigdom enligt nationella definitioner.
Införa nationellt lämpliga system och åtgärder för socialt skydd för alla, inklusive grund- skydd, och senast 2030 säkerställa att de omfattar en väsentlig andel av de fattiga och de utsatta.
Senast 2030 säkerställa att alla män och kvinnor, i synnerhet de fattiga och de utsatta, har lika rätt till ekonomiska resurser, till- gång till grundläggande tjänster, möjlighet att äga och kontrollera mark och andra former av egendom samt tillgång till arv, naturresurser, lämplig ny teknik och finansiella tjänster, inklusive mikrokrediter.
Till 2030 bygga upp mot- ståndskraften hos de fattiga och människor i utsatta situationer och minska deras utsatthet och sårbarhet för extrema klimatrelaterade händelser och andra ekonomiska, sociala och miljömässiga chocker och katastrofer.
Säkra en betydande resursmobilisering från en mängd olika källor, inklusive genom ökat utvecklingssamarbete, i syfte att ge utvecklingsländerna, i synnerhet de minst utvecklade länderna, tillräckliga och förutsebara medel för att genomföra program och politik för att avskaffa all form av fattigdom.
Upprätta sunda policy ramverk på nationell, regional och internationell nivå på grundval av utvecklingsstrategier som stödjer de fattiga och tar hänsyn till jämställdhetsaspekter, för att stödja ökade investeringar i åtgärder för att avskaffa fattigdom.

Engagera dig i en organisation
Handla hållbart
Sprid kunskap
Organisera eller delta i en utbildning i entreprenörskap
Organisera eller delta i en utbildning som lär dig en konkret färdighet
Lär dig mer om ekonomiska rättigheter, sparande och skuldhantering
Lär dig mer om ekonomiska rättigheter, sparande och skuldhantering
Ta reda på vilka statliga program som finns som kan hjälpa människor som har det svårt
Stöd insamlingar till människor som har det svårt
Få mer kunskap!
Ingen kan göra allt, men alla kan göra något.
Välgörenhet vid födelsedagar
Handla fair trade
Handla från affärer som skänker till välgörenhet
Bli fadder
Diskutera fattigdom
Skänk till behövande

Engagera dig i en organisation som syftar till att sprida kunskap om orsakerna bakom fattigdom eller som på olika sätt arbetar med insatser för att minska fattigdomen i världen.
Köp Fairtrade-produkter och bidra till hållbar handel och att de som producerat det du köper får en schysst ersättning för sitt arbete.
Alla människor vet inte vilka möjligheter de har att få statlig hjälp när de har det svårt ekonomiskt. Ta reda på vilken statlig hjälp som finns till för att hjälpa människor i svåra situationer. Sprid kunskapen till alla du kan, så att de också kan sprida den vidare.
Fler entreprenörer kan bidra till att minska fattigdomen runt om i världen – det gör att fler kan få jobb och en inkomst, och bidrar på det sättet till att minska fattigdomen. Bjud in lokala entreprenörer till din skola för att hålla en utbildning!
Att lära dig en ny färdighet gör att du blir mer rustad för att ge dig ut på arbetsmarknaden och få ett arbete. Bjud in personer från olika yrkesområden till din klass – eller till och med någons föräldrar – till din skola och låt dem hålla en kurs.
Be din lärare att hålla en kurs om lagar och regler kring rätten till land och egendom, vilka lagar och regler som påverkar småföretag, ekonomi och mikrolån. Gör en personlig budget som gör att du får koll på hur mycket inkomster och utgifter du har.
Gör research om eller gå en kurs i privatekonomi. Kolla upp vad som gäller kring rättigheter till land och egendom, vilka lagar och regler som påverkar småföretag, ekonomi och mikrolån. Se till att ha en personlig budget som gör att du får koll på hur mycket inkomster och utgifter du har.
Alla människor vet inte vilka möjligheter de har att få statlig hjälp när de har det svårt ekonomiskt. Ta reda på vilken statlig hjälp som finns till för att hjälpa människor i svåra situationer. Sprid kunskapen till alla du kan, så att de också kan sprida den vidare.
Många organisationer har insamlingar för människor som har det svårt och tar emot donationer i form av kläder, mat och annat. Du har säkert något hemma som du kan bli av med – bidra med det du kan! Gå ihop med andra från din skola eller klass och gör en gemensam insamling.
Läs på om de utmaningar och framgångar som sker inom den globala fattigdomsbekämpningen. Visste du till exempel att fattigdomen i världen har mer än halverats sedan 1990? Desto mer vi vet och sprider ordet, desto större är chanserna att målet uppnås.
Det finns flera faktorer som leder till fattigdom, därför flera sätt att motverka fattigdom. Utbildning, sjukvård och tillgång till rent vatten är några av de faktorer som ger människor förutsättningar att styra sin framtid.
När du fyller år kan du uppmana släkt och vänner till att skänka pengar till en organisation du tycker om istället för att köpa födelsedagspresenter.
När du köper fair trade-produkter så bidrar du till hållbar handel och att de som tagit fram det du köper får en schysst ersättning för sitt arbete.
Köp kläder och andra produkter från affärer som skänker delar av sin vinst till välgörande ändamål.
Bli fadder till ett barn så att barnet kan få tillgång till mat, utbildning och sjukvård.
Skapa en diskussion om fattigdom genom att uppmärksamma ämnet i sociala medier.
Om du kan, ge något till människor som tigger på gatan. Ett äpple, något att dricka, lite växelpengar eller bara ett leende är bättre än inget.
"""

doc = nlp(text)

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.dep_, token.ent_type_)
print(doc)

# tr = TextRank()
# # add PyTextRank to the spaCy pipeline
# nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

# doc = nlp(text)
# print(doc)

# displacy.render(doc, style="ent")

