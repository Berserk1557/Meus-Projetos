import math
pi = math.pi

# raio = diametro/2
# raio_2 = raio * raio
# raio_3 = raio * raio * raio

# diametro = circulo ao meio
# raio = metade do diametro
# π = 3,14(arredondado,π e infinito)

# formulas de π: 

# circunferencia = diametro * π(3,14)
# area do circulo = π * (raio * raio)
# volume da esfera = 4/3 * π * (raio * raio * raio)
# area da superficie da esfera = 4 * π * (raio * raio) 
# volume do cilindro = π * (raio * raio) * altura
print('____________________________________________________________')
print('************************************************************')

print('calcular a Circunferencia do Circulo - 1')
print('Calcular a Area do Circulo - 2')
print('Calcular o Volume da Esfera - 3')
print('Calcular a Area da Superficie da Esfera - 4')
print('Calcular o Volume do Cilindro - 5')
print(' ')

escolha = int(input('Qual Calculo Deseja Fazer? '))


if escolha == 1:
    print(' ')
    diametro = int(input('Diametro do Seu Circulo em Cm: '))
    print(' ')
    calculo_circunferencia = diametro * pi
    resCC = calculo_circunferencia
    resCC_arredondado= round(resCC,2)
    print(f'A Circunferencia do seu Circulo é de {resCC_arredondado}cm.')

if escolha == 2:
    print(' ')
    raio = int(input('Raio do Seu Circulo em cm: '))
    print(' ')
    raio_ao_quadrado = (raio * raio)
    resAC = pi * raio_ao_quadrado
    resAC_arredondado = round(resAC,2)
    print(f'A Area do seu Circulo é de {resAC_arredondado}cm.')

