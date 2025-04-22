import emoji
from random import shuffle #Função que as listas e as deixa embaralhadas.

print(emoji.emojize("      :alien_monster:SORTEIO 5S:alien_monster:\n-- :black_heart:Yasmin Novais Vieira:black_heart: --\n"))

nomes=["Ana Clara Grizotto Casagrande",
       "André Luís Sousa Dantas",
       "Antônio Carlos Rodrigues da Silva",
       "Emily Gabrielle Oliveira",
       "Enzo Gabriel Previtale Silva",
       "Julya Jacometti",
       "Ketlyn Lorayne Niza de Araújo",
       "Laura Vieira da Silva",
       "Layslla Eduarda Oreti dos Santos",
       "Letícia Alves Roth",
       "Luiza Santos Gonçalves",
       "Mariana Macena de Magalhães",
       "Rebeca Bugati Pizza",
       "Giovanna Marques",
       "Thainara Cristina Marques da Silva",
       "Yasmin Novas Vieira"]


tarefas=["Varrer chão",
         "Limpar as mesas",
         "Organizar fios dos computadores",
         "Limpar televisão e os monitores",
         "Monitorar atividades",
         "Verificar e organizar armários",
         "Verificar etiquetas",
         "Limpar cadeiras"]

shuffle(nomes)

for i in range(len(tarefas)):
    pessoa1 = nomes[2 * i]
    pessoa2 = nomes[2 * i + 1]
    tarefa = tarefas[i]

    if tarefa == "Varrer chão":
        print(emoji.emojize(f":broom:{tarefa}:broom:"))
        print(f"   - {pessoa1}")
        print(f"   - {pessoa2}\n")

    elif tarefa == "Limpar as mesas":
        print(emoji.emojize(f":sponge:{tarefa}:sponge:"))
        print(f"   - {pessoa1}")
        print(f"   - {pessoa2}\n")

    elif tarefa == "Organizar fios dos computadores":
        print(emoji.emojize(f":electric_plug:{tarefa}:electric_plug:"))
        print(f"   - {pessoa1}")
        print(f"   - {pessoa2}\n")

    elif tarefa == "Limpar televisão e os monitores":
        print(emoji.emojize(f":desktop_computer:{tarefa}:desktop_computer:"))
        print(f"   - {pessoa1}")
        print(f"   - {pessoa2}\n")

    elif tarefa == "Monitorar atividades":
        print(emoji.emojize(f":clipboard:{tarefa}:clipboard:"))
        print(f"   - {pessoa1}")
        print(f"   - {pessoa2}\n")

    elif tarefa == "Verificar e organizar armários":
        print(emoji.emojize(f":file_cabinet:{tarefa}:file_cabinet:"))
        print(f"   - {pessoa1}")
        print(f"   - {pessoa2}\n")

    elif tarefa == "Verificar etiquetas":
        print(emoji.emojize(f":label:{tarefa}:label:"))
        print(f"   - {pessoa1}")
        print(f"   - {pessoa2}\n")

    elif tarefa == "Limpar cadeiras":
        print(emoji.emojize(f":chair:{tarefa}:chair:"))
        print(f"   - {pessoa1}")
        print(f"   - {pessoa2}\n")

# 👾 == :alien_monster:
# 🖤 == :black_heart:
# 🧹 == :broom:
# 🔌 == :electric_plug:
# 🖥️ == :desktop_computer:
# 📋 == :clipboard:
# 🗄️ == :file_cabinet:
# 🏷️ == :label:
# 🪑 == :chair:
# 🧽 == :sponge:

# Emojis disponíveis: https://carpedm20.github.io/emoji/
