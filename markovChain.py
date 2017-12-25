import random
import cPickle as pickle

class MarkovChain(object):
    def __init__(self, inputString): #CONSTRUCTOR FOR THE MARKOV CHAIN OBJECT
           
           self.inputString = inputString 
           self.states = {}    #STORES THE PROBABILITES OF EACH TRANSITION, PRINT THE OBJECT TO SEE PROBABILITIES AND TRANSITIONS
    
    def __str__(self):    #JUST USED FOR WHEN SOMEONE TRIES TO PRINT THE OBJECT
        for f in self.states:
            print f, self.states[f]
            
    def createSequence(self, length, start1, start2):    #CREATES A VARIABLE LENGTH SEQUENCE BASED UPON A TRAINED MARKOV CHAIN
        string = start1 + " " + start2 +" "
        for f in range(length):
            string += self.transition(start1,start2)+" "
            start1 = start2
            start2 = self.transition(start1,start2)
            
        return string
    
    def transition(self, a, b): #RANDOMLY USES TRAINED MARKOV CHAIN TO TRANSITION FROM A GIVEN STRING TO ANOTHER GIVEN STRING, BOTH MUST BE PRESENT IN THE MARKOV CHAIN
            gen = random.random()
            tot = 0.0
            for f in self.states:
                if f[0] == a and f[1] == b:
                    if self.states[f]+tot > gen:
                        return f[2]
                    else:
                        tot += self.states[f]
            return random.choice(self.states.keys())[2]
    def train(self):
        string = self.inputString.split(" ")

        for f in range(0,len(string)-2):
            a = string[f]
            b = string[f+1]
            c = string[f+2]
            if (a,b,c) not in self.states:
                self.states[(a,b,c)] = 1
            else:
                self.states[(a,b,c)] += 1

        done = {}
        for f in self.states:
            if (f[0],f[1]) not in done:
                done[(f[0],f[1])] = self.states[f]
            else:
                done[(f[0],f[1])] += self.states[f]

        for g in self.states:
            if done[(g[0],g[1])] != 0:
                self.states[g] = float(self.states[g])/float(done[g[0],g[1]])

        
if __name__ == "__main__":
    with open('HHGG.txt', 'r') as myfile:
        data = myfile.read()
    m = MarkovChain(data)
    m.train()
    with open('markovHHGG.pkl', 'wb') as output:
        pickle.dump(m, output, pickle.HIGHEST_PROTOCOL)
