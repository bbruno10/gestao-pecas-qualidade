"""
Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento
Disciplina: Algoritmos e Lógica de Programação - UNIFECAF
Autor: Bruno Brandao

Sistema de controle de produção e qualidade de peças industriais.
Critérios de aprovação:
  - Peso entre 95g e 105g
  - Cor azul ou verde
  - Comprimento entre 10cm e 20cm
"""

# ─── Constantes 
PESO_MIN = 95.0
PESO_MAX = 105.0
CORES_ACEITAS = ("azul", "verde")
COMPRIMENTO_MIN = 10.0
COMPRIMENTO_MAX = 20.0
CAPACIDADE_CAIXA = 10

# ─── Estruturas de dados 
pecas_aprovadas = []
pecas_reprovadas = []  
caixas_fechadas = []   
caixa_atual = []       


# ─── Funções de validação 

def validar_peca(peso, cor, comprimento):
    
    motivos = []

    if not (PESO_MIN <= peso <= PESO_MAX):
        motivos.append(f"Peso fora do padrão ({peso}g) — aceito: {PESO_MIN}g a {PESO_MAX}g")

    if cor.lower() not in CORES_ACEITAS:
        motivos.append(f"Cor inválida ('{cor}') — aceitas: {', '.join(CORES_ACEITAS)}")

    if not (COMPRIMENTO_MIN <= comprimento <= COMPRIMENTO_MAX):
        motivos.append(f"Comprimento fora do padrão ({comprimento}cm) — aceito: {COMPRIMENTO_MIN}cm a {COMPRIMENTO_MAX}cm")

    aprovada = len(motivos) == 0
    return aprovada, motivos


def armazenar_peca_aprovada(peca):
    # Adiciona a peça na caixa atual e fecha se atingir capacidade.
    global caixa_atual
    caixa_atual.append(peca)

    if len(caixa_atual) >= CAPACIDADE_CAIXA:
        caixas_fechadas.append(list(caixa_atual))
        numero_caixa = len(caixas_fechadas)
        print(f"\n Caixa #{numero_caixa} fechada com {CAPACIDADE_CAIXA} peças! Nova caixa iniciada.")
        caixa_atual = []


# ─── Funções do menu 

def cadastrar_peca():
    # Opção 1 — Cadastrar nova peça.
    print("\n" + "=" * 50)
    print("  CADASTRAR NOVA PEÇA")
    print("=" * 50)

    # Ler ID
    id_peca = input("ID da peça: ").strip()
    if not id_peca:
        print("ID não pode ser vazio.")
        return

    # Verificar ID duplicado
    for p in pecas_aprovadas:
        if p["id"] == id_peca:
            print(f"Já existe uma peça aprovada com o ID '{id_peca}'.")
            return
    for item in pecas_reprovadas:
        if item["peca"]["id"] == id_peca:
            print(f"Já existe uma peça reprovada com o ID '{id_peca}'.")
            return

    # Ler peso
    try:
        peso = float(input("Peso (g): "))
    except ValueError:
        print("Peso inválido. Use um valor numérico.")
        return

    # Ler cor
    cor = input("Cor: ").strip()
    if not cor:
        print("Cor não pode ser vazia.")
        return

    # Ler comprimento
    try:
        comprimento = float(input("Comprimento (cm): "))
    except ValueError:
        print("Comprimento inválido. Use um valor numérico.")
        return

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
    }

    aprovada, motivos = validar_peca(peso, cor, comprimento)

    if aprovada:
        pecas_aprovadas.append(peca)
        armazenar_peca_aprovada(peca)
        print(f"\n Peça '{id_peca}' APROVADA e armazenada na caixa atual.")
    else:
        pecas_reprovadas.append({"peca": peca, "motivos": motivos})
        print(f"\n Peça '{id_peca}' REPROVADA.")
        print("   Motivos:")
        for m in motivos:
            print(f"   • {m}")


def listar_pecas():
    # Opção 2 — Listar peças aprovadas e reprovadas.
    print("\n" + "=" * 50)
    print("  PEÇAS APROVADAS")
    print("=" * 50)

    if pecas_aprovadas:
        print(f"  Total: {len(pecas_aprovadas)} peça(s)\n")
        print(f"{'ID':<12} {'Peso (g)':<10} {'Cor':<10} {'Comp. (cm)':<12}")
        print("-" * 44)
        for p in pecas_aprovadas:
            print(f"{p['id']:<12} {p['peso']:<10.1f} {p['cor']:<10} {p['comprimento']:<12.1f}")
    else:
        print("Nenhuma peça aprovada até o momento.")

    print("\n" + "=" * 50)
    print("  PEÇAS REPROVADAS")
    print("=" * 50)

    if pecas_reprovadas:
        print(f"  Total: {len(pecas_reprovadas)} peça(s)\n")
        for item in pecas_reprovadas:
            p = item["peca"]
            print(f"\nID: {p['id']}  |  Peso: {p['peso']}g  |  Cor: {p['cor']}  |  Comp.: {p['comprimento']}cm")
            print("  Motivos da reprovação:")
            for m in item["motivos"]:
                print(f"    • {m}")
    else:
        print("Nenhuma peça reprovada até o momento.")


