from markov import Markov

f = open('zaurgPosts.txt')

m = Markov(f)

print(m.generate_markov_text(400))
