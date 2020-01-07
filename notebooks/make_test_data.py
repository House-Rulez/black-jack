import csv
import random


def make_deck(hands):
  points = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
  cards = []
  for point in points:
    for _ in range(4):
      if point not in hands:
        cards.append(point)
      else:
        hands.remove(point)

  return cards


def make_deal(cards=[]):
  if cards:
    return cards

  for _ in range(4):
    cards.append(random.randint(2, 11))

  return cards


def make_file(contents, filename):

  with open(filename, mode="w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    if filename == 'notebooks/deck.csv':
      csv_writer.writerow(['Points'])
    elif filename == 'notebooks/hand.csv':
      csv_writer.writerow(['Points'])

    for content in contents:
      csv_writer.writerow([str(content)])


if __name__ == "__main__":
  cards = make_deal([2, 8, 10, 3])
  hand = cards[:2]
  deck = make_deck(cards)
  make_file(hand, 'notebooks/hand.csv')
  make_file(deck, 'notebooks/deck.csv')
