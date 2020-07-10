n = int(input())
cards = list(map(int, input().split()))
cards = sorted(cards, reverse=True)

alice = 0
bob = 0

for i, card in enumerate(cards):
    if i % 2 == 0:
        alice += card
    else:
        bob += card

print(alice - bob)
