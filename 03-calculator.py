{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Levimelodev/portfolio/blob/main/03-calculator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true
        },
        "id": "8pwh4vk4qBhH"
      },
      "outputs": [],
      "source": [
        "while True:\n",
        "\n",
        "  print(\"==CALCULADORA==\\n\")\n",
        "  opcao = int(input(\"Bem vindo a calculadora, por favor, digite a operação que deseja realizar:\\n1 - Soma\\n2 - Subtração\\n3 - Multiplicação\\n4 - Divisão\\n5 - Encerrar programa\\nSua opção: \"))\n",
        "\n",
        "#Soma\n",
        "  if opcao == 1:\n",
        "   total = 0\n",
        "   entrada = input(\"Digite os números separados por >> + <<\\n\")\n",
        "   soma = entrada.split(\"+\")\n",
        "   for item in soma:\n",
        "    total = total + int(item)\n",
        "   print(f\"O resultado foi: \\n>>> {total} <<<\\n\")\n",
        "\n",
        "   opcao = 0\n",
        "   opcao = input(\"O que deseja fazer agora?\\n1 - Soma\\n2 - Subtração\\n3 - Multiplicação\\n4 - Divisão\\n5 - Encerrar programa\\nSua resposta:\")\n",
        "\n",
        "#Subtração\n",
        "  if opcao == 2:\n",
        "   entrada = input(\"Digite os números separados por >> - <<\\n\")\n",
        "   numeros = entrada.split(\"-\")\n",
        "\n",
        "   total = int(numeros[0])\n",
        "\n",
        "   for item in numeros[1:]:\n",
        "     total = total - int(item)\n",
        "\n",
        "   print(f\"O resultado foi: \\n>>> {total} <<<\\n\")\n",
        "\n",
        "   opcao = input(\"O que deseja fazer agora?\\n1 - Soma\\n2 - Subtração\\n3 - Multiplicação\\n4 - Divisão\\n5 - Encerrar programa\\nSua resposta:\")\n",
        "\n",
        "#Multiplicação\n",
        "  if opcao == 3:\n",
        "   entrada = input(\"Digite os números separados por >> * <<\\n\")\n",
        "   numeros = entrada.split(\"*\")\n",
        "\n",
        "   total = int(numeros[0])\n",
        "   for item in numeros[1:]:\n",
        "    total = total * int(item)\n",
        "   print(f\"O resultado foi: \\n>>> {total} <<<\\n\")\n",
        "\n",
        "#Divisão\n",
        "  if opcao == 4:\n",
        "   entrada = input(\"Digite os números separados por >> / <<\\n\")\n",
        "   numeros = entrada.split(\"/\")\n",
        "\n",
        "   total = int(numeros[0])\n",
        "   for item in numeros[1:]:\n",
        "    total = total / int(item)\n",
        "   print(f\"O resultado foi: \\n>>> {total} <<<\\n\")\n",
        "\n",
        "#Encerramento\n",
        "  if opcao == 5:\n",
        "   print(\"Programa encerrado.\")\n",
        "   break"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNqkA4IuNIfDovZkttbWcCG",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}