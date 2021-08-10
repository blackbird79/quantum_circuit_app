from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer
from qiskit import QuantumCircuit
from qiskit import Aer,execute
from qiskit.visualization import plot_histogram
import logging
import plotly
import json

logger = logging.getLogger(__name__)

# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer
    


    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        uri = request.build_absolute_uri()
        command = uri.split("/")[-2] if uri.split("/")[-1] ==""  else uri.split("/")[-1]
        str_text = ''
        for line in file_uploaded:
            str_text = str_text + line.decode() 
        str_text=str_text.replace('\t',' ') 
        str_text=str_text.replace('\r\n',' ') 
        if command=='analyze': 
            try:    
                qc= QuantumCircuit.from_qasm_str(str_text)
                counts_gates = qc.count_ops()
                num_qubits= qc.num_qubits
                depth = qc.depth()
                response = "Number of qubits: {}, Depth: {}, Gate Count: {}".format(num_qubits,depth,counts_gates)
            except:
                response = "There was an error when trying to get the circuit"
                logger.error(response)
        elif command=='simulate':
            response = self.simulate(str_text)
        else: 
            response = "There was an error- only analyze or simulate api"
            logger.error(response)   
        return Response(response)


    def simulate(self,str_text):
        try:    
            qc= QuantumCircuit.from_qasm_str(str_text)
            aer_sim = Aer.get_backend('aer_simulator')
            qasm_job = execute(qc,backend=aer_sim,shots=1024).result()
            counts = qasm_job.get_counts()
            response=json.dumps(counts, cls=plotly.utils.PlotlyJSONEncoder)
        except:
            response = "Can't simulate the qasm string"
            logger.error(response)  
        return  response   







