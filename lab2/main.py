print("Перша константа", False)

print(abs(-13.7), f"є рівним {abs(13.7)}")

A = True
print("Значить А=True" if A else "Значить А=False")

B = 0
try:
    print("Що буде якщо", 12/B, "?")
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")

with open("README.md", "r") as f:
    for line in f:
         print(line)

this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
         print("Це просто функція:", this_is_lambda)
         print("Це її виклик:", this_is_lambda('Андрій', 'Рубець'))
