
from __future__ import print_function

import logging

import grpc
import project_1_pb2
import project_1_pb2_grpc

#running client side
def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = project_1_pb2_grpc.QuadraticSolverStub(channel)
        variables = project_1_pb2.variables(a=2, b=3, c=-2)
        response = stub.QuadraticSolver(variables)
        print(response.solutions)

if __name__ == '__main__':
    logging.basicConfig()
    run()
