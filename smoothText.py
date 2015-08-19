from markov import Markov_n2

f = open('poems.txt')

m = Markov_n2(f)

print(m.generate_markov_text(1000))
