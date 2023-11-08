from concurrent import futures
import logging

import grpc, project_1_pb2, project_1_pb2_grpc

import math

class Quadratic(project_1_pb2_grpc.QuadraticSolverServicer):
    
    def QuadraticSolver(self, request, context):
        
        # get each variable value for a, b, and c
        a = request.a
        b = request.b
        c = request.c

        # within the square root
        d = (b**2) - (4*a*c)

        #different real roots
        if d > 0:

            x1 = ((-b - math.sqrt(abs(d)))/(2*a))
            x2 = ((-b + math.sqrt(abs(d)))/(2*a))

        #same real roots
        elif d == 0:
            x1 = (-b/(2*a))
            x2 = (-b/(2*a))

        #complex roots
        else:
            x1 = f'{(-b/(2*a))}-i{math.sqrt(abs(d))}'
            x2 = f'{(-b/(2*a))}+i{math.sqrt(abs(d))}'

        #if a is 0 there is no solution
        if a!= 0:
            solutions = f'X1: {x1}\nX2: {x2}'
        else:
            solutions = 'no solutions'

        return project_1_pb2.x_solutions(solutions = solutions)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    project_1_pb2_grpc.add_QuadraticSolverServicer_to_server(Quadratic(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()