if escolha == 3:
    print(' ')
    raio = int(input('Raio da sua Esfera em cm: '))
    raio_ao_cubo = (raio * raio * raio)
    res_VE = 4/3 * pi * raio_ao_cubo
    res_VE_aredondado = round(res_VE,2)
    print(' ')
    print(f'O Volume da sua Esfera é de {res_VE_aredondado}cm³.')
    print(' ')
    print('Água - 1')
    print('Ferro - 2')
    print('Aluminio - 3')
    print('Aço - 4')
    print('Ferro Fundido - 5')
    print('Cobre - 6')
    print('Plastico - 7')
    print('Argila - 8')
    print('Madeira - 9 ')
    print('Borracha - 10')
    print(' ')
    escolha2 = int(input('Qual Material Voce Quer  Que Seja Feito o Calculo? '))
    if escolha2 == 1:
        calculo_agua = res_VE_aredondado / 1000
        calculo_agua_aredondado = round(calculo_agua,2)
        print(f'Sua Esfera Tem ou Suporta {calculo_agua_aredondado} Litros de Água.')
    if escolha2 == 2:
        print(' ')
        calculo_ferro = res_VE_aredondado * 7.87
        calculo_ferro_kg = calculo_ferro / 1000
        calculo_ferro_aredondado = round(calculo_ferro_kg,2)
        print(f'Sua Esfera Tem ou Suporta {calculo_ferro_aredondado}kg de Ferro.')
    if escolha2 == 3:
        print(' ')
        calculo_aluminio = res_VE_aredondado * 2.70
        calculo_aluminio_kg = calculo_aluminio / 1000
        calculo_aluminio_aredondado = round(calculo_aluminio_kg,2)
        print(f'Sua Esfera Tem ou Suporta {calculo_aluminio_aredondado}kg de Aluminio.')
    if escolha2 == 4:
        calculo_aco = res_VE_aredondado * 7.85
        calculo_aco_kg = calculo_aco / 1000
        calculo_aco_aredondado = round(calculo_aco_kg,2)
        print(f'Sua Esfera Tem ou Suporta {calculo_aco_aredondado}kg de Aço.')
    if escolha2 == 5:
        print(' ')
        print('Ferro fundido Branco - 1')
        print('Ferro fundido Cinzento - 2')
        print(' ')
        BC_or_CZ = int(input('Qual dos Tipos de Ferro Fundido? '))
        if BC_or_CZ == 1:
            print(' ')
            calculo_Ferro_F_BC = res_VE_aredondado * 7.50
            calculo_ferro_F_BC_kg = calculo_Ferro_F_BC / 1000
            calculo_ferro_F_BC_aredondado = round(calculo_ferro_F_BC_kg,2)
            print(f'Sua Esfera Tem ou Suporta {calculo_ferro_F_BC_aredondado}kg de Ferro Fundido Branco.')
        if BC_or_CZ == 2:
            print(' ')
            calculo_Ferro_F_CZ = res_VE_aredondado * 7.25
            calculo_ferro_F_CZ_kg = calculo_Ferro_F_CZ / 1000
            calculo_ferro_F_CZ_aredondado =round(calculo_ferro_F_CZ_kg,2)
            print(f'Sua Esfera Tem ou Suporta {calculo_ferro_F_CZ_aredondado}kg de Ferro Fundido Cinzento.')
        if BC_or_CZ > 2:
            print('Voce Digitou um Número No Qual Não Esta na Lista.')
        if BC_or_CZ < 1:
            print('Voce Digitou um Número No Qual Não Esta na Lista.')
    if escolha2 == 6:
        print(' ')
        calculo_cobre = res_VE_aredondado * 8.93
        calculo_cobre_kg = calculo_cobre / 1000
        calculo_cobre_aredondado = round(calculo_cobre_kg,2)
        print(f'Sua Esfera tem ou Suporta {calculo_cobre_aredondado}kg de Cobre.')
    if escolha2 == 7:
        print(' ')
        print('polietileno (PE) - 1')
        print('Politereftalato de etileno (PET) - 2')
        print('Policloreto de Vinila (PVC) - 3')
        print('Poliestireno (PS) - 4')
        print(' ')
        escolha_pst = int(input('Qual tipo de Plastico Quer Calcular? '))
        if escolha_pst == 1:
            print(' ')
            print('PEAD - 1')
            print('PEBD - 2')
            print(' ')
            escolha_PE = int(input('Qual Tipo de Polietileno? '))
            if escolha_PE == 1:
                print(' ')
                calculo_PEAD = res_VE_aredondado * 0.96
                calculo_PEAD_kg = calculo_PEAD / 1000
                calculo_PEAD_aredondado = round(calculo_PEAD_kg,2)
                print(f'Sua Esfera tem ou Suporta {calculo_PEAD_aredondado}kg de Polietileno de Alta Densidade(PEAD).')
            if escolha_PE == 2:
                print(' ')
                calculo_PEBD = res_VE_aredondado * 0.92
                calculo_PEBD_kg = calculo_PEBD / 1000
                calculo_PEBD_aredondado = round(calculo_PEBD_kg,2)
                print(f'Sua esfera  Tem ou Suporta {calculo_PEBD_aredondado}kg de Polietileno de Baixa Desidade(PEBE).')
            if escolha_PE > 2:
                print('Voce Digitou um Número No Qual Não Esta na Lista.')
            if escolha_PE < 1:
                print('Voce Digitou um Número No Qual Não Esta na Lista.')
        if escolha_pst == 2:
            print(' ')
            calculo_PET = res_VE_aredondado * 1.3
            calculo_PET_kg = calculo_PET / 1000
            calculo_PET_aredondado = round(calculo_PET_kg,2)
            print(f'O Sua Esfera Tem ou Suporta {calculo_PET_aredondado}kg de Politereftalato de etileno(PET).')
        if escolha_pst == 3:
            print(' ')
            calculo_PVC = res_VE_aredondado * 1.39
            calculo_PVC_kg = calculo_PVC / 1000
            calculo_PVC_aredondado = round(calculo_PVC_kg,2)
            print(f'Sua Esfera Tem ou Suporta {calculo_PVC_aredondado}kg de Policloreto de vinilo(PVC).')
        if escolha_pst == 4:
            print(' ')
            calculo_PS = res_VE_aredondado * 1.05
            calculo_PS_kg  = calculo_PS / 1000
            calculo_PS_aredondado = round(calculo_PS_kg,2)
            print(f'Sua Esfera Tem ou Suporta {calculo_PS_aredondado}kg de poliestireno(PS)')
        if escolha_pst > 4:
            print('Voce Digitou um Número No Qual Não Esta na Lista.')
        if escolha_pst < 1:
            print('Voce Digitou um Número No Qual Não Esta na Lista.')
    if escolha2 == 8:
        print(' ')
        calculo_argila = res_VE_aredondado * 1.7
        calculo_argila_kg = calculo_argila / 1000
        calculo_argila_aredondado = round(calculo_argila_kg,2)
        print(f'Sua Esfera Tem ou Suporta {calculo_argila_aredondado}kg de Argila')
    if escolha2 == 9:
        print(' ')
        print('Pinus - 1')
        print('Eucalipto - 2')
        print('Carvalho - 3')
        print(' ')
        madeiras = int(input('Qual tipo de Madeira? '))
        if madeiras == 1:
            print(' ')
            calculo_pinus = res_VE_aredondado * 0.60
            calculo_pinus_kg = calculo_pinus / 1000
            calculo_pinus_aredondado = round(calculo_pinus_kg,2)
            print(f'Sua Esfera Tem ou Possui {calculo_pinus_aredondado}kg de pinus')
        if madeiras == 2:
            print(' ')
            calculo_eucalipto = res_VE_aredondado * 0.75
            calculo_eucalipto_kg = calculo_eucalipto / 1000
            calculo_eucalipto_aredondado = round(calculo_eucalipto_kg,2)
            print(f'Sua Esfera Tem ou Suporta {calculo_eucalipto_aredondado}kg de Eucalipto')
        if madeiras == 3:
            print(' ')
            calculo_carvalho = res_VE_aredondado * 0.8
            calculo_carvalho_kg = calculo_carvalho / 1000
            calculo_carvalho_aredondado = round(calculo_carvalho_kg,2)
            print(f'Sua Esfera Tem ou Suporta {calculo_carvalho_aredondado}kg de Carvalho')
        if madeiras > 3:
            print('Voce Digitou um Número No Qual Não Esta na Lista.')
    if escolha2 == 10:
        print(' ')
        calculo_borracha = res_VE_aredondado * 1.5
        calculo_borracha_kg = calculo_borracha / 1000
        calculo_borracha_aredondado = round(calculo_borracha_kg,2)
        print(f'Sua Esfera Tem ou Suporta {calculo_borracha_aredondado}kg de Borracha')
    if escolha2 > 10:
        print('Voce Digitou um Número No Qual Não Esta na Lista.')
    if escolha2 <1:
        print('Voce Digitou um Número No Qual Não Esta na Lista.')

