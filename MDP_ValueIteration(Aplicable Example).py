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

####################


State = {Fixed,Broken,VeryBroken}

Action_Fixed = {"Mantain": Mantain,"NoMantain": NoMantain}
Action_Broken = {"FixYourself": FixYourself,"Wait": Wait,"Shop": Shop}
Action_VeryBroken = {"Ignore": Ignore,"Shop": Shop2}

####################


##Fixed:
def ValueIteration_Fixed(FixedF, BrokenF, VeryBrokenF):
    Mantain = (Fix_F_M*FixedF + Broken_F_M*BrokenF)
    NoMantain = (Fix_F_NM*FixedF + Broken_F_NM*BrokenF + VeryBroken_F_NM*VeryBrokenF)
    Action_Fixed = {"Mantain": Mantain,"NoMantain": NoMantain}
    best_action_Fixed = max(Action_Fixed, key=Action_Fixed.get)
    return best_action_Fixed

##Broken
def ValueIteration_Broken(FixedB, BrokenB, VeryBrokenB):
    FixYourself = (Fix_B_FY*FixedB+Broken_B_FY*BrokenB+VeryBroken_B_FY*VeryBrokenB)
    Wait = (Fix_B_W*FixedB+Broken_B_W*BrokenB)
    Shop = (Fixed_B_S*FixedB+Broken_B_S*BrokenB)
    Action_Broken = {"FixYourself": FixYourself,"Wait": Wait,"Shop": Shop}

    best_action_broken = max(Action_Broken, key=Action_Broken.get)
    return best_action_broken

##VeryBroken
def ValueIteration_VeryBroken(FixedV, BrokenV, VeryBrokenV):
    Ignore = (Fix_vb_w*FixedV+Broken_vb_w*BrokenV+VeryBroken_vb_w*VeryBrokenV)
    Shop2 = (Fixed_vb_S2*FixedV + Broken_vb_S2*BrokenV)
    Action_VeryBroken = {"Ignore": Ignore,"Shop": Shop2}
    best_action_vbroken = max(Action_VeryBroken, key=Action_VeryBroken.get)
    return best_action_vbroken
    

##############################


while True:
    #Fix
    

    if ValueIteration_Fixed(Fixed,Broken,VeryBroken) == "Mantain":
        Fixed = 5 + 0.5*(Fix_F_M*Fixed + Broken_F_M*Broken)
    else:
        Fixed = 5 + 0.5*(Fix_F_NM*Fixed + Broken_F_NM*Broken + VeryBroken_F_NM*VeryBroken)

    #Broken
    
    if ValueIteration_Broken(Fixed,Broken,VeryBroken) == "FixYourself":
        Broken = -4 + 0.5*(Fix_B_FY*Fixed + Broken_B_FY*Broken + VeryBroken_B_FY*VeryBroken)
    elif ValueIteration_Broken(Fixed,Broken,VeryBroken) == "Wait":
        Broken = -4 + 0.5*(Fix_B_W*Fixed + Broken_B_W*Broken)
    else:  # "SendTechnician" 
        Broken = -4 + 0.5*(Fixed_B_S*Fixed + Broken_B_S*Broken)

        
    #Very Broken

    if ValueIteration_VeryBroken(Fixed,Broken,VeryBroken) == "Ignore":
        VeryBroken = -6 + 0.5*(Fix_vb_w*Fixed + Broken_vb_w*Broken + VeryBroken_vb_w*VeryBroken)
    else:  # "SendTechnician2" o la acción alternativa
        VeryBroken = -6 + 0.5*(Fixed_vb_S2*Fixed + Broken_vb_S2*Broken)



    #####Evaluation of the Actions (Policy Iteration):


    print("Fixed: ", Fixed )
    print("Broken: " , Broken )
    print("VeryBroken: " ,VeryBroken )


    print(" ")
    print("Nuevas acciones")
    print("Fixed: ", ValueIteration_Fixed(Fixed,Broken,VeryBroken))
    print("Broken: ", ValueIteration_Broken(Fixed,Broken,VeryBroken))
    print("Very Broken: ", ValueIteration_VeryBroken(Fixed,Broken,VeryBroken))

    entrada = input("Escribe algo (o 'salir' para terminar): ")

    if entrada.lower() == "salir":
        break

print("Programa terminado.")
