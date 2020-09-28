dia = int(input())
mes = int(input())
    
if ((dia>=20 and mes==1) or (dia<=18 and mes==2)):
    print("signo zodiacal acuario")
elif ((dia>=19 and mes==2) or (dia<=20 and mes==3)):
    print("signo zodiacal piscis")
elif((dia>=21 and mes==3) or (dia<=19 and mes==4)):
    print("signo zodiacal aries")
elif((dia>=20 and mes==4) or (dia<=20 and mes==5)):
    print("signo zodiacal tauro")
elif((dia>=21 and mes==5) or (dia<=20 and mes==6)):
    print("signo zodiacal geminis")
elif((dia>=21 and mes==6) or (dia<=22 and mes==7)):
    print("signo zodiacal cancer")
elif((dia>=23 and mes==7) or (dia<=22 and mes==8)):
    print("signo zodiacal leo")
elif((dia>=23 and mes==8) or (dia<=22 and mes==9)):
    print("signo zodiacal virgo")
elif((dia>=23 and mes==9) or (dia<=22 and mes==10)):
    print("signo zodiacal libra")
elif((dia>=23 and mes==10) or (dia<=21 and mes==11)):
    print("signo zodiacal escorpio")
elif((dia>=22 and mes==11) or (dia<=21 and mes==12)):
    print("signo zodiacal sagitario")
else:
    print("signo zodiacal capricornio")