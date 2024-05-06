import grpc
from concurrent import futures
import math
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    
    def Add(self, request, context):
        result = request.num1 + request.num2
        return calculator_pb2.AddResponse(result=result)
    
    def Subtract(self, request, context):
        result = request.num1 - request.num2
        return calculator_pb2.SubtractResponse(result=result)
    
    def Multiply(self, request, context):
        result = request.num1 * request.num2
        return calculator_pb2.MultiplyResponse(result=result)
    
    def Divide(self, request, context):
        if request.num2 == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Division by zero is not allowed.")
            return calculator_pb2.DivideResponse()
        result = request.num1 / request.num2
        return calculator_pb2.DivideResponse(result=result)
    
    def SquareRoot(self, request, context):
        if request.num < 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Square root of a negative number is not allowed.")
            return calculator_pb2.SquareRootResponse()
        result = math.sqrt(request.num)
        return calculator_pb2.SquareRootResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()