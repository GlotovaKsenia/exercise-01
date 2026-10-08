# bytecode_two_params.py
# Add-in: Bytecode vergleichen, wenn aus der Konstante 1.19 ein zweiter
# Parameter wird (siehe Kapitel 1, Bytecode-Beispiel).
import dis


def multiply(net, tax_rate):
    return net * tax_rate


dis.dis(multiply)

# ast_demo.py
# Add-in 1: den Syntaxbaum eines Ausdrucks ansehen.
import ast

tree = ast.parse("net_price * (1 + tax_rate)", mode="eval")
print(ast.dump(tree))