def remover_peca():
    # Opção 3 — Remover peça cadastrada pelo ID.
    print("\n" + "=" * 50)
    print("  REMOVER PEÇA CADASTRADA")
    print("=" * 50)

    id_peca = input("ID da peça a remover: ").strip()
    if not id_peca:
        print("ID não pode ser vazio.")
        return

    # Procurar nas aprovadas
    for i, p in enumerate(pecas_aprovadas):
        if p["id"] == id_peca:
            pecas_aprovadas.pop(i)
            # Remover também da caixa atual (se ainda estiver lá)
            for j, pc in enumerate(caixa_atual):
                if pc["id"] == id_peca:
                    caixa_atual.pop(j)
                    break
            print(f"Peça aprovada '{id_peca}' removida com sucesso.")
            return

    # Procurar nas reprovadas
    for i, item in enumerate(pecas_reprovadas):
        if item["peca"]["id"] == id_peca:
            pecas_reprovadas.pop(i)
            print(f"Peça reprovada '{id_peca}' removida com sucesso.")
            return

    print(f"Peça com ID '{id_peca}' não encontrada.")


def listar_caixas_fechadas():
    # Opção 4 — Listar caixas fechadas.
    
    print("\n" + "=" * 50)
    print("  CAIXAS FECHADAS")
    print("=" * 50)

    if caixas_fechadas:
        for i, caixa in enumerate(caixas_fechadas, start=1):
            print(f"\n Caixa #{i} — {len(caixa)} peças:")
            print(f"  {'ID':<12} {'Peso (g)':<10} {'Cor':<10} {'Comp. (cm)':<12}")
            print(f"  {'-' * 44}")
            for p in caixa:
                print(f"  {p['id']:<12} {p['peso']:<10.1f} {p['cor']:<10} {p['comprimento']:<12.1f}")
    else:
        print("Nenhuma caixa fechada até o momento.")

    # Info da caixa atual
    print(f"\n Caixa atual (aberta): {len(caixa_atual)}/{CAPACIDADE_CAIXA} peças")


def gerar_relatorio():
    # Opção 5 — Gerar relatório final consolidado.
    
    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)
    total_pecas = total_aprovadas + total_reprovadas
    qtd_caixas_fechadas = len(caixas_fechadas)
    pecas_caixa_atual = len(caixa_atual)

    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL CONSOLIDADO")
    print("=" * 60)

    print(f"\n  Total de peças cadastradas:    {total_pecas}")
    print(f"  Total de peças APROVADAS:      {total_aprovadas}")
    print(f"  Total de peças REPROVADAS:     {total_reprovadas}")

    if total_pecas > 0:
        taxa = (total_aprovadas / total_pecas) * 100
        print(f"  Taxa de aprovação:             {taxa:.1f}%")

    print(f"\n  Caixas fechadas:               {qtd_caixas_fechadas}")
    print(f"  Peças na caixa atual (aberta): {pecas_caixa_atual}/{CAPACIDADE_CAIXA}")

    if pecas_reprovadas:
        print("\n  ─── Detalhamento das reprovações ───")
        for item in pecas_reprovadas:
            p = item["peca"]
            print(f"\n  ID: {p['id']}  |  Peso: {p['peso']}g  |  Cor: {p['cor']}  |  Comp.: {p['comprimento']}cm")
            for m in item["motivos"]:
                print(f"    • {m}")

    print("\n" + "=" * 60)


# ─── Menu principal ───────────────────────────────────────────

def exibir_menu():
    """ Exibe o menu interativo e retorna a opção escolhida. """
    print("\n" + "=" * 50)
    print("GESTÃO DE PEÇAS — CONTROLE DE QUALIDADE")
    print("=" * 50)
    print("  1. Cadastrar nova peça")
    print("  2. Listar peças aprovadas/reprovadas")
    print("  3. Remover peça cadastrada")
    print("  4. Listar caixas fechadas")
    print("  5. Gerar relatório final")
    print("  0. Sair")
    print("-" * 50)
    return input("  Escolha uma opção: ").strip()


def main():
    """ Loop principal do programa. """
    print("\n Bem-vindo ao Sistema de Gestão de Peças Industriais!")
    print("   Controle de qualidade e armazenamento automatizado.\n")

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas_fechadas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("\n Encerrando o sistema. Até logo!\n")
            break
        else:
            print("\n Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
