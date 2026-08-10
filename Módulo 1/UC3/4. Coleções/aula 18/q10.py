# 10. Ranking de vendas com múltiplas operações
# Uma loja registrou o nome e o total de vendas de 5 vendedores em duas listas paralelas. O aluno deve: (a) exibir o ranking completo; (b) encontrar o melhor vendedor pelo maior valor; (c) calcular a média de vendas da equipe; (d) exibir apenas os vendedores acima da média; (e) verificar se algum vendedor atingiu a meta de R$ 5.000 usando any(). Todo o processamento deve usar for, enumerate() e as funções max(), min(), sum() e len().

vendedores = ["Paulo", "Gabriel", "Luiza", "Fernando", "Pedro"]
faturamentos = [3200, 5500, 4300, 6200, 6000]

melhor_vendedor = ""
maior_faturamento = 0
acima_media = ""

print("VENDENDOR - FATURAMENTO")
for i in range(len(vendedores)):
    print(f"{vendedores[i]} - R$ {faturamentos[i]:,.2f}")

    if faturamentos[i] > maior_faturamento:
        maior_faturamento = faturamentos[i]
        melhor_vendedor = vendedores[i]

    if faturamentos[i] >= 5000:
        acima_media += f"{vendedores[i]} - R$ {faturamentos[i]:,.2f}\n"

media = sum(faturamentos)/len(faturamentos)

print(f"""
Média de faturamento: R$ {media:,.2f}

Melhor vendedor e seu faturamento:
{melhor_vendedor} - R$ {maior_faturamento:,.2f}

Vendedores acima da média (R$ 5000) e seus faturamentos:
{acima_media}
""")