if escolha == 4:
    print(' ')
    raio = int(input('raio da sua esfera em cm: '))
    print(' ')
    raio_ao_quadrado = raio * raio
    res_SE = 4 * pi * raio_ao_quadrado
    res_SE_aredondado = round(res_SE,2)
    print(f'a superficie da sua esfera tem {res_SE_aredondado}cm².')

if escolha == 5:
    print(' ')
    raio = int(input('Raio do seu Cilindro em cm: '))
    print(' ')
    altura = int(input('Altura do seu Cilindro em cm: '))
    print(' ')
    raio_ao_quadrado = raio * raio
    res_VC = pi * raio_ao_quadrado * altura 
    res_VC_aredondado = round(res_VC,2)
    print(f'O Volume do Seu Cilindro é De {res_VC_aredondado}cm³.')
    print(' ')
    print('Água - 1')
    print('Ferro - 2')
    print('Aluminio - 3')
    print('Aço - 4')
    print('Ferro Fundido - 5')
    print('Cobre - 6')
    print('Plastico - 7')
    print('Argila - 8')
    print('Madeira - 9 ')
    print('Borracha - 10')
    print(' ')
    escolha2 = int(input('Qual Material Voce Quer  Que Seja Feito o Calculo? '))
    if escolha2 == 1:
        calculo_agua = res_VC_aredondado / 1000
        calculo_agua_aredondado = round(calculo_agua,2)
        print(f'Seu Cilindro Tem ou Suporta {calculo_agua_aredondado} Litros de Água.')
    if escolha2 == 2:
        print(' ')
        calculo_ferro = res_VC_aredondado * 7.87
        calculo_ferro_kg = calculo_ferro / 1000
        calculo_ferro_aredondado = round(calculo_ferro_kg,2)
        print(f'Seu Cilindro Tem ou Suporta {calculo_ferro_aredondado}kg de Ferro.')
    if escolha2 == 3:
        print(' ')
        calculo_aluminio = res_VC_aredondado * 2.70
        calculo_aluminio_kg = calculo_aluminio / 1000
        calculo_aluminio_aredondado = round(calculo_aluminio_kg,2)
        print(f'Seu Cilindro Tem ou Suporta {calculo_aluminio_aredondado}kg de Aluminio.')
    if escolha2 == 4:
        calculo_aco = res_VC_aredondado * 7.85
        calculo_aco_kg = calculo_aco / 1000
        calculo_aco_aredondado = round(calculo_aco_kg,2)
        print(f'Seu Cilindro Tem ou Suporta {calculo_aco_aredondado}kg de Aço.')
    if escolha2 == 5:
        print(' ')
        print('Ferro fundido Branco - 1')
        print('Ferro fundido Cinzento - 2')
        print(' ')
        BC_or_CZ = int(input('Qual dos Tipos de Ferro Fundido? '))
        if BC_or_CZ == 1:
            print(' ')
            calculo_Ferro_F_BC = res_VC_aredondado * 7.50
            calculo_ferro_F_BC_kg = calculo_Ferro_F_BC / 1000
            calculo_ferro_F_BC_aredondado = round(calculo_ferro_F_BC_kg,2)
            print(f'Seu Cilindro Tem ou Suporta {calculo_ferro_F_BC_aredondado}kg de Ferro Fundido Branco.')
        if BC_or_CZ == 2:
            print(' ')
            calculo_Ferro_F_CZ = res_VC_aredondado * 7.25
            calculo_ferro_F_CZ_kg = calculo_Ferro_F_CZ / 1000
            calculo_ferro_F_CZ_aredondado =round(calculo_ferro_F_CZ_kg,2)
            print(f'Seu Cilindro Tem ou Suporta {calculo_ferro_F_CZ_aredondado}kg de Ferro Fundido Cinzento.')
        if BC_or_CZ > 2:
            print('Voce Digitou um Número No Qual Não Esta na Lista.')
        if BC_or_CZ < 1:
            print('Voce Digitou um Número No Qual Não Esta na Lista.')
    if escolha2 == 6:
        print(' ')
        calculo_cobre = res_VC_aredondado * 8.93
        calculo_cobre_kg = calculo_cobre / 1000
        calculo_cobre_aredondado = round(calculo_cobre_kg,2)
        print(f'Seu Cilindro tem ou Suporta {calculo_cobre_aredondado}kg de Cobre.')
    if escolha2 == 7:
        print(' ')
        print('polietileno (PE) - 1')
        print('Politereftalato de etileno (PET) - 2')
        print('Policloreto de Vinila (PVC) - 3')
        print('Poliestireno (PS) - 4')
        print(' ')
        escolha_pst = int(input('Qual tipo de Plastico Quer Calcular? '))
        if escolha_pst == 1:
            print(' ')
            print('PEAD - 1')
            print('PEBD - 2')
            print(' ')
            escolha_PE = int(input('Qual Tipo de Polietileno? '))
            if escolha_PE == 1:
                print(' ')
                calculo_PEAD = res_VC_aredondado * 0.96
                calculo_PEAD_kg = calculo_PEAD / 1000
                calculo_PEAD_aredondado = round(calculo_PEAD_kg,2)
                print(f'Seu Cilindro tem ou Suporta {calculo_PEAD_aredondado}kg de Polietileno de Alta Densidade(PEAD).')
            if escolha_PE == 2:
                print(' ')
                calculo_PEBD = res_VC_aredondado * 0.92
                calculo_PEBD_kg = calculo_PEBD / 1000
                calculo_PEBD_aredondado = round(calculo_PEBD_kg,2)
                print(f'Seu Cilindro Tem ou Suporta {calculo_PEBD_aredondado}kg de Polietileno de Baixa Desidade(PEBE).')
            if escolha_PE > 2:
                print('Voce Digitou um Número No Qual Não Esta na Lista.')
            if escolha_PE < 1:
                print('Voce Digitou um Número No Qual Não Esta na Lista.')
        if escolha_pst == 2:
            print(' ')
            calculo_PET = res_VC_aredondado * 1.3
            calculo_PET_kg = calculo_PET / 1000
            calculo_PET_aredondado = round(calculo_PET_kg,2)
            print(f'O Seu Cilindro Tem ou Suporta {calculo_PET_aredondado}kg de Politereftalato de etileno(PET).')
        if escolha_pst == 3:
            print(' ')
            calculo_PVC = res_VC_aredondado * 1.39
            calculo_PVC_kg = calculo_PVC / 1000
            calculo_PVC_aredondado = round(calculo_PVC_kg,2)
            print(f'Seu Cilindro Tem ou Suporta {calculo_PVC_aredondado}kg de Policloreto de vinilo(PVC).')
        if escolha_pst == 4:
            print(' ')
            calculo_PS = res_VC_aredondado * 1.05
            calculo_PS_kg  = calculo_PS / 1000
            calculo_PS_aredondado = round(calculo_PS_kg,2)
            print(f'Seu Cilindro Tem ou Suporta {calculo_PS_aredondado}kg de poliestireno(PS)')
        if escolha_pst > 4:
            print('Voce Digitou um Número No Qual Não Esta na Lista.')
        if escolha_pst < 1:
            print('Voce Digitou um Número No Qual Não Esta na Lista.')
    if escolha2 == 8:
        print(' ')
        calculo_argila = res_VC_aredondado * 1.7
        calculo_argila_kg = calculo_argila / 1000
        calculo_argila_aredondado = round(calculo_argila_kg,2)
        print(f'Seu Cilindro Tem ou Suporta {calculo_argila_aredondado}kg de Argila')
    if escolha2 == 9:
        print(' ')
        print('Pinus - 1')
        print('Eucalipto - 2')
        print('Carvalho - 3')
        print(' ')
        madeiras = int(input('Qual tipo de Madeira? '))
        if madeiras == 1:
            print(' ')
            calculo_pinus = res_VC_aredondado * 0.60
            calculo_pinus_kg = calculo_pinus / 1000
            calculo_pinus_aredondado = round(calculo_pinus_kg,2)
            print(f'Seu Cilindro Tem ou Possui {calculo_pinus_aredondado}kg de pinus')
        if madeiras == 2:
            print(' ')
            calculo_eucalipto = res_VC_aredondado * 0.75
            calculo_eucalipto_kg = calculo_eucalipto / 1000
            calculo_eucalipto_aredondado = round(calculo_eucalipto_kg,2)
            print(f'Seu Cilindro Tem ou Suporta {calculo_eucalipto_aredondado}kg de Eucalipto')
        if madeiras == 3:
            print(' ')
            calculo_carvalho = res_VC_aredondado * 0.8
            calculo_carvalho_kg = calculo_carvalho / 1000
            calculo_carvalho_aredondado = round(calculo_carvalho_kg,2)
            print(f'Seu Cilindro Tem ou Suporta {calculo_carvalho_aredondado}kg de Carvalho')
        if madeiras > 3:
            print('Voce Digitou um Número No Qual Não Esta na Lista.')
    if escolha2 == 10:
        print(' ')
        calculo_borracha = res_VC_aredondado * 1.5
        calculo_borracha_kg = calculo_borracha / 1000
        calculo_borracha_aredondado = round(calculo_borracha_kg,2)
        print(f'Seu Cilindro Tem ou Suporta {calculo_borracha_aredondado}kg de Borracha')
    if escolha2 > 10:
        print('Voce Digitou um Número No Qual Não Esta na Lista.')
    if escolha2 <1:
        print('Voce Digitou um Número No Qual Não Esta na Lista.')
if escolha > 5:
    print('Voce Digitou um Número No Qual Não Esta na Lista.')
if escolha < 1:
    print('Voce Digitou um Número No Qual Não Esta na Lista.')

print(' ')
print('************************************************************')