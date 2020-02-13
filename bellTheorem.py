#Code Author : Usama Ahsan

#This code is to prove the concept provided at
#https://www.wired.com/2014/01/bells-theorem/

#Article Name : The Experiment That Forever Changed How We Think About Reality
#Article Author: Aatish Bhatia

#The confidence interval function is taken from
#https://stackoverflow.com/questions/15033511/compute-a-confidence-interval-from-sample-data
#In the answer of the question of  Compute a confidence interval from sample data

import numpy as np

import scipy.stats

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

def compile_result(exp,tr,data):
    print('\nExperiments Performed\t\t:\t'+str(exp)+' times')
    print('\nTrial count in each experiment\t:\t'+str(tr)+' trials')
    print('\n')
    print('Result of Experiments\t\t:\t',np.float16(np.mean(data)),'±',np.float16(np.std(data)))
    m,nm,pm=mean_confidence_interval(data)
    print('Confidence Interval at 95%\t:\t',np.float16(nm),'≤',np.float16(m),'≤',np.float16(pm))

def generateParticle(door):
    a=np.random.randint(door)
    b=np.random.randint(door)
    c=np.random.randint(door)
            
    p1=[a,b,c]
    p2=p1
    
    return p1,p2
         
   
def classicalPhysics(exp,tr,door):
    
    prob=[]
    for i in range(exp):
        r1=[]
        r2=[]
        for j in range(tr):
            
            p1,p2=generateParticle(door)
            rnd1=np.random.randint(door)
            rnd2=np.random.randint(door)
            
            phy1=p1[rnd1]
            phy2=p2[rnd2]
            
            r1.append(phy1)
            r2.append(phy2)

        r1=np.array(r1)
        r2=np.array(r2)
        
        similar=r1==r2
        
        prob.append(sum(similar)/len(similar))
    return prob


if __name__ == '__main__' :
    experimentRun=100
    trials=100
    door=3
    
    
    
    prob=classicalPhysics(experimentRun,trials,door)
    compile_result(experimentRun,trials,prob)
