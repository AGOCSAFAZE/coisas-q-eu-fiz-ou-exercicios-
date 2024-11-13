populacao_a = float(input("Digite a populacao do pais A: "))
taxa_crescimento_a = float(input("Digite a taxa de crescimento da populacao do pais A: "))

populacao_b = int(input("Digite a populacao do pais B: "))
taxa_crescimento_b = float(input("Digite a taxa de crescimento da populacao do país B: "))

anos = 0

while populacao_a <= populacao_b:
    populacao_a += populacao_a * taxa_crescimento_a
    populacao_b += populacao_b * taxa_crescimento_b
    anos += 1

print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")