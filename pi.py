from flask import Flask, jsonify
from flask import request
import json

import pickle
import pandas as pd
import numpy as np
#import model.pkl


import os
#import cPickle as pickle

my_dir = os.path.dirname(__file__)
pickle_file_path = os.path.join(my_dir, 'model.pkl')

with open(pickle_file_path, 'rb') as pickle_file:
    demo = pickle.load(pickle_file)


#################
    pred= pd.DataFrame(arr3),
                   columns = ['feeling.nervous','panic','breathing.rapidly','sweating','trouble.in.concentration',
                              'having.trouble.in.sleeping',
                             'having.trouble.with.work','hopelessness','anger','over.react',
                             'change.in.eating','suicidal.thought','feeling.tired','close.friend','social.media.addiction',
                             'weight.gain','material.possessions'
                             ,'introvert','popping.up.stressful.memory',
                             'having.nightmares','avoids.people.or.activities',
                             'feeling.negative','trouble.concentrating','blamming.yourself'])

########33333
response =''
app = Flask(__name__)

@app.route('/name', methods = ['GET', 'POST'])
def nameRoute():
    global response
    if(request.method == 'POST'):
       request_data =request.data
       request_data = json.loads(request_data.decode('utf-8'))
       name = request_data['name']
       response = f'HI {name}! this is python'

       return " "
    else:
        
        '''
      data =  run.fun()
        numpyData = {'name':data}
        encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)
        return(encodedNumpyData)
'''

        #numpyData = {"array": numpyArrayOne}
#encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
#print("Printing JSON serialized NumPy array")
#print(encodedNumpyData)
       
        #return jsonify({'name':'h'})

        data = demo.predict(pred)
        tojeson = data.tolist()
        return jsonify({'name':tojeson})
        


def afun():




    return('hi')


if __name__ == "__main__":
    app.run(debug = True)




