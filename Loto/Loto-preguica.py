import random

print("Bem-vindo ao programa da Loteria da preguiça! \nEscolha uma opção:")
print("1.Mega-sena  2.Lotofácil  3.Quina  4.Lotomania  5.Timemania  6.Dupla Sena  7.Dia de Sorte  8.Sair")
resposta = int(input())

if resposta == 1:
    sena = random.sample(range(1,61),6)
    sena.sort()
    print("Seus números da sorte são:\n",sena)
    
elif resposta == 2:
    lotofacil = random.sample(range(1,26),15)
    lotofacil.sort()
    print("Seus números da sorte são:\n",lotofacil)

elif resposta == 3:
    quina = random.sample(range(1,81),5)
    quina.sort()
    print("Seus números da sorte são:\n",quina)
    
elif resposta == 4:
    lotomania = random.sample(range(0,100),50)
    lotomania.sort()
    print("Seus números da sorte são:\n",lotomania)

elif resposta == 5:
    numTimemania = random.sample(range(1,81),10)
    numTimemania.sort()
    times = {(1,"ABC-RN"),(2,"América-MG"),(3,"América-RJ"),(4,"América-RN"),(5,"Americano-RJ"),(6,"Atlético-GO"),
         (7,"Atlético-MG"),(8,"Atlético-PR"),(9,"Avaí-Sc"),(10,"Bahia-BA"),(11,"Bangu-RJ"),(12,"Barueri-SP"),
         (13,"Botafogo-PB"),(14,"Botafogo-RJ"),(15,"Bragantino-SP"),(16,"Brasiliense-DF"),(17,"Ceará-CE"),
         (18,"Corinthias-SP"),(19,"Coritiba-PR"),(20,"CRB-AL"),(21,"Criciúma-SC"),(22,"Cruzeiro-MG"),(23,"CSA-AL"),
         (24,"Desportiva-ES"),(25,"Figueirense-SC"),(26,"Flamengo-RJ"),(27,"Fluminense-RJ"),(28,"Fortaleza-CE"),
         (29,"Gama-DF"),(30,"Goiás-GO"),(31,"Grêmio-RS"),(32,"Guarani-SP"),(33,"Inter de Limeira-SP"),(34,"Internacional"),
         (35,"Ipatinga-MG"),(36,"Ituano-SP"),(37,"JI-Paraná-RO"),(38,"Joinville-SC"),(39,"Juventude-RS"),(40,"Juventus-SP"),
         (41,"Londrina-PR"),(42,"Marília-SP"),(43,"Mixto-MT"),(44,"Moto Clube-MA"),(45,"Nacional-AM"),(46,"Náutico-PE"),
         (47,"Olaria-RJ"),(48,"Operário-MS"),(49,"Palmas-TO"),(50,"Palmeiras-SP"),(51,"Paraná-SP"),(52,"Paulista-SP"),
         (53,"Paysandu-Pa"),(54,"Ponte Preta-SP"),(55,"Portuguesa de desportos-SP"),(56,"Remo-PA"),(57,"Rio Branco-AC"),
         (58,"Rio Branco-ES"),(59,"River-Pi"),(60,"Roraima-RR"),(61,"Sampaio Corrêa-MA"),(62,"Santa Cruz-PE"),
         (63,"Santo André-SP"),(64,"Santos-SP"),(65,"São Caetano-SP"),(66,"São Paulo-SP"),(67,"São Raimundo-AM"),
         (68,"Sergipe-SE"),(69,"Sport-PE"),(70,"Treze-PB"),(71,"Tuna Luso-PA"),(72,"Uberlândia-MG"),(73,"União Barbarense-SP"),
         (74,"União São João-SP"),(75,"Vasco-RJ"),(76,"Vila Nova-GO"),(77,"Villa Nova-MG"),(78,"Vitória-BA"),
         (79,"XV de Piracicaba-SP"),(80,"Ypiranga-AP")}
    timeTimemania = random.sample((times),1)
    print("Seus números da sorte são:\n",numTimemania)
    print(timeTimemania)

elif resposta == 6:
    duplaSena = random.sample(range(1,51),6)
    duplaSena.sort()
    print("Seus números da sorte são:\n",duplaSena)
    
elif resposta == 7:
    diaDeSorte = random.sample(range(1,32),7)
    diaDeSorte.sort()
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    mesdiaDeSorte = random.sample((meses),1)
    print("Seus números da sorte são:\n",diaDeSorte)
    print(mesdiaDeSorte)

else:
    print("Boa Sorte e até logo!")