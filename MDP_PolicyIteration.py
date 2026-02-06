#Initial
Fixed = 0
RBroken = 0
RVeryBroken = 0

#State
Fixed = 0.0
Broken = 0.0
VeryBroken = 0.0

#Action
Wait = 0.0
FixYourself = 0.0
Shop = 0.0
Shop2 = 0.0
Mantain= 0.0
NoMantain = 0.0
Ignore = 0.0

#Probabilities
Fix_B_FY = 0.6
Broken_B_FY = 0.3
VeryBroken_B_FY = 0.1

Fixed_B_S = 0.9
Broken_B_S = 0.1

Fix_B_W = 0.2
Broken_B_W = 0.8

VeryBroken_vb_w = 0.85
Fix_vb_w = 0.05
Broken_vb_w = 0.1

Fixed_vb_S2 = 0.8
Broken_vb_S2 = 0.2

Broken_F_M = 0.3
Fix_F_M = 0.7

Fix_F_NM = 0.5
Broken_F_NM = 0.4 
VeryBroken_F_NM = 0.1


State = {Fixed,Broken,VeryBroken}

Action_Fixed = {"Mantain": "Mantain","NoMantain": "NoMantain"}
Action_Broken = {"FixYourself": "FixYourself","Wait": "Wait","Shop": "Shop"}
Action_VeryBroken = {"Ignore": "Ignore","Shop": "Shop2"}


policy = {
    "Fixed": "Mantain",
    "Broken": "FixYourself",
    "VeryBroken": "Ignore"
}

##############################

while True:

    while True:
        #Fix
        if policy["Fixed"] == "Mantain":
            Fixed = 5 + 0.5*(Fix_F_M*Fixed + Broken_F_M*Broken)
        else:
            Fixed = 5 + 0.5*(Fix_F_NM*Fixed + Broken_F_NM*Broken + VeryBroken_F_NM*VeryBroken)

        #Broken
        
        if policy["Broken"]  == "FixYourself":
            Broken = -4 + 0.5*(Fix_B_FY*Fixed + Broken_B_FY*Broken + VeryBroken_B_FY*VeryBroken)
        elif policy["Broken"]  == "Wait":
            Broken = -4 + 0.5*(Fix_B_W*Fixed + Broken_B_W*Broken)
        else:  # "SendTechnician" o lo que sea tu tercera acción
            Broken = -4 + 0.5*(Fixed_B_S*Fixed + Broken_B_S*Broken)

            
        #Very Broken

        if policy["VeryBroken"]  == "Ignore":
            VeryBroken = -6 + 0.5*(Fix_vb_w*Fixed + Broken_vb_w*Broken + VeryBroken_vb_w*VeryBroken)
        else:  # "SendTechnician2" o la acción alternativa
            VeryBroken = -6 + 0.5*(Fixed_vb_S2*Fixed + Broken_vb_S2*Broken)
        

        print("Fixed: ", Fixed )
        print("Broken: " , Broken )
        print("VeryBroken: " ,VeryBroken )

        entrada = input("Ingresa 'salir' para salir o cualquier tecla para continuar: ")
        if entrada.lower() == "salir":
            break



    #####Evaluation of the Actions (Policy Iteration):

    ##Fixed:
    Mantain = (Fix_F_M*Fixed + Broken_F_M*Broken)
    NoMantain = (Fix_F_NM*Fixed + Broken_F_NM*Broken + VeryBroken_F_NM*VeryBroken)

    ##Broken
    FixYourself = (Fix_B_FY*Fixed+Broken_B_FY*Broken+VeryBroken_B_FY*VeryBroken)
    Wait = (Fix_B_W*Fixed+Broken_B_W*Broken)
    Shop = (Fixed_B_S*Fixed+Broken_B_S*Broken)

    ##VeryBroken

    Ignore = (Fix_vb_w*Fixed+Broken_vb_w*Broken+VeryBroken_vb_w*VeryBroken)
    Shop2 = (Fixed_vb_S2*Fixed + Broken_vb_S2*Broken)


    Action_Fixed = {"Mantain": Mantain,"NoMantain": NoMantain}
    Action_Broken = {"FixYourself": FixYourself,"Wait": Wait,"Shop": Shop}
    Action_VeryBroken = {"Ignore": Ignore,"Shop": Shop2}

    
    AF_print = max(Action_Fixed, key=Action_Fixed.get)
    AB_print = max(Action_Broken, key=Action_Broken.get)
    AVB_print = max(Action_VeryBroken, key=Action_VeryBroken.get)


    policy = {"Fixed":AF_print,"Broken":AB_print,"VeryBroken": AVB_print}

    print(" ")
    print("Nuevas acciones")
    print("Fixed: ", AF_print, " ", Action_Fixed)
    print("Broken: ", AB_print, " ", Action_Broken)
    print("Very Broken: ", AVB_print, " ", Action_VeryBroken)

    entrada = input("Escribe algo (o 'salir' para terminar): ")

    if entrada.lower() == "salir":
        break

    print("Programa terminado.")
