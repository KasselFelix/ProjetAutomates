from automate import *

#Determinisation
print("Pour tester la fonction determinisation")

st0 = State(0,True,False)
st1 = State(1,False,False)
st2 = State(2,False,True)

t0 = Transition(st0,"a",st0)
t1 = Transition(st0,"b",st1)
t2 = Transition(st1,"a",st2)
t3 = Transition(st1,"b",st2)
t4 = Transition(st2,"a",st0)
t5 = Transition(st2,"b",st1)

print("L automate auto\n")


auto = Automate([t1,t2,t3,t4,t5,t5])
print (auto)
auto.show("Auto")

print("Automate autoDeterminisation resultant de la determinisation\n")

autoDeterminisation= Automate.determinisation(auto)
print(autoDeterminisation)
autoDeterminisation.show("AutoDeterminisation")



# Intersection
print("Pour tester la fonction intersection")

st0a = State(0,True,False)
st1a = State(1,False,False)
st2a = State(2,False,True)

t0a = Transition(st0a,"a",st0a)
t1a = Transition(st0a,"b",st1a)
t2a = Transition(st1a,"b",st1a)
t3a = Transition(st1a,"a",st2a)
t4a = Transition(st2a,"a",st2a)
t5a = Transition(st2a,"b",st2a)

print("L automate autoInterA\n")
autoInterA = Automate([t0a,t1a,t2a,t3a,t4a,t5a])
print(autoInterA)
autoInterA.show("AutoInterA")


st0b = State(0,True,False)
st1b = State(1,False,False)
st2b = State(2,False,True)

t0b = Transition(st0b,"a",st0b)
t1b = Transition(st0b,"b",st0b)
t2b = Transition(st0b,"a",st1b)
t3b = Transition(st1b,"b",st2b)
t4b = Transition(st2b,"a",st2b)
t5b = Transition(st2b,"b",st2b)

print("L automate autoInterB\n")
autoInterB = Automate([t0b,t1b,t2b,t3b,t4b,t5b]) 
print(autoInterB)
autoInterB.show("AutoInterB")


print("Automate autoInterAB resultant de l intersection de l autoInterA et de l autoInterB\n")
autoInterAB = Automate.intersection(autoInterA,autoInterB)
print(autoInterAB)
autoInterAB.show("AutoInterAB") 






# Union
print("Pour tester la fonction union")

st0a = State(0,True,False)
st1a = State(1,False,False)
st2a = State(2,False,True)

t0a = Transition(st0a,"a",st0a)
t1a = Transition(st0a,"b",st1a)
t2a = Transition(st1a,"b",st1a)
t3a = Transition(st1a,"a",st2a)
t4a = Transition(st2a,"a",st2a)
t5a = Transition(st2a,"b",st2a)


print("AutoUnionA\n")
autoUnionA = Automate([t0a,t1a,t2a,t3a,t4a,t5a])
print(autoUnionA)
autoUnionA.show("AutoUnionA")

st0b = State(0,True,False)
st1b = State(1,False,False)
st2b = State(2,False,True)

t0b = Transition(st0b,"a",st0b)
t1b = Transition(st0b,"b",st0b)
t2b = Transition(st0b,"a",st1b)
t3b = Transition(st1b,"b",st2b)
t4b = Transition(st2b,"a",st2b)
t5b = Transition(st2b,"b",st2b)

print("AutoUnionB\n")
autoUnionB = Automate([t0b,t1b,t2b,t3b,t4b,t5b])
print(autoUnionB)
autoUnionB.show("AutoUnionB")

autoUnionAB = Automate.union(autoUnionA,autoUnionB)
print("L automate autoUnion resultant de l union entre autoUnionA et autoUnionB\n")
print(autoUnionAB)
autoUnionAB.show("AutoUnionAB") 




# Concatenation
print("Pour tester la fonction concatenation")

st0a = State(0,True,False)
st1a = State(1,False,False)
st2a = State(2,False,True)

t0a = Transition(st0a,"a",st0a)
t1a = Transition(st0a,"b",st1a)
t2a = Transition(st1a,"b",st1a)
t3a = Transition(st1a,"a",st2a)
t4a = Transition(st2a,"a",st2a)
t5a = Transition(st2a,"b",st2a)


print("AutoConcatenationA\n")
autoConcatenationA= Automate([t0a,t1a,t2a,t3a,t4a,t5a])
print(autoConcatenationA)
autoConcatenationA.show("AutoConcatenationA")

st0b = State(0,True,False)
st1b = State(1,False,False)
st2b = State(2,False,True)

t0b = Transition(st0b,"a",st0b)
t1b = Transition(st0b,"b",st0b)
t2b = Transition(st0b,"a",st1b)
t3b = Transition(st1b,"b",st2b)
t4b = Transition(st2b,"a",st2b)
t5b = Transition(st2b,"b",st2b)

print("AutoConcatenationB\n")
autoConcatenationB= Automate([t0b,t1b,t2b,t3b,t4b,t5b])
print(autoUnionB)
autoConcatenationB.show("AutoConcatenationB")

autoConcatenationAB = Automate.concatenation(autoConcatenationA,autoConcatenationB)
print("L automate autoConcatenationAB resultant de la concatenation entre autoConcatenationA et autoConcatenationB\n")
print(autoConcatenationAB)
autoConcatenationAB.show("AutoConcatenationAB")
