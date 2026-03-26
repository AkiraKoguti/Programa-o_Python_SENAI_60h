import statistics


empresa1 = [1000,6000,1200,8000,1400]

empresa2 = [5000,4000,3000,2000,7000]

empresa3 = [1200,1300,8000,3000,15000]

empresa4 = [1400,1750,2000,4500,5900]

def comparacao(empre1,empre2,empre3,empre4):
    print('Comparação de Média')
    med1 = [statistics.mean(empre1), 'Empresa 1']
    med2 = [statistics.mean(empre2), 'Empresa 2']
    med3 = [statistics.mean(empre3), 'Empresa 3']
    med4 = [statistics.mean(empre4), 'Empresa 4']
    print('Média empresa 1 =',med1[1])
    print('Média empresa 2 =',med2[1])
    print('Média empresa 3 =',med3[1])
    print('Média empresa 4 =',med4[1])
    medl = [med1,med2,med3,med4]
    print()

    print('Comparação de Mediana')
    mediana1 = [statistics.median(empre1), 'Empresa 1']
    mediana2 = [statistics.median(empre2), 'Empresa 2']
    mediana3 = [statistics.median(empre3), 'Empresa 3'] 
    mediana4 = [statistics.median(empre4), 'Empresa 4']
    print('Mediana empresa 1 =',mediana1[1])
    print('Mediana empresa 2 =',mediana2[1])
    print('Mediana empresa 3 =',mediana3[1])
    print('Mediana empresa 4 =',mediana4[1])
    medianal = [mediana1,mediana2,mediana3,mediana4]
    print()

    print('Comparação de Desvio')
    des1 = [round(statistics.stdev(empre1),2), 'Empresa 1']
    des2 = [round(statistics.stdev(empre2),2), 'Empresa 2']
    des3 = [round(statistics.stdev(empre3),2), 'Empresa 3']
    des4 = [round(statistics.stdev(empre4),2), 'Empresa 4']
    print('Desvio empresa 1 =',des1[1])
    print('Desvio empresa 2 =',des2[1])
    print('Desvio empresa 3 =',des3[1])
    print('Desvio empresa 4 =',des4[1])
    desl = [des1,des2,des3,des4]
    print()

    print('Melhor Média')
    print(max(medl))
    print()

    print('Melhor Mediana')
    print(max(medianal))
    print()

    print('Melhor Desvio')
    print(min(desl))


comparacao(empresa1,empresa2,empresa3,empresa4)