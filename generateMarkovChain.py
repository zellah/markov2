from markov import Markov

f = open('poems.txt')

m = Markov(f)

print(m.generate_markov_text(500